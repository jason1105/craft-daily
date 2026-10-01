---
date: 2026-10-01
tool: hermes-studio
tool_name: Hermes Studio
title: "JEV 出站请求按完整 UTF-8 字节数限流"
level: 进阶
source_title: "docs/planning/jev-sidecar-pr0-design.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/jev-sidecar-pr0-design.md
---

# JEV 出站请求按完整 UTF-8 字节数限流

## 什么时候用得上

你在为 JEV provider 加旁路调用，请求里会带中文或工具证据，既怕超限又不想悄悄删内容。此时应先对完整 request 做 UTF-8 字节校验，而不是只检查 state。

## 怎么做

在发 provider 前，将有效 model 写入完整 request 后序列化，并用以下判断作为发送门限：

```ts
Buffer.byteLength(serialized, 'utf8') <= 64_000
```

超限返回 `input_too_large`；序列化失败返回 `invalid_input`。

## 为什么

只量 state 会漏掉 model、模板等包装内容；为凑大小先删中文/工具证据，会让模型判断失真。超限应返回 input_too_large，且零 provider 请求。

## 原文依据

> 将有效 model 写入完整 request 后序列化，`Buffer.byteLength(serialized, 'utf8') <= 64_000` 才发送；不能只量 state，也不能先删减中文/工具证据再获得可靠判断。

来源：[docs/planning/jev-sidecar-pr0-design.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/jev-sidecar-pr0-design.md)
