---
content_type: explanation
status: draft
faction: academy
title: How the game deploys a neutral army
lang: en
section: players
kicker: PLAYERS · COMBAT MECHANICS
translation: players/army-placement/
description: From preparing stacks to selecting cells — Heroes V Universe deployment with actual battle examples.
updated: 2026-09-23
---
# How the game deploys a neutral army

The game first prepares **combat stacks**, selects a formation method, determines available cells and places creature groups in sequence. Army composition, obstacles, creature size and the selected algorithm branch can therefore change starting positions. “Shooters behind, everyone else in front” is not a sufficient rule.

This account applies to the investigated **Heroes V: Tribes of the East with Universe** build. It combines code analysis, execution of individual code sections and two test-map observations. It is not a complete specification of every mode; [evidence and limits](#evidence) appear below. The subject is the game, not a third-party predictor.

## 1. Combat stacks are prepared first

The adventure-map army and the combat stack list are separate preparation stages.

The investigated preparation function copies types and quantities when there are at least two source records. A single record takes a splitting branch: initial stack count depends on a ratio of strength evaluations, followed by a random adjustment and a limit based on creature quantity. Earlier army changes and other combat paths have not been ruled out. [Verification points S1](#evidence).

Once stack count is selected, creatures are divided with a remainder. **If ten creatures have already been assigned to three stacks**, distribution is **4 + 3 + 3**: three each, with the remaining creature assigned to the first stack. This does not mean ten creatures always split into three stacks.

Under additional conditions, interior stacks can receive a type from the source creature's upgrade list; the endpoints retain the original type. Splitting, upgrading and selecting a cell are distinct operations. No exact probabilities are claimed: code comparison boundaries were checked, but the random generator's distribution was not independently established.

## 2. The game selects a formation path

There are simple and extended auto-placement paths. Selection depends on `combat_active_auto_placement` and a source-army condition. For the investigated ordinary neutral, that condition refers to nonempty records in the map object's army, not the number of distinct creature portraits. The timing of mod changes to this army needs separate verification. [S2](#evidence).

The extended path prepares defensive and spread-formation flags. Evaluations consider ranged strength, large enemies and area attacks, with further conditions. Seeing a shooter is therefore insufficient to determine the formation reliably.

The following stages mainly describe the extended path. The simple path distributes stacks along the field's height and has its own fallback attempts.

## 3. The entire footprint must fit

A small creature occupies **1×1** cell; a large creature occupies **2×2**. All four cells must be free for a large creature. An obstacle or an already placed stack can invalidate several possible large-creature positions.

For example, an obstacle at `(2,2)` invalidates large-creature anchors `(2,2)`, `(3,2)`, `(2,3)` and `(3,3)`. An anchor `(x,y)` represents cells `(x,y)`, `(x−1,y)`, `(x,y−1)` and `(x−1,y−1)`. This example was checked by executing the mask-processing code section. [S3](#evidence).

The game also calculates **deployment depth**: how many initial columns are available. The battlefield itself does not expand. Free space and small/large stacks matter; minimum depth is connected to the Tactics advantage. In the checked Universe run, runtime changes also altered the large-stack capacity calculation and added a column with four or more large stacks. This is build-specific evidence, not a universal Heroes V rule.

## 4. Rows receive priorities

The algorithm measures each row's continuous free approach from its designated column to an obstacle or boundary. Large creatures depend on neighboring rows: a narrow approach in one constrains the whole square.

For shooters, a cyclic row window with the minimum sum of approach lengths is selected. Its length depends on the number of shooter-category stacks. Equal sums retain the first window found. This is a geometric evaluation, not a full simulation of enemy movement or shooting. [S4](#evidence).

**Equal scores do not imply top-to-bottom order.** In the checked sort, ten equally ranked rows produce candidate order `8, 4, 6, 10, 2, 7, 3, 5, 9, 1` in field coordinates. This is not a finished ten-stack formation: obstacles, occupancy and branch selection still affect the result.

## 5. Groups are placed in sequence

The extended algorithm's general pass processes these categories: [S5](#evidence).

| Order | Group | Why the distinction matters |
|---|---|---|
| 1 | Large non-shooters without the magic-resistance aura | Require a free 2×2 footprint |
| 2 | Shooter category | Uses prepared shooter rows; includes an exception for throwers with compatible goblins |
| 3 | Linked goblins and creatures that use them | Have separate neighboring-cell selection |
| 4 | Magic-resistance-aura or shield-other creatures | Receive a separate placement attempt |
| 5 | Ordinary small non-shooters | Use suitable remaining spaces |

This is category-call order, not a universal sort of every creature or combat turn order. A defensive pass can run first; further attempts handle unplaced stacks.

Within groups, stack evaluation considers quantity, damage, attack, defence and health rather than simply creature tier. One special comparator puts non-flyers before flyers, then conditionally compares speed, then score. Sorting by initiative or portrait order cannot replace the whole mechanism.

Support units are not guaranteed to stand beside a shooter. The investigated function uses world coordinates in a local-coordinate check, so that attempt can produce no candidates. This is a limitation observed in specific code, not a reason to substitute the intended-looking behavior.

## 6. When suitable cells run out

Successful placement reserves the occupied cells. Later stacks cannot reuse them.

If some stacks remain, the extended algorithm can shift its row window and retry. Additional passes scan deployment columns. In the checked code, the apparent same-type merging branch never enters its inner loop for a valid vector size. Thus “the game always merges stacks when space runs out” would be incorrect. Excluding a record from another placement attempt also does not, by itself, prove creatures disappeared from the army. [S6](#evidence).

## Example: three Academy stacks

[![Opening of an actual battle with genies, iron golems and gremlins](../../assets/placement/pack_8.png)](../../assets/placement/pack_8.png)

*Actual early-combat frame, with the predictor DLL not loaded. Genies have already cast a spell; this is not the exact Start event frame. The table was recorded separately in Start before turns. Open the image for full resolution.*

| Stack | Starting anchor `(x,y)` | Occupied cells |
|---|---|---|
| Genies | `(13,8)` | `(12,7)`, `(13,7)`, `(12,8)`, `(13,8)` |
| Iron golems | `(12,4)` | One cell |
| Gremlins | `(13,9)` | One cell |

![Recorded columns 12–13: genies occupy rows 7–8, golems row 4 and gremlins row 9](../../assets/placement/academy-cells.svg){ width="340" }

*Diagram from Start records, not the camera angle: 1 — genies, 2 — golems, 3 — gremlins. Only columns 12–13 are shown; obstacles and the rest of the field are omitted.*

The example shows different sizes and roles: genies need four cells, shooting gremlins need one, and golems occupy another available position. The frame alone cannot establish the selected branch or each row's score; those claims need the code analysis above. [Observation record](../../assets/placement/observations.json).

## Example: seven stacks

[![Seven stacks grouped near the battlefield edge and obstacles](../../assets/placement/pack_15.png)](../../assets/placement/pack_15.png)

*A second battle on the same test map with different obstacle geometry. Predictor disabled. The frame is from early combat; coordinates were recorded separately at Start.*

| In-game type identifier | Starting anchor |
|---|---|
| `CREATURE_GRAND_ELF` | `(13,3)` |
| `CREATURE_ARCHER` | `(13,1)` |
| `CREATURE_PEASANT` | `(12,1)` |
| `CREATURE_PIT_FIEND` — size 2×2 | `(13,5)` |
| `CREATURE_INFERNAL_SUCCUBUS` | `(13,2)` |
| `CREATURE_CERBERI` | `(12,2)` |
| `CREATURE_FAMILIAR` | `(12,3)` |

Identifiers allow exact matching against the [observation record](../../assets/placement/observations.json) regardless of name localization. The large demon's anchor `(13,5)` also occupies `(12,4)`, `(13,4)` and `(12,5)`; adjacent small stacks do not overlap its square. An army need not be evenly distributed across the entire field height.

Both composition and obstacles differ between these battles. They show two possible outcomes, not an isolated experiment changing only one factor.

## What can be inferred before combat

- Sizes and roles help identify space requirements, but do not define one universal formation.
- Obstacles affect both valid cells and candidate-row order.
- Unknown splitting, upgrades, quantities and branch selection leave uncertainty. A battlefield screenshot alone lacks some game inputs.
- Do not transfer an example to another arena or build without checking. This article does not establish identical algorithms for sieges, special battles or other mods.

## Evidence and limits {#evidence}

Battle date: **2026-09-23**, test map `WorkshopPolygon`. This is our own executable analysis and observation, not an official Nival specification. The account incorporates corrections made after the initial September 21–22 investigation.

Investigated `H5_Game.exe` SHA-256: `88c9dc6107b9bced0649924a86360f1c56397ee00de0413f6f2b08f865ed5519`. Matching the EXE does not establish identical DLL/resource modifications; the examples concern the tested Universe installation.

| Label | Verification point | Method and limitation |
|---|---|---|
| S1 | Preparation/splitting `0x855240`; CombatSize/Upgrades | Code and XML-loader analysis, stack-count code execution; not a complete probability test |
| S2 | Path selection `0x85a190`; strategy `0xa30730` | Call/source-army tracing; not every strategy condition has live coverage |
| S3 | Footprints `0xb3efb0`; depth `0x85a2a0`; Tactics `0x4d8c10` | Mask/count code execution, static Tactics chain; Universe depth modifications observed separately on September 22 |
| S4 | Rows `0x857b60`, `0x857e60`; sorting `0x85a700` | Instructions and sort controls including equal keys; not one formation for every field |
| S5 | General pass `0x859670`; score `0xbf9b80`; support `0x8580e0` | Code and selected code-section checks; do not replace adjacency exceptions with assumed behavior |
| S6 | Retries `0x859eb0`; merging `0x8599d0` | Merge inner loop shown unreachable in the checked EXE; not a claim covering all modified versions |

On your own test map, starting coordinates can be recorded in the combat `Start` callback **before the first turn**:

```lua
function Start()
    for index, unit in GetDefenderCreatures() do
        local x, y = GetUnitPosition(unit);
        print("PLACEMENT", unit, GetCreatureType(unit), x, y);
    end;
end;
```

This belongs to a map's combat script, not the ordinary adventure console. Our experiments used this defender enumeration and a separate observer of `GetUnitPosition` results. No predictor was loaded; the observer does not assign positions. The prepared [public record](../../assets/placement/observations.json) contains coordinates and hashes of unchanged screenshots. The polygon is not yet public, so reproducing these exact arenas is not currently provided; a reader's own map can test the recording method without necessarily producing the same cells.
