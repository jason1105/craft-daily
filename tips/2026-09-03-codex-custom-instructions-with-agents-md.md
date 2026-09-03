---
date: 2026-09-03
tool: codex
tool_name: Codex CLI
title: "复用 TEAM_GUIDE.md 作为 Codex 指令"
level: 进阶
source_title: "Custom instructions with AGENTS.md"
source_url: https://learn.chatgpt.com/docs/agent-configuration/agents-md.md
---

# 复用 TEAM_GUIDE.md 作为 Codex 指令

## 什么时候用得上

仓库已有 TEAM_GUIDE.md，但 Codex 默认不会读取它，任务中团队约定没生效。把该文件名加入 fallback 列表，Codex 就会把它当成指令文件加载。

## 怎么做

1. 编辑 `~/.codex/config.toml`：
```toml
# ~/.codex/config.toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```
2. Restart Codex or run a new command so the updated configuration loads.

之后 Codex 按此顺序检查：`AGENTS.override.md` → `AGENTS.md` → `TEAM_GUIDE.md` → `.agents.md`。

## 为什么

不用把团队现有文档改名或复制成 AGENTS.md，就能让它参与指令合并；不在 fallback 列表里的旧文件名仍会被忽略。提高字节上限还能容纳更多项目约定，避免截断。

## 原文依据

> Now Codex checks each directory in this order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`. Filenames not on this list are ignored for instruction discovery. The larger byte limit allows more combined guidance before truncation.

来源：[Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md)
