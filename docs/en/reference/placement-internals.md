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
updated: '2026-10-11'
---
# Placement internals and corrected assumptions

Technical reference for **stack splitting, sorting and cell selection**. Start with the illustrated [player explanation](../players/army-placement.md). The inspected mechanisms belong to the [pinned EXE](universe-build.md); validation scope is listed at the end.

## Overall sequence

1. Prepare combat stacks. One source stack uses splitting; multiple source stacks follow a separate preparation branch.
2. Evaluate both armies using creature and hero parameters and applicable corrections.
3. Select the simple or extended path, defensive formation and spread.
4. Sort stacks within groups and execute their placement passes.
5. Check free cells and the complete footprint of large creatures; resolve ties in engine order.
6. Leave unplaced stacks for the final column passes.

## Army preparation

The combat-army preparation function builds records before placement. Its inspected multiple-source-record branch copies types/counts; one record enters splitting. Earlier composition changes remain possible.

For normally loaded CombatSize 1/2, M=4. The tested property is CombatSize, not tier; the loader clamps it to1…2, so the CombatSize>2 branch selecting M=2 is unreachable for those values.

| Strength ratio R | Initial K when M=4 |
|---|---:|
| R<0.5 | 4 |
| 0.5≤R<1 | 3 |
| R≥1 | 2 |

RNG(1,100) results≤30 decrement K; results≥70 increment it when K<M. Then clamp K to1…N. These are code comparisons, not verified RNG percentages. With K>2 and Upgrades, another test strictly<50 can substitute interior-stack types; endpoints keep the original. Divide N by K with remainder: first r stacks get q+1, others q. Ten into three gives 4/3/3.

Splitting strength differs from placement score. For the inspected CHero path, numerator evaluates its army with hero context, denominator evaluates the opposing vector without a hero. An extra getter context is week type; WEEK_OF_TOUGHNESS uses H+H div 5. This is static tracing, not coverage of every Universe week/interface implementation.

## Entry paths

The automatic-placement entry checks combat_active_auto_placement and nonempty source descriptors. For ordinary CAdvMapMonster the chain reaches the map object's army, not unique portrait count. The placement-completion entry preserves existing positions and fills gaps.

The extended path controls retries, builds a placement context, then selects the formation. Formation selection conditionally runs the defensive pass, always runs the general pass, then tries remaining stacks by column. The simple path has its own fallback.

In the pinned Universe settings, the relative shooter-power threshold is 20% (`OurShootersMinRelativePower`); relative advantage must exceed 1.3 (`OurShootersMinRelativeAdvantage`). Both comparisons are strict. Capability checks and early conditions also apply, so those thresholds alone do not determine the formation. Spread uses an area-attack threshold of 35% (`EnemyAreaAttackMinRelativePower`) and its own conditions. Defence and spread can both be enabled. [Formation observations](research-diary.md#placement-defence-2026-09-26).

The defensive candidate-selection function lists free neighbors of occupied cells, removes duplicates, and sorts candidates. The shooter-window row scorer assigns weight 2 to chosen shooter-window rows, 1 to their neighbors, and 0 to other rows; the candidate-order comparators resolve ties in the game's order. Large and small defenders keep separate candidate sequences, and an entire 2×2 footprint is checked before placement. Combined defence and spread use selected spaced rows rather than ordinary adjacency. [Candidate and footprint verification](#current-research).

## Scores and ties

Placement scoring uses a synthetic one-peasant reference without a hero, not the player's army. The aggregate-construction function uses:

```text
D = truncate(((minDamage + maxDamage) * N) / 2)
H = healthPerCreature * N
```

Multiply before division: damage 1–2 at N=3 gives 4, not 3. Attack is weighted by integer damage, defence by health. The scorer reads a separate reference-defence parameter, which this chain leaves zero; it does not read the ordinary defence field. Final scores/fractional reference parameters truncate toward zero.

The arithmetic control used DamageIncrease/Decrease 0.05. Adjacent cap fields 3/0.1 are not read by the placement scorer; do not import them based on neighboring names. This is not the damage-dealt formula.

The ordinary numeric-sort function merges decreasing-stride lanes; ties take the right lane. Ten equal rows produce 8,4,6,10,2,7,3,5,9,1. All 3280 sequences of length 0…7 over{0,1,2} matched original numeric-sort instructions; that does not test getter-dependent comparators.

The special placement comparator orders stacks as follows: non-flying before flying; speed when max(speed 1,speed 2)≥distance; then score. General-pass distance=width−deploymentColumns−6. The [executable walkthrough](../../assets/placement/placement_walkthrough.py) covers one confirmed case, not every branch.

## Rows, spread and depth

For shooters, the game first evaluates how clear the approach is along each row and selects the first window with the lowest total score. Spread formation retains spaced candidates: for example, three stacks on ten playable rows select the first, fifth and tenth rows. Candidates then retain their previous priority order. If occupancy filtering removes them all, the spaced list from before that filter is retained.

A candidate row and a stack's final cell are separate stages. If a large shooter's complete footprint cannot fit the candidate cell, its anchor can shift down. In spread formation, that shift preserves the original candidate's score and order. [Rule verification](research-diary.md#placement-spread-shooter).

Different candidates can lead a large stack to the same cell. In a dense spaced list, the first candidate shifts while the second already fits without shifting. They remain separate candidates, each with its own score and priority. Conflating them changed the large stack's first cell and then two further positions through occupancy. [Replay of the retained field](research-diary.md#placement-dense-spread).

If selected rows cannot place the next stack, it remains unplaced until the final column passes. Switching to arbitrary rows within the current pass changes the result. [Pass-transition control](research-diary.md#placement-runic-matrix).

??? info "Exact calculation of spaced candidates"

    For R playable rows and N stack records, the step is integer division `(R−1)/(N−1)` plus `0.001`. Truncate `i×step` for the first N−1 indices, then append `R−1`. These indices start at zero: ten rows and three stacks yield `{0,4,9}`, meaning the first, fifth and tenth playable rows.

Large units reserve all 2×2 cells. The large-footprint mask builder derives anchor restrictions from a copy, avoiding recursive propagation.

[![Large-footprint validation on the full field](../../assets/placement/pack_8-footprint.svg)](../../assets/placement/pack_8-footprint.svg)

The deployment-depth function calculates the number of placement columns inside the field. The observed Universe patch changes the large-position threshold 2L→3L and adds a column at L≥4. Minimum 2/3 depends on effective Tactics advantage; equal effective opportunities clear both flags. The extra blocking predicate is not conclusively mapped to a named specialization.

## Activity and survivability corrections

Activity evaluation uses initiative, morale, luck, speed, initial turn-bar position and remaining ability resources. Retaliation bonuses and the final evaluation limit follow the preceding corrections.

Known runes add a separate correction. Only runic descriptors count: their states receive full, partial or zero weight. Partial weight is one third of full weight; the exact meaning of every state has not been established. The average weight sets a correction of up to 10% to the activity factor before retaliation bonuses and the final limit. [Descriptor-state and live verification](research-diary.md#placement-runic-matrix).

Damage absorption also changes survivability evaluation through its protection reserve and absorbed fraction. Starting Orc rage can activate this branch before the first turn. [Blood Rage controls](research-diary.md#placement-rage-control).

## Linked groups and retries

Goblins and their users have a separate adjacency-selection function. Candidate scoring considers membership in multiple lists; the choice is greedy, not globally optimal.

The shooter-support adjacency function uses world coordinates in a local-coordinate filter. An empty local 3×10 zone yielded no candidates for world anchor(13,5), but neighbors for(2,5). Guaranteed shooter adjacency is not established.

The apparent same-type merging function has an unreachable inner loop for valid vector sizes; tested N0,1,2,3,7,64. Window shifts/retries exist, but a branch name does not establish working merging. Excluding a record from an attempt does not prove creatures disappear from the map army.

The additional-ability evaluator has separate applicability/target tests. In the inspected call, contribution=min(uses,10)×value div 10; EXPLOSION 162 and DEATH_WAIL316 are excluded. Initial-value semantics/all predicates remain incomplete; not a complete ranged-damage formula.

## Rule verification {#current-research}

The latest independent comparison achieved **273/273 complete matches: 757 stacks, ten map runs and 16,830 numerical values**. Creature, quantity and cell forecasts were retained before Start; the actual army was read afterwards. The series used different armies and heroes, but every observed hero level was one.

Separate checks covered 512 protective-candidate and creature-footprint cases, 524 runic descriptor-state combinations and 880 initial-activity cases. Each set validates its own branches; they do not cover every hero, effect and arena combination. [Conditions, results and limits](research-diary.md#placement-runic-matrix).

[Illustrated explanation](../players/army-placement.md) · [Definitions](creatures.md) · [Research map](research-index.md).
