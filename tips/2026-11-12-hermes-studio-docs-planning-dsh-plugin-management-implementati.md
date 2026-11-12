---
date: 2026-11-12
tool: hermes-studio
tool_name: Hermes Studio
title: "跑插件测试先清 NODE_ENV 和 PORT"
level: 进阶
source_title: "docs/planning/dsh-plugin-management-implementation.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/dsh-plugin-management-implementation.md
---

# 跑插件测试先清 NODE_ENV 和 PORT

## 什么时候用得上

在本地或 CI 中运行 DSH 插件相关 vitest 套件时，当前 shell 可能继承了 Studio 服务的 NODE_ENV=production 或 PORT，导致测试行为异常。用 env -u 隔离环境后再执行。

## 怎么做

```sh
env -u NODE_ENV -u PORT npx vitest run tests/server/dsh-plugin-inventory.test.ts tests/server/dsh-plugins.test.ts tests/server/dsh-plugin-routes.test.ts tests/server/dsh-runtime-config.test.ts
```
运行前先清除这两个环境变量，再执行 vitest。

## 为什么

原文明确要求环境不应继承 Studio 服务的 NODE_ENV=production 或 PORT。如果不清理，vitest 可能读到生产端口或生产模式，导致测试结果不可信甚至挂起。

## 原文依据

> 环境不应继承 Studio 服务的 NODE_ENV=production 或 PORT。

来源：[docs/planning/dsh-plugin-management-implementation.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/dsh-plugin-management-implementation.md)
