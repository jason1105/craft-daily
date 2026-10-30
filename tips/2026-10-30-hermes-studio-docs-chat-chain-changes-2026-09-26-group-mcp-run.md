---
date: 2026-10-30
tool: hermes-studio
tool_name: Hermes Studio
title: "Group MCP 核对每轮 auth.json"
level: 专家
source_title: "docs/chat-chain-changes/2026-09-26-group-mcp-run-credentials.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-26-group-mcp-run-credentials.md
---

# Group MCP 核对每轮 auth.json

## 什么时候用得上

当 Group Coding Agent 的 task-plan/clarification 被 interaction endpoint 拒绝，或长任务疑似 token 过期时，先核对本轮凭证而不是共享 worker 环境。

## 怎么做

把下面当作本轮请求的鉴权核对清单（不要改共享 worker 环境）：
```text
run context header: matching
profile: local profile
context_id: current request's context_id
task-plan and clarification bodies: exact context
auth.json: runtime/mcp-credentials/auth.json
```
若 `auth.json` 缺失、格式错误或 foreign-profile，按 fail closed 处理；不要回退到 environment tokens、tool-argument tokens 或 another session's profile token。长任务没有固定 one-hour cutoff，别按 1 小时换 token。

## 为什么

按每轮 `auth.json` 和精确 `context_id` 核对，才能命中 opaque capability；否则 missing/malformed/foreign-profile 会 fail closed，且不会回退到 environment/tool-argument/session token。长任务也不会被固定 one-hour cutoff 打断。

## 原文依据

> The MCP client reads the bound file for every request. A missing, malformed or
foreign-profile file fails closed, without falling back to environment tokens,
tool-argument tokens or another session's profile token.

来源：[docs/chat-chain-changes/2026-09-26-group-mcp-run-credentials.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-26-group-mcp-run-credentials.md)
