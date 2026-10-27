---
date: 2026-10-27
tool: hermes-studio
tool_name: Hermes Studio
title: "云端批处理需双端能力位同时开启"
level: 进阶
source_title: "docs/chat-chain-changes/2026-09-05-remote-agent-event-batching.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-remote-agent-event-batching.md
---

# 云端批处理需双端能力位同时开启

## 什么时候用得上

你在联调云端中转的受邀 Agent 流式输出，房间显示了部分 reasoning 后却可能缺少最终回复。先核对两端能力位，而不是先怀疑 30 秒 acknowledgement 超时。

## 怎么做

目标 Studio 声明：
```
capabilities: ['agent.events.v1']
```
云端声明：
```
relayCapabilities: ['agent.events.v1']
```
只开目标端仅对直连生效；云端 batching 必须两个 flag 同时存在。

## 为什么

否则新 source 会回退到 legacy `agent.event` 包，云端 batching 不会启用；排障时容易误判为网络或超时问题。

## 原文依据

> Cloud batching requires both flags; direct batching requires only the target flag.

来源：[docs/chat-chain-changes/2026-09-05-remote-agent-event-batching.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-remote-agent-event-batching.md)
