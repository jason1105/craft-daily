---
date: 2026-10-05
tool: codex
tool_name: Codex CLI
title: "用 codex exec 做 CI 非交互执行"
level: 进阶
source_title: "Glossary"
source_url: https://learn.chatgpt.com/docs/glossary.md
---

# 用 codex exec 做 CI 非交互执行

## 什么时候用得上

需要在 CI 或脚本里自动跑 Codex，而不是打开交互式终端时。仓库有固定规范时，把它写进 AGENTS.md，让非交互执行也继承持久指令。

## 怎么做

在 CI 脚本中直接调用非交互命令；并用 `AGENTS.md` 提供持久指令。

```bash
codex exec
```

## 为什么

交互式 CLI 适合人工操作；`codex exec` 明确定义为从脚本或 CI 非交互运行。配合 `AGENTS.md` 的持久指令，可减少每次执行重复交代仓库约束。

## 原文依据

> CLI command for running Codex non-interactively from scripts or CI.

来源：[Glossary](https://learn.chatgpt.com/docs/glossary.md)
