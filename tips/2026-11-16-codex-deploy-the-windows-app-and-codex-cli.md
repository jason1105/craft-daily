---
date: 2026-11-16
tool: codex
tool_name: Codex CLI
title: "Intune 卸载命令勿用环境变量"
level: 专家
source_title: "Deploy the Windows app and Codex CLI"
source_url: https://learn.chatgpt.com/docs/enterprise/windows-deployment.md
---

# Intune 卸载命令勿用环境变量

## 什么时候用得上

在用 Intune 的 Win32 工作流分发离线 MSIX，并为 Codex 配置安装/卸载命令时，卸载字段常被随手写成 %SystemRoot%，结果 Intune 不展开变量导致失败。默认 Windows 目录为 C:\Windows 的设备可直接用字面 Sysnative 路径规避。

## 怎么做

在 Intune 的 Windows app (Win32) 设置中分别填入：

```text
Install command:
%SystemRoot%\Sysnative\WindowsPowerShell\v1.0\powershell.exe -NoProfile -File .\Install-ChatGPT.ps1

Uninstall command:
C:\Windows\Sysnative\WindowsPowerShell\v1.0\powershell.exe -NoProfile -File .\Uninstall-ChatGPT.ps1
```

卸载字段不要写 `%SystemRoot%`；若 Windows 目录不是 `C:\Windows`，换成实际目录。

## 为什么

Intune 的卸载字段不会展开 `%SystemRoot%`，写成变量会失去可靠的 PowerShell 路径；字面 `C:\Windows\Sysnative\...` 路径还能从 32 位命令上下文选择 64 位 Windows PowerShell。若 Windows 目录不同，替换为实际目录，或按文档改用 wrapper script。

## 原文依据

> Do not substitute `%SystemRoot%` in the uninstall field: Intune does not expand environment variables there.

来源：[Deploy the Windows app and Codex CLI](https://learn.chatgpt.com/docs/enterprise/windows-deployment.md)
