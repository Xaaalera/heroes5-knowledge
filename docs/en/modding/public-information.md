---
content_type: explanation
status: draft
faction: dungeon
title: Inputs available for a public prediction
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/public-information/
description: Inputs available for a public prediction
updated: '2026-09-24'
---
# Inputs available for a public prediction

A pre-battle prediction can use **visible creature types, the displayed quantity range and reference stats**. It cannot use the exact hidden army composition, even if the quantity is rounded after reading it.

## What is known before combat

| Source | Available information | Still unknown |
|---|---|---|
| Tooltip portrait | Creature type | Number of combat stacks after splitting |
| Displayed quantity range | Lower and upper calculation bounds | Exact quantity |
| Creature XDB | Properties of that type | Hidden stack's upgrade |
| Bank AG_INFO/DefaultStats | Possible guard compositions | Selected tier of this object |
| Combat Start coordinates | Actual placement for comparison | This is an outcome, not a prediction input |

For example, a displayed range supports calculations at both endpoints. It does not identify one exact quantity inside the range.

Inputs must belong to **the current attack target**. The inspected integration binds the target description to the new battle grid of the attack command. A previous hover, unknown portrait or ambiguous portrait is insufficient.

## Can the built-in danger rating be used?

The danger text uses `MonsterTooltip/Danger.(WindowTextView).xdb` and `ARMY_DANGER_*` strings. The origin of all rating inputs remains unknown, including whether they are limited to information available to the player.

The custom battle assessor is also unfinished. Its prototype button accepted clicks and returned a diagnostic response. Victory, loss and range-based risk calculations remained a plan.

## Checking recognized text

OCR extracts text from an image, but can miss a readable card:

- A synthetic “Imps 20–30” example was recognized. This did not test the game font.
- One full golem-card attempt returned only “00.”. Processing separate image regions recovered the name and fields.
- Reject a range such as `40–32` as an error; do not silently swap its bounds.

Missing OCR text therefore does not establish that a card is absent from the screen.

**Evidence:** MonsterTooltip/AG_INFO inspection and button/OCR checks on September 21–23, 2026. [Creatures](../reference/creatures.md) · [Banks](../reference/banks.md) · [Projections](../players/deployment-preview.md).

[Research record](../reference/research-diary.md#assessor-inputs).

The environment uses [game-ui.ps1](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game-ui.ps1) for capture and recognition; see the [devkit command reference](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md#capture-input-and-shutdown) for parameters.
