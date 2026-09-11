---
date: 2026-09-11
tool: claude-code
tool_name: Claude Code
title: "抢在 8/14 前把 auto mode 设为默认"
level: 进阶
source_title: "Week 32 · August 3–7, 2026"
source_url: https://code.claude.com/docs/en/whats-new/2026-w32.md
---

# 抢在 8/14 前把 auto mode 设为默认

## 什么时候用得上

你在 Pro/Max/Team 计划上，8 月 14 日起 auto mode 会成为新会话的默认权限模式。与其那天被一次性切换提示打断，不如现在就把默认模式锁定成你选定的那个。

## 怎么做

打开用户设置 `~/.claude/settings.json`，显式指定默认权限模式：

```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

保存后新开会话，状态栏会显示 `auto mode on`。注意：若你此前自己设过默认模式，它会保持原样，直到你接受那个一次性切换提示；组织托管的默认模式则完全不受影响。

## 为什么

被动等 8 月 14 日切换，等于让别人替你决定新会话的权限行为；写进用户设置后每次启动都按你选的模式走，语义可控。而且该模式下 classifier 的调用已不再计入用量限额，等于白得。

## 原文依据

> To start every session in auto mode before the switch, set it as your default in your user settings:

来源：[Week 32 · August 3–7, 2026](https://code.claude.com/docs/en/whats-new/2026-w32.md)
