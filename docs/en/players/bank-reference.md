---
content_type: how-to
status: draft
faction: fortress
title: Bank reference — installation and cards
lang: en
section: players
kicker: HEROES V · UNIVERSE
translation: players/bank-reference/
description: Source, installation, reading the reference and removal.
updated: 2026-09-24
---
# Bank reference — installation and cards

[Source](https://github.com/Xaaalera/heroes5-bank-reference) · [Universe](https://h5lobby.com/) · [tested devkit](https://github.com/Xaaalera/heroes5-mod-devkit/tree/1b8934ac084491da460ce8bb145819e41e2cf888).

The mod shows **possible armies by tier**, portraits, ranges and alternatives. It does not reveal an object's actual hidden guards.

## Installation

Use Windows, Git, Python 3.10+ x64 and the [supported Universe build](../reference/universe-build.md). The prototype requires **H5U plus the devkit native diagnostic launch**. No standalone player DLL installer exists yet.

Exit game/editor. In a new PowerShell directory:

```powershell
git clone --recursive https://github.com/Xaaalera/heroes5-bank-reference.git
cd heroes5-bank-reference
python -m venv .venv
.venv/Scripts/python -m pip install -r devkit/requirements.txt
$env:H5_WORKSPACE = [IO.Path]::GetFullPath('../bank-reference-workspace')
$env:H5_GAME_DIR = (Resolve-Path '../HeroesV-Universe').Path
.venv/Scripts/python devkit/scripts/mod-dev.py prepare --sandbox
.venv/Scripts/python devkit/scripts/mod-dev.py build --sandbox --mod army-reference --source .
.venv/Scripts/python devkit/scripts/mod-dev.py deploy --sandbox --mod army-reference
.venv/Scripts/python devkit/scripts/native-probe.py launch --army-layout --control
```

Replace the example game path and choose a separate workspace. Prepare runs once and refuses to overwrite an existing copy. Set variables again in new shells. Rebuild after recipe edits; deploy installs the existing H5U.

Open a map and hover a supported bank. The earlier imp-cache check showed T1–T4 with 90–135 / 120–165 / 150–195 / 180–225. Later presentation changes and other banks lack the same complete visual confirmation.

## Read the reference

- T1/T2… describes a possible tier, not scouted guards of this object.
- A/B separates alternative complete armies; do not sum them.
- Split portraits show substitutable species. A percentage applies per stack.
- The paired count is the whole group's range, not a guaranteed count of each species.

[Where tiers and ranges come from](../reference/banks.md). Thirteen families map 19 public titles to 12 confirmed types. OrcDeposit remains unbound; renamed objects are unsupported by title-based selection.

## Removal

Exit the test game and verify process termination. In the same environment:

```powershell
.venv/Scripts/python devkit/scripts/mod-dev.py rollback --sandbox --mod army-reference
```

Only the owned unchanged H5U is removed; unrelated mods and the sandbox remain. An ordinary later launch without --army-layout does not install the selector.

## Validation

The standalone build was byte-identical to the earlier package: SHA-256 `824a14b48fbdadce9ea0475b49bc4d1f1f6d2ef112ef8294b63cc1ea4ebf7f1e`. Four recipe/native-selector checks passed. No fresh live launch followed extraction; combined use with the predictor is unverified.

[Repository instructions](https://github.com/Xaaalera/heroes5-bank-reference#readme) · [Both mods and installation rules](mods.md) · [Tooltip history](../reference/research-diary.md#army-tooltip-probe).
