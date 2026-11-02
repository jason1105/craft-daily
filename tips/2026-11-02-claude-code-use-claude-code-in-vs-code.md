---
date: 2026-11-02
tool: claude-code
tool_name: Claude Code
title: "用 code . 启动 VS Code 以继承环境变量"
level: 进阶
source_title: "Use Claude Code in VS Code"
source_url: https://code.claude.com/docs/en/vs-code.md
---

# 用 code . 启动 VS Code 以继承环境变量

## 什么时候用得上

你已经在 shell 里设置好了 ANTHROPIC_API_KEY，但打开 VS Code 扩展后仍看到 Not logged in / 登录提示。这通常是因为 VS Code 没有继承你的 shell 环境。

## 怎么做

在已设置 `ANTHROPIC_API_KEY` 的终端里执行：

```
code .
```

这会从该终端启动 VS Code，让扩展继承 shell 环境变量；若仍提示登录，也可直接用 Claude 账号登录。

## 为什么

从桌面图标或开始菜单启动的 VS Code 不会继承终端里的环境变量，扩展因此看不到 `ANTHROPIC_API_KEY`，只能反复走浏览器登录。用 `code .` 从终端启动可以让它继承环境变量，省去登录排查。

## 原文依据

> Launch VS Code from a terminal with `code .` so it inherits your environment variables, or sign in with your Claude account instead.

来源：[Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code.md)
