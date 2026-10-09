---
date: 2026-10-09
tool: hermes-studio
tool_name: Hermes Studio
title: "直聊定位：0 是合法坐标，别当空值"
level: 专家
source_title: "docs/chat-chain-changes/2026-08-31-agent-mobile-location.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-08-31-agent-mobile-location.md
---

# 直聊定位：0 是合法坐标，别当空值

## 什么时候用得上

你在直聊 Agent 中调用 `hermes_studio_use_mobile_location`，App 回传的坐标位于赤道或本初子午线，但 Agent 把 0 当成缺失而报 `location_invalid_result`。或者 App 未显式声明 wgs84，你希望 Hermes 自动转换，却直接失败。

## 怎么做

在直聊里用 `/chat-run` 触发请求后，App 回 `location.respond` 时按下面最小合法载荷返回（经纬度可为 0）：

```json
{
  "coordinateSystem": "wgs84",
  "latitude": 0,
  "longitude": 0
}
```

要点：`coordinateSystem` 必须显式写 `wgs84`；`latitude`/`longitude` 必须是有限数值，0 合法，不要传 `null`、字符串 `"0"`、布尔、数组或对象。若上游不是 wgs84，先在 App Relay 侧转好再响应。

## 为什么

Hermes 只接受显式 `coordinateSystem: wgs84` 和有限数值；缺少坐标系、其他坐标系或 null/字符串等强制转换值都会变成 `location_invalid_result`，不会帮你重标或转换。把 0 当无效还会漏掉赤道/本初子午线的合法坐标。

## 原文依据

> Successful responses must explicitly declare `coordinateSystem: wgs84` and
  provide finite numeric latitude/longitude within their valid ranges. Missing
  or other coordinate systems and coerced values (nulls, strings, booleans,
  arrays, or objects) resolve as `location_invalid_result`; coordinates are
  never silently relabeled or converted. Numeric zero remains valid.

来源：[docs/chat-chain-changes/2026-08-31-agent-mobile-location.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-08-31-agent-mobile-location.md)
