---
content_type: reference
status: draft
faction: stronghold
title: 'Banks: types, tiers and guard ranges'
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/banks/
description: 'Banks: types, tiers and guard ranges'
updated: '2026-09-24'
---
# Banks: types, tiers and guard ranges

**One bank tier can have several guard compositions.** The crypt, for example, has eight variants across four tiers. A reference must map variants to tiers rather than use array indices as tier numbers. Below are the catalog and two quantity examples.

## Resource mapping

The local PAK review mapped 25 object definitions to12 confirmed Types. AG_INFO has 13 families; OrcDeposit's XDB binding remains unresolved. The prototype's BUILDING_ORC_DEPOSIT configuration key is not a confirmed game Type.

| Type / ключ | AG_INFO | Таблица / table | Тиры / tiers |
|---|---|---|---|
| BUILDING_CRYPT | 01 | BankCrypt | 1–4 |
| BUILDING_DWARVEN_TREASURE | 02 | BankDwarvenTreasure | 1–4 |
| BUILDING_GARGOYLE_STONEVAULT | 03 | BankGargoyleStonevault | 1–4 |
| BUILDING_PYRAMID | 04 | BankPyramid | 1–3 |
| BUILDING_SUNKEN_TEMPLE | 05 | BankSunkenTemple | 1–4 |
| BUILDING_BLOOD_TEMPLE | 06 | BankBloodTemple | 1–4 |
| BUILDING_UNKEMPT | 07 | BankUnkempt | 1–5 |
| BUILDING_CYCLOPS_STOCKPILE | 08 | BankElementalsStockpile | 1–4 |
| BUILDING_NAGA_BANK | 09 | BankMagiVault | 1–3 |
| BUILDING_TREANT_THICKET | 10 | BankTreantThicket | 1–3 |
| BUILDING_DEMOLISH | 11 | BankDemolish | 1–4 |
| OrcDeposit: Type не установлен / unresolved | 12 | BankNagaTemple | 1–3 |
| BUILDING_DRAGON_UTOPIA | 13 | BankDragonUtopia | 1–5 |

Names and Types are not one-to-one. BUILDING_SUNKEN_TEMPLE covers the old temple and Universe demon bank; BUILDING_CYCLOPS_STOCKPILE is used for the elemental bank. UNKEMPT covers ship objects and the Order magistrate, DEMOLISH covers wrecks and the necromancer estate. Do not choose a model alphabetically from Type alone.

Check MapObjects/Universe_mod/Demonbank, Monasterybank and NecroEstate `(AdvMapBuildingShared).xdb`, plus `MapObjects/MagiVault.xdb`, `Elemantal_Stockpile.(AdvMapBuildingShared).xdb` (original spelling) and `WitchBank.(AdvMapBuildingShared).xdb`.

## Variant index is not tier

DefaultStats contains 8 Crypt variants for 4 tiers,5 MagiVault variants for 3, and 7 DragonUtopia variants for 5. Match each variant's army, rewards and AG_INFO panel. Aggregate identical creatures within one complete variant, never mutually exclusive substitutions.

## Example: demon-bank guard quantity

AG_INFO05_01_SIZE…05_04_SIZE describe five groups of three guard slots, totaling 15:

| Tier | Per slot | Total across 15 slots |
|---|---|---|
| T1 | 6–9 | 90–135 |
| T2 | 8–11 | 120–165 |
| T3 | 10–13 | 150–195 |
| T4 | 12–15 | 180–225 |

Combining species-specific minima across different alternatives produced the discarded “8 imps” result. These are complete-tier bounds, not revelation of a visited bank's actual guards.

## Elemental bank

Four variants contain 5,10,15 or20 of **each of four types**. The 15-per-type variant therefore has 60 creatures before additional rules, not 15 total. Resource data alone does not establish DLL/map modifications.

## Ground resources are separate

Inspected AdvMapTreasureShared values: wood/ore 4–7, rare resources 2–4, gold 5–10 internal units. A ×100 gold conversion was not verified by our controlled experiment; do not present 500–1000 as an established payout from this evidence.

**Evidence:** MapObjects, UI/AGINFO and DefaultStats Banks, September 21 and corrected grouping. Slot counts checked across 13 families; probabilities, all labels and runtime rules remain incomplete. [Public information](../modding/public-information.md) · [Build](universe-build.md).

[Research record](research-diary.md#banks).

[object_reference.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/object_reference.py) implements stack grouping and reference-text generation. It compiles recipes; individual mod recipes are not bundled with the devkit.

[Portrait-reference mod: source and installation](../players/bank-reference.md).
