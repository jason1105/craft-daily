---
date: 2026-11-25
tool: hermes-studio
tool_name: Hermes Studio
title: "用 timeline.before 翻历史"
level: 进阶
source_title: "docs/person-display.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/person-display.md
---

# 用 timeline.before 翻历史

## 什么时候用得上

新 App 接入 Person 共享时间线后，做历史下拉或重连回看；某一页的 `messages` 可能为空，但 `timeline.has_more` 仍为真。若照旧按数组长度停止，就会丢掉更早的卡片和消息。

## 怎么做

新 App 在 `app.resume` 的 payload 里显式加 `timeline:true`：
```json
{session_id, id, timeline:true}
```
取更早页时带上：
```http
timeline=true&before=<opaque cursor>&limit=150
```
停止条件别用 `messages.length`；用 `timeline.has_more` 和 `timeline.before` 推进，即使 `messages` 为空也继续。合并 `personFlows.timeline`、`personFlows.cards` 与 `messages` 时最多保留 300 个引用；重连保留旧阅读窗口，回尾部显式重载最新页。

## 为什么

`messages` 为空不等于没有更早历史；用数组长度当停止条件会漏掉保留在时间线里的旧卡片/消息。改用 `timeline.has_more` 和 `timeline.before` 按游标推进，才能在空页时继续取到更早记录，并与原始分页字段兼容。

## 原文依据

> `timeline.before` to advance even when `messages` is empty.

来源：[docs/person-display.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/person-display.md)
