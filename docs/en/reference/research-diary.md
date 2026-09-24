---
content_type: reference
status: draft
faction: fortress
title: Research diary
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/research-diary/
description: Research diary
updated: 2026-09-24
---
# Research diary

This page preserves **experiments, original results and corrections**. [Articles](research-index.md) explain the current understanding; diary entries record its basis.

September 21–23 entries were reconstructed on **September 24, 2026**. This begins the journal; entries identify source data that remain unpublished.

Experiments below use the [pinned Universe build](universe-build.md) unless stated otherwise.

## September 24 — public polygon copy {#map-release}

**Task:** make the experimental map available to readers.

**Actions:** removed the diagnostic `UniverseTrigger` subscription and post-battle results collector from the working H5M. Only `MapScript.lua` changed. Objects, armies, terrain and six arena calls were preserved.

**Check result:** nine ZIP entries, no CRC errors, internal XDB references resolve. Both language versions download the same 10172-byte file.

[Download H5M](../../assets/WorkshopPolygon.h5m) · [Installation and objects](../modding/test-maps.md).

SHA-256: `b5baf474cb523dfa9ec66831676d9c98c722198f1e8af017290d38ec38fa68dc`.

**Limit:** the cleaned copy has not had a separate menu launch. Earlier live movement/battle checks used the original polygon. Archive validation does not replace a fresh launch.

**Original harness history, September 21–23:** the following three checks preceded the September 24 public-copy release.

### Flat terrain that did not permit walking

An early polygon had StoneRoad without a base terrain layer. Generator reachability checks passed while in-game walking failed. Adding Grass **beneath** the road restored movement, confirmed by the user.

```text
upper layer: StoneRoad
base layer:  Grass
heightmap:   authored flat terrain
```

Flat elevation and graph reachability do not establish valid in-game terrain. Generator tests now check both containers; the live check exercises actual movement.

### Movement refill versus the daily cap

Normal ChangeHeroStat movement additions were clamped to the daily maximum. A special temporary test-process adjustment bypassed the cap only for addition 9999999; current points 9999999 were observed with maximum 2500. This is a test-harness modification, not ordinary API behavior or a property of the resource mod. An unconfirmed BaseHeroMovement resource override was removed.

### Automated startup: harness limitation

The inspected -advmap handler existed, but subsequent mainmenu could leave the game in its menu. Redirecting the startup command in an owned suspended test process loaded the map. Process creation still does not establish readiness; verify API response/screen state.

Stage a changed H5M separately while the game is running and install after exit. CloseMainWindow may only open confirmation; verify process termination.

## September 23 — why the elementals occupied these cells {#elementals}

**Question:** does reconstructed cell selection match the game's placement attempts?

**Input:** four elemental types, 15 each, versus a hero with angels. Recorded defender mode: depth 2, defensive pass 0, spread 0; the opposing army has a large creature, and there is one shooter stack. No predictor was loaded.

**Method:** record obstacles before Start, candidate/result at placement function entry/return, and starting positions of both armies separately. Reconstruction uses inputs and rules rather than reading final defender cells.

| Attempt | Creature | Candidate (X,Y) | Result |
|---|---|---|---|
| 1 | Fire | (13,2) | Success |
| 2 | Earth | (12,8) | Success |
| 3 | Water | (12,8) | Failure |
| 4 | Water | (12,4) | Success |
| 5 | Air | (12,8) | Failure |
| 6 | Air | (12,4) | Failure |
| 7 | Air | (12,10) | Success |

**Observation:** seven attempts, four successes and three failures matched the executable reconstruction. The hero's angels stand at (3,4).

**Conclusion:** the ordinary pass is confirmed for this field and recorded mode. This experiment does not test other strategies.

**Artifacts:** [JSON with both armies, masks and context](../../assets/placement/observations.json), record `elementals_trace`; [reconstruction code](../../assets/placement/placement_walkthrough.py); [step-by-step diagrams](../players/army-placement.md).

JSON SHA-256 at this entry: `3865ebc7623a024edafc5f208834070916b0bf651e27f5f3e63ba01b64f0718c`.

**Review correction:** the older `pack_12` record has no captured mode. Code requires explicit `assumed_context`; matching cells under that assumption does not prove the game selected that branch. The article retains this limit.

## September 23 — battle images and failed capture {#captures}

**Task:** compare a full 2D diagram with the actual battle view.

**Preserved:** `pack_15` and `pack_12` frames with different armies, plus an archived Academy before/after Start pair. Original PNGs were not retouched. Diagram coordinates came from Start records, not camera interpretation.

**Failure:** later captures of new launches produced blank black/white frames, including without tracing. The cause remains unknown; those frames were not used as confirmation. No successful new capture is claimed.

[Data and image hashes](../../assets/placement/observations.json) · [Article images and diagrams](../players/army-placement.md). Raw failed-launch logs are not yet public.

## September 22–23 — placement-model corrections {#placement-corrections}

| Earlier assumption | Check result | Consequence |
|---|---|---|
| Field `+0xdc` is creature tier | Registration/XML loading identify CombatSize, range 1…2 | Do not substitute tier into CombatSize>2 |
| Equal scores retain input order | Ordinary sorting selects the right lane on equality; 10 equal rows yield 8,4,6,10,2,7,3,5,9,1 | Preserve native ordering instead of arbitrary stable sorting |
| Spread evenly rounds rows | Integer division gives {0,4,9} for R=10,N=3 | Rounding to {0,5,9} changes the result |
| Crowded stacks always merge | The inner loop at `0x8599d0` is unreachable for tested valid vectors N=0,1,2,3,7,64 | A branch name does not establish merging |

**Method:** instruction/field-loader analysis and emulation of individual routines. Ordinary numeric sorting matched 3280 sequences of length 0…7 over {0,1,2}; this enumeration did not test the getter-dependent comparator.

[Formulas and addresses](placement-internals.md) · [Creature fields](creatures.md). Full original emulator traces are not public; this table is a reconstructed record of findings, not a new live test.

## September 21–23 — grouping bank guards {#banks}

**Question:** can variant indices be labelled T1,T2,T3… directly?

**Resource check:** crypt has eight variants across four tiers, magi vault five across three, utopia seven across five. Variants therefore need mapping through armies, rewards and AG_INFO panels.

**Correction:** demon-bank `05_01_SIZE.txt`…`05_04_SIZE.txt` describe five groups of three slots. Totals across 15 slots: T1 90–135, T2 120–165, T3 150–195, T4 180–225. The earlier “8 imps” minimum mixed different variants and was discarded.

**Limit:** resource inspection does not reveal an individual object's chosen guards. Twelve game Types and 13 AG_INFO families were mapped; OrcDeposit's Type remains unresolved.

[Catalog, resource paths and calculation](banks.md). The full original resource extraction is not attached; game archives are not distributed with this knowledge base.

## September 21 — main-menu marker {#menu-marker}

**Question:** does the game load text from a separate H5U in UserMODs?

**Experiment:** override `UI/MainMenu2/Version.txt`, append `[DEV: menu-marker]`, preserve UTF-16LE BOM. ZIP-member timestamp was the original plus two seconds. Restart between installation and removal.

**Observation:** the owner confirmed appearance after installation and disappearance after removal. The first test-copy launch exited unexpectedly; a retry succeeded. The first exit's cause remains unknown.

**Conclusion:** this resource override worked. General archive precedence and resource hot reload remain unestablished.

[Reproducible packager and steps](../modding/resource-overrides.md). The original experiment log is unpublished; this entry is retrospective.

## Recording rules

- Each experiment records its date, question, build, inputs, actions, observation, conclusion, limits and result files.
- Distinguish **observation**, **inference** and **hypothesis**. Preserve failed experiments too.
- Do not rewrite a published observation to fit a new conclusion. Append a dated correction linking the earlier entry. Typo fixes and removal of accidentally published personal data are allowed; technical corrections must preserve history.
- Articles link to entries; entries link to data, code and images. Record SHA-256 for files important to reproduction and retain earlier versions in Git when replacing them.
- An ADR records **a project decision**: context, options, choice and consequences. Game experiments belong here rather than becoming ADRs.
