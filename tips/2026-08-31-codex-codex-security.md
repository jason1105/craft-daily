---
date: 2026-08-31
tool: codex
tool_name: Codex CLI
title: "CLI 与插件用同一扫描器，放心进 CI"
level: 进阶
source_title: "Codex Security"
source_url: https://learn.chatgpt.com/docs/security.md
---

# CLI 与插件用同一扫描器，放心进 CI

## 什么时候用得上

当你想在 CI 或 commit 前自动跑安全扫描，而不是只坐在桌面插件里手动点扫描时。

## 怎么做

先用 `npx @openai/codex-security --help` 确认 CLI 可执行；按 CLI quickstart 做 setup、preflight、首次本地扫描。之后在 CI 里用同一 CLI：review pull-request changes、preserve artifacts、upload SARIF、set a severity policy。需要时可 add your architecture and security policies，并 set an estimated cost limit。

```bash
npx @openai/codex-security --help
```

## 为什么

桌面插件和 CLI 共用同一个扫描器，所以在 CI/终端里跑 CLI 不会出现与桌面插件口径不一致的结果。若只依赖桌面界面，批量仓库、历史记录和自动化门槛都会受限。

## 原文依据

> Use the same scanner as the plugin across repositories and over time.

来源：[Codex Security](https://learn.chatgpt.com/docs/security.md)
