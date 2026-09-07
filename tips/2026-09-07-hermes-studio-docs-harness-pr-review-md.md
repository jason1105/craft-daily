---
date: 2026-09-07
tool: hermes-studio
tool_name: Hermes Studio
title: "矩阵 target 产物校验开关勿删"
level: 进阶
source_title: "docs/harness/pr-review.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/pr-review.md
---

# 矩阵 target 产物校验开关勿删

## 什么时候用得上

你在改一个 workflow；它里面的每个 matrix target 都有自己的 expected artifact list。提交前先确认产物校验配置仍然保留。

## 怎么做

只要每个 matrix target 还有自己的 expected artifact list，就保留这个配置：

```
fail_on_unmatched_files: true
```

改完再跑一遍文档中的校验命令：

```
npm run harness:check
```

## 为什么

文档把它放在 Release and CI 检查项里，并且只有在 matrix target 各有自己的产物列表时才要求保留。没有它，某个 target 的预期产物缺失时不会强制失败，合并门禁就等于少看了一道风险。

## 原文依据

> - `fail_on_unmatched_files: true` is preserved when each matrix target has its own
  expected artifact list.

来源：[docs/harness/pr-review.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/pr-review.md)
