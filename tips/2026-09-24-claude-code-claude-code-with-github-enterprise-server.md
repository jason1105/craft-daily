---
date: 2026-09-24
tool: claude-code
tool_name: Claude Code
title: "GHES App 权限和事件需手动补"
level: 专家
source_title: "Claude Code with GitHub Enterprise Server"
source_url: https://code.claude.com/docs/en/github-enterprise-server.md
---

# GHES App 权限和事件需手动补

## 什么时候用得上

你在 GHES 上已经创建过 Claude 的 GitHub App，后来需要新增权限或 webhook 事件。旧安装不会自动获得这些变更。

## 怎么做

在 GHES 实例的 GitHub App 设置里补齐缺失权限和事件；改完后，GitHub 会要求每个 installation 的 owner 批准，批准前安装仍保留旧权限。

```text
Contents: Read and write
Pull requests: Read and write
Issues: Read and write
Checks: Read and write
Actions: Read
Commit statuses: Read
Repository hooks: Read and write
Metadata: Read
Organization members: Read
pull_request
issue_comment
pull_request_review_comment
pull_request_review
check_run
status
```

## 为什么

GitHub 只在创建 App 时应用 manifest，旧 App 会一直保留创建时的权限和事件。不手动补齐并让安装 owner 批准，新增功能会因缺少权限或事件而不可用。

## 原文依据

> GitHub applies a manifest only when the app is created, so an app created from an earlier version of the manifest keeps the permissions and events it was created with.

来源：[Claude Code with GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server.md)
