---
date: 2026-11-18
tool: claude-code
tool_name: Claude Code
title: "定时任务用 Worktree 隔离脏工作区"
level: 进阶
source_title: "Schedule recurring tasks in Claude Code Desktop"
source_url: https://code.claude.com/docs/en/desktop-scheduled-tasks.md
---

# 定时任务用 Worktree 隔离脏工作区

## 什么时候用得上

你在活跃仓库上跑每日代码审查，工作区常有未提交改动，导致每次审查结果被脏状态干扰。

## 怎么做

新建本地任务时，跳过 Trigger，先在 Advanced settings 的 General 页打开 Only on this computer 并选择 Local folder；创建后在任务详情页点铅笔进入 Edit 表单勾选 Worktree。该 checkbox 仅在任务 folder 是 Git repository 时可用。配置清单：
```
Advanced settings
General
Only on this computer
Local folder
Edit form
Worktree
```

## 为什么

不勾 Worktree 时，本地定时任务默认直接跑当前 working directory 的状态，包括未提交改动；勾选后每次运行获得独立 isolated Git worktree，审查/审计不会被脏工作区污染。

## 原文依据

> To give each run its own [isolated Git worktree](https://code.claude.com/docs/en/desktop.md#run-a-session-in-its-own-worktree) instead, select **Worktree** in the task's [**Edit** form](#manage-scheduled-tasks) after you create it.

来源：[Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks.md)
