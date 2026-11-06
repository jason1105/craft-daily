---
date: 2026-11-06
tool: codex
tool_name: Codex CLI
title: "CI 中用环境变量令牌跑 Codex"
level: 进阶
source_title: "Service accounts"
source_url: https://learn.chatgpt.com/docs/enterprise/service-accounts.md
---

# CI 中用环境变量令牌跑 Codex

## 什么时候用得上

在 CI runner 或共享/临时 runner 上执行 headless Codex 任务，不能依赖员工个人账号，也不应把登录凭据落盘。用服务账号访问令牌通过环境变量注入即可无浏览器运行。

## 怎么做

确保 Codex CLI 版本不低于 `0.142.0`，在 CI 的 secret manager 或 runner secret 中注入服务账号令牌，然后直接执行：

```bash
export CODEX_ACCESS_TOKEN="<service-account-access-token>"
codex exec --json "Inspect this repository and summarize its current state."
```

共享或临时 runner 上保持这种环境变量方式，不要改用 `codex login --with-access-token` 把凭据保存到本地。

## 为什么

环境变量方式让每次运行都代表服务账号而非某个人，并且不会在共享/临时 runner 上留下可复用的本地登录态。若改用 login 保存凭据，临时环境被复用时会增加凭据泄露风险。

## 原文依据

> This saves the credential locally. On shared or temporary runners, use `CODEX_ACCESS_TOKEN` without saving a login.

来源：[Service accounts](https://learn.chatgpt.com/docs/enterprise/service-accounts.md)
