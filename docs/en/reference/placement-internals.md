---
content_type: reference
status: draft
faction: academy
title: Placement internals and corrected assumptions
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/placement-internals/
description: Placement internals and corrected assumptions
updated: '2026-09-26'
---
# Placement internals and corrected assumptions

Technical reference for **stack splitting, sorting and cell selection**. Start with the illustrated [player explanation](../players/army-placement.md). All addresses below refer to the [pinned EXE](universe-build.md); validation scope is listed at the end.

## Army preparation

0x855240 builds combat records before placement. Its inspected multiple-source-record branch copies types/counts; one record enters splitting. Earlier composition changes remain possible.

For normally loaded CombatSize 1/2, M=4. Field+0xdc is CombatSize, not tier; the loader clamps it to1…2, so the CombatSize>2 branch selecting M=2 is unreachable for those values.

| Strength ratio R | Initial K when M=4 |
|---|---:|
| R<0.5 | 4 |
| 0.5≤R<1 | 3 |
| R≥1 | 2 |

RNG(1,100) results≤30 decrement K; results≥70 increment it when K<M. Then clamp K to1…N. These are code comparisons, not verified RNG percentages. With K>2 and Upgrades, another test strictly<50 can substitute interior-stack types; endpoints keep the original. Divide N by K with remainder: first r stacks get q+1, others q. Ten into three gives 4/3/3.

Splitting strength differs from placement score. For the inspected CHero path, numerator evaluates its army with hero context, denominator evaluates the opposing vector without a hero. An extra getter context is week type; WEEK_OF_TOUGHNESS uses H+H div 5. This is static tracing, not coverage of every Universe week/interface implementation.

## Entry paths

0x85a190 checks combat_active_auto_placement and nonempty source descriptors. For ordinary CAdvMapMonster the chain reaches the map object's army, not unique portrait count. 0x85a040 preserves existing positions and fills gaps.

Extended: 0x859eb0→0x859cd0→0x8598e0. Defensive 0x8593c0 is conditional; general 0x859670 always runs, followed by remaining-column passes. Simple 0x85a110 has its own fallback.

In the pinned Universe `DefaultStats.xdb`, the defensive comparison uses `OurShootersMinRelativePower=0.2` and `OurShootersMinRelativeAdvantage=1.3`, both with strict greater-than tests. An opposing-capability check at `0xa2f710` and early conditions also apply; the two thresholds are not the complete formula. Spread is related to `EnemyAreaAttackMinRelativePower=0.35` and its own conditions. Defence and spread can both be enabled. Two recorded `pack_15` battles with the same captured public quantity bands had shooter-power shares of about 0.217 and 0.183 with different defensive flags; exact neutral counts were not retained and arenas differed. [Observation record](research-diary.md#placement-defence-2026-09-26).

The defensive pass at `0x857cc0` lists free neighbors of occupied cells, removes duplicates, and sorts candidates. `0x857f90` assigns weight 2 to chosen shooter-window rows, 1 to their neighbors, and 0 to other rows; `0x85a9b0/0x85a850` resolves ties in the game's order. Large and small defenders keep separate candidate sequences, and an entire 2×2 footprint is checked before placement. Combined defence and spread use selected spaced rows rather than ordinary adjacency. Recorded Polygon `pack_15` attempts from rounds 1, 4, and 10 passed offline when the defensive branch was supplied; the newer DLL has no fresh live campaign.

## Scores and ties

0x858d40 uses a synthetic one-peasant reference without hero, not the player's army. Aggregate construction 0xbfaa70 uses:

```text
D = truncate(((minDamage + maxDamage) * N) / 2)
H = healthPerCreature * N
```

Multiply before division: damage 1–2 at N=3 gives 4, not 3. Attack is weighted by integer damage, defence by health. The scorer reads the reference defence parameter from+0x24, left zero by this chain, not ordinary defence+0x1c. Final scores/fractional reference parameters truncate toward zero.

The arithmetic control used DamageIncrease/Decrease 0.05. Adjacent cap fields 3/0.1 are not read by scorer 0xa58d30; do not import them based on neighboring names. This is not the damage-dealt formula.

Ordinary sort 0x85a700 merges decreasing-stride lanes; ties take the right lane. Ten equal rows produce 8,4,6,10,2,7,3,5,9,1. All 3280 sequences of length 0…7 over{0,1,2} matched original numeric-sort instructions; that does not test getter-dependent comparators.

Special comparator 0x85aba0: non-flying before flying; speed when max(speed 1,speed 2)≥distance; then score. General-pass distance=width−deploymentColumns−6. The [executable walkthrough](../../assets/placement/placement_walkthrough.py) covers one confirmed case, not every branch.

## Rows, spread and depth

0x857b60 measures approaches;0x857e60 retains the first minimum shooter window. Spread 0x858700 uses integer division(R−1)/(N−1), then adds 0.001. Truncate i×step for the first N−1 indices; append R−1. R10,N3 gives{0,4,9}, not{0,5,9}. Preserve original candidate order; occupancy filtering falls back to the prior list if empty.

Large units reserve all 2×2 cells. 0xb3efb0 derives anchor restrictions from a copy, avoiding recursive propagation.

[![Large-footprint validation on the full field](../../assets/placement/pack_8-footprint.svg)](../../assets/placement/pack_8-footprint.svg)

0x85a2a0 calculates deployment depth inside the field. The observed Universe patch changes the large-position threshold 2L→3L and adds a column at L≥4. Minimum 2/3 depends on effective Tactics advantage; equal effective opportunities clear both flags. The extra blocking predicate is not conclusively mapped to a named specialization.

## Linked groups and retries

Goblins and their users have separate adjacency selection 0x858fb0. Candidate scoring considers membership in multiple lists; the choice is greedy, not globally optimal.

Shooter support 0x8580e0 uses world coordinates in a local-coordinate filter. An empty local 3×10 zone yielded no candidates for world anchor(13,5), but neighbors for(2,5). Guaranteed shooter adjacency is not established.

The apparent same-type merger 0x8599d0 has an unreachable inner loop for valid vector sizes; tested N0,1,2,3,7,64. Window shifts/retries exist, but a branch name does not establish working merging. Excluding a record from an attempt does not prove creatures disappear from the map army.

Additional ability evaluator 0xbfa360 has separate applicability/target tests. In the inspected call, contribution=min(uses,10)×value div 10; EXPLOSION 162 and DEATH_WAIL316 are excluded. Initial-value semantics/all predicates remain incomplete; not a complete ranged-damage formula.

## Evidence scope

Sort/truncation/footprint and parts of split/spread arithmetic ran in original-code emulation. Universe width changes were observed in a separate process. The live elemental journal confirms seven attempts/four cells only for its ordinary pass. It does not validate every special mode.

**Evidence:** September 21–23 analysis and corrections; published [example data](../players/army-placement.md). [Definitions](creatures.md) · [Research map](research-index.md).

[Research record](research-diary.md#placement-corrections).
