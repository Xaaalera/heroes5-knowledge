---
content_type: explanation
status: draft
faction: academy
title: What a deployment projection shows
lang: en
section: players
kicker: HEROES V · UNIVERSE
translation: players/deployment-preview/
description: What a deployment projection shows
updated: '2026-09-24'
---
# What a deployment projection shows

A projection marks **a creature's predicted position and movement area**. It uses a known type without revealing hidden guard quantities or upgrades. This is an experimental mod for the inspected Universe build; no universal release is available.

## Controls

| Action | Result |
|---|---|
| Hover | Movement area of the selected reference type |
| First RMB | Full card of the base or already known upgrade |
| Repeated RMB when upgrade is unknown | Base → upgrade → alternative upgrade → base |
| Double LMB | Native detailed creature window |
| Detailed-window arrows | Switch available variants |
| Start | Remove projections, cards and highlighting |

If the upgrade is known, the card shows it. Figures are opaque with a subtle warm glow. The current version has no additional lower arrows.

## Example: gremlin and upgrade

[![Base gremlin: speed 3, health 5](../../assets/preview/gremlin-base.png)](../../assets/preview/gremlin-base.png)

[![Master gremlin: speed 5, health 6](../../assets/preview/gremlin-upgrade.png)](../../assets/preview/gremlin-upgrade.png)

Switching changes speed from **3 to 5** and health from **5 to 6**. The movement area is recalculated with the card.

Stats are not hardcoded for the pictured creatures. `Speed`, `Flying` and `CombatSize` come from the [selected type definition](../reference/creatures.md); the native descriptor supplies the name and card fields. The cache key includes the type, preventing reuse of the previous upgrade's movement area.

## Why the detailed window shows “1”

The reference contains one creature without a hero or real combat stack. This **does not mean the guard has one enemy**. The card also does not establish effects that apply in an actual battle.

## When prediction and battle differ

The prototype assumes one stack per publicly known type. The game can split it, change the composition or choose a special strategy.

In one observed example, a single peasant projection before Start became **three combat stacks of 10**. Splitting explains the mismatch, not cell size. [How the game builds the army](army-placement.md).

**Checks on September 21–23, 2026:** the user confirmed opening and cycling with physical RMB. Holding RMB remains unconfirmed; background window messages do not replace that check. The prediction does not read hidden quantities, final upgrades or the completed combat army as inputs.
