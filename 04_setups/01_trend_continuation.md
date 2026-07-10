# 趋势延续 Setup

> **状态：Learning / Non-normative**
>
> 用于概念学习；文档职责与执行权威入口见 [`README.md`](../README.md#权威层级)。

## 它解决什么问题

趋势延续 setup 试图顺着当前控制方入场。典型场景是强趋势或有效通道中出现回调，反方尝试失败，原趋势恢复。

## 常见背景

- Always In 方向清晰。
- 回调较浅或没有破坏结构。
- 反方信号缺乏跟进。
- 出现 H2/L2、wedge pullback、double bottom bull flag 或 double top bear flag。
- 到前高、前低、有效的 Leg 1 = Leg 2 projection 或最近 magnet 有足够现实空间；更远的量度目标只是条件式延伸目标。

## 入场和管理

趋势延续常用 stop entry，因为交易者希望市场先证明它恢复趋势。强趋势中普通 signal bar 也可能足够；弱通道中则需要更重视位置和目标空间。

止损通常放在回调结构外。第一现实目标先看前高前低、前 swing、最近 magnet，或已有明确参照与投射起点的 Leg 1 = Leg 2；只有趋势持续强并持续获得跟进时，才启用更远的 spike、旗形或其他 measured move 作为延伸目标或 runner 依据。

## 常见失败

- 把 trading range 中的普通反弹当趋势恢复。
- 在宽通道边缘追随。
- 忽略合理止损太远。
- 把 scalp 入场改成 swing 管理。

来源审计见 `reference/official_sources.md` 中的 `SRC-10-PATTERNS`、`SRC-GLOSSARY`。
