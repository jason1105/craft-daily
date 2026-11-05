---
date: 2026-11-05
tool: claude-code
tool_name: Claude Code
title: "给状态栏设 refreshInterval"
level: 进阶
source_title: "Customize your status line"
source_url: https://code.claude.com/docs/en/statusline.md
---

# 给状态栏设 refreshInterval

## 什么时候用得上

主会话挂着后台 subagents 时，事件驱动更新会静默，状态栏里的时钟或外部 git 状态停更。你需要状态栏在空闲期也按固定节奏刷新。

## 怎么做

在 `~/.claude/settings.json` 的 `statusLine` 中加入 `refreshInterval`；下面把秒数设为 `1`（原文最小值），按需调大：

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "refreshInterval": 1
  }
}
```

## 为什么

默认只在事件触发时重跑脚本，主会话空闲（例如等待后台 subagent）时事件可能静默，时间型或外部数据段就会冻结。设置 `refreshInterval` 后会在事件更新之外按固定时间额外重跑命令，最小值为 `1` 秒。

## 原文依据

> The minimum is `1`. Set this when your status line shows time-based data such as a clock, or when background subagents change git state while the main session is idle.

来源：[Customize your status line](https://code.claude.com/docs/en/statusline.md)
