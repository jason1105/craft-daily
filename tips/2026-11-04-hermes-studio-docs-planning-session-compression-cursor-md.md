---
date: 2026-11-04
tool: hermes-studio
tool_name: Hermes Studio
title: "迁移压缩游标时保留旧快照"
level: 专家
source_title: "docs/planning/session-compression-cursor.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/session-compression-cursor.md
---

# 迁移压缩游标时保留旧快照

## 什么时候用得上

你准备上线 `compressed_through_message_id` 等新列，担心旧会话的压缩快照被清掉或被迫重新全量摘要。需要在不打断现有会话的前提下完成 schema 迁移。

## 怎么做

1. 只执行 schema 变更，保留 `last_message_index`，不要清空或重写既有快照：
```sql
ALTER TABLE sessions
  ADD COLUMN history_revision INTEGER NOT NULL DEFAULT 0;

ALTER TABLE chat_compression_snapshots
  ADD COLUMN compressed_through_message_id INTEGER;

ALTER TABLE chat_compression_snapshots
  ADD COLUMN history_revision INTEGER NOT NULL DEFAULT 0;

ALTER TABLE chat_compression_snapshots
  ADD COLUMN protected_head_through_message_id INTEGER;
```
2. 快照读取按原文优先级实现：
```text
1. When `compressed_through_message_id` is present, use the cursor path.
2. When the cursor is absent but `last_message_index` is present, use the
   existing index-based path unchanged.
3. When neither boundary exists, treat the session as having no snapshot.
```

## 为什么

这样旧快照在迁移期间继续有效，只会在该会话下一次真实压缩周期原地升级；若部署时清空或重写，会迫使旧会话重新生成摘要，违背原文的兼容性目标。

## 原文依据

> Do not clear or rewrite existing snapshots during schema migration. New snapshot
writes should use the cursor as the source of truth while continuing to populate
the legacy field where it is inexpensive to do so.

来源：[docs/planning/session-compression-cursor.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/session-compression-cursor.md)
