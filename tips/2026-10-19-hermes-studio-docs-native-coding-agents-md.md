---
date: 2026-10-19
tool: hermes-studio
tool_name: Hermes Studio
title: "Qoder BYOK 只能走 /model 向导"
level: 进阶
source_title: "docs/native-coding-agents.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/native-coding-agents.md
---

# Qoder BYOK 只能走 /model 向导

## 什么时候用得上

你想在 Studio 里用 Qoder 的 BYOK 自定义模型，却发现没有 scoped endpoint 注入入口，或者手改 settings.json 不生效。别继续绕配置，先按官方限制走账号向导。

## 怎么做

Qoder 只走 Global，不要给它配 scoped endpoint，也不要手改 settings.json。先在 Qoder CLI 的账号向导里执行：
```
/model
```
Studio 侧接入时用 managed transport：
```
qoder --acp
```

## 为什么

官方明确要求账号向导并禁用 settings.json 手配；强行注入 scoped endpoint 不会生效，反而浪费排错时间。Qoder 还是 global-only，只能复用既有账号/CLI 状态。

## 原文依据

> Qoder CLI has BYOK, but its [official guide](https://docs.qoder.com/cli/custom-models)
requires the account wizard and explicitly disallows manual settings.json
configuration. Studio therefore does not advertise arbitrary scoped endpoint
injection for it.

来源：[docs/native-coding-agents.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/native-coding-agents.md)
