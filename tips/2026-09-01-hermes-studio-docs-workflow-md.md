---
date: 2026-09-01
tool: hermes-studio
tool_name: Hermes Studio
title: "局部更新用 PATCH，不必回传全图"
level: 进阶
source_title: "docs/workflow.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/workflow.md
---

# 局部更新用 PATCH，不必回传全图

## 什么时候用得上

当你只改了画布 viewport 或 workspace，想通过 API 更新 workflow，而不想把整个 nodes/edges 再传一遍。

## 怎么做

只发送要改的字段到 PATCH 路由：

```
PATCH /api/studio/workflows/:id
{
  "workspace": "/path/to/workspace",
  "viewport": { "x": -200, "y": 120, "zoom": 0.9 }
}
```

## 为什么

PATCH 是局部更新语义，只传要改的字段，避免把 nodes/edges 一并回传；在自动化调整画布位置或 workspace 时更干净。

## 原文依据

> Patch body supports partial updates:

来源：[docs/workflow.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/workflow.md)
