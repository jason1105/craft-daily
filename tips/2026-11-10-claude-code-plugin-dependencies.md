---
date: 2026-11-10
tool: claude-code
tool_name: Claude Code
title: "用两个 --plugin-dir 联调插件与依赖"
level: 进阶
source_title: "Plugin dependencies"
source_url: https://code.claude.com/docs/en/plugins/dependencies.md
---

# 用两个 --plugin-dir 联调插件与依赖

## 什么时候用得上

你在同一个仓库里同时改一个插件和它依赖的另一个插件（比如共享的 MCP server 插件），想立刻验证改动，而不是每次发版再从 marketplace 装一遍。

## 怎么做

把依赖和插件两个目录都用 `--plugin-dir` 传给同一次启动，本地副本会直接满足 `dependencies` 条目：

```bash
claude --plugin-dir ./my-dependency --plugin-dir ./my-plugin
```

此时本地 `plugin.json` 不必写 `version`——版本约束不会对本地副本做校验。代价是：只要本地副本被禁用、或本次启动漏传它的 `--plugin-dir`，你的插件就会加载失败；错误里出现 `<name>@inline` 指的就是 `--plugin-dir` 那份副本。

## 为什么

否则你只能装 marketplace 上的版本，而带约束的依赖要求维护者打了 git tag 才能解析到，改一行依赖代码就得走一轮发布。用本地双目录加载，改完重启即生效，约束也不必为了调试而放宽。

## 原文依据

> The local copy of the dependency satisfies your plugin's dependency entry, so you don't need to install the dependency from its marketplace.

来源：[Plugin dependencies](https://code.claude.com/docs/en/plugins/dependencies.md)
