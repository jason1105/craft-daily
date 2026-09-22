---
date: 2026-09-22
tool: codex
tool_name: Codex CLI
title: "GitLab 项目在环境创建时选"
level: 进阶
source_title: "Codex cloud"
source_url: https://learn.chatgpt.com/docs/cloud.md
---

# GitLab 项目在环境创建时选

## 什么时候用得上

你刚把团队 GitLab 接到 Codex cloud，连接后却找不到仓库选择入口。别在连接阶段反复找，GitLab 的项目选择在创建 environment 时完成。

## 怎么做

进入 environment settings 创建 environment 时选择 GitLab project；GitHub 则是在连接时选择 repositories Codex can access。

```text
https://chatgpt.com/codex/settings/environments
https://learn.chatgpt.com/docs/third-party/gitlab
```

第一个链接进入 environment settings；第二个链接查看 GitLab setup、webhook permissions、merge request reviews。

## 为什么

GitHub 和 GitLab 的选择时机不同：GitHub 在连接时选 repositories，GitLab 在创建 environment 时选 project。照搬 GitHub 流程会在 GitLab 连接后找不到项目选择入口，导致创建环境时流程混乱。

## 原文依据

> For GitHub, choose the repositories Codex can access; for GitLab, select a project when you create the environment.

来源：[Codex cloud](https://learn.chatgpt.com/docs/cloud.md)
