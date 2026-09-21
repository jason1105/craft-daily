---
date: 2026-09-21
tool: claude-code
tool_name: Claude Code
title: "个人覆盖：settings.local.json"
level: 进阶
source_title: "Settings files and precedence"
source_url: https://code.claude.com/docs/en/settings.md
---

# 个人覆盖：settings.local.json

## 什么时候用得上

你在团队仓库里要改 Claude Code 设置，但不想改共享配置、也不想影响自己其他项目。此时应把覆盖写到项目本地文件，而不是 `.claude/settings.json` 或 `~/.claude/settings.json`。

## 怎么做

按原文优先级从高到低确认位置，个人覆盖落到 `Project local`：
```text
Managed settings: managed-settings.json, MDM, or the claude.ai console
Command line:     claude --settings
Project local:    .claude/settings.local.json
Shared project:   .claude/settings.json
User:             ~/.claude/settings.json
```
把个人覆盖写进 `.claude/settings.local.json`；临时本次会话覆盖用 `claude --settings`。

## 为什么

同一 key 在更高层会覆盖低层；`.claude/settings.local.json` 高于 Shared project 和 User，所以适合做仅你、仅本项目的覆盖。若改 `.claude/settings.json` 会影响团队，改 `~/.claude/settings.json` 会影响你所有项目。

## 原文依据

> Settings precedence, highest first: managed settings, command line, project local, shared project, user. A key set at a higher level overrides the same key set lower down.

来源：[Settings files and precedence](https://code.claude.com/docs/en/settings.md)
