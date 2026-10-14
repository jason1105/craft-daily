---
date: 2026-10-14
tool: hermes-studio
tool_name: Hermes Studio
title: "手动定价别漏 cache read/write"
level: 进阶
source_title: "docs/harness/usage-cost.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/usage-cost.md
---

# 手动定价别漏 cache read/write

## 什么时候用得上

你在自定义 relay 或未收录模型上发现成本总是 unknown，准备在 Usage 页 Model pricing 里手填价格。

## 怎么做

在 Usage 页的 Model pricing 对话框里，按 `Provider and model IDs must match exactly` 的要求把四类费率都填上；不要只填 ordinary input 和 output，否则缓存用量不会计价。可对照下面四项确认无遗漏：
```
ordinary input: <USD prices per million>
output: <USD prices per million>
cache read: <USD prices per million>
cache write: <USD prices per million>
```
注意价格在 recording time 生效，改价不会回溯历史行。

## 为什么

缺失的 cache 费率会让缓存部分保持未计价；部分手动价格不会从 catalog 借缺失费率。价格只在 recording time 应用，改价也不会回填历史行，所以上线前一次填全最省事。

## 原文依据

> Missing cache rates leave cached usage unpriced. Reasoning is already included in output tokens. Reported cost wins over configured rates, which win over models.dev rates. A partial manual price does not borrow missing rates from the catalog.

来源：[docs/harness/usage-cost.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/usage-cost.md)
