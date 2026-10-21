---
date: 2026-10-21
tool: codex
tool_name: Codex CLI
title: "别信preflight的archiveDir"
level: 进阶
source_title: "Codex Security TypeScript SDK"
source_url: https://learn.chatgpt.com/docs/security/sdk.md
---

# 别信preflight的archiveDir

## 什么时候用得上

同一 outputDir 反复扫描并开启 archiveExisting 时，需要把真实归档目录写进审计日志或后续清理。preflight 返回的 archiveDir 只是命名预览，直接使用会指错路径。

## 怎么做

在 `run` 的回调里取实际归档路径，不要用 `preflight` 的预览值：

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});
```

## 为什么

preflight 的 archiveDir 只预览归档命名；run 会生成自己的唯一目标，最终路径可能不同。用 onOutputArchived 才能拿到实际路径，否则审计日志或清理操作会指向错误目录。

## 原文依据

> The returned `archiveDir` previews the archive naming.

来源：[Codex Security TypeScript SDK](https://learn.chatgpt.com/docs/security/sdk.md)
