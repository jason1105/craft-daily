---
date: 2026-11-03
tool: codex
tool_name: Codex CLI
title: "AIRS 失败时改为 Block prompts"
level: 进阶
source_title: "Prisma AIRS"
source_url: https://learn.chatgpt.com/docs/enterprise/prisma-airs.md
---

# AIRS 失败时改为 Block prompts

## 什么时候用得上

安全策略要求所有受覆盖的 Codex 提示在到达模型前都必须获得扫描决策。默认 On AIRS failure 是 Allow prompts，AIRS 不可用时会放行未完成扫描的请求。

## 怎么做

在 Admin Console 的 **Policy & security > External guardrails > Prisma AIRS** 中完成连接配置，并把失败行为显式改为阻断；保存后必须再开启扫描。

```text
Admin Console → Policy & security → External guardrails → Prisma AIRS
Endpoint URL: https://service.api.aisecurity.paloaltonetworks.com
Enforcement mode: Block
On AIRS failure: Block prompts
Save connection → Test connection → Turn on Enable Prisma AIRS
```

若数据驻留要求使用其他区域，Endpoint URL 换成文档表中对应区域的端点。

## 为什么

默认 Allow prompts 在 Prisma AIRS 不可用或未响应时继续执行，等于 fail-open；要求每个覆盖提示都获得扫描决策时应改用 Block prompts。另注意 Save connection 不会启用扫描，必须 Turn on Enable Prisma AIRS。

## 原文依据

> - **Block prompts**: Stop the prompt until Prisma AIRS can scan it.

来源：[Prisma AIRS](https://learn.chatgpt.com/docs/enterprise/prisma-airs.md)
