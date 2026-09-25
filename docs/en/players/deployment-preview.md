---
content_type: how-to
status: draft
faction: academy
title: 'Deployment preview: installation and controls'
lang: en
section: mods
kicker: HEROES V · UNIVERSE
translation: players/deployment-preview/
description: 'Deployment preview: installation and controls'
updated: '2026-09-24'
---
# Deployment preview: installation and controls

A projection marks **a creature's predicted position and movement area**. It uses a known type without revealing hidden guard quantities or upgrades. This is an experimental mod for the inspected Universe build; no universal release is available.

## Source and installation

[Predictor source](https://github.com/Xaaalera/heroes5-deployment-preview) · [Universe / Heroes V Lobby](https://h5lobby.com/) · [tested devkit](https://github.com/Xaaalera/heroes5-mod-devkit/tree/1b8934ac084491da460ce8bb145819e41e2cf888).

Use Windows, CMake 3.21+ and Visual Studio 2022 C++ x86 tools. In an **x86 Native Tools Command Prompt**:

```bat
git clone --recursive https://github.com/Xaaalera/heroes5-deployment-preview.git
cd heroes5-deployment-preview
cmake -G "NMake Makefiles" -S . -B .local/build/deployment-preview-native -DCMAKE_BUILD_TYPE=Release
cmake --build .local/build/deployment-preview-native --config Release
cmake --install .local/build/deployment-preview-native --config Release --prefix .local/dist/deployment-preview-native
```

Exit the game. Keep the resulting `workshop_preview_loader.exe` and `WorkshopDeploymentPreview.dll` together in a separate mod directory. **Do not replace game DLLs or put this DLL in UserMODs.**

Example from the checkout root:

```powershell
.local/dist/deployment-preview-native/workshop_preview_loader.exe --game "../HeroesV-Universe/bin/H5_Game.exe"
```

Replace the example with your game EXE. The loader accepts only the [four pinned binary hashes](../reference/universe-build.md); a current lobby build may differ. Do not bypass a mismatch. Check projections/cards before Start in an ordinary attack. Python is for development checks, not the installed EXE/DLL pair.

## Disable and remove

Exit and launch the ordinary game EXE directly to leave the plugin unloaded. Remove the two mod files from their separate directory after exit; the loader does not patch game binaries on disk.

Extraction checks built x86 and passed nine C++/emulator checks with the local game oracle. No fresh live launch followed extraction; combined use with bank reference is unverified. [Full instructions](https://github.com/Xaaalera/heroes5-deployment-preview#readme) · [Both mods and installation rules](mods.md).

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
