---
date: 2026-11-23
tool: claude-code
tool_name: Claude Code
title: "失败评审用顶层评论重触发"
level: 进阶
source_title: "Troubleshoot Code Review"
source_url: https://code.claude.com/docs/en/code-review-troubleshooting.md
---

# 失败评审用顶层评论重触发

## 什么时候用得上

自动 Code Review 超时或失败，或你希望重跑一次但不想让该 PR 从此订阅后续 push 时，需要手动重触发评审。

## 怎么做

在 PR 上新建一条顶层评论，命令必须位于评论开头：
```
@claude review
```
若 PR 不是来自 fork，也可在 GitHub 的 Checks 标签页对 Claude Code Review check 点击 Re-run；它覆盖当前 head commit，且同样不会订阅后续 push。

## 为什么

顶层评论会启动一次全新评审，并避免把 PR 订阅到未来 push；发成 inline comment、review body 或编辑旧评论都不符合触发条件。失败/超时场景下先看 check run summary，若已提示自动排队则无需再操作。

## 原文依据

> post it as a top-level comment on the pull request. This starts a fresh review without subscribing the pull request to future pushes.

来源：[Troubleshoot Code Review](https://code.claude.com/docs/en/code-review-troubleshooting.md)
