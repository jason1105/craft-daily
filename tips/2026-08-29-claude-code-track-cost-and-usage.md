---
date: 2026-08-29
tool: claude-code
tool_name: Claude Code
title: "流式输入成本：读最新 result 别逐条相加"
level: 进阶
source_title: "Track cost and usage"
source_url: https://code.claude.com/docs/en/agent-sdk/cost-tracking.md
---

# 流式输入成本：读最新 result 别逐条相加

## 什么时候用得上

在 streaming input mode 下跑 Agent，一个 query() 里有多轮用户输入，还可能出现 /clear 等重置操作。这时需要准确统计整次调用成本，而不是把每个 result 的 usage 累加起来。

## 怎么做

不要对每个 result 的 usage 求和，直接读最后一个 result 的 total_cost_usd（Python 中先判空）。一旦发送以下命令，运行中的累计成本会从头开始：
```
/clear
/reset
/new
```
若要统计含多次清除的整段 query()：把每次 /clear 之前的最后一条 result 的 total_cost_usd，加上整次调用最终 result 的 total_cost_usd；其他中间 result 都会被后续 result 取代，不要重复加。代码里可用 SDKConversationResetMessage（TypeScript）或 ConversationResetMessage（Python）识别重置点。

## 为什么

在 streaming input mode 下，usage 只覆盖当前轮次，而 total_cost_usd 才是整次调用到当前的运行总和；逐条相加会重复计算已被后续 result 取代的中间轮次。只有按 /clear 分段的边界结果相加，才能得到跨重置的整段成本。

## 原文依据

> In a call where your app never sends `/clear`, `/reset`, or `/new`, read the latest result for call totals rather than summing across results.

来源：[Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking.md)
