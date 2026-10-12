---
date: 2026-10-12
tool: claude-code
tool_name: Claude Code
title: "用 context: fork 隔离 Skill 执行"
level: 进阶
source_title: "Extend Claude Code"
source_url: https://code.claude.com/docs/en/features-overview.md
---

# 用 context: fork 隔离 Skill 执行

## 什么时候用得上

当某个 Skill 会读很多文件或产生大量中间输出，而你的主会话上下文已经吃紧。你希望它照常执行，但别把过程全塞回当前对话。

## 怎么做

在 Skill 中使用：

```
context: fork
```

调用该 Skill 时，它会在隔离上下文中运行，只把结果带回主对话。

## 为什么

默认 Skill 会加载进当前对话；`context: fork` 让它改在隔离上下文运行，主对话只接收结果。这样既能复用 Skill，又不让中间读取和输出挤占主上下文。

## 原文依据

> A skill can run in isolated context using `context: fork`.

来源：[Extend Claude Code](https://code.claude.com/docs/en/features-overview.md)
