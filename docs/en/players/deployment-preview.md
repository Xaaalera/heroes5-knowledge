---
content_type: how-to
status: draft
faction: academy
title: 'Deployment predictor'
lang: en
section: mods
kicker: HEROES V · UNIVERSE
translation: players/deployment-preview/
description: 'Deployment predictor'
updated: '2026-09-25'
---
# Deployment predictor

A projection marks **a creature's predicted position and movement area**. It uses a known type without revealing hidden guard quantities or upgrades. This is an experimental mod for the inspected Universe build; no universal release is available.

## Download and install

**Package `0.1.0-preview.1` is prepared but not published:** its new launch path still awaits in-game acceptance. Code → Download ZIP downloads source code, not the player package.

[Mod on GitHub](https://github.com/Xaaalera/heroes5-deployment-preview) · [Universe](https://h5lobby.com/).

The player ZIP needs Windows and the supported game. No Python, Git or compiler is needed.

1. Exit the game. Extract `Heroes5DeploymentPreview` beside the game's `bin` folder.
2. Double-click `workshop_preview_loader.exe`. Keep `WorkshopDeploymentPreview.dll` beside it.
3. If a file picker appears, select your Universe installation's `bin/H5_Game.exe`. Cancel closes the launcher without starting the game.
4. Start an ordinary battle: enemy projections should appear before Start. Hover for movement range; right-click for a creature card.

If the build is unsupported, compare it with the linked build below. If the DLL is missing, extract the entire archive again. Do not replace game DLLs.

## Disable and remove

Exit the game. Launch the ordinary game EXE to play without the mod. Delete the `Heroes5DeploymentPreview` folder to remove it; the predictor installs nothing in `UserMODs`.

[Developers: source build and test environment](../modding/devkit.md#mod-sources).

## Compatibility

Developed for the [inspected Universe build](../reference/universe-build.md). Other versions and combined use with bank reference are unverified.

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

[Research record](../reference/research-diary.md#projection-range).
