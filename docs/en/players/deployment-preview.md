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

The experimental projection shows a **hypothesized position for a publicly known creature type**, not an actual hidden stack. If one type splits, projection and actual stack counts can differ.

| Action | Checked prototype behavior |
|---|---|
| Hover | Movement area for the selected reference type |
| First RMB | Full base/known-type card |
| Repeated RMB for an uncertain grade | Base → upgrade → alternate → base |
| Double LMB | Native detailed creature window |
| Detail-window arrows | Cycle available reference variants |
| Start | Release projections, cards and highlights |

Physical RMB holding remains separately unconfirmed. Extra bottom arrows were an experiment and removed. A known upgraded type should not imply all grades are equally possible.

## Stats come from the selected definition

[![Base gremlin card: speed 3, health 5](../../assets/preview/gremlin-base.png)](../../assets/preview/gremlin-base.png)

[![Master gremlin card: speed 5, health 6](../../assets/preview/gremlin-upgrade.png)](../../assets/preview/gremlin-upgrade.png)

In this control, base speed is3 and upgraded speed 5. Switching updates both the card and movement calculation because the cache key includes creature type. Speed/Flying/CombatSize come from [definitions](../reference/creatures.md); the native descriptor supplies text/stats. This is not a three-creature hardcoded stat table.

The reference descriptor represents one creature without a hero or real combat stack. Quantity 1 in its detailed window does not reveal a single enemy; real combat effects are not established by this reference.

## Why it does not fully reproduce the game

Inputs are public types and geometry, excluding hidden quantities, final upgrades and actual defender stacks. The basic assumption is one stack per public type; special strategies/splitting/composition changes can differ.

A live solo control showed one peasant projection before Start and three actual stacks of10 afterwards. That demonstrates the assumption's limit, not incorrect cell geometry. [The game's algorithm](army-placement.md) is documented separately.

## Status

This describes a September 21–23 prototype on our build, not a public universal-compatibility release. The user confirmed physical RMB opening/cycling; addressed-message tests are separate evidence. Current presentation uses opaque figures with subtle warm glow. Holding RMB remains unconfirmed.
