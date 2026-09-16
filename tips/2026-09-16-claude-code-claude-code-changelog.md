---
date: 2026-09-16
tool: claude-code
tool_name: Claude Code
title: "开网关提示头，按 agent 归因流量"
level: 进阶
source_title: "Claude Code changelog"
source_url: https://code.claude.com/docs/en/changelog.md
---

# 开网关提示头，按 agent 归因流量

## 什么时候用得上

你们把 Claude Code 的流量统一收敛到自建 LLM 网关做审计、限流和计费，但网关只看得到模型名与 token 数，分不清一条请求来自主 agent、sub-agent 还是上下文压缩流程。

## 怎么做

在网关侧链路生效的环境里打开开关（默认不发送）：

```bash
export CLAUDE_CODE_GATEWAY_HINT_HEADERS=1
```

开启后请求上会多出这些头，网关按需读取即可：

`x-claude-code-request-class`、`x-claude-code-agent-type`、`x-claude-code-prev-tool-durations`、`x-claude-code-compaction`、`x-claude-code-context-compacted`

## 为什么

不开启时网关拿不到任何请求语义，sub-agent、压缩等流量会和正常任务混在同一个桶里，限流和成本归因只能按总量粗暴切分。开启后可以按 agent type / request class 做分流与归因，还能识别出 compaction 请求，避免把上下文压缩的开销误记到业务任务上。

## 原文依据

> Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`

来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)
