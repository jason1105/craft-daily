---
date: 2026-10-22
tool: hermes-studio
tool_name: Hermes Studio
title: "登录 IP 锁死时清锁并重启"
level: 进阶
source_title: "README_zh.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/README_zh.md
---

# 登录 IP 锁死时清锁并重启

## 什么时候用得上

自托管 Ekko Studio Web 控制台连续登录失败触发 IP 锁，或默认管理员密码丢失，团队被挡在管理页外。用 CLI 在不重装、不清库的情况下恢复访问。

## 怎么做

先清掉持久化登录锁并重启正在运行的 Studio 服务：
```bash
ekko-studio-web clear-login-locks --restart
```
如果还需要把已存在的 `admin` 重置为默认超级管理员，再执行：
```bash
ekko-studio-web reset-default-login
```
只想清锁、稍后手动重启时可用：
```bash
ekko-studio-web clear-login-locks
```
锁文件位于 `${HERMES_WEB_UI_HOME:-~/.hermes-web-ui}/.login-lock.json`；登录后尽快修改默认账户和密码。

## 为什么

只删 `.login-lock.json` 不够：运行中的服务还会在内存保留锁定状态，必须重启才会释放。`reset-default-login` 则直接更新 Studio 账户数据库，把已存在的 `admin` 重置为 `123456` 并启用为超级管理员，避免重装或清库。

## 原文依据

> `clear-login-locks` 会删除 `${HERMES_WEB_UI_HOME:-~/.hermes-web-ui}/.login-lock.json`。如果服务正在运行，需要重启服务才能清理内存中的锁定状态。`reset-default-login` 会更新 Studio 账户数据库；如果已存在 `admin` 用户，则会把密码重置为 `123456`，并启用为超级管理员账户。

来源：[README_zh.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/README_zh.md)
