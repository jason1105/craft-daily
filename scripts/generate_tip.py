#!/usr/bin/env python3
"""
generate_tip.py — 每个工作日生成一条「有据可查」的工具使用技巧。

设计要点（与站内其他应用一脉相承）：
  1. 事实必须有来源：只把一个真实文档/源码页喂给模型，不让它凭记忆发挥。
  2. 编造在结构上不可能：模型必须交回一段 evidence（原文摘录），
     脚本逐字校验这段话确实出现在抓下来的原文里，对不上就判定为编造。
  3. 宁可不发，也不发假的：三次都取证失败则非零退出，触发失败告警。

环境变量：
  LLM_API_KEY / OPENROUTER_API_KEY   必填
  LLM_BASE_URL                       默认 https://api.deepseek.com
  LLM_MODEL                          默认 deepseek-v4-flash
  GH_TOKEN                           读公开仓库目录树用，避免匿名限流
"""

import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
TIPS_DIR = ROOT / "tips"
DATA_DIR = ROOT / "data"
TOOLS_FILE = ROOT / "tools.yml"

MODEL = os.environ.get("LLM_MODEL") or "deepseek-v4-flash"
BASE_URL = (os.environ.get("LLM_BASE_URL") or "https://api.deepseek.com").rstrip("/")
API_KEY = os.environ.get("LLM_API_KEY") or os.environ.get("OPENROUTER_API_KEY", "")
GH_TOKEN = os.environ.get("GH_TOKEN", "")

MAX_SOURCE_CHARS = 14000      # 单页喂给模型的上限
MIN_EVIDENCE_CHARS = 24       # 太短的"摘录"没有取证意义
MAX_ATTEMPTS = 3
# 思考模型的 reasoning_content 与正文共用 completion 预算，留足空间，
# 否则长原文下推理占满额度、正文返回空。
MAX_TOKENS = 8192
UA = {"User-Agent": "craft-daily/1.0 (+https://github.com/jason1105/craft-daily)"}


# ── 页面发现 ────────────────────────────────────────────────────────────────

def discover_llms_index(src: dict) -> list:
    """解析官方 llms.txt（专供 LLM 的文档索引），取出全部文档页。"""
    r = requests.get(src["url"], headers=UA, timeout=30)
    r.raise_for_status()
    only = src.get("only_path", "")
    match_any = [m.lower() for m in src.get("match_any", [])]
    pages, seen = [], set()
    # 条目形如：- [标题](https://.../page.md): 描述
    pattern = r"\[([^\]]+)\]\((https?://[^)\s]+\.md)\)(?::\s*([^\n]*))?"
    for title, url, desc in re.findall(pattern, r.text):
        if only and only not in url:
            continue
        if match_any:
            hay = f"{title} {desc} {url}".lower()
            if not any(m in hay for m in match_any):
                continue
        if url in seen:
            continue
        seen.add(url)
        pages.append({"id": url, "title": title.strip(), "url": url})
    return pages


def discover_github_repo(src: dict) -> list:
    """列出公开仓库里指定路径下的文档/源码文件。

    优先用 GitHub API 列目录树（能自动发现新增文件）；
    若 API 不可用（限流/网络策略），回落到 tools.yml 里的显式清单，
    保证事实源永远可用，不会因为一个接口挂掉就整个应用停摆。
    """
    repo, branch = src["repo"], src.get("branch", "main")
    raw = f"https://raw.githubusercontent.com/{repo}/{branch}"
    html = f"https://github.com/{repo}/blob/{branch}"

    def as_page(path):
        return {"id": f"{repo}:{path}", "title": path,
                "url": f"{raw}/{path}", "html_url": f"{html}/{path}"}

    includes = src.get("include", [])
    exts = tuple(src.get("ext", [".md"]))
    headers = dict(UA)
    if GH_TOKEN:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    api = f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1"
    try:
        r = requests.get(api, headers=headers, timeout=30)
        r.raise_for_status()
        pages = []
        for node in r.json().get("tree", []):
            if node.get("type") != "blob":
                continue
            path = node["path"]
            if not path.endswith(exts):
                continue
            if includes and not any(path == inc or path.startswith(inc) for inc in includes):
                continue
            pages.append(as_page(path))
        if pages:
            return pages
        print("  GitHub API 返回空列表，改用显式清单")
    except Exception as exc:
        print(f"  GitHub API 不可用（{type(exc).__name__}），改用显式清单")

    return [as_page(p) for p in src.get("fallback_files", [])]


def discover_pages(tool: dict) -> list:
    src = tool["source"]
    if src["type"] == "llms_index":
        return discover_llms_index(src)
    if src["type"] == "github_repo":
        return discover_github_repo(src)
    raise ValueError(f"未知的 source.type: {src['type']}")


def fetch_page(page: dict) -> str:
    r = requests.get(page["url"], headers=UA, timeout=30)
    r.raise_for_status()
    return r.text


# ── 取证校验 ────────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    """归一化：全角/半角、各类空白、markdown 强调符，降低无谓的匹配失败。"""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("​", "")
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def evidence_is_grounded(evidence: str, source_text: str) -> bool:
    """evidence 必须逐字出现在原文中——这是拦住编造的那道闸。"""
    if not evidence or len(evidence.strip()) < MIN_EVIDENCE_CHARS:
        return False
    return normalize(evidence) in normalize(source_text)


# ── 生成 ────────────────────────────────────────────────────────────────────

PROMPT = """你是一位资深工程师，正在为另一位资深工程师写「今日一招」。

下面是工具 **{tool_name}** 的一页真实文档/源码，标题《{page_title}》。
请只依据这一页的内容，提炼出一条**具体、可立刻上手**的使用技巧。

读者画像：8 年以上经验的资深研发，已经会该工具的基本操作。
不要教「怎么安装」「怎么开始用」这类入门内容，
要挑配置、自动化、组合用法、容易忽略的选项、或反直觉的坑。

请严格返回如下 JSON，不要有任何其他文字：
{{
  "title": "技巧标题，一句话，不超过 24 字",
  "scenario": "什么时候用得上——描述一个具体的工作场景，2 句以内，让读者代入",
  "steps": "怎么做。必须包含可直接复制粘贴的命令或配置，用 markdown 代码块包裹。可以有简短说明。",
  "why": "为什么这样更好 / 不这样会怎样。2-3 句。",
  "evidence": "从上面原文中**逐字复制**的一段话，用来支撑这条技巧。必须与原文一字不差，不得改写、翻译或拼接。至少 24 个字符。",
  "level": "入门 / 进阶 / 专家 三选一"
}}

=== 硬性约束（最高优先级）===
1. steps 里出现的每一个命令、参数、配置项、文件名，都必须在下面原文中真实出现。
   原文里没有的，一个字都不许编。拿不准就换一条能被原文支撑的技巧。
2. evidence 必须是原文的**逐字摘录**。系统会用字符串匹配校验，
   改写或凭印象复述会被判定为编造并作废。
3. scenario 允许你组织语言（这是编辑加工），但不得引入原文没有的技术事实。
4. 如果这一页内容太薄、提炼不出对资深工程师有价值的技巧，
   请在 title 里写「SKIP」，其余字段留空。

=== 原文（工具 {tool_name}，页面《{page_title}»）===
{source}
"""


def ask_model(client: OpenAI, tool: dict, page: dict, source: str) -> dict:
    prompt = PROMPT.format(
        tool_name=tool["name"],
        page_title=page["title"],
        source=source[:MAX_SOURCE_CHARS],
    )
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    choice = resp.choices[0]
    raw = (choice.message.content or "").strip()

    # 诊断信息：思考模型（如 deepseek-v4-flash）的 reasoning 也吃 completion 预算，
    # 预算不够时 content 会是空的。把这些数字打出来，下次失败一眼能看出是哪种情况。
    if not raw:
        reasoning = getattr(choice.message, "reasoning_content", None) or ""
        usage = getattr(resp, "usage", None)
        raise ValueError(
            f"模型返回空正文 —— finish_reason={choice.finish_reason}, "
            f"reasoning 长度={len(reasoning)}, max_tokens={MAX_TOKENS}, usage={usage}"
        )

    m = re.search(r"```(?:json)?\s*(.+?)```", raw, re.S)
    if m:
        raw = m.group(1).strip()
    i, j = raw.find("{"), raw.rfind("}")
    if i != -1 and j > i:
        raw = raw[i:j + 1]
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        # 把模型实际返回的东西打出来。不这么做，"解析失败"四个字什么也说明不了，
        # 只能靠猜——而猜过两轮都是错的。
        reasoning = getattr(choice.message, "reasoning_content", None) or ""
        raise ValueError(
            f"返回内容不是 JSON（{exc}）| finish_reason={choice.finish_reason} "
            f"| content 长度={len(choice.message.content or '')} "
            f"| reasoning 长度={len(reasoning)} | usage={getattr(resp, 'usage', None)}\n"
            f"    content 开头: {(choice.message.content or '')[:300]!r}"
        ) from None


# ── 落盘 ────────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return (s or "tip")[:48]


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return default


def write_tip(tip: dict, tool: dict, page: dict, date_str: str) -> Path:
    TIPS_DIR.mkdir(exist_ok=True)
    slug = slugify(page["title"])
    path = TIPS_DIR / f"{date_str}-{tool['id']}-{slug}.md"
    link = page.get("html_url", page["url"])
    body = f"""---
date: {date_str}
tool: {tool['id']}
tool_name: {tool['name']}
title: {json.dumps(tip['title'], ensure_ascii=False)}
level: {tip.get('level', '进阶')}
source_title: {json.dumps(page['title'], ensure_ascii=False)}
source_url: {link}
---

# {tip['title']}

## 什么时候用得上

{tip['scenario']}

## 怎么做

{tip['steps']}

## 为什么

{tip['why']}

## 原文依据

> {tip['evidence']}

来源：[{page['title']}]({link})
"""
    path.write_text(body, encoding="utf-8")
    return path


def main() -> None:
    if not API_KEY:
        print("ERROR: 缺少 LLM_API_KEY / OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    tools = yaml.safe_load(TOOLS_FILE.read_text(encoding="utf-8"))["tools"]
    DATA_DIR.mkdir(exist_ok=True)

    # 前端要用的工具元信息（名称/配色/简介），每次运行同步一次
    (DATA_DIR / "tools.json").write_text(json.dumps(
        [{k: t.get(k) for k in ("id", "name", "accent", "blurb", "home")} for t in tools],
        ensure_ascii=False, indent=2), encoding="utf-8")
    coverage = load_json(DATA_DIR / "coverage.json", {})
    index = load_json(DATA_DIR / "index.json", [])

    today = datetime.now(timezone.utc)
    date_str = today.strftime("%Y-%m-%d")
    if any(t.get("date") == date_str for t in index):
        print(f"今天（{date_str}）已经有一条了，跳过。")
        return

    # 按已产出条数轮转工具，保证长期均衡
    tool = tools[len(index) % len(tools)]
    print(f"今日工具：{tool['name']}")

    pages = discover_pages(tool)
    print(f"发现 {len(pages)} 个可用页面")
    if not pages:
        print("ERROR: 未发现任何页面，事实源可能已失效", file=sys.stderr)
        sys.exit(1)

    covered = set(coverage.get(tool["id"], []))
    pool = [p for p in pages if p["id"] not in covered]
    if not pool:
        print("该工具所有页面都讲过了，开始新一轮。")
        covered, pool = set(), pages

    # 用日期做种子，保证可复现
    pool.sort(key=lambda p: p["id"])
    page = pool[hash(date_str) % len(pool)]
    print(f"选中页面：{page['title']}")

    source = fetch_page(page)
    print(f"抓取正文 {len(source)} 字符")

    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    tip = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            candidate = ask_model(client, tool, page, source)
        except Exception as exc:
            print(f"  第 {attempt} 次：调用/解析失败 —— {type(exc).__name__}: {exc}")
            continue

        if str(candidate.get("title", "")).strip().upper().startswith("SKIP"):
            print(f"  第 {attempt} 次：模型判定该页提炼不出有价值内容")
            # 记为已覆盖，避免明天又抽中同一页
            coverage.setdefault(tool["id"], []).append(page["id"])
            (DATA_DIR / "coverage.json").write_text(
                json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
            print("已标记该页为跳过，今日不发。")
            sys.exit(1)

        missing = [k for k in ("title", "scenario", "steps", "why", "evidence")
                   if not str(candidate.get(k, "")).strip()]
        if missing:
            print(f"  第 {attempt} 次：字段缺失 {missing}，重试")
            continue

        if not evidence_is_grounded(candidate["evidence"], source):
            print(f"  第 {attempt} 次：⚠️ evidence 无法在原文中匹配 —— 判定为编造，作废重试")
            print(f"    模型给出：{candidate['evidence'][:120]}")
            continue

        tip = candidate
        print(f"  第 {attempt} 次：✅ 取证通过")
        break

    if tip is None:
        print(f"ERROR: {MAX_ATTEMPTS} 次均未通过取证校验，今日不发（宁可不发也不发假的）",
              file=sys.stderr)
        sys.exit(1)

    path = write_tip(tip, tool, page, date_str)
    print(f"已写入：{path.relative_to(ROOT)}")

    index.insert(0, {
        "date": date_str,
        "tool": tool["id"],
        "tool_name": tool["name"],
        "title": tip["title"],
        "scenario": tip["scenario"],
        "level": tip.get("level", "进阶"),
        "file": f"tips/{path.name}",
        "source_title": page["title"],
        "source_url": page.get("html_url", page["url"]),
    })
    (DATA_DIR / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    coverage.setdefault(tool["id"], []).append(page["id"])
    (DATA_DIR / "coverage.json").write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")

    total = sum(len(v) for v in coverage.values())
    print(f"完成。累计 {len(index)} 条，已覆盖 {total} 个页面。")


if __name__ == "__main__":
    main()
