---
date: 2026-10-20
tool: claude-code
tool_name: Claude Code
title: "先 pilot 估算月成本再全量"
level: 进阶
source_title: "Code Review costs and usage"
source_url: https://code.claude.com/docs/en/code-review-costs.md
---

# 先 pilot 估算月成本再全量

## 什么时候用得上

准备给多个仓库开启 Code Review，需要先给出可解释的月度预算，而不是等默认 After every push 跑完才看账单。用少量代表仓库做 pilot，再反推全量成本。

## 怎么做

1. 在 `https://claude.ai/admin-settings/usage` 为 Claude Code Review 服务设置月度 spend limit。
2. 在 `https://claude.ai/admin-settings/claude-code#code-review` 给少量代表仓库开启 Code Review，把 **Review runs** 设为以下之一：
```text
Once after PR creation
```
或
```text
Manual (@claude review)
```
3. 跑若干次后，到 **Admin settings > Claude Code** 的 **Repositories** 表读 **Average cost** 列；用该平均值乘仓库每月 pull request 数。若仓库用 **After every push**，再乘每个 pull request 的典型 push 数。

## 为什么

这样先用小样本得到本组织真实单次评审成本，避免默认 After every push 把成本按 push 次数放大。原文还提醒 Average cost 会随 pull request 大小和 review level 变化，所以 pilot 仓库要尽量代表真实变更。

## 原文依据

> Multiply that average by the number of pull requests the repository opens in a month. For **After every push**, multiply again by the typical number of pushes per pull request.

来源：[Code Review costs and usage](https://code.claude.com/docs/en/code-review-costs.md)
