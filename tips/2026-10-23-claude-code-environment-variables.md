---
date: 2026-10-23
tool: claude-code
tool_name: Claude Code
title: "用空字符串中和无法 unset 的变量"
level: 专家
source_title: "Environment variables"
source_url: https://code.claude.com/docs/en/env-vars.md
---

# 用空字符串中和无法 unset 的变量

## 什么时候用得上

你的 shell profile 导出了 stale 的 CLAUDE_CODE_USE_VERTEX，但你不方便改 profile；你想让它对 provider selection 按未设置处理。

## 怎么做

在 `~/.claude/settings.json` 的 `env` 中写入空字符串：

```json
{
  "env": {
    "CLAUDE_CODE_USE_VERTEX": ""
  }
}
```

Claude Code 会把空值当作未设置用于 provider selection；注意子进程仍会继承这个空值。

## 为什么

settings 文件只能设置变量、不能删除变量，遇到不可控 shell profile 导出的陈旧变量时很难清掉。把 `env` 中的值设为空字符串，Claude Code 会在 provider selection 上按未设置处理；但子进程仍会继承空值，所以别把它当成彻底 unset。

## 原文依据

> Claude Code treats the empty value as unset for provider selection.

来源：[Environment variables](https://code.claude.com/docs/en/env-vars.md)
