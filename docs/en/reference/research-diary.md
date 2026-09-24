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

**Correction on September 24, 2026, after publication:** the previous hash belongs to the local Windows copy with CRLF. The downloadable JSON and Git blob use LF: 22919 bytes, SHA-256 `cdb06375ba4a46194f32eab8337a0087ca4df2cfab67b5633f33954b8f26ab28`. Byte comparison confirmed only line-ending conversion; experiment data are identical. Use this second hash to verify the download.

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

## September 24 — reading ArmyWnd from the archive again {#army-resource-check}

**Question:** can readers independently reproduce the size and `Visible=true` finding without running the mod?

**Actions:** opened the original `data.pak` with a standard ZIP reader, read three UI resources as bytes and parsed their XML. This repeat ran on September 24 without launching the game; it checks files, not live hovering.

| Resource under `UI/Tooltips/CommonAdvObjTooltip/` | SHA-256 of bytes inside ZIP |
|---|---|
| `ArmyWnd.(WindowSimple).xdb` | `30a503de3aa0d28c29229a5d9d51cc98ea324ac32ea27a8388ebb8067bc1a2e9` |
| `ArmyWnd.(WindowSimpleShared).xdb` | `782648e5e3e329701e261eced6f5b41da13830c61691a7c7dd833ed048eb531f` |
| `MainWnd.(WindowGatheringShared).xdb` | `3b41fc1c4979187c74e4bd0ccc28bd7ebed9bfd30a1c700bcebfedfccb0ff617` |

**Result:** the ArmyWnd instance has size 197×110 and `Visible=true`. Its Shared resource has `Size/First=0×0` and `Size/Second=false`; reading only Shared does not establish a zero-sized panel. All three hashes match the September 21 research record.

**Conclusion:** resource visibility is already enabled. This does not establish that the game supplied model data or selected the window. [Reproduction code and explanation](../modding/native-ui.md#read-army-resource). Game XDB files are not distributed; the example reads an installed copy.

## September 23 — projection range and input checks {#projection-range}

**Question:** can reachable cells be highlighted before Start using public creature properties?

**Method:** the C++ function receives speed, Flying, CombatSize and an obstacle mask. Orthogonal steps cost 2, diagonals 3, with a `speed × 2` budget; highlighting includes complete legal landing footprints. Other projections and visible player-army cells are added to the static mask.

**Algorithm check:** 16 authored fields matched execution of original `0xb5f0d0` in an emulator. Allocation/free were substituted and the source EXE hash was checked. Cases covered diagonals, a wall, flight/landing, a 2×2 corridor, boundaries and buffer guards. This is the preserved September 23 result, not a new September 24 run.

**In-game observation:** frames showed the 2×2 genie's range, a smaller golem range and dismissal on exit. A subsequent background run passed five battles, card switching, cursor exit, menu blocking, type changes and cleanup after Start. These results do not confirm physical RMB holding.

**Prediction limit:** another control matched pack_8 at 3/3, pack_12 at 4/4 and pack_15 at 3/7; a further run gave 0/7 for pack_15. Single-type pack_0/pack_1 had one projection against three/two actual stacks. Successful rendering does not establish exact placement for every army.

[Cards and current prototype limits](../players/deployment-preview.md) · [Input boundary](../modding/public-information.md). Original run reports and the 16-field fixture are not public yet. Reconstructed September 24 from preserved results.

## September 22 — five battles in one process {#projection-lifecycle}

**Question:** can native projections survive another battle without leftover models and references?

**Scenario:** ordinary attacks on `pack_8 → pack_12 → pack_15 → pack_0 → pack_1`, creating **3 / 4 / 7 / 1 / 1 projections**. These were not artificial `StartCombat` calls with supplied armies.

**Result:** each battle checked boundaries, non-overlapping footprints and cleanup; generations increased from 1 through 5. The first also checked hover and the card. Two recorded processes completed the sequence and normal exit; 42 tests passed at that checkpoint.

**Established:** repeated creation/removal in these scenarios. **Not established:** agreement with final AI deployment. Upgrade cycling did not yet exist in this checkpoint and cannot be credited to that earlier run.

Historical DLL hash: `8290957f03a1eb526168430f69fefb45fa2a01859a96f19f2251d7dd273dfa4b`. This identifies the checked file, not an available release. Original logs and this DLL are unpublished. [Why second-battle cleanup matters](../modding/native-ui.md). Reconstructed September 24.

## September 21 — from army template to renderer invocation {#army-tooltip-probe}

**Initial hypothesis:** enabling the stock `ArmyWnd` container through XDB might show reference bank guards.

**Resource check:** ArmyText, seven CreatureFace.1–7 cells, 40×40 frames and 34×34 portraits were found. `Visible` was already true; visibility alone was insufficient.

**Next experiment:** a temporary entry counter at `0x5f8050`, without reading actual guards.

| Action | Cumulative counter |
|---|---:|
| Before hovering | 0 |
| Hovering bank and neutral pack | 47 |
| Then bank and empty ground only | 51 |

**Conclusion:** the bank tooltip path invokes the renderer. The four additional calls cannot be separated into show/hide events; no frame recording exists for this experiment. Invocation does not establish safe integration of a new reference model.

**Static refinement:** model slots `+0x38/+0x3c/+0x40` supply population condition, count and indexed access. The inspected implementation uses a 24-byte stride; `0x5fd080` computes count and `0x5fd0a0` obtains an entry. An entry carries texture, numeric and string labels. This describes one implementation, not a ready ABI for arbitrary objects.

[Current native-window explanation](../modding/native-ui.md). Addresses apply only to the pinned EXE. The manual record was reconstructed September 24; no separate public counter dump is available.

## September 21 — assessor button and OCR {#assessor-inputs}

**Task:** selected hero → visible neutral tooltip → Assess button.

**Options:** integrated button or external window. The integrated route had WindowMSButton and a UI_SHOW_WINDOW example, but these did not establish arbitrary Lua callbacks. An external window required capturing the tooltip before losing hover and validating recognized text.

**Checked:** a hidden Tk 8.6.12 test window opened and closed; Windows OCR recognized synthetic “Imps 20–30”. Later, the user confirmed the persistent button accepted a click and displayed a diagnostic response.

**Unfinished:** victory/loss model, automatic selected-hero acquisition and the complete visible-input path. Recognizing a synthetic image does not test the game font or a fullscreen external overlay.

**Retained calculation requirement:** use known own-hero data and visible enemy types/ranges; compare endpoint cases. If outcomes differ across the range, report uncertainty/risk, but this remains an unimplemented plan. Reject `40–32` rather than silently swap bounds. Stock Danger is not treated as a validated estimate because its input origins remain unknown.

[Available inputs and OCR checks](../modding/public-information.md). Original button/Tk/OCR logs are not public yet. Reconstructed September 24.

## September 21 — Universe inventory and comparison-base correction {#archive-inventory}

**Method:** eight `data/*.pak` files opened as ZIP; resources compared byte-for-byte against local `data.pak`, `a2p1-data.pak`, `texts.pak` and `a2p1-texts.pak`.

| Archive | Total | Changed | New paths | Identical |
|---|---:|---:|---:|---:|
| Universe_mod.pak | 5159 | 1075 | 4047 | 37 |
| universe_mod_texts_ru.pak | 1771 | 605 | 942 | 224 |

**Correction:** the initial main-archive count without text baselines was 1074 changed / 4048 new. Including all four baseline archives produced 1075 / 4047. Difference counts therefore need their comparison-base definition.

**Limit:** the local baseline was not independently verified as clean stock ToE. File counts are not feature counts; DLLs can change behavior beyond resources. Menu version 2.0 and a DLL PAK-check string 1.8 do not identify one version unambiguously.

[Original comparison CSV](../../assets/archive-diff.csv) — all 6930 rows for two archives, without game resource contents. Publication on September 24 normalized line endings to LF only; original rows/fields were preserved. Recounting CSV rows confirmed the table; no fresh comparison of all game archives was performed.

Download SHA-256: `81115018610632c94b9db9566b28cc85afa3e42b76cf2c37e3ffbfc4a5af4299` (732359 bytes). [Fields and recount code](universe-build.md#archive-diff). The experiment record was reconstructed September 24; the complete inventory of all eight archives remains unpublished.

## Recording rules

- Each experiment records its date, question, build, inputs, actions, observation, conclusion, limits and result files.
- Distinguish **observation**, **inference** and **hypothesis**. Preserve failed experiments too.
- Do not rewrite a published observation to fit a new conclusion. Append a dated correction linking the earlier entry. Typo fixes and removal of accidentally published personal data are allowed; technical corrections must preserve history.
- Articles link to entries; entries link to data, code and images. Record SHA-256 for files important to reproduction and retain earlier versions in Git when replacing them.
- An ADR records **a project decision**: context, options, choice and consequences. Game experiments belong here rather than becoming ADRs.
