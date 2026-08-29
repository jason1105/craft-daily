# craft-daily · 每日一招

每个工作日一条工具用法，**全部出自官方文档与公开源码，每条都附可核对的原文依据**。

**线上：** https://jason1105.github.io/craft-daily/

## 为什么要有原文依据

让模型凭记忆写「工具最佳实践」，产出会是这样的东西：

> 💡 用 `claude --compact` 压缩上下文，避免长会话超限。

看起来很专业——但这个命令可能根本不存在。工具迭代快，模型训练截止后的变化它一概不知；
而编造出来的技巧**你没有任何办法一眼分辨真假**，试了浪费时间，不试就记住了错的。

所以这个仓库的核心不是「生成」，是**取证**：

1. 每天只把**一个真实文档页或源码文件**喂给模型，不让它凭记忆发挥
2. 模型必须交回一段 `evidence`——原文的逐字摘录
3. 脚本用字符串匹配**校验这段话确实出现在原文里**，对不上就判定为编造，作废重试
4. 三次都过不了取证，**当天不发**（宁可不发，也不发假的）

编造因此在结构上不可能，而不是靠提示词请求模型别瞎编。
页面上每条 tip 都带原文出处链接，你随时能自己复核。

**取证只卡技术事实。** 「什么时候用得上」那一段是模型基于原文组织的语言，属于编辑加工，
允许它组织表达，但不得引入原文没有的技术事实——两者在页面上分开标注。

## 收录的工具

| 工具 | 事实源 |
|------|--------|
| Claude Code | [官方文档 llms.txt](https://code.claude.com/docs/llms.txt)（约 190 页） |
| Codex CLI | [官方文档 llms.txt](https://developers.openai.com/codex/llms.txt)（约 88 页） |
| Hermes Studio | [公开仓库](https://github.com/EKKOLearnAI/hermes-studio)的文档与源码 |

**加一个新工具，只改 `tools.yml`，不用动代码。** 支持两种事实源：

- `llms_index` — 官方提供 llms.txt（专供 LLM 的文档索引）时，自动发现全部页面
- `github_repo` — 读公开仓库；优先用 GitHub API 列目录树，接口不可用时回落到显式清单

## 不会讲重复的

`data/coverage.json` 记录每个工具已经讲过哪些页，只从没讲过的里面挑。
一轮讲完自动开始新一轮（换个角度重讲）。

## 学完之后

每条 tip 可以标记 **待实践 / 已掌握 / 已用上**，标「已用上」时还能记一句用在哪了。
工具知识的验证是**真的用过**，不是背下来。

这些标记存在你自己浏览器的 localStorage 里，不上传、不同步。
知识本身（`tips/*.md`）才提交进仓库——应用会死，笔记不该死：
纯 markdown 你能 grep、能在 GitHub 上直接读、能喂给任何 LLM，十年后还打得开。

## 目录

```
tools.yml                 工具注册表（加工具只改这里）
scripts/generate_tip.py   取证流水线
tips/YYYY-MM-DD-*.md      每日一招（知识落盘）
data/index.json           前端索引
data/coverage.json        已覆盖页面，保证不重复
data/tools.json           前端用的工具元信息
index.html                前端
```

## 配置

| 变量 | 类型 | 说明 |
|------|------|------|
| `LLM_API_KEY` | secret | DeepSeek API key（`OPENROUTER_API_KEY` 亦可作兜底） |
| `LLM_MODEL` | variable | 默认 `deepseek-v4-flash` |
| `LLM_BASE_URL` | variable | 默认 `https://api.deepseek.com`，可指向任何 OpenAI 兼容服务 |

## 本地跑一次

```bash
pip install requests pyyaml openai
export LLM_API_KEY=sk-...
python scripts/generate_tip.py
```

---

由 GitHub Actions + DeepSeek 驱动 · 站群应用之一，导航见 [dev-hub](https://jason1105.github.io/dev-hub/)
