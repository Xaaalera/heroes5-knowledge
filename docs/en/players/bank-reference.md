---
content_type: how-to
status: draft
faction: fortress
title: Bank reference
lang: en
section: mods
kicker: HEROES V · UNIVERSE
translation: players/bank-reference/
description: 'Possible bank armies: what the mod shows and how to read its cards.'
updated: 2026-09-25
---
# Bank reference


The mod shows **possible armies by tier**, portraits, ranges and alternatives. It does not reveal an object's actual hidden guards.

## Download and install

**Package `0.1.0-preview.1` is prepared but not published:** its new launch path still awaits in-game acceptance. Code → Download ZIP downloads source code, not the player package.

[Mod on GitHub](https://github.com/Xaaalera/heroes5-bank-reference) · [Universe](https://h5lobby.com/).

The player ZIP needs Windows and the [supported game build](../reference/universe-build.md). No Python, Git or devkit is needed.

1. Exit the game and editor. Extract `Heroes5BankReference` beside the game's `bin` folder.
2. Double-click `workshop_bank_reference.exe`. Keep `workshop-army-reference.h5u` beside it.
3. If a file picker appears, select your Universe installation's `bin/H5_Game.exe`. Cancel installs and starts nothing.
4. The launcher checks the version, copies its H5U into `UserMODs` and starts the game. Hover a supported bank on the map: the possible-army reference should appear.

A differing existing `UserMODs/workshop-army-reference.h5u` is not overwritten. Exit the game and preserve that earlier file separately before replacing it. If the game version or EXE/H5U pair does not match, check compatibility and extract the complete package again.

## Disable and remove

Exit the game. Delete `UserMODs/workshop-army-reference.h5u` and the `Heroes5BankReference` folder. Leave other UserMODs files alone. The ordinary game EXE launches without the reference selector.

[Developers: source build and test environment](../modding/devkit.md#mod-sources).

## Use the mod

On the adventure map, hover a supported bank to display its possible guard armies.

## Read the reference

- T1/T2… describes a possible tier, not scouted guards of this object.
- A/B separates alternative complete armies; do not sum them.
- Split portraits show substitutable species. A percentage applies per stack.
- The paired count is the whole group's range, not a guaranteed count of each species.

[Where tiers and ranges come from](../reference/banks.md). Thirteen families map 19 public titles to 12 confirmed types. OrcDeposit remains unbound; renamed objects are unsupported by title-based selection.

## Example: imp cache

Public imp-cache data gives these reference ranges by tier:

| Tier | Range |
|---|---|
| T1 | 90–135 |
| T2 | 120–165 |
| T3 | 150–195 |
| T4 | 180–225 |

The T2 range belongs only to that variant: do not add other tiers or infer that the selected bank actually has T2. [Calculation source](../reference/research-diary.md#banks).

## Limits

An in-game check confirmed the imp cache. Other banks and later presentation changes have not received complete visual verification. Combined use with the predictor is unverified.

