---
content_type: landing
status: draft
faction: haven
title: Mods and installation
lang: en
section: mods
kicker: HEROES V · UNIVERSE
translation: players/mods/
description: Two mods, their source and distinct installation methods.
updated: 2026-09-24
---
# Mods and installation

Two experimental add-ons for **[Heroes V Universe / Heroes V Lobby](https://h5lobby.com/)**. [Universe community](https://vk.com/h5universe) · [Development page](https://boosty.to/verydobro).

| Mod | Display | Connection | Source |
|---|---|---|---|
| [Deployment preview](deployment-preview.md) | Projections, upgrade cards and movement range | Built EXE + DLL, started through its loader | [GitHub](https://github.com/Xaaalera/heroes5-deployment-preview) |
| [Bank reference](bank-reference.md) | Possible armies by tier, ranges and alternatives | H5U plus devkit native diagnostic launch | [GitHub](https://github.com/Xaaalera/heroes5-bank-reference) |

## Rules for both mods

1. Check the [supported build](../reference/universe-build.md). Matching Universe labels do not guarantee matching files. Keep hash checks enabled.
2. Exit before installing, replacing or removing files. Use a [test copy](../modding/devkit.md) for experiments.
3. Follow the chosen mod's guide. UserMODs cannot load the predictor DLL; the reference H5U does not replace its native startup.
4. Verify the in-game result after installation. A successful build or file write does not establish that a window appears.
5. Disable the predictor by ordinary game EXE startup; remove bank reference through its rollback. Each mod page gives exact commands.

Combined use is not separately verified; check each mod individually first. Repositories do not distribute the game, Universe or profiles.

## Development environment

Both repositories pin the [devkit](https://github.com/Xaaalera/heroes5-mod-devkit) as a submodule and name the tested revision. Each includes AGENTS.md, tests and mandatory pre-push review. [How the environment works](../modding/devkit.md).
