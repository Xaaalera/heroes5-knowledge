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
updated: '2026-10-12'
---
# Deployment predictor

A projection marks **a creature's predicted position and movement area** before Start. Once combat starts, **«Расстановка» (Deployment)** above the action bar opens the forecast and actual positions side by side. This alpha targets the [tested Universe build](../reference/universe-build.md), not every game version.

## Development status

Package **0.2.0-alpha.2** corrects row selection against a shooter hero army. In a new series on October 12, its approximate forecast matched every occupied cell in **165 of 213 mixed battles — 77.5%**. Here a mixed guard has multiple publicly shown source stacks before combat; single-source guards that split in combat are counted separately. Previous alpha.1 achieved 171/213 — 80.3%; quantities and arenas differ between fresh loads, so these percentages do not measure the correction on identical inputs or guarantee results on every map.

There are two independent calculations. **The approximate forecast is visible** and uses public types, numeric quantity ranges and the known hero army. For tested ordinary guards, Scouting or an equipped Crown of Many Eyes admits exact source composition. The completed neutral split and hidden upgrades are not its inputs. Quick Combat result integration remains planned.

**The full calculation is hidden before Start** and does not fill the approximate forecast. It supports algorithm verification and explanations after combat starts. In the same series it reproduced creatures, quantities, footprints and cells exactly in **273 of 273 battles**. Standalone package startup passed without the SDK. Other levels, effects and arenas need separate checks. [Campaign conditions and limits](../reference/research-diary.md#placement-melee-window-2026-10-12).

The Deployment window has two equally sized fields: forecast left, facts right. Blue marks the forecast, orange the facts and green the hero army. Both fields show obstacles; large creatures occupy their complete 2×2 footprint. Cell labels identify stacks, and row numbers appear on the neutral side.

Select a stack to see its position and placement rule. The mod generates explanations locally without AI or an external service. If the full calculation does not match the entire pack, the cause is marked unconfirmed. If no forecast was available, only facts are shown.

Maximum variation of armies, levels, skills, artifacts and arenas remains planned. Historical DLL results stay in the diary and do not transfer to a new version.

## Download and install

**[Download package 0.2.0-alpha.2](https://github.com/Xaaalera/heroes5-deployment-preview/releases/download/v0.2.0-alpha.2/Heroes5DeploymentPreview-0.2.0-alpha.2.zip)**. It contains a separate predictor DLL, the H5U interface resource and shared loader DLLs. Code → Download ZIP downloads source, not the player package.

[Mod on GitHub](https://github.com/Xaaalera/heroes5-deployment-preview) · [Universe](https://h5lobby.com/).

The player ZIP needs Windows and the supported game. No Python, Git or compiler is needed.

1. Exit the game.
2. Extract the ZIP into a separate folder. Back up existing `bin/dinput8.dll`, `bin/d3d9.dll` and `bin/d3d9.universe.dll`, if present.
3. On the first installation of our new DLL mods, rename the original game `bin/d3d9.dll` to `bin/d3d9.universe.dll`. Keep an original already saved under that name. If its origin is unknown, restore the original from your verified Universe installation first.
4. Copy **both `bin` and `UserMODs`** from the archive into the game folder. The mod files are `bin/Heroes5Mods/Plugins/deployment-preview.dll` and `UserMODs/workshop-deployment-preview-ui.h5u`; shared `dinput8.dll` and `d3d9.dll` belong beside `H5_Game.exe`. Use one shared DLL version for our mods. Other loaders require separate compatibility checks.
5. When upgrading from preview.2, remove its old `bin/Heroes5Mods/WorkshopDeploymentPreview.dll` to prevent loading two predictor versions.
6. Start Heroes/Lobby normally. There is no separate player EXE, and players do not need the SDK.
7. Start an ordinary battle: projections should appear before Start. Hover for movement range, right-click for a creature card. After Start, open «Расстановка» above the action bar.

On a compatibility error, check the [supported build](../reference/universe-build.md) and restore your backups. Do not replace the retained original `d3d9.universe.dll`, `uni.dll` or `um.dll` with files from an unknown archive.

## Disable and remove

Exit the game and remove `bin/Heroes5Mods/Plugins/deployment-preview.dll` and `UserMODs/workshop-deployment-preview-ui.h5u`. Keep shared `dinput8.dll` and `d3d9.dll` while our other mods use them. After removing every such mod, remove our `d3d9.dll`, rename the retained original `d3d9.universe.dll` back to `d3d9.dll` and restore the `dinput8.dll` backup. If no game-folder `dinput8.dll` existed before installation, remove our file instead of restoring a backup, after removing every one of our DLL mods. Do not delete the retained Universe original when removing one plugin.

[Developers: source build and test environment](../modding/devkit.md#mod-sources).

## Compatibility

Developed for the [tested Universe build](../reference/universe-build.md). The current package passed standalone startup and its declared 273-battle campaign. Other builds, third-party loaders and every possible mod combination remain unverified.

## Controls

| Action | Result |
|---|---|
| Hover | Movement area of the selected reference type |
| First RMB | Full card of the base or already known upgrade |
| Repeated RMB when upgrade is unknown | Base → upgrade → alternative upgrade → base |
| Double LMB | Native detailed creature window |
| Detailed-window arrows | Switch available variants |
| Start | Remove projections, cards and highlighting |
| «Расстановка» after Start | Forecast, initial positions and explanations |

If the upgrade is known, the card shows it. Figures are opaque with a subtle warm glow. The current version has no additional lower arrows.

## Example: gremlin and upgrade

[![Base gremlin: speed 3, health 5](../../assets/preview/gremlin-base.png)](../../assets/preview/gremlin-base.png)

[![Master gremlin: speed 5, health 6](../../assets/preview/gremlin-upgrade.png)](../../assets/preview/gremlin-upgrade.png)

Switching changes speed from **3 to 5** and health from **5 to 6**. The movement area is recalculated with the card.

Stats are not hardcoded for the pictured creatures. `Speed`, `Flying` and `CombatSize` come from the [selected type definition](../reference/creatures.md); the native descriptor supplies the name and card fields. The cache key includes the type, preventing reuse of the previous upgrade's movement area.

## Why the detailed window shows “1”

The reference contains one creature without a hero or real combat stack. This **does not mean the guard has one enemy**. The card also does not establish effects that apply in an actual battle.

## When prediction and battle differ

The approximate forecast can miss because of unknown quantities, upgrades, splitting or formation choice. The new series on October 12 retained **51 stack-count differences and 48 cell differences with equal stack counts**. Unknown inputs do not automatically explain every miss. [Results and limits](../reference/research-diary.md#placement-melee-window-2026-10-12).

Before Start, the forecast creates one stack per public source entry. The game can split a single original stack; the completed split is not inserted into the approximate calculation.

In one observed example, a single peasant projection before Start became **three combat stacks of 10**. Splitting explains the mismatch, not cell size. [How the game builds the army](army-placement.md).

Card opening, upgrade cycling, the native detailed window and its arrows have separate checks. Holding RMB and every possible creature remain unconfirmed. After Start, the window compares forecast with facts and explains the verified actual-placement rule. It does not retroactively correct the forecast shown before Start.

[Research record](../reference/research-diary.md#projection-range).

