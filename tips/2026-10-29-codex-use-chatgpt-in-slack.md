---
date: 2026-10-29
tool: codex
tool_name: Codex CLI
title: "首条请求点名共享环境，续跑别换线程"
level: 进阶
source_title: "Use ChatGPT in Slack"
source_url: https://learn.chatgpt.com/docs/third-party/slack.md
---

# 首条请求点名共享环境，续跑别换线程

## 什么时候用得上

你在 Slack 线程里让 @ChatGPT 把仓库改造派给 Codex Cloud，接着想让它补测试、或换个环境重跑。随手换个账号或新开线程追问，就会另起一个 coding task，之前的环境和上下文全丢。

## 怎么做

首条请求就把仓库（或 workspace 共享环境）点出来，并固定在这条 thread 里继续：

```text
@ChatGPT investigate the failing checkout tests in acme/storefront and propose a fix.
```

后续追问留在这条 thread，且用**同一个账号**发送：

```text
@ChatGPT add a regression test for the fix and summarize the checks you ran.
```

要换环境时不要在 thread 里追问，直接新开一条会话并重新点名仓库/共享环境。

## 为什么

同一 thread 的后续请求只有用同一账号运行，才会续用同一个 coding task 和 environment；换账号会另起一个任务，换环境在原线程里追问则对不上。首条不点名仓库或共享环境，ChatGPT 只能自己从你有权限的 workspace 共享环境中挑，很容易落到不是你预期的那个上。

## 原文依据

> the repository or shared environment in your request to help ChatGPT choose.

来源：[Use ChatGPT in Slack](https://learn.chatgpt.com/docs/third-party/slack.md)
