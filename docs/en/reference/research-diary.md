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
updated: 2026-09-26
---
# Research diary

## September 26: sheltered formation and prediction limits {#placement-defence-2026-09-26}

**Question:** why does a seven-stack pack sometimes shelter its shooters and sometimes use ordinary placement despite similar visible composition?

**Retrospective record:** we compared a completed ten-load series from September 25 with the defensive-pass analysis from September 26. Prediction was frozen before Start; the game's decision and actual cells were read separately after Start. EXE SHA-256 was `88c9dc6107b9bced0649924a86360f1c56397ee00de0413f6f2b08f865ed5519` and the older DLL SHA-256 was `30caceb1a584a99418d37b6a2f7424dc18c5214cbb6a4ccbbbe92d05f4a1498e`. The full working JSON is not published.

| Polygon `pack_15` | Round 1 | Round 7 |
|---|---:|---:|
| Hero army | 10 Angels | 10 Angels |
| Hero Attack / Defence | 1 / 2 | 1 / 2 |
| Day and visible quantity bands of seven neutral stacks | Same | Same |
| Internal shooter-power share; threshold 0.2 | ≈0.217 | ≈0.183 |
| Game's sheltered formation | Yes | No |
| Exact “type + cell” pairs from older DLL | 3/7 | 7/7 |

**Finding and limit:** public quantity bands do not determine exact neutral strength; hidden quantities can affect sheltering. But exact counts for these two records were not retained, and the arenas differed. The table establishes different internal estimates and decisions with the listed visible inputs unchanged; it does **not** establish the sole cause. Do not invent a terrain rule to fill the missing input or attribute every miss to this ambiguity.

Across ten loads, the older candidate matched **all occupied cells in 111 of 149 mixed battles**. This counts **battles**, not individual cells, and does not ensure every creature type occupies its exact expected cell. Polygon `pack_15` had only 3/7 exact pairs in rounds 1 and 10, so an every-battle 5/7 threshold remains unproven. Two mismatch explanations in the series remained incomplete. The newer C++ defensive ordering passed recorded offline attempts but has not completed a fresh live campaign; the older DLL's score does not transfer to it.

[Player explanation](../players/army-placement.md#mixed-armies) · [technical rules](placement-internals.md). This is a prepared summary of local observations, not a release of the full raw log.

## September 25 — why the mixed pack matched 1/7 {#placement-policy}

**Question:** observer error, DLL startup or placement calculation?

**Method:** ordinary DLL loading, WorkshopPolygon, pack_8 → pack_12 → pack_15. Predictions were saved before Start; GetUnitPosition recorded positions separately. An additional observer captured parameters before `0x8598e0`; these records were read after combat and never supplied to the predictor. Random state was not fixed between runs.

**Observations:** the general formation matched 5/7 and 6/7. Run32808 matched1/7 with `defensive=1`: the engine used a protective pass the predictor does not yet implement. This establishes a different placement sequence, not the sole cause of older run31848, whose flag was not recorded. No causal link to DLL loading was established.

A separate shooter-window defect was found: with `enemyLarge=1`, the engine uses the minimum approach length of two neighboring rows; the predictor always used one. Replaying record13044 moves the three-row window from6–8 to7–9. A dedicated test reproduces this without reading final positions.

**Local C++ DLL correction:** the owner authorized the known hero army as input. Large-creature share is estimated from its types/counts, public definitions and the threshold in loaded game settings. Hidden neutral upgrades, quantities and splitting are not read. Mixed hero-army weights remain approximate: a synthetic reference score without hero bonuses is used.

The candidate passed11 tests without skips. A new general pass matched7/7; a protective pass still matched1/7. Replacing angels with peasants switched `enemyLarge` to0, but the protective mixed pack matched0/7. **Overall accuracy is not fixed.** The protective pass and mode selection remain separate work; selection also depends on unavailable neutral strength. This candidate is not part of published preview.2.

[Data: predictions, Start positions, flags and approach lengths](../../assets/preview/accuracy-policy-2026-09-25.json) · [Predictor](../players/deployment-preview.md). Full working logs are unpublished; the artifact contains sanitized numerical records and the EXE/candidate SHA-256 hashes. All test processes exited normally.

## September 25 — generator packs and Superadmin source {#rmg-placement-check}

**Question:** does accuracy hold for Universe RMG neutrals, and what causes the failures?

**Method:** two local RMG maps were copied into the sandbox. Only the copies received addressable monster names, forced combat instead of flee/join, and an after-Start cell observer. Original maps and creature armies were unchanged. Predictions were frozen before Start. Separate after-Start observers recorded placement policy, the spread decision ratio, splitting and candidate-cell attempts. Hidden source inspection required an explicit Superadmin opt-in; ordinary runs did not read it.

**One ordinary RMG-A pass:** **9/24** selected packs matched all cells, including **9/18** mixed packs. This is one pass, not the ten-load result. Six misses were solo-stack splits, eight were mode mismatches, and one still needs exact cell-order reconstruction. An earlier pass of the same map matched3/24 with different hero/RNG state. Solo results remain recorded; the primary gate now concerns mixed packs.

**PanUI reference check:** the image's `4,9,1,6,3,8,2,7,5,10` labels are already reproduced by the DLL's five-bit reversal of `y−1` when row scores tie. The portrait groups show creature priorities, but their full mapping to game IDs and categories has not yet been checked; the DLL reduces them to three broad groups. The image does not select defensive or spread placement, so changing the number order cannot repair the eight branch mismatches.

**A measured split:** in one solo encounter, ratio `1.0189` selected two initial stacks; RNG roll `44` left it unchanged, so the original30 creatures became two combat stacks. The cause is captured from the engine, not inferred from final cells alone. In a separate RMG encounter, the engine enabled spread and chose rows `y=10` and `y=1`, while the ordinary DLL showed `y=8` and `y=4`. The published data include approach lengths and accepted/rejected candidates.

**Research Superadmin:** an explicitly enabled DLL returned RMG source `(92,18),(98,8)` **before Start**; ordinary startup returned an empty list. Manually selecting spread and using hidden counts matched4/4 in one isolated four-stack control. This isolates rules, not an automatic exact mode: a different manually forced spread series matched only6/19, then4/19 when the engine chose another policy. The100/100 target has not been reached.

[Numerical records and build hashes](../../assets/preview/rmg-accuracy-2026-09-25.json) · [technical mechanism](placement-internals.md). Complete logs and RMG map archives remain local. The final ten-load campaign and≥70% complete matches among **mixed** packs have not passed; newer DLL changes need fresh validation.

**Later September25 control:** one RMG-A pass, with the player's own army restored to its starting composition before each battle, fully matched10/18 mixed packs. All eight misses used another native branch: five spread, three defensive. On RMG-B,0/13 mixed packs fully matched: the engine spread twelve and used defensive plus spread for one. Neutral compositions were unchanged, but arenas and random decisions varied between passes. These two loads do not replace the required ten.

**Next September25 candidate:** the DLL now reads qualitative count bands from stock public cards, never exact neutral quantities, and uses them to estimate spread and defensive selection. Separate fresh loads matched all cells in13/18 mixed RMG-A packs and11/13 mixed RMG-B packs. On the polygon, one defensive seven-stack battle against a small hero army matched all seven creature+cell pairs. With10 Angels, the DLL often falsely enables defence that the game suppresses; the exception is still under study. Reconstructed spread arithmetic matched205/205 native calls **after Start**, but those observations never feed ordinary prediction. These are separate experiments, not the required ten-load campaign or the independent pre-publication review.

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

[Original comparison CSV](../../assets/archive-diff.csv) — all 6930 rows for two archives, without game resource contents. Publication on September 24 removed the UTF-8 BOM and normalized line endings to LF; original rows/fields were preserved. Recounting CSV rows confirmed the table; no fresh comparison of all game archives was performed.

Download SHA-256: `81115018610632c94b9db9566b28cc85afa3e42b76cf2c37e3ffbfc4a5af4299` (732359 bytes). [Fields and recount code](universe-build.md#archive-diff). The experiment record was reconstructed September 24; the complete inventory of all eight archives remains unpublished.

## September 24 — extracting the development environment {#devkit-extraction}

**Task:** make shared tools usable without the private workshop or an individual mod.

**Change:** builder, control-channel, map-generator, UI-helper and archive-inspection source/tests moved to [heroes5-mod-devkit](https://github.com/Xaaalera/heroes5-mod-devkit). H5_WORKSPACE/H5_GAME_DIR locate mutable data; old workshop commands bridge to the canonical implementation. The predictor C++ DLL stays with its mod.

**Dependency found:** the generator read its bank list from the object-reference recipe and assumed the journal directory existed. The first empty-workspace build left an H5M without its journal and then refused to overwrite it. The recipe dependency was removed and the journal directory is created before writing. A new empty-directory run passed: 60 objects, six arenas and valid ZIP. The initial failure is not described as a successful first attempt.

**Checks:** 37 isolated devkit tests and 48 workshop checks through bridges passed. PowerShell forwarding used an inert fixture without a game. Experimental UniverseTrigger subscriptions were removed from the generic generator. No separate live-game launch followed extraction; these checks establish code portability and file generation.

**Review correction:** the old tools prepended workspace `.local/native-analysis` to Python imports. An inert fixture demonstrated module shadowing before PID checks. The devkit now imports no code from that data directory and uses installed Python-environment dependencies. The old version failed the fixture; the corrected version passed. Map-startup path validation also received regression cases.

**CI correction:** GitHub Windows used a short `RUNNER~1` path while the CLI returned its full form. The first path-string comparison failed despite an identical destination. The test now compares resolved paths; runtime code did not change.

[Environment and commands](../modding/devkit.md). This publishes tools; earlier statements that command tooling was unpublished describe the period before extraction. No universal native API is claimed.

## September 24 — two mod repositories {#mod-repositories}

**Task:** separate predictor and bank-reference source from the shared workshop and pin the development environment.

**Result:** [predictor](https://github.com/Xaaalera/heroes5-deployment-preview) owns its C++ DLL/loader and checks; [bank reference](https://github.com/Xaaalera/heroes5-bank-reference) owns its window recipe with embedded catalog. Both pin devkit 1b8934ac084491da460ce8bb145819e41e2cf888 as a submodule. SDK --source builds from a separate checkout; deploy installs the existing H5U.

**Preservation check:** C++ logic was unchanged, with text-format normalization only. The standalone bank package, 1215708 bytes, was byte-identical to the former build: SHA-256 824a14b48fbdadce9ea0475b49bc4d1f1f6d2ef112ef8294b63cc1ea4ebf7f1e. The original 17 native/prototype tests were partitioned into 9 predictor, 2 reference and 6 retained private Python-prototype checks. Two new recipe and two new SDK cases increased the workshop suite to 52.

**Checks:** x86 Release built in the new directory; 9 predictor checks with the local game oracle and 4 reference checks passed. The first isolated reference-test run found a missing random import; it was restored before the passing run. Without a game, only the explicitly identified EXE oracle may be skipped; other skips prevent acceptance. This is not a fresh live battle.

**Installation:** predictor uses its own DLL loader; reference currently needs H5U plus devkit's diagnostic --army-layout. Combined use remains unverified. [Both installation guides](../players/mods.md). Earlier H5U/Python experiments and the diagnostic assessor are not part of these deliveries.

## September 25 — ordinary startup and DLL mods {#dll-delivery}

**Decision:** separate player EXEs were rejected. Preserve normal Heroes/Lobby startup; both EXE candidates were withdrawn. This corrects delivery after the [repository split](#mod-repositories), without rewriting earlier experiments.

**Mechanism:** the pinned H5_Game.exe imports DirectInput8Create and had no adjacent dinput8.dll. A new file from [devkit 71509e4](https://github.com/Xaaalera/heroes5-mod-devkit/tree/71509e43af0faf080d8a47ed5b3ff8c72da2a3e9) forwards to the Windows system library and initializes our DLLs under bin/Heroes5Mods, outside DllMain. Original EXE/d3d9/uni/um files are not replaced. Game hashes establish compatibility, not plugin authenticity.

**Actions and observation:** ordinary H5_Game.exe reached the menu with the predictor DLL; both DLLs then loaded together. Five battles used the ordinary game process with development-only polygon startup, command mailbox and separate Start observer. Card input used addressed messages, not a new physical-RMB acceptance. Projections cleared, the map returned and the game exited normally.

| Scenario | Predicted / after Start | Exact cell matches |
|---|---|---|
| pack_8 | 3 / 3 | 3 |
| pack_12 | 4 / 4 | 4 |
| pack_15 | 7 / 7 | 1 |
| pack_0 | 1 / 2 | 0 |
| pack_1 | 1 / 1 | 1 |

**Conclusion:** startup/card/cleanup checks passed, not five exact predictions. Mixed-pack placement and stack splitting differ. A relationship to DLL initialization timing is not established because runs did not fix the same random state. [Summary and after-Start observations](../../assets/preview/dll-checks-2026-09-25.json).

**Environment correction:** the sandbox still had old workshop-object-reference.h5u, which inserted long text above portraits and stretched the card off-screen. After its normal removal, the [crypt card](../../assets/preview/bank-reference-crypt.png) was captured with both DLLs automatically loaded. It is an actual 1264×921 foreground-client capture, not a reconstruction; SHA-256 18beb8c79f7e627a52ecf9e5a510653a15be8f5f01cf4d4fcc762af1f9d4279e.

**Invalid package:** missing bank H5U initially could leave the predictor partly installed. Policy changed to cancel startup. The first dialog inside InitOnce hung; reporting moved after InitOnce, rejecting reentrant input. The repeat showed one dialog and exit code 1114. The temporarily removed H5U was restored. A separate fixture checks preservation of foreign content on installation refusal.

**Limits:** SDK passed 39 Python, 8 Node and 2 native CTest checks; predictor passed 9 and reference 6. This does not cover every bank, arena or display size. The Heroes/Lobby UI itself was not automated; the ordinary game EXE and automatic loading mechanism were checked. New DLL packages remain under acceptance at this entry's date. No game distributions, profiles or private logs are published.

### Follow-up after DLL package publication

[Predictor preview.2](https://github.com/Xaaalera/heroes5-deployment-preview/releases/tag/v0.1.0-preview.2) and [reference preview.2](https://github.com/Xaaalera/heroes5-bank-reference/releases/tag/v0.1.0-preview.2) are published. Unauthenticated downloads returned HTTP 200 and neither ZIP contains an EXE. Shared dinput8.dll is identical in both archives: SHA-256 7959116c5e61369a9af533eb460b09b0e7a897543a6ede2fc1075800a7a62837.

| Archive | Bytes | SHA-256 |
|---|---|---|
| Heroes5DeploymentPreview-0.1.0-preview.2.zip | 155145 | cd9470ee0ecf44ceaddf4eb994ae2ba0a7ad3447dd618d2a9862245a25a1acda |
| Heroes5BankReference-0.1.0-preview.2.zip | 773747 | 8371720bc99d0f7a92f9416eb7945f5c6cab5d6927cb00d7e9fcbd1e54c7b52f |

After temporarily removing both mod DLLs, shared dinput8.dll and the H5U, the ordinary game EXE reached the menu and exited normally with code 0. Test files were then restored. All four original binary hashes stayed unchanged. This checks disabling the complete pair, not every combination with other mods.

The five battles used a local WorkshopPolygon variant with SHA-256 85247993da2370ae3325d4f41d3c89e4395b7a60dab31e9d7149ec0662e2c587, different from the article's published map. The linked observation summary is available, but is not a claim of exact reproduction on any polygon version.

## Recording rules

- Each experiment records its date, question, build, inputs, actions, observation, conclusion, limits and result files.
- Distinguish **observation**, **inference** and **hypothesis**. Preserve failed experiments too.
- Do not rewrite a published observation to fit a new conclusion. Append a dated correction linking the earlier entry. Typo fixes and removal of accidentally published personal data are allowed; technical corrections must preserve history.
- Articles link to entries; entries link to data, code and images. Record SHA-256 for files important to reproduction and retain earlier versions in Git when replacing them.
- An ADR records **a project decision**: context, options, choice and consequences. Game experiments belong here rather than becoming ADRs.
