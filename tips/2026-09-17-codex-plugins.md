---
date: 2026-09-17
tool: codex
tool_name: Codex CLI
title: "CLI 装完插件必须新开会话"
level: 进阶
source_title: "Plugins"
source_url: https://learn.chatgpt.com/docs/plugins.md
---

# CLI 装完插件必须新开会话

## 什么时候用得上

你在 Codex CLI 里用插件浏览器装好了一个带 skills / MCP tools 的插件，回到当前会话直接让它干活，却发现这些能力和工具完全不存在，第一反应是怀疑安装失败或权限没配好。

## 怎么做

在 Codex CLI 中打开插件浏览器，从 configured marketplace 安装插件后，**不要**在当前会话里继续尝试调用它，而是重新起一个 session 再用：

```bash
# 1. 打开插件浏览器
/plugins

# 2. 在浏览器里从 configured marketplace 安装插件

# 3. 退出当前对话，start a new session
#    然后才能使用该插件 bundled 的 skills 或 tools
```

如果插件还带 **Hooks**，额外注意：hook scripts 必须 already available in the execution environment；在 web 上安装插件并不会把脚本 deploy 到你的环境，需要脚本已在环境中（企业可由 admin 通过 MDM 下发），并在运行前 review 并 trust 这些 hooks。

## 为什么

插件安装的动作只改变了后续会话的可用能力集合，当前会话已经加载的 skills 和 MCP tools 不会热更新，所以你会在旧会话里得到一个「怎么都没有」的假象，白白去排查 marketplace 或鉴权。另外 hooks 是执行环境侧的东西，web 端点击安装不等于脚本就位，混在一起排查会非常耗时。

## 原文依据

> In Codex CLI, enter `/plugins` to open the plugin browser. Install a plugin from a configured marketplace, then start a new session before using its bundled skills or tools.

来源：[Plugins](https://learn.chatgpt.com/docs/plugins.md)
