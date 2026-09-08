---
date: 2026-09-08
tool: claude-code
tool_name: Claude Code
title: "Bash(rm *) 拦 rm，别禁用 Bash"
level: 进阶
source_title: "Configure permissions"
source_url: https://code.claude.com/docs/en/agent-sdk/permissions.md
---

# Bash(rm *) 拦 rm，别禁用 Bash

## 什么时候用得上

你在用 Claude Agent SDK 做自动化，开了 `bypassPermissions` 让 Claude 放手执行，但不能让它碰 `rm *`。用带作用域的 deny 规则把它拦在权限模式判定之前，Bash 其余命令照常可用。

## 怎么做

不要配置 `disallowed_tools=["Bash"]`——那样整个 Bash 工具会从 Claude 的上下文里消失。配置作用域 deny：

```
disallowed_tools=["Bash(rm *)"]
```

这样 `Bash` 仍然可用，只有匹配 `rm *` 的调用被拒绝。

## 为什么

deny 规则在权限模式和 allow 规则之前检查，所以一旦命中，`bypassPermissions` 也绕不过它。裸 `Bash` deny 会让整个工具不可见，属于一刀切；作用域规则既守住危险删除，又不牺牲 shell 能力。

## 原文依据

> `Bash` stays available. Calls matching `rm *` are denied in every permission mode, including `bypassPermissions`.

来源：[Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions.md)
