---
date: 2026-10-13
tool: codex
tool_name: Codex CLI
title: "CI 临时任务别持久化 Codex 登录"
level: 进阶
source_title: "Access tokens"
source_url: https://learn.chatgpt.com/docs/enterprise/access-tokens.md
---

# CI 临时任务别持久化 Codex 登录

## 什么时候用得上

你在共享 CI runner 或临时脚本里跑 `codex exec`，只想要一次性的非交互运行。不要把 agent identity credential 写进 runner 的 Codex CLI auth storage。

## 怎么做

用环境变量做一次性自动化：
```bash
export CODEX_ACCESS_TOKEN="<access-token>"
codex exec --json "review this repository and summarize the top risks"
```
只有在确实要持久本地登录时，才用 login：
```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"
```

## 为什么

`codex login --with-access-token` 会把 agent identity credential 存入 Codex CLI auth storage；临时或共享环境应改用 `CODEX_ACCESS_TOKEN` 环境变量，避免把凭据持久化到机器上。原文明确这是不落盘的替代方案。

## 原文依据

> `codex login --with-access-token` stores an agent identity credential in Codex CLI auth storage. If you prefer not to persist credentials on the machine, use the `CODEX_ACCESS_TOKEN` environment variable instead.

来源：[Access tokens](https://learn.chatgpt.com/docs/enterprise/access-tokens.md)
