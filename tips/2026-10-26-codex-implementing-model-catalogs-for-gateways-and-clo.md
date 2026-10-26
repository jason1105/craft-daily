---
date: 2026-10-26
tool: codex
tool_name: Codex CLI
title: "透传 client_version 回源"
level: 进阶
source_title: "Implementing model catalogs for gateways and clouds"
source_url: https://learn.chatgpt.com/docs/model-catalogs.md
---

# 透传 client_version 回源

## 什么时候用得上

你在实现网关的模型目录，需要同时服务多个 Codex 版本，并希望保留上游模型的 instructions、reasoning 默认值和上下文限制。直接打包一份 models.json 容易随版本漂移。

## 怎么做

按 Codex 请求里的 `client_version` 回源拉取 OpenAI 默认 catalog，再单独叠加你的 override；先解析完整响应（含顶层 `models` 数组）。

```bash
curl --fail --silent --show-error \
  'https://chatgpt.com/backend-api/codex/models?client_version=0.162.1' \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

把 `0.162.1` 换成当前 Codex 请求携带的版本值。

## 为什么

bundled models.json 只是发布快照，不能代表当前默认；不按请求版本回源会拿到过时或不匹配的 schema。public /v1/models 也不提供这份 catalog。

## 原文依据

> The bundled file is a release snapshot. Fetch current defaults before producing your catalog.

来源：[Implementing model catalogs for gateways and clouds](https://learn.chatgpt.com/docs/model-catalogs.md)
