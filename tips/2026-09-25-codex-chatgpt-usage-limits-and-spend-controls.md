---
date: 2026-09-25
tool: codex
tool_name: Codex CLI
title: "先分清 Codex 用量与 workspace 限额"
level: 进阶
source_title: "ChatGPT usage limits and spend controls"
source_url: https://learn.chatgpt.com/docs/enterprise/usage-limits.md
---

# 先分清 Codex 用量与 workspace 限额

## 什么时候用得上

团队用 ChatGPT Enterprise/Business 的共享或采购额度覆盖 Codex，财务让你评估本季度成本归属；你需要先判断哪些 Codex 活动走 workspace 额度、哪些完全在体系之外，再决定要不要找管理员调 spend controls。

## 怎么做

先按原文给出的三个触发条件自查，全部命中才说明这套控件与你的 Codex 用量相关：组织协议使用 shared or purchased ChatGPT workspace credits；eligible Codex activity 会消耗这些 credits；管理员需要 user guardrails、workspace-level spend controls 或 usage notifications。

确认命中后，直接走「当前」流程（原文明确要求用 current procedures，别照着旧文章或别处抄的设置项操作）：

```
# Enterprise / Edu：usage limits and overages
https://help.openai.com/en/articles/20001001
# Business：credits and spend controls
https://help.openai.com/en/articles/20001155
# 成本口径单列：Codex pricing
https://learn.chatgpt.com/docs/pricing
```

要对齐完整的管理模型，读这篇，并给 URL 追加 `.md` 拿 Markdown 原文：

```
https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions
# Markdown 版本：documentation pages are available by appending `.md` to the page URL
```

## 为什么

把 workspace 的 usage/spend 控件当成 Codex 的通用限额系统，会导致两个方向的误判：一边以为它管得住全部 Codex 消耗，另一边对账时漏掉 Platform API 的账单。反过来，额度耗尽会暂停 eligible features 的访问，但它并不配置 feature entitlement 或权限，所以别拿它当权限治理或成本归属的唯一依据。

## 原文依据

> These controls aren't a universal Codex limit system and don't govern OpenAI API Platform billing.

来源：[ChatGPT usage limits and spend controls](https://learn.chatgpt.com/docs/enterprise/usage-limits.md)
