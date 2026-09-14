---
date: 2026-09-14
tool: codex
tool_name: Codex CLI
title: "用 /memories 控制单次对话记忆"
level: 进阶
source_title: "Computer History"
source_url: https://learn.chatgpt.com/docs/customization/computer-history.md
---

# 用 /memories 控制单次对话记忆

## 什么时候用得上

你让 Codex 借助 Computer History/Memories 追查最近工作，但这次对话包含敏感数据或只是一次性实验。此时先控制本次 chat 的 memories 使用和贡献，避免污染后续上下文。

## 怎么做

在单次 chat 中发送：

```text
/memories
```

然后在该控制里分别决定这个 chat 是否使用 local memories、是否贡献给 future memories。处理敏感或临时任务前，不要让本次对话贡献给 future memories。

## 为什么

Computer History 依赖 Memories，而 `/memories` 提供单 chat 粒度的记忆控制。若不限制贡献，这次对话可能进入未来 memories，污染后续 Codex/ChatGPT 的上下文，并扩大敏感信息的保留范围。

## 原文依据

> Use `/memories` to control whether an individual chat can use local memories

来源：[Computer History](https://learn.chatgpt.com/docs/customization/computer-history.md)
