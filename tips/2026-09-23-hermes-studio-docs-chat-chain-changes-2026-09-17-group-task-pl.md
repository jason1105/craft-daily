---
date: 2026-09-23
tool: hermes-studio
tool_name: Hermes Studio
title: "群任务卡排障：按 task_plan 快照定位"
level: 专家
source_title: "docs/chat-chain-changes/2026-09-17-group-task-plan-cards.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-17-group-task-plan-cards.md
---

# 群任务卡排障：按 task_plan 快照定位

## 什么时候用得上

群聊里多个 Agent 并发生成任务卡，卡片不更新或分页/重连后消失。你打开 tool trace 排查，但 Tool trace visibility does not hide cards，按 trace 找会跑偏。

## 怎么做

用 `role`/`tool_name` 过滤 group `message` transport 中的持久化快照；`plan.updated` 走 `ChatRunSocket` 只是事件，不是卡片存储本身。去重时用确定性 message ID：hash room、Agent session、plan identity。

```json
{
  "role": "tool",
  "tool_name": "task_plan",
  "run_id": "group response run"
}
```

Hermes group bridge 的 per-turn、plan-only MCP context 会在 bridge finalizer 过期；别把它当长期可查上下文。

## 为什么

Task cards 不进入模型会话历史、摘要、token 估算或 Agent mention routing，而是单独于普通 tool traces 渲染。若只查 tool trace 或会话历史，会误判卡片丢失；按 `task_plan` 快照和确定性 ID 才能正确关联并发、分页、重连场景。

## 原文依据

> with `role: tool` and `tool_name: task_plan`.

来源：[docs/chat-chain-changes/2026-09-17-group-task-plan-cards.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-17-group-task-plan-cards.md)
