---
date: 2026-10-28
tool: claude-code
tool_name: Claude Code
title: "网关别按完整 URL 匹配推理请求"
level: 进阶
source_title: "Claude Code gateway compatibility guide"
source_url: https://code.claude.com/docs/en/llm-gateway-protocol.md
---

# 网关别按完整 URL 匹配推理请求

## 什么时候用得上

你正在给公司 LLM 网关写路由或日志过滤规则，Claude Code 以 Anthropic Messages 格式接入。若规则按完整 URL 匹配，带 `?beta=true` 的推理请求容易被漏掉。

## 怎么做

在网关路由或日志过滤规则中，不要匹配完整 URL；用下面两行确认实际请求与应匹配的 path：
```
/v1/messages?beta=true
/v1/messages
```
第一行是 Claude Code 实际发出的推理请求，第二行是路由/日志过滤应命中的 path。

## 为什么

完整 URL 含 `?beta=true`，按完整 URL 匹配会把实际请求和 `/v1/messages` 规则错开；按 path 匹配才稳定覆盖推理请求。不这样，网关规则可能看似正确却漏掉 Claude Code 的推理流量。

## 原文依据

> Match on the path, not the full URL:

* Inference requests post to `/v1/messages?beta=true`

来源：[Claude Code gateway compatibility guide](https://code.claude.com/docs/en/llm-gateway-protocol.md)
