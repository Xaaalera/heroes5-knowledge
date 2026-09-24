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

**Evidence:** September 21–23 polygon experiments and later placement captures. Polygon/command SDK are not publicly distributed; this describes a testing method, not a downloadable harness. [Combat callbacks](combat-scripts.md) · [Map formats](../reference/formats.md).
