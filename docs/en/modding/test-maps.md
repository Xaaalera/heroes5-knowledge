---
content_type: explanation
status: draft
faction: haven
title: 'Test maps: repeatable battles and movement checks'
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/test-maps/
description: 'Test maps: repeatable battles and movement checks'
updated: '2026-09-24'
---
# Test maps: repeatable battles and movement checks

An ordinary neutral attack tests actual army preparation. Scripted StartCombat with a supplied composition isolates arena effects. Neither substitutes for full coverage of the other.

## Download and open the map

[Download WorkshopPolygon.h5m](../../assets/WorkshopPolygon.h5m) — a 96 × 96 test polygon with eight towns and heroes, 12 banks, 16 neutral armies and six arena launch objects.

1. Install **Heroes V: Tribes of the East with Universe**. The polygon was used on the [pinned build](../reference/universe-build.md); other builds have not been separately checked.
2. Close the game. Copy the downloaded file into `Maps`, beside `bin` and `data` in the game directory. Create `Maps` if missing. **Do not extract the H5M.** Back up an existing `WorkshopPolygon.h5m` before replacing it.
3. Launch the game and find **«Полигон Universe / Workshop»** in the single-player custom map list. Start a new game on this map; an old save will not pick up a replaced H5M.
4. The map should be revealed and heroes from all eight factions available. Approach a neutral army for an ordinary battle. Use the six objects at `y = 7` for arena comparisons. Coordinates below refer to the adventure map, not the battlefield.
5. Restart the map to reset defeated armies and visited objects. To uninstall, close the game and remove this H5M from `Maps`.

| Objects | Adventure-map coordinates |
|---|---|
| Towns | `x = 14, 36, 58, 80`; rows `y = 17, 41` |
| Neutrals `pack_0…pack_3` | Same X; `y = 28` |
| Neutrals `pack_4…pack_7` | Same X; `y = 48` |
| Neutrals `pack_8…pack_11` | Same X; `y = 51` |
| Neutrals `pack_12…pack_15` | Same X; `y = 54` |
| Banks | `x = 12, 26, 40, 54, 68, 82`; rows `y = 60, 72` |
| Arenas `arena_1…arena_6` | `x = 10, 25, 40, 55, 70, 85`; `y = 7`, in the scene order below |

Scripted arenas call `StartCombat` against 80 peasants, 35 footmen and 12 priests. Ordinary neutrals use map-object attacks. Startup grants 1000 of each non-gold resource and 100000 gold; a script periodically refills hero movement within the ordinary daily cap. This is a test polygon, not a balanced playable scenario.

**File contents:** map, authored flat terrain, text and Lua scripts. Models and object definitions come from the installed game. Neither the predictor DLL nor the command SDK is required. The public copy removes the diagnostic `UniverseTrigger` subscription and post-combat result collection; object positions, armies, terrain and arena calls are preserved. The combat script only prints defender positions after Start.

**Release check:** ZIP/XDB structure, internal references and differences from the working polygon were checked on September 24. Movement and battles were previously tested on the original polygon; this cleaned copy has not yet had a separate menu-launch test. This does not certify all six arenas. If the map is missing from the list, check that it is in the launched installation's `Maps` directory and that the browser did not append `.zip`.

Download SHA-256: `b5baf474cb523dfa9ec66831676d9c98c722198f1e8af017290d38ec38fa68dc`.

## Same composition, multiple arenas

The polygon generator prepares Grass_Big_01, Dirt_Small_01, Sand_Big_01, Snow_01, Lava_Small_01 and River_Grass_Big_01 under data.pak Scenes/CombatArenas. Scenery references are checked separately. Six prepared scenarios are not six certified live passes. Ordinary pack_0…pack_15 additionally exercise actual attacks.

Record composition/counts, hero, obstacles and Start positions. Changing both army and field cannot isolate an obstacle's effect.

## Flat terrain that did not permit walking

An early polygon had StoneRoad without a base terrain layer. Generator reachability checks passed while in-game walking failed. Adding Grass **beneath** the road restored movement, confirmed by the user.

```text
upper layer: StoneRoad
base layer:  Grass
heightmap:   authored flat terrain
```

Flat elevation and graph reachability do not establish valid in-game terrain. Generator tests now check both containers; the live check exercises actual movement.

## Movement refill versus the daily cap

Normal ChangeHeroStat movement additions were clamped to the daily maximum. A special temporary test-process adjustment bypassed the cap only for addition 9999999; current points 9999999 were observed with maximum 2500. This is a test-harness modification, not ordinary API behavior or a property of the resource mod. An unconfirmed BaseHeroMovement resource override was removed.

## Startup and restart

The inspected -advmap handler existed, but subsequent mainmenu could leave the game in its menu. Redirecting the startup command in an owned suspended test process loaded the map. Process creation still does not establish readiness; verify API response/screen state.

Stage a changed H5M separately while the game is running and install after exit. CloseMainWindow may only open confirmation; verify process termination.

**Evidence:** September 21–23 polygon experiments and later placement captures. The polygon is downloadable above; the command SDK remains unpublished. [Combat callbacks](combat-scripts.md) · [Map formats](../reference/formats.md).
