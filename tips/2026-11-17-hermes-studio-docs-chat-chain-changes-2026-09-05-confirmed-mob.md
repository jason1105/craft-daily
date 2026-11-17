---
date: 2026-11-17
tool: hermes-studio
tool_name: Hermes Studio
title: "移动删除校验 id 与 deleted=true"
level: 进阶
source_title: "docs/chat-chain-changes/2026-09-05-confirmed-mobile-delete.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-confirmed-mobile-delete.md
---

# 移动删除校验 id 与 deleted=true

## 什么时候用得上

你正在接移动端日历/提醒单条删除，准备复用批量删除或兼容旧 App 时，先用返回契约和版本门槛卡住。否则很容易把单条删除做成越权或误删。

## 怎么做

把删除响应按下面 JSON 契约校验，id 必须等于 requested id，且 deleted 显式为 true：
```json
{
  "id": "requested id",
  "deleted": true
}
```
调用前确认已有 matching App update；older Apps do not support delete。不要放开 list/batch/series deletion、profile scope 或 background access。

## 为什么

只校验“删除成功”不够：结果必须匹配 requested id 并显式 deleted=true，才能避免误删和假成功。忽略版本门槛会让旧 App 调用失败；顺手放开批量/系列删除或 profile/background 范围则超出了这次单条删除的边界。

## 原文依据

> Delete results must match the requested id and explicitly report
deleted=true. No list/batch/series deletion, profile scope or background access
expansion.

来源：[docs/chat-chain-changes/2026-09-05-confirmed-mobile-delete.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-confirmed-mobile-delete.md)
