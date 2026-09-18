---
date: 2026-09-18
tool: hermes-studio
tool_name: Hermes Studio
title: "启动不写配置，显式选默认才落盘"
level: 进阶
source_title: "docs/opencode-free.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/opencode-free.md
---

# 启动不写配置，显式选默认才落盘

## 什么时候用得上

你看到 opencode-free 已在启动时列出，于是以为默认模型会随 Studio 启动自动持久化；但重启后发现默认模型仍是旧的。要在默认模型选择里显式选它，才会写配置。

## 怎么做

不要等启动去改 `config.yaml`、`.env` 或默认模型；到 Studio 的默认模型选择里显式选中 `opencode-free`。只有这个动作会写入以下配置（并带上 selected model ID）：

```yaml
model.provider: opencode-free
```

之后可在 `config.yaml` 中确认；启动本身不会写它。

## 为什么

如果期待启动自动改配置，你会一直看不到 `model.provider: opencode-free` 落盘，默认模型也不会持久化。把显式默认模型选择当作唯一写入点，能避免在 `.env` 或 `config.yaml` 上做无效排查。

## 原文依据

> Startup does not modify Hermes `config.yaml`, `.env`, or the default model. Only
an explicit default-model selection writes `model.provider: opencode-free` and
the selected model ID.

来源：[docs/opencode-free.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/opencode-free.md)
