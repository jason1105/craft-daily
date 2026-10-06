---
date: 2026-10-06
tool: hermes-studio
tool_name: Hermes Studio
title: "重启后 /context 只是本地历史估算"
level: 专家
source_title: "docs/ekko-session-commands.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/ekko-session-commands.md
---

# 重启后 /context 只是本地历史估算

## 什么时候用得上

你刚重启 Hermes Studio，想用 `/context` 判断当前会话离模型上限还有多远，再决定是否压缩。

## 怎么做

```
/context
```
如果当前 Studio 进程重启过，先让 Ekko 完成一次 run，再执行 `/context`；否则它只是 local assembled history 的估算，不会刷新 cached system/tool context 的开销。

## 为什么

`/context` 里的 cached system/tool context 只在当前 Studio 进程的一次 run 后可用；重启后直接看它会漏掉或滞后 system/tool overhead，容易误判上下文余量。它不是 provider 当前上下文的精确测量。

## 原文依据

> After a restart, `/context` remains an estimate of local assembled history

来源：[docs/ekko-session-commands.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/ekko-session-commands.md)
