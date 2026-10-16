---
date: 2026-10-16
tool: codex
tool_name: Codex CLI
title: "Mac 合盖远程访问需外接显示器"
level: 进阶
source_title: "Remote connections"
source_url: https://learn.chatgpt.com/docs/remote-connections.md
---

# Mac 合盖远程访问需外接显示器

## 什么时候用得上

你用 Mac 笔记本作为 Codex/ChatGPT 远程 host，离开工位后想用手机继续任务。直接合盖会让远程连接断掉，除非按下面方式保持可用。

## 怎么做

在作为 host 的 Mac 上打开 ChatGPT desktop app，进入：
```text
Settings > Connections > Control this Mac or PC
```
审批远程访问。再到：
```text
Settings > Connections
```
选择 keep the computer awake。Mac 笔记本若要合盖时仍可远程访问，必须接电源并外接显示器；不要选择 Sleep。

## 为什么

否则电脑 sleep、丢网或关闭 app 时，远程访问会停止直到重新可用；合盖但没有外接显示器也不行，Sleep 仍会停止远程访问。提前配置能避免你在手机上看到连接不可用。

## 原文依据

> With the lid closed, connect an external display as well.

来源：[Remote connections](https://learn.chatgpt.com/docs/remote-connections.md)
