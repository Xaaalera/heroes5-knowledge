---
content_type: landing
status: draft
faction: necropolis
title: 'Knowledge map: investigated topics'
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/research-index/
description: 'Knowledge map: investigated topics'
updated: '2026-10-10'
---
# Knowledge map: investigated topics

Choose a question from the table. For experiments, failed assumptions and corrections, see the [research diary](research-diary.md).

| Question | Article | Contents |
|---|---|---|
| How do I set up a development environment? | [Devkit and workflow](../modding/devkit.md) | Repository, sandbox, builds, control and shutdown |
| Why these starting cells? | [Player placement explanation](../players/army-placement.md) | Full grids, row calculation, seven native attempts, executable example |
| Other algorithm branches? | [Placement internals](placement-internals.md) | Splitting, sort, spread, depth, adjacency and corrected assumptions |
| Which build? | [Universe baseline](universe-build.md) | Four hashes, change layers and archive counts |
| Where are resources? | [Formats/encodings](formats.md) | ZIP members, XDB links, encodings, precedence limits |
| How to verify an override? | [Menu marker](../modding/resource-overrides.md) | Standalone packer, appearance and rollback |
| What bank variants exist? | [Bank catalog](banks.md) | 13 reference families,12 confirmed Types, tiers/range corrections |
| Where do stats/grades come from? | [Creature definitions](creatures.md) | Fields, footprints, Upgrades, elemental data |
| How to record combat results? | [Combat scripts](../modding/combat-scripts.md) | Prepare/Start, both armies, post-combat data |
| Test-map pitfalls? | [Test maps](../modding/test-maps.md) | Terrain base, arenas, movement cap, startup |
| Why did army UI stay empty? | [Native UI](../modding/native-ui.md) | Model/root selection, cards and second-battle cleanup |
| Which prediction inputs are public? | [Information boundary](../modding/public-information.md) | Visible data, hidden armies and assessor status |
| What does a projection card mean? | [Deployment preview](../players/deployment-preview.md) | Grades, movement, synthetic count and prototype limits |

## External research under verification {#external-research}

[homm5-editor](https://github.com/senyaak/homm5-editor/tree/e40be948d16757ec8cff7f7d1be87b9956fc2d64) is an independent map editor and collection of Heroes V research. We retained that revision and inventoried all 900 files. This is a material survey, not confirmation of every finding for Universe.

| Author's material | Use for our work | Verification so far |
|---|---|---|
| [Battle scripting](https://github.com/senyaak/homm5-editor/blob/e40be948d16757ec8cff7f7d1be87b9956fc2d64/docs/engineInternals/BATTLE_SCRIPTING.md) | Find the correct result-collection point and way to reach the battle script | The defender-list chain is confirmed; native roster size now verifies collection completeness, with ten controls passed. The author's battle-Lua invocation method remains unverified on our build |
| [Lua and function registration](https://github.com/senyaak/homm5-editor/blob/e40be948d16757ec8cff7f7d1be87b9956fc2d64/docs/engineInternals/LUA.md) | Locate available EXE functions and verify their arguments | Our EXE contains entries for units, positions, quantities and game variables; dialect restrictions need separate experiments |
| [Battle AI](https://github.com/senyaak/homm5-editor/blob/e40be948d16757ec8cff7f7d1be87b9956fc2d64/docs/engineInternals/COMBAT_AI.md) | Design checks for power valuation and spell effects | The author's conclusions are not yet confirmed on our build |
| [Native UI](https://github.com/senyaak/homm5-editor/blob/e40be948d16757ec8cff7f7d1be87b9956fc2d64/docs/UI_INTERNALS.md) and [stack counters](https://github.com/senyaak/homm5-editor/blob/e40be948d16757ec8cff7f7d1be87b9956fc2d64/docs/engineInternals/STACK_PLATE.md) | Improve creature cards and post-battle explanations | The described counter XDB files and window identifier exist in our PAKs; active resource precedence, native bindings and UI behaviour are not yet verified |

**The builds differ.** All six checked entry points have different instructions in our EXE. Addresses and field offsets cannot be transferred directly. We verify the mechanism, locate its counterpart in our build and retain our own evidence. No editor code has been incorporated into our plugins or SDK.

Remaining material—map and resource formats, map generation, creatures, artifacts, specializations, necromancy, war machines and networking—is queued for later verification. Confirmed findings go into the relevant site section with their source and applicability limits; hypotheses are labelled separately.

### Other projects found

The initial search also found these sources. Their stated purpose and descriptions were checked; Universe compatibility and their individual mechanics were not.

| Project | Next verification target |
|---|---|
| [homm5-runtime](https://github.com/pegnoly/homm5-runtime) | The author describes Lua/dialog/map generation, resource packaging and Frida tooling; assess relevance to xkit commands and controlled tests |
| [MMH55](https://github.com/Might-Magic-Heroes-5-5/MMH55) | Heroes 5.5 development sources; locate relevant battle scripts and solutions while preserving build/mod differences |
| [HoMM5MapScriptsEditor](https://github.com/HSerg/HoMM5MapScriptsEditor) | Lua script editing/checking; investigate game-dialect support and diagnostics |
| [Heroes5MapEnhancer](https://github.com/proxeeus/Heroes5MapEnhancer) | Map-object parsing and script generation; assess controlled test-case generation |

A [proposal to share research and documentation corrections](https://github.com/senyaak/homm5-editor/discussions/2) was posted in homm5-editor Discussions. No response or joint agreement has been confirmed yet.

## Not established as complete results

- Every combat branch, expansion or mod.
- A general native-plugin API for Universe.
- Universal native-plugin API or universal predictor installer. [Development tools are available separately](../modding/devkit.md). [The test polygon is available](../modding/test-maps.md).
- A working victory/loss assessor or hidden quantities/upgrades.
- Universal archive precedence or hot reload.
- OrcDeposit's exact object XDB and complete live bank coverage.

Research preserves these open questions instead of inventing answers. Draft articles can contain concrete findings while their scope expands; each states evidence and limits. [Contribute a verifiable addition](../contributing.md).
