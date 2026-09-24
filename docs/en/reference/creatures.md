---
content_type: reference
status: draft
faction: dungeon
title: 'Creature definitions: stats, size and upgrades'
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/creatures/
description: 'Creature definitions: stats, size and upgrades'
updated: '2026-09-24'
---
# Creature definitions: stats, size and upgrades

A creature-type definition is reference data. It does not reveal the quantity or hidden upgrade of a particular neutral army.

| XDB field | Meaning in inspected mechanisms | Definition offset in the pinned x86 build |
|---|---|---|
| AttackSkill / DefenceSkill | Base attack/defence | +0x44 / +0x48 |
| Shots | Used by the basic shooter-role test | +0x4c |
| MinDamage / MaxDamage | Ordinary damage limits | +0x50 / +0x54 |
| Speed / Flying | Base speed and flight | +0x58 / +0x60 |
| Health | Health per creature | +0x64 |
| CreatureTier | Tier, distinct from CombatSize | +0x8c |
| CombatSize | 1×1 or2×2 | +0xdc |
| Upgrades | Upgrade-reference range | +0x104…+0x108 |

Offsets belong to the [pinned build](universe-build.md), not another version's API. Heroes, effects, skills and week rules can alter final values.

## Universe elemental definitions

Source: Universe_mod.pak `GameMechanics/Creature/Creatures/Neutrals/*_Elemental.xdb`.

| Type | Attack | Defence | Damage | Health | Speed | Flying | Shots | Size |
|---|---:|---:|---|---:|---:|---|---:|---:|
| Earth | 8 | 14 | 10–14 | 72 | 4 | No | 0 | 1 |
| Water | 10 | 10 | 8–12 | 48 | 5 | No | 0 | 1 |
| Fire | 12 | 4 | 11–20 | 33 | 5 | No | 50 | 1 |
| Air | 8 | 4 | 6–8 | 34 | 8 | Yes | 0 | 1 |

This separates Fire as a shooter and Air as flying in the [placement example](../players/army-placement.md).

## Corrected size/upgrade interpretations

Field registration and the XML loader establish +0xdc as CombatSize, clamped to1…2. The investigated archive contains 179 Creature definitions:102 size 1 and 77 size 2. Other archives/DLLs may add more creatures.

Consequently the neutral-splitting condition CombatSize>2 cannot occur after that loader; creature tier is not the tested value. Upgrades is independently confirmed by its loader; Peasant.xdb lists MILITIAMAN and LANDLORD. A reference list does not establish the hidden army's actual upgrade.

**Evidence:** registration/loader analysis and ZIP definitions, September 22–23,2026. [Placement internals](placement-internals.md) · [Public versus hidden information](../modding/public-information.md).
