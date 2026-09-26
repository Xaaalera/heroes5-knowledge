---
content_type: explanation
status: draft
faction: academy
title: How the game deploys a neutral army
lang: en
section: players
kicker: PLAYERS · COMBAT MECHANICS
translation: players/army-placement/
description: 'Why neutrals occupy particular cells: stack roles, obstacles, placement order, and recorded Heroes V Universe battles.'
updated: 2026-09-26
---
# How the game deploys a neutral army

**Neutral stacks do not appear on random free cells.** The game prepares the stacks, selects a formation method, places them in sequence, and marks occupied cells after each placement. One obstacle or an earlier stack can therefore change where later stacks stand.

This account concerns the tested **Heroes V: Tribes of the East with Universe** build. We reconstructed several rules from the game and its code, but have not established every combat path. Below is what the visible field can tell a player, followed by a battle where the game's placement attempts were recorded.

## Reading the diagrams

[![Complete field: hero army on the left, neutrals on the right, X and Y axes](../../assets/placement/pack_8-positions.svg)](../../assets/placement/pack_8-positions.svg)

Each diagram shows the **whole field**. Cyan `A` stacks belong to the hero; orange `N` stacks are neutrals. The letter and number identify a stack, not its quantity. Hatching marks obstacles and the field boundary.

`X` is the column from left to right; `Y` is the row from bottom to top. These are grid coordinates, not screen positions: rotating the camera does not change them. For example, genie stack `N1` has anchor `(13,4)` near the right edge and occupies a 2×2 square. Open a diagram to inspect its cells.

## Before cells are chosen

**The game first decides how many battle stacks the map object's army will produce.** In the inspected path, two or more original stacks are copied into combat with their types and quantities. A separate splitting rule applies when there is **one** original stack. This does not rule out a mod or special combat changing the army earlier.

For one stack, the game evaluates the hero army's strength against the neutrals and chooses an **initial** number of parts. In the investigated ordinary path, both small and large creatures have a limit of four:

| Hero strength relative to neutrals | Initial parts |
|---|---:|
| Less than half | 4 |
| From half up to neutral strength | 3 |
| At least neutral strength | 2 |

The game then makes a random adjustment: one result reduces the number by one; another can increase it by one up to the limit. Finally, there cannot be more parts than creatures or fewer than one. **When there is no split:** one original stack can remain one if an initial count of two is reduced to one; a lone creature also cannot form two stacks. With two or more original stacks, this splitting branch does not run at all. **One map stack therefore need not split the same way in every battle:** relative strength, exact neutral quantity, and the random result can change. The table gives the initial choice, not a guaranteed combat-stack count; code conditions were checked, but random-result frequencies were not. [Technical limits](../reference/placement-internals.md).

Once the part count is chosen, creatures are distributed nearly evenly. **If ten creatures have already been assigned to three parts**, the result is **4 + 3 + 3**. With three or four parts, interior stacks may receive an upgrade of the original creature; the endpoints keep the original type. Splitting, a possible upgrade, and cell selection are three separate decisions.

Exact neutral quantities are hidden before combat behind labels such as “pack” or “lots.” Players know their own army, but not every number in this comparison. See the [research diary](../reference/research-diary.md#placement-policy) for the checks.

[![Before combat the hero army and obstacles are visible, but neutral models are hidden](../../assets/placement/academy-before.png)](../../assets/placement/academy-before.png)

*Before confirmation, the player sees their creatures and the obstacles. Neutral models are not shown yet.*

[![After combat begins, genies, golems, and gremlins stand on the same field](../../assets/placement/academy-after.png)](../../assets/placement/academy-after.png)

*After confirmation, the neutral positions become visible in the same battle.*

## When ordinary, sheltered, or spread formation is chosen

**After preparing stacks, the game selects a formation method before choosing cells.** Investigated ordinary combat has a simple path that distributes stacks along the field's height and a more complex path that evaluates both armies. The path choice depends on the auto-placement setting and the map object's original army records; not all special entry conditions have been identified. If some stacks have already been placed, a separate path preserves their cells and fills the remaining positions. The rules below concern the **complex path**.

| Decision | What the game compares | What changes on the field |
|---|---|---|
| Shelter shooters | Their share of their army's strength must be **strictly above 20%**, and their relative advantage **strictly above 1.3×**. The game also checks opposing capabilities and special conditions. | A defensive pass runs before ordinary placement. Without spread, some stacks seek cells near shooters. |
| Spread stacks | The game evaluates opposing area-attack strength; this comparison has a **35%** threshold in the tested Universe settings. Further conditions apply. | Candidate rows are spaced so stacks do not all cluster together. |
| Ordinary formation | Neither extra decision is enabled. | Stacks follow the general category and row order. |

“Own shooters” here means the shooters of **the side currently being deployed**; for neutrals, those are neutral shooters. Merely having a shooter is insufficient: the game compares its strength with the rest of the army and with the opponent. These thresholds come from the tested build, but **do not constitute the whole formula**: early conditions and an opposing-ability check remain partly unresolved. Shelter and spread can occur together; the defensive pass then uses spaced rows instead of simple adjacency. [What has been checked](../reference/placement-internals.md).

Spread is not an eyeballed “every second row” rule. With **10 available rows** and **3 stacks**, the initial spaced set is **1, 5, 10**. The game retains its previous priority among those rows and rejects occupied places; a large creature still needs a free 2×2 square. If spaced positions do not fit, other valid cells are attempted.

This is why a visually similar pack may form differently. In two recorded battles with the same hero and the same visible neutral quantity labels, the game's internal shooter-strength share was **0.217** and **0.183**. The first exceeded the 0.20 threshold and accompanied sheltering; the second fell below it and accompanied ordinary formation. Exact neutral counts were not retained for those two battles, and the arenas differed, so no single changed input can be declared the sole cause. The record does show **which comparison switched branches**. [Both observations](../reference/research-diary.md#placement-defence-2026-09-26).

## How the chosen formation becomes cells

The following is the general placement path. When sheltering is enabled, the defensive pass runs **before it**; the general pass still attempts to place any remaining stacks.

First the game calculates **deployment depth**: how many columns at that side of the field can hold starting positions. The whole battlefield does not change size. Free space, large creatures, and the Tactics advantage affect the depth; in the tested Universe build, four or more large stacks added a column. This is not a rule established for every Heroes V version.

1. **Check size.** A small creature needs one free cell; a large creature needs a free 2×2 square. One obstacle or occupied cell inside that square rejects the entire position.
2. **Rank rows.** From the deployment edge, the game checks how far each row remains free towards the opposing side before an obstacle. Shooters and other stacks use the row information differently.
3. **Place groups in sequence.** The general pass handles large non-shooters, then shooters, linked goblins and creatures that use them, then creatures with a magic-resistance aura or shield cover, and finally ordinary small non-shooters. Within groups, quantity, damage, attack, defence, and health matter; one special sort puts non-flyers before flyers. This is **not combat turn order**.
4. **Reserve cells immediately.** Each later stack tries suitable positions again, skips occupied cells, and takes the first available one. If space runs out, the game has further attempts.

If a stack still lacks a cell, the complex path may **shift its chosen row window and retry**, then scan other available deployment columns. This does not mean the game necessarily merges stacks or deletes creatures: in the checked code, an apparent same-type merging branch never enters its inner loop. [Fallback analysis](../reference/placement-internals.md).

[![Complete field with a rejected large-creature square crossing an obstacle](../../assets/placement/pack_8-footprint.svg)](../../assets/placement/pack_8-footprint.svg)

*The red outline is an illustrative 2×2 attempt. A blocked cell inside it rejects the entire square; both armies retain their recorded positions.*

[![Complete field with free approach lengths for each row](../../assets/placement/pack_8-approach.svg)](../../assets/placement/pack_8-approach.svg)

*Lines show where an obstacle stops a row scan. This measures available space before deployment; it is not a creature's movement route in combat.*

When rows score equally, the game does not simply proceed top to bottom. For ten equal rows in the checked field, candidate-row order was **8, 4, 6, 10, 2, 7, 3, 5, 9, 1**. This is a list of *candidate rows*, not ten creatures' final cells: occupancy and footprint still change the outcome. [Tie rule and exceptions](../reference/placement-internals.md).

## Worked battle: four elementals

Here **four stacks of 15 elementals** face the hero's angels. We recorded both final cells and the game's placement attempts. In the diagram, `A1` marks angels; `N1` Earth, `N2` Air, `N3` Water, and `N4` Fire.

[![Complete field: angels on the left and four elemental stacks on the right](../../assets/placement/elementals_trace-positions.svg)](../../assets/placement/elementals_trace-positions.svg)

The game chose neither sheltering nor spread formation in this battle. The 16×12 grid includes a service boundary; playable cells here have `X=2…13` and `Y=1…10`. In the recorded pass, the shooter starts in column `X=13` and small non-shooters in `X=12`.

### Why Fire stands low

Fire is the only shooter. The game measured free approach in each row. An obstacle leaves only one approach cell in **Y=2**, making this the shooter's first row.

[![In the complete elemental field, row Y=2 has the shortest free approach](../../assets/placement/elementals_trace-approach.svg)](../../assets/placement/elementals_trace-approach.svg)

Cell `(13,2)` was free, so Fire succeeded on the first attempt.

[![Fire is placed in cell 13,2 on its first attempt](../../assets/placement/elementals_trace-fire.svg)](../../assets/placement/elementals_trace-fire.svg)

### Why the others do not simply line up

Among the three remaining stacks, Earth and Water cannot fly, while Air can. In the checked comparison, Earth precedes Water by stack-strength score; Air follows them. Their first suitable rows are **8, 4, 10**. This comes from the row scan and the game's tie order, not from counting down the picture.

[![Earth takes the free cell 12,8](../../assets/placement/elementals_trace-earth.svg)](../../assets/placement/elementals_trace-earth.svg)

Earth first tries `(12,8)` and occupies it. Water **starts at the beginning of the same list**: `(12,8)` is now occupied, so it moves to `(12,4)`.

[![Water skips occupied cell 12,8 and takes 12,4](../../assets/placement/elementals_trace-water.svg)](../../assets/placement/elementals_trace-water.svg)

Air also starts at the beginning: Earth occupies `(12,8)`, Water occupies `(12,4)`, and the third attempt `(12,10)` succeeds.

[![Air skips two occupied cells and takes 12,10](../../assets/placement/elementals_trace-air.svg)](../../assets/placement/elementals_trace-air.svg)

| Stack | Game attempts | Final cell |
|---|---|---|
| Fire | `(13,2)` free | `(13,2)` |
| Earth | `(12,8)` free | `(12,8)` |
| Water | `(12,8)` occupied; `(12,4)` free | `(12,4)` |
| Air | `(12,8)` and `(12,4)` occupied; `(12,10)` free | `(12,10)` |

**All seven attempts and four final cells match the game's record.** This explains *this* battle, not every sheltered or spread formation. The [field and attempt data](../../assets/placement/observations.json) are available separately.

## A different arena

Another field contained the same four creature types. Row `Y=2` offered more free space, while an obstacle shortened the approach in `Y=3`. If we apply the same ordinary pass, Fire moves from `(13,2)` to `(13,3)`; Earth, Water, and Air remain in rows 8, 4, and 10.

[![Complete second field: Fire in row 3 and the other elementals in rows 8, 4, and 10](../../assets/placement/pack_12-positions.svg)](../../assets/placement/pack_12-positions.svg)

[![Screenshot of the second battle with four elemental stacks](../../assets/placement/pack_12.png)](../../assets/placement/pack_12.png)

All four calculated cells match that battle's Start record. But its internal formation mode was not captured: a matching result **does not prove** the game used this particular pass.

## A large stack needs a whole square

In a different mixed battle, a large demon occupies `(12,3)`, `(13,3)`, `(12,4)`, and `(13,4)`. Checking only one “main” cell is insufficient: the whole square must be free.

[![Complete mixed-army field showing large-creature footprints](../../assets/placement/pack_15-positions.svg)](../../assets/placement/pack_15-positions.svg)

[![Mixed-battle screenshot: a large demon on the right and angels on the left](../../assets/placement/pack_15.png)](../../assets/placement/pack_15.png)

The screenshot shows the stack's size but does not explain **all seven** neutral positions. That requires a game attempt record like the elemental example.

## What we found in mixed armies {#mixed-armies}

**Sheltering changes more than row rankings: it changes the candidate cells.** The defensive pass visits free neighbors of occupied cells and removes duplicates. Cells in the chosen shooter rows rank highest, neighboring rows next, and other rows lowest. Ties follow the game's traversal order, not a random pick.

A large defender must fit its entire 2×2 square at each attempt. Giving every defender “the next row” therefore fails: placing one stack changes the next stack's options. When sheltering and spread are both enabled, spaced rows are used. [Pass analysis and verified limits](../reference/placement-internals.md).

## What can be predicted beforehand

The field, obstacles, creature sizes, and the player's own army help identify possible positions. Before combat, however, the player lacks exact neutral quantities, possible splitting, and some of the game's formation decisions. Even identical visible quantity labels do not guarantee the same sheltered formation. This is **expected uncertainty**, not an explanation for every predictor miss.

The findings cover investigated ordinary Universe battles. Sieges, special combats, and other builds have not been established as equivalent. Exact technical rules, code for the worked pass, and exceptions are in the [reference](../reference/placement-internals.md). The [research diary](../reference/research-diary.md#elementals) records the experiment; the [test map](../modding/test-maps.md) is available separately.

## Evidence and limits {#evidence}

The battles were recorded on **September 23, 2026**, on `WorkshopPolygon`. Both armies' cells were recorded at combat Start, before the first turn; obstacles were recorded beforehand. For the main example, the game mode and seven placement attempts were also captured. Final cells were not supplied as calculation inputs. This is our research, not an official Nival specification.

[Investigated build and EXE SHA-256](../reference/universe-build.md) · [Published diagram data](../../assets/placement/observations.json) · [Method and technical limits](../reference/placement-internals.md). The public map copy does not lock the hero, random state, or arena of each archived run, so a repeat playthrough may produce different cells.
