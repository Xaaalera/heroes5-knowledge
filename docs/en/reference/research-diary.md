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
updated: 2026-10-08
---
# Research diary

## 2026-10-08 — current placement-algorithm status {#placement-checkpoint}

Algorithm work has been paused since the switch to SDK development on 4 October. The [technical account](placement-internals.md#current-research) is updated; the research DLL's new mechanisms have not shipped in the player package.

The last tested DLL before the pause corrects source shooter classification. Its own results are **60/60 native tests**, **3/3 stacks** in the counterexample and **36/36 full-polygon battles** with 100 Archers in the hero army. The full ten-load campaign stopped after two loads and three battles of the third. It is not a completed ten-load success.

Earlier builds retain separate results: **151/151** across five loads for the preceding version and **273/273** across ten loads for an older one. Each result has its own DLL and scope. The early 111/149 occupied-cell matches and 14 native tests are historical stages rather than the current result.

Evidence: locally verified records `definition-category-counterexample-verification`, `cc368-ranged-full36-verification` and `new-dll-rmg43-verification`, plus the owner's campaign-stop record. The research DLL and raw reports remain local; this version is not downloadable from the website. Reading source and reports is not a new game run. The complete algorithm, ordinary-mode input policy and post-Start explanations for every player remain unfinished.

## 2026-10-08 — resource mod without installed xkit

- The owner clarified player delivery: install a ready mod and start Heroes/Lobby normally. A required shared DLL may accompany the mod; players do not need xkit development tools.
- `xkit release` retains the separate H5U and creates a ZIP containing it, the verified graphics DLL, notices and bilingual instructions. `xkit build` still produces the H5U. The DLL comes from the prepared SDK without invoking a compiler; the game original is not redistributed. This addition is published in preview.5; preview.4 does not contain it.
- The exact generated ZIP was checked in the test game: a complete menu displayed the resource mod marker, while the loaded-module inventory excluded the SDK core, developer console, plugin bootstrap and controller. The game exited normally through its menu buttons; the test game's original graphics DLL was restored. The complete run took 19.34 seconds.
- This checks a resource package with the shared graphics facade. It does not certify original-DLL test startup without that facade or multiplayer compatibility. Granny failure history remains separate; the established workaround serves working player delivery.
- Mechanism and installation: [SDK commands](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/docs/commands.md). [Preview.5](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.5) is published from `757a19a`: five independent reviews, 199 Python tests, 8 review checks, 7 native suites and CI passed. The public SDK archive digest matches the separately installed complete SDK; its short CLI released a resource player ZIP without a compiler. Installation uses the README's `--editable` flag; the control omitting it is retained as a procedure error, not a product fix.

## 2026-10-08 — published SDK preview.4 acceptance

- [xkit preview.4](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.4), revision `0c406f4`, fixes short-cache selection after moving SDK source. Five independent reviews, 198 Python tests, 8 JavaScript checks, 7 native suites and CI passed. The archive digest matches the published asset.
- The actual public ZIP was downloaded and installed through uv in an isolated test environment. `xkit start` automatically applied native source 42→77 in the same process; DLL release used the verified 77 source. Game and monitor exited normally. Installation took 6.60 seconds; the separate startup/release run took 109.12 seconds; save to confirmed application took 3.28 seconds. These intervals are not first visible-frame timing. Resource H5U build and release through the installed CLI also passed.
- Pure H5U acceptance without SDK remains open. The original game crashed in Granny after temporarily removing the test package; no other H5Us were present. A separate dump with no SDK modules confirmed the earlier fault: the graphics library occupied Granny's preferred region while an internal memory pointer still referenced the old placement. The package was restored with a hash check. This explains the observed original-chain crash, not a resource-mod visual acceptance pass.

## 2026-10-08 — frame capture and complete HMR timing

- Published [xkit preview.3](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.3) from revision `f5d9a76`, with Game API `a71985c`. Five independent reviews and final CI passed: 198 Python tests, 8 JavaScript checks and 7 native suites. The published archive digest matches the verified build.
- `xkit game screenshot` received a new complete PNG through the active SDK core; the test frame showed the intro. Dispatch return does not establish map readiness. Refusals do not replay through another route; diagnostic-client exit does not stop plugins.
- A separate control of exact bank player archive preview.4 verified the Crypt card: ordinary startup, installed DLL checked before diagnostic connection, selector code unchanged. The hero was then positioned diagnostically; an actual capture showed T1–T4, A/B, portraits and counts. Scope: one object, Russian interface, 1024×768; full check 26.72 seconds, normal exit.
- Native test-plugin timing starts before saving source and ends after capturing the visibly changed `2001` inside the same owned game window. 3.31 seconds to capture, 1.82 seconds to build, 10.21 seconds for the full run. The result was placed inside the game window outside a Discord notification. This is an upper bound to observing the test UI including capture and positioning, not exact first game-frame time or universal mod performance. The game exited normally.
- Prior CI failed because the new test compared short and full Windows temporary-folder paths. Resolving the expected path fixed the test; production process guards stayed unchanged. Separate resource-H5U visual acceptance without SDK remains open because of the known original graphics-chain Granny failure.

## 2026-10-08 — SDK release and bank development adapter

- Published [xkit v0.1.1-preview.1](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.1) and [bank reference preview.4](https://github.com/Xaaalera/heroes5-bank-reference/releases/tag/v0.1.0-preview.4). Remote archive digests match verified local files. SDK CI passed 197 Python tests, 8 JavaScript checks and 7 native tests; bank reference passed 6 checks with no skips.
- Bank development verifies the crypt card and populated cache through automatic bank DLL and SDK core updates. A comment change checks the update lifecycle; a separate version-marked callback verifies changed code execution. Incompatible data structures are rejected. Predictor work remains paused.
- The fresh bank player archive passed ordinary startup: installed selector instructions match the build and the game exits normally. The full check took 6.19 seconds. Card rendering from this exact archive is still unverified; development results do not establish it.
- A new attempt to observe standalone H5U output without the SDK crashed. Windows attributes the fault to Granny, the game's animation library. Earlier dumps linked similar failures to DLL placement; this run has no new dump. [Microsoft PE documentation](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format) explains relocation but does not prove this crash's cause. Ordinary startup and the visible marker remain unverified in a single matching process.

## 2026-10-07 — published xkit SDK

- [xkit 0.1.0](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.0) includes sources, Game API and a ready runtime. The downloaded archive matches the verified bundle by SHA-256. Python176, native7 and hosted CI passed.
- Live `xkit check --player` verified added functions/core export, two-plugin HMR, state transfer, callback teardown, rollback and independent DLL packages during ordinary startup. Both owned games exited0; full111.33-second cycle. This is SDK evidence, not a new predictor accuracy result.
- Console checks used physical Ctrl+Enter, history, Tab, mouse resizing and overflowing log scrolling without camera zoom. Returning to the map restored zoom. Severity levels and full structured journals remain available.
- CI first exposed short/full Windows path comparisons, then missing Game API checkout. Both attempts are retained and corrected; final hosted CI passed. Predictor algorithm work remains paused.

## 2026-10-06 — added core export through automatic HMR

- The baseline DLL lacked the new named console-command export. Canonical core replacement made it available in the same game, retained the plugin counter, and allowed the CLI to load the map and read expected heroes.
- A separate control used the existing source watcher. Saving the file automatically built/applied the new core in4.23 seconds from save to confirmed application. The new command worked, counter persisted and generation correctly advanced. Watcher/game exited normally; full control27.71 seconds.
- This was an acceptance source snapshot, not another active devkit. Canonical checkout stayed unchanged. The first control incorrectly required generation to stay constant; that failed report remains retained. HMR advances generation while retaining state.
- SDK archive inclusion and current source matching are verified. They do not establish fresh independent installation, physical input or ordinary delivery. Whole acceptance continues; new changes are unpublished.

## 2026-10-06 — map restart and return to the menu

- Added xkit game restart with an explicit map name and xkit game menu. Command help and human results share the terminal and embedded-console registry.
- An owned process changed a map resource, then confirmed its reset and the startup script running again. The first read showed the base resource; the next showed the scripted value. Dispatcher return does not mean map initialization is finished.
- A stock game capture confirmed the actual main menu in that same process. Subsequent map loading returned the eight expected heroes; the active plugin retained its counter and generation. The complete capture control took15.97 seconds with normal game/client exits.
- Initial control-script errors remain separately preserved. Command tests passed29 and console17; a separate routing review found no issue. Physical panel input, added-export HMR and ordinary delivery are not certified by this control. New changes are unpublished.

## 2026-10-06 — map loading through the human xkit command

- xkit game map WorkshopPolygon is connected to stock native dispatch. Help and output support Russian and English, Tab completes map filenames, and the embedded console uses the same command registry.
- The short client borrows the resident core without stopping plugins when it exits. Live control loaded the map, returned the eight expected heroes and preserved the active plugin's counter and generation. The corrected complete control took10.37 seconds with normal client/game exits.
- The first control caught the map receipt being overwritten by status; it was fixed and the original report retained. Command JSON separates dispatcher return from verified game effect. Native checks passed6/6 and Python149; separate review concerns the new client mode and routing only.
- Physical console entry, added-export HMR, the current independent archive and ordinary released-mod startup still need acceptance. New changes are unpublished.

## 2026-10-06 — stock map loading from the menu

- Shared Game API gained an experimental stock-console binding. It uses the game's string and allocator on the verified main thread; SDK marshals a separate message without taking plugin command numbers.
- Menu command registration and an actual setting change were confirmed. Requesting WorkshopPolygon produced a captured loaded map; a separate query returned the eight expected heroes. The final complete control took8.07 seconds with normal client/game exits. Native checks passed6/6 and a separate review found no issue.
- Two verification limits were found separately: an interpreter count stayed zero on the loaded map, and the first custom query assumed the wrong GetAllNames result format. Original unsuccessful reports remain retained; positive facts have a separate bounded acceptance record.
- Public CLI integration is pending. It needs a resident-core borrowing mode that does not stop plugins when the diagnostic client closes. New-export HMR, full console and ordinary delivery acceptance remain open. The sandbox used import repair and its existing controller before first thread resume; new changes are unpublished.

## 2026-10-06 — command errors now retain the latest outcome

- The console panel connected to the real Universe menu. Previously a failed request displayed its message but left the latest outcome empty or stale; initial UI validation waited until timeout.
- Native response handling now retains the public error outcome, displays its message and does not resend the command. A live control confirmed return to the commands tab with the failed outcome. Console checks passed15/15; a separate review found no issue in this delta.
- Full menu acceptance has not passed. The seven current scenarios assume the authored map's hero. Existing game-command transport did not complete a menu hero query in time even with the controller installed before launch. A separate menu workflow and supported map loading from it are still needed; map-check requirements were retained. Original unsuccessful controls and timings remain in local logs.

## 2026-10-06 — SDK core connection to the Universe menu

- A capture of the owned test-process window confirmed the actual Universe menu. Its class differs from the original game's class; the previous SDK main-window check excluded this menu.
- Window ownership, primary thread, absence of parent/owner and the window-instance module were verified. The core now recognizes both confirmed classes and refuses to choose among multiple eligible windows. Auxiliary and hidden windows remain rejected.
- The current core DLL connected to the menu and closed the game through its native command; client and game returned success. The complete control took 4.51 seconds. Native checks passed6/6 and console checks15/15.
- The control repaired only the known import ordering in the test process. No debugger, process-mitigation overrides or startup-script changes were used. This proves core menu dispatch, not reliable ordinary released-mod startup. Console-in-menu and transition-to-map still need live checks. Original logs and capture remain local; new changes are unpublished.

## 2026-10-06 — separate animation-library placement failure

- Rechecking the fixture revealed a limit in the earlier two-DLL result: the developer launcher repaired dependency ordering and the startup script in memory. It proves mod execution after that preparation, not ordinary released-package startup. The checker now creates an ordinary process without those patches; fresh live acceptance remains required.
- An ordinary test-start dump without SDK DLLs confirmed a different failure: Granny accessed its old data location while a Universe graphics library occupied that location. This is a separate observation; the cause of the earlier freed graphics-device access remains unknown.
- The existing animation preload did not establish reliable startup. With a monitor the process remained alive without a game window; a subsequent launch without a monitor failed in Granny. Successful startup and a fix are not confirmed.
- Original dumps and numeric bindings remain local. Test-game files were restored. The next check must establish actual dependency placement in a failing preload launch. [Microsoft PE documentation](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format) explains preferred versus actual image placement; the specific finding comes from the local dump.

## 2026-10-06 — first test-start graphics failure

- Two access-violation dumps were captured on fresh test profiles of the supported Universe build. The main game thread accessed freed Direct3D device data while checking available texture memory.
- The second control failed before loading SDK or console DLLs. Early console-device creation does not explain this run; the experimental map-response wait was removed.
- A comparable ordinary process-creation control also failed, with an unhandled breakpoint. A prepared SDK had previously passed on repeat startup; first-start reliability remains open. Device-release cause and the role of the launch method are not established.
- Dumps, stacks and numeric bindings remain in unpublished local logs. Heap policy, registry and ordinary player startup were not changed. These findings concern the test setup and do not establish a defect across all Heroes V builds.

## 2026-10-06 — suppressing camera mouse input

- Question: does the SDK mouse suppression cover wheel zoom? The supported Universe build is identified in [Game API](https://github.com/Xaaalera/heroes5-game-api/blob/main/include/h5/build.hpp).
- The base-camera constructor places `camera_zoom_mouse` in the mouse group. Its event handler skips that group when mouse input is suppressed; keyboard suppression gates another group.
- Original machine-code emulation passed four flag combinations. The external binding helper was stubbed: calls and branches were checked, not camera movement.
- Physical wheel input, delegation to another controller and full panel isolation remain unverified. Automated wheel input did not change zoom even with the panel hidden; that does not prove a fix.
- Original logs remain local. The updated [Game API explanation](https://github.com/Xaaalera/heroes5-game-api/blob/main/docs/mechanisms/game-bindings.md) is prepared but unpublished. Microsoft documents separate [wheel-message](https://learn.microsoft.com/en-us/windows/win32/inputdev/wm-mousewheel) and [DirectInput mouse-state](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ee416630(v=vs.85)) interfaces; the current game session's route is not established.

## 2026-10-05 — shared in-game diagnostics started

- The owner requested a common bus for all modules: connection state and debug/info/warning/error messages in the game console. The requirement is tracked in the active backlog.
- An SDK prototype keeps a bounded process-shared journal without DLL code pointers. Two simultaneously loaded DLLs published records that survived replacement and unloading while a buffer owner remained. Levels, UTF-8, bounds, overflow and pagination were checked; native tests: 6/6.
- New starter plugins report their project name on the first actual callback. Python: 102 passed. Console output and the automatic module lifecycle registry are not implemented yet.
- Nival documents Lua print as console output. No native ConsoleAppend contract was verified. Future live checks must distinguish output from command echo; Lua return does not prove visible console text. No game was launched for this stage.

## 2026-10-05 — operation journals and retention

- Main CLI commands record total time and outcome; nested builds link to their release. Journal write or close failures preserve the original command exception.
- Shared writes use concurrent-log-handler. Four independent processes produced 100 large JSON records without loss; parallel operation contexts were checked separately.
- Event journals rotate at approximately 10 MiB, keeping five gzip backups and deleting older event archives. `xkit diagnostics` lists archive paths. Reports, dumps and separate raw logs remain retained; no age-based cleanup is configured.
- Python: 102 passed, including real rotation and preservation of unrelated files. Installed CLI produced an H5U in 1.32 seconds and a native package in 10.34 seconds. No game was launched for this logging work; direct legacy backend commands still need the common policy.

## 2026-10-05 — complete current SDK check

- `xkit check --player` passed in 65.2 seconds from a separate workspace. Added plugin functions and headers, a core export, core replacement and rollback, independent removal and reattachment worked in the same game.
- Two packages built from the accepted sources loaded automatically. Stopping one preserved the other; callbacks were removed, both games exited with code 0 and staged files were restored.
- Earlier checks found a missing test map and an overly long MSVC temporary object filename. The check now prepares a missing map while preserving an existing one and uses a short temporary filename. Compilation errors fail immediately instead of waiting for plugin application.
- The HMR-ready message now waits for the selected plugin to be applied. Python: 95 passed; the message change was checked without the game. Map transitions, scene rendering in this run and published-source availability remain outside this check.

## 2026-10-05 — canonical early dependency integration

- Each native archive contains one plugin DLL plus shared `dinput8.dll` and `wsock32.dll`. The latter loads animation before the graphics wrapper and preserves all 75 socket export names/ordinals. Test fixtures are excluded.
- Two independently released packages auto-loaded during ordinary startup and displayed 42/84. Stopping the first left the second active at 84. Shared hashes match and complete frames are retained.
- Game and monitor ultimately exited with code 0, without dumps. The native exit deadline elapsed; a retained handle confirmed termination after WM_CLOSE. That limit remains explicit in the report.
- Test deployment now writes a temporary file and atomically replaces the destination; restoration preserves external modifications. Python 92, native 5/5 and three GUI exit-race cases passed. Bounded review's restoration and partial-write findings were separately corrected and verified.

## 2026-10-05 — successful early-loading experiment

- Loader tracing identified why the first prototype failed: the audio DLL dynamically requested a socket export by ordinal. Direct executable imports did not cover that request.
- The prototype now preserves all 75 system socket export names and ordinals. Four native implementations delegate to the actual system DLL; the others use standard export forwarding. [Windows mechanism](https://learn.microsoft.com/en-us/cpp/build/reference/exports).
- Ordinary CreateProcess with the released plugin and prototype reached a rendered menu. Value 42 is visible in the full frame, and animation-image placement passed an owned post-initialization check. This run did not rewrite game imports or model descriptors.
- Game and monitor exited with code 0, without dumps. Staged DLLs were hash-checked and removed. This is one successful monitored experiment; canonical integration and a final explanation of the earlier breakpoint remain open.

## 2026-10-05 — stale reference provenance during ordinary startup

- An ordinary-start monitor captured an animation-library fault after released-DLL auto-loading. A full dump includes the loaded model's type-description table, which the earlier mini-dump omitted.
- The stale nested reference belongs to `IndicesMapFromTriToAnnotation`, part of the model's geometry description. Checked mapped-library tables and `GrannyInt32Type` relocate correctly. The call path reads file information and converts a legacy model format. The writer remains unidentified; an independent bounded analysis confirmed this limit.
- A private early-dependency prototype passed local UDP forwarding. The game then rejected DLL initialization with that prototype. It is not included in the SDK or released packages.
- The earlier executable breakpoint remains a separate observation; this dump does not establish its cause. Temporary DLLs were restored or removed after hash checks.

## 2026-10-05 — managed shutdown after visual HMR

- `xkit start` changed 42 → 43 → 42 in one process. The complete menu frame contains the updated value and an independently installed H5U marker. Ctrl+C closed the game with code 0 and no session failures.
- Change detection to successful invocation took 1.816 seconds. Restoring the earlier source reused compiled objects and took 0.243 seconds. These are not full startup durations or measured pixel-update latency.
- Switching SDK locations exposed CMake's source-bound cache. The fix selects a separate cache for another source location and preserves the prior files. Real startup and regression passed; Python 89 and native 4/4 passed, with no findings in the bounded cache review.
- The earlier ordinary released-DLL startup exception outside the SDK remains separately unresolved.

## 2026-10-05 — complete released DLL and H5U frames

- A later menu control resolves the earlier capture limitation: the full window contains the rendered scene and value 42 from an independently released DLL. Windows Graphics Capture independently obtained a populated frame. The owned window was on-screen, responsive and not minimized; isolated child capture remains unsuitable for this scene.
- A separate H5U-only session visibly shows the complete `[XalKit: solo-resource]` marker. The installed package matches the released hash and no native plugin was installed. Managed `xkit start` exited normally with game code 0.
- The DLL session terminated after the private test's exit deadline. Its kernel handle was not retained, so the exit code is unknown. Visual delivery is verified; successful shutdown for that session is not claimed.
- These frames use SDK test startup. The earlier breakpoint during ordinary released-DLL startup remains a separate unresolved case.

## 2026-10-05 — released DLL and visual acceptance limits

- An independently released plugin auto-loaded through the shared bootstrap in a placement-guarded game. No watcher was running; an addressed window event changed its UI caption to 42. Native shutdown returned 0 and staged files were hash-checked and removed.
- PrintWindow rejected the child capture. WM_PRINT completed but produced a black image without recognized text. A window caption is not rendered-effect evidence; visual acceptance remains open.
- Ordinary package startup ended with a breakpoint exception in the game executable before the plugin control appeared. Its system report is retained and its cause remains unknown.
- A control without the installed bootstrap/plugin survived 25 seconds. After a diagnostic core was loaded to request shutdown, it faulted in the animation library. The dump shows a relocated image accessed through its former location. This is a separate failure, not a dump of the uninstrumented game before diagnostic loading.

## 2026-10-05 — independent SDK installation

- A frozen current-source export was installed into a fresh Python environment. Its Game API dependency was complete, with no Git metadata or workshop junctions. The export is an acceptance fixture, not another editable SDK.
- From a separate project directory, help, setup, doctor, new, build, release and diagnostics passed. It produced an independent resource H5U and a ZIP containing one named plugin DLL plus the shared loader. Archive integrity passed and all 111 source hashes remained unchanged.
- This verifies local candidate installation. Public-clone availability and visible in-game mod effects were not covered.

## 2026-10-05 — SDK startup image check

- Native `xkit start` checks the animation DLL at its loader event before initialization and records successful validation in the session report.
- The initial guarded live plugin changed 42 → 43 → 42 in one game. After strengthening identity handoff, a repeat connected the plugin and exited normally; game and monitor returned 0.
- Cancelling before resume terminates only the created test child. Native 4/4 and Python 88 checks passed; bounded review closed the handoff and cancellation defects it found.
- A retained loader thread proved successful completion after 18.1 seconds. The previous 10-second wait was insufficient; the underlying delay remains unexplained. Only the loading budget increased; uncertainty never authorizes replay.
- This verifies native SDK startup. Visible released-mod effects, ordinary startup outside the SDK and resource H5U remain separate acceptance scopes. [Developer workflow](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/docs/commands.md).

## 2026-10-05 — ordinary startup and failed clean control {#sdk-ordinary-capture}

Startup without SDK diagnostic patches also produced a blank window capture. The local DLL bootstrap and crash monitor remained in this control; the process closed normally. Window readiness does not prove a fully loaded map.

A separate launch without either component failed in granny2.dll, confirmed by the Windows event for the owned process. It is not successful visual acceptance and does not establish the cause of earlier blank frames. Bootstrap hashes were restored; no identical crash retry was performed. Original reports/events remain private. Startup cause and visual H5U acceptance remain open.

## 2026-10-05 — active-window capture and further exclusions {#sdk-capture-dc}

Copying the active owned game's window DC also produced a blank frame. Two further launches separately restored the background-update default and excluded legacy DLL mods from automatic loading. The map answered commands, captures remained blank and games closed normally. Profile bytes and DLL hashes were restored. Focus and cursor were untouched.

These factors alone do not explain the observed result. Diagnostic startup changes remained enabled; an ordinary launch without them is still untested. The cause and visual acceptance of the finished H5U remain open. Frames and reports are retained in the workshop's private journal.

## 2026-10-05 — negative SDK scene-capture control {#sdk-capture-order}

In two owned test launches, the map answered a hero-list request while its window capture showed no scene. The first called Windows Graphics Capture before the first PrintWindow and again afterwards, without a diagnostic HUD. Both frames stayed blank. The second changed only the test profile's fullscreen setting; the result was unchanged and the original file was restored byte-for-byte.

These observations do not support HUD, PrintWindow order or that window-mode setting as a sufficient explanation. They do not establish the physical display's image. Visual H5U acceptance remains open. Both games closed normally; shared cursor and focus were untouched. Original frames and reports remain in the workshop's private journal. This is local research, not a published release verification.

## 2026-10-04 — editorial clarification of native mechanisms {#native-names-editorial}

The [native UI](../modding/native-ui.md), [placement internals](placement-internals.md), [creature definitions](creatures.md), [build reference](universe-build.md) and earlier diary entries now describe native operations by their verified roles. Existing SDK symbols, including BankLayout and ScriptDispatchCall, link to their source; descriptive roles elsewhere are not claims of recovered original function names. Lookup tables now explain behavior and evidence rather than listing numeric pointers or structure offsets.

This is an editorial change, not a new game experiment or algorithm correction. Original documents were preserved privately; experiment dates, build hashes, formulas, observed results and unresolved semantics are retained. Earlier observations remain subject to their dated corrections and evidence limits. Predictor work remains paused.

## 2026-10-04 — multiple plugins and shared library

The supervisor adds plugins without restart, routes commands by ID and stops removed plugins. Live control175242: state10/20→22 stays independent; new cpp returns77, a header changes it to88, deletion restores42. Alpha compile failure does not stop Beta; conflicting CALL ownership is rejected without damaging its owner. Removing Alpha restores the CALL, re-add starts fresh state, Beta retains22. Two same-source release packages load together. PID23568/50924 close normally; full cycle53.541s, second-plugin add4.678s, removal0.547s.

Earlier172417 text readback passed while screenshots lacked UI. Shared WS_CLIPCHILDREN ownership fixes overdraw;173124 visibly shows both controls,175242 additionally checks diagnostic-control pixels. Readback alone is not rendered acceptance.

[Game API](https://github.com/Xaaalera/heroes5-game-api) published at93ca6e7: C++ fingerprint/hash guards, five known hook sites from both mods/SDK, owned PID/creation/path checks. Consumers share one canonical library. Five independent lenses passed10/10 after test/doc fixes; native1/review9/docs/secrets/pre-push and GitHub CI37216059445 PASS. Native consumers compile; bank1/SDK51+4 PASS. Predictor algorithm work remains paused; historical accuracy is not transferred to a new hash.

## 2026-10-04 — SDK ABI3 prototype final acceptance

Reproducible plugin-check.py --live passes the current code's complete cycle: automatic compilation/reload of functions, window event/UI and real engine CALL observer; state persists, wrong hooks/rejected probes roll back, compiler errors retain the working version. Disable restores original CALL bytes and removes UI. The same source produces a package that starts through the ordinary DLL bootstrap and executes its engine callback without watcher/client.

Final sdk-acceptance-20261004T170427/report.json and audit.json: PID49896/36064, both close normally after confirmed map readiness; sandbox restored. Save→UI2.101s, complete cycle38.385s. Current core-source/DLL/package hashes match; live and release source hashes are identical. map-49896.png visually confirms UI3001 over the adventure map.

Python51/51 and native4/4 PASS. Machine tests compare GPR/ESP/flags, stack argument and x87/SSE for direct original call versus thunk; DF is cleared before C++ and restored before the original function. Map readiness and scaled OCR resolve the observed close issue; earlier failed records remain retained.

This completes prototype acceptance, not arbitrary interception of any function: one main-thread E8 CALL observer and window event are supported; arbitrary prologues, multithread patching, schema migration, native crash containment and a complete UI toolkit remain extensions. Native mods use DLL/bootstrap; H5U supports resources/scripts referenced by the relevant game context. Code remains local and unpublished.

## 2026-10-04 — real engine CALL hook and concurrent replacement

ABI3 declares one x86 CALL site with its expected original target. In PID52212, the handler at [ScriptDispatchCall](https://github.com/Xaaalera/heroes5-game-api/blob/main/include/h5/hooks.hpp), the engine script-dispatch call, changes from version 3 to 4. A wrong hook site is rejected with rollback; disable restores the original 5 bytes and state survives. A native test separately proves reload waits for an active old call. Arbitrary prologues and cross-thread installation are unsupported; register preservation still needs a dedicated machine-level test.

The complete live run is marked failed: OCR misses OK during close. The screenshot confirms the dialog and a background click closes that same PID. A retained image shows2x OCR recognizes OK; the fix is added. The next close control ran too early during startup-window replacement, then remained at a splash; normal recovery failed, so only verified owned PID46704 was terminated. Both failures are retained; successful close acceptance still requires confirmed map readiness.

## 2026-10-04 — automatic UI reload and same-source release

PID52020 verifies window callback registration/removal and UI2007→2010; sdk-event-ui-first-live.png shows the control over the map. PID49128 passes automatic source edits: UI2001→4002 in2.162s, rejected probe rolls the DLL back, compiler error retains working code, subsequent events4003/4004 preserve state. Returning to a version without events removes UI; both games close normally. This is a Windows child control and custom window message, not an arbitrary engine hook or XDB UI.

The same payload source builds with the permanent bridge into one DLL. Its ZIP contains that DLL, shared dinput8 and hashes. PID19292 ordinary startup without watcher/client produces UI0→2001; complete cycle6.689s, normal close, sandbox restored. Artifacts sdk-auto-event-ui-live.json, sdk-release-build.json, sdk-release-first-live.json.

Two-cpp incremental builds compile2→1→0→2→1 units: initial, one cpp edit, cache, header, release bridge. The tiny helper edit takes0.153s; not a large-mod estimate. Python51/51/native3/3 PASS. Prototype unpublished; engine detours and concurrent-update verification remain open.

## 2026-10-04 — replaceable plugin calls on the game's window thread

A persistent SDK bridge thread installs WH_CALLWNDPROC on the owned game window thread. PID48772 passes48 commands: thread ID independently matches process windows, new function42 is available, counter7 survives10 DLL switches and5 schema rejections. Whole cycle6.125s, hook/installer stop and game closes normally; bridge image stays until game exit. Artifact sdk-main-thread-first-live.json.

First control PID52168 loses its hook after the temporary installer thread exits: the first call passes, the next returns102. Failure retained and fixed with a persistent installer; both games close normally. This proves window-thread dispatch; gameplay UI, arbitrary engine hooks/API and automatic save→main-call remain unverified. [Windows thread hook documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowshookexw).

## 2026-10-04 — automatic native reload after source save

The SDK watcher detects a C++ edit, builds a generation DLL and applies it through a persistent bridge in owned visible game PID3320. The sequence1→2→compile error→1 passes without restart; save→confirmed call2.126s, complete launch/check/normal close9.286s. One stateless-function sample; game hooks/UI and live state are unverified. The first attempt lacked keystone in system Python before launch completion; the dependency-checked venv passed and no game remains.

Separate local integration verifies a new function, retained counter7, schema rejection and recovery after compiler error. Watcher boundary tests4/4, native CTest3/3 PASS. Artifacts sdk-watch-local-integration.json, sdk-auto-watch-local.json, sdk-auto-watch-first-live.json. Sources remain local uncommitted devkit changes; the universal development environment is incomplete.

## 2026-10-04 — SDK plugin lifecycle prototype

The canonical devkit adds native/plugin_runtime.hpp: C ABI, persistent host-owned state, serialized calls and DLL switching. Game-free checks preserve state through20 switches, observe changed/new functions, reject incompatible ABI/schema and roll back state on a rejected call. MSVC x86 Release and CTest3/3 PASS, no skips. Watcher, game hooks/UI, schema migration and packaging remain open; native crashes and external game effects are outside rollback.

A separate tiny-DLL benchmark reuses one MSVC environment: setup1.452s, five builds0.375–0.565s, all exit0. This is not full-mod or live-reload latency. [SDK source and limitations](https://github.com/Xaaalera/heroes5-mod-devkit): local uncommitted changes; the public link does not establish publication.

## 2026-10-04 — first live native HMR experiment

In one owned game process a research DLL first returns1. Its code is changed and rebuilt while the game runs; the new DLL returns2 and an added function42. PID remains unchanged, both research DLLs unload after completed calls, and the game closes normally. Edit→new call2.946s,build2.890s; one measurement, not a general mod speedup.

The DLLs have no hooks or transferable state. Existing game mods retain detours/callbacks and lack a detach API; this experiment does not establish their reload. Write-opening the loaded file yields sharing violation, supporting separate generation filenames. Next: persistent bridge, versioned ABI, state transfer and old-call quiescence. [Windows FreeLibrary](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary), [DllMain constraints](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-best-practices). Local evidence sdk-native-hmr-first-live.json; predictor remains paused.

## 2026-10-04 — RMG and refined source category

DLL3199 passes five fresh loads: three fullPolygon profiles108/108, RMG-A24/24 andRMG-B19/19,total151/151. Full composition/quantities/cells, both actual snapshots, frozenSHA/time and game closures are independently checked.

Follow-up tracing establishes a boundary: source category reads declared shots from the definition, while actor physical state may differ. A failing regression is added, then the predicate corrected. Current DLLcc368 passes60/60 native gates and retains3/3 on the original counterexample; games close and resources are restored. The151 result is not transferred to this new build. Local evidence new-dll-rmg43-verification.json and definition-category-counterexample-verification.json. Next: fresh broad matrix and remaining branches.

## 2026-10-04 — defensive counterexample fixed

The0/3 cause was category membership: the engine includes a Cyclops with an available Goblin among shooters, although its separate physical state did not confirm a shot. The predictor placed it among large stacks and counted one shooter. Defensive category and window size are corrected; ordinary large-pass precedence remains. Cyclops first takes13,2, Archer then13,8, Goblin13,3.

New DLL3199e570 matches the retained counterexample3/3 completely.60/60 native tests and fresh fullPolygon36/36 (mixed30/30) pass, games close and temporary resources are restored. FrozenSHA/time/both observations/new build hashes are independently checked. Old108/273 results are not transferred to the new DLL. Local evidence protected-linked-fix-verification.json and shooter-category-new-dll-full36-verification.json. The full goal remains open.

## 2026-10-04 — defensive placement counterexample

An authored Goblin/Cyclops/Archer army on selective obstacles yields **0/3 exact creature+quantity+cell tuples**. Composition and quantities are correct;1/3 occupied-cell overlap is not tuple accuracy. The game closes, map/manifest are restored and temporary obstacles removed. The negative forecast and both observations are retained.

New protected/linked phase snapshots show the engine places all three stacks inside protection before the general pass. Investigate protective candidate order and carrier placement. Separately, original dispatcher execution confirms a mandatory general pass after protection; C++ omits that stage, but it does not explain this negative. DLL31cc03e0 unchanged. Local evidence protected-linked-confirmed-miss.json; next step is a reproducible correction and new-DLL control.

## 2026-10-04 — live equality under threshold calibration

In three owned loads an army containing only large stacks has invariant ratio1. Three neighbouring float thresholds around1 are temporarily applied; the actual engine flag istrue/false/false for thresholdbelow/equal/above the ratio. The comparison is strict: equality does not enable the rule. The observer records the native flag at calculation time.

All three complete forecasts frozen before Start match7/7; the threshold is restored before game exit. This is calibration, not stock0.55 equality or replay of one RNG state. Game/map/DLL files unchanged; the observer addition changes the tool hash. Local evidence large-threshold-calibrated-triple-verification.json. Natural equality and remaining branches still need verification.

## 2026-10-04 — initial placement-score boundary

The initial baseline passes two zeros to the caster calculation.776 comparisons of original scorer with C++ now check these arguments;1/1 PASS5.835s. A separate spell-damage path calls the caster directly only for Snipe Dead. Other descriptors use actor methods; their indirect paths are not excluded.

Three corresponding loaded-code ranges match the EXE. Both Brem descriptors in the control are non-damaging, score24; the complete forecast frozen before Start matches7/7 and the game closes. This narrows the previously tested arithmetic boundary, not global reachability of other actions. DLL31cc03e0 unchanged. Local evidence initial-area-reachability-verification.json. Next: threshold equality and remaining placement dispatcher transitions.

## 2026-10-04 — nonzero hero action codes

1536 synthetic cases execute the original hero dispatcher and Universe patch. Five known actions use different level bonuses; Holy Charge additionally clamps the Jousting coefficient, applies the original-level multiplier and triples the result with Absolute Charge. The specialization predicate uses original equality against one stored code, not several simultaneous specializations.

The test1/1 PASS3.293s retains earlier checks. Coefficient values are synthetic; the loaded value and enabled actions in a live game remain unverified. First establish which paths are reachable during the initial placement score. DLL31cc03e0 unchanged, no game launch. [Reproducible oracle](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py); local timing journal retained.

## 2026-10-04 — complete specialization series

Jazaz and level7 Hero1 each pass36 complete packs:72/72,mixed60/60,solo12/12. All pre-Start hero scores are28 and70 respectively. Composition, quantities, cells, frozenSHA/time and both after-Start checks are independently verified. Games close and original map/manifest are restored. Total measurement333.748s; phase timers overlap it. With the earlier Calid series three current profiles give108/108, but the complete algorithm is not accepted.

The mastery patch is a separate War Machines bonus from Ring of Machine Affinity. Artifact91 is not Critical Strike skill91: these are distinct enums.192 synthetic cases execute original artifact search, patch and final0…4 range;1/1 PASS3.849s. Real equipment state and the meaning of the flag that makes the artifact scanner skip an entry remain unverified. Local evidence jazaz-full36-verification.json and hero1-offender-full36-verification.json; DLL31cc03e0 unchanged. Other branches and the final matrix remain open.

## 2026-10-04 — positive controls for two specializations

Temporary authored Jazaz confirms actual specialization17 and a pre-Start score28 at level1: base24 plus4. Hero1 with starting experience9000 loads at level7, confirms code74 and score70: base58 plus the3%-per-level bonus with native rounding. Each complete seven-stack forecast matches7/7 and games close; composition/quantities/cells/frozenSHA/time are independently checked.

The entire291-byte Universe patch stage and its constants/transfers match the pinned DLL after relocation. This closes the previous256-byte capture limitation for this range. Map and manifest are restored byte-for-byte after each experiment; original game binaries unchanged. Level7 is added to the oracle:1/1 PASS2.941s,640 Universe cases and retained EXE checks. Local evidence hero-specialization-positive-verification.json; DLL31cc03e0 unchanged. Full specialization matrices and other branches remain open.

## 2026-10-04 — complete polygon with Critical Strike

Calid with verified Critical Strike passes all36 authored armies: complete matches36/36, mixed30/30,solo6/6. All72 pre-Start hero-score rows contain36; composition, quantities and cells are checked against both after-Start snapshots, with frozenSHA/time verification. The game closes normally. Total launch measurement180.283s includes completion-observation latency. This is one polygon load, not complete-algorithm acceptance.

A subsequent Hero1 control identifies the actual owner asCHero. The specialization predicate compares one stored enum with the requested enum; its live bytes match the EXE and25 oracle cases pass. Another Universe patch in skill reading contains an extra skill2 branch; its meaning remains open. DLL31cc03e0 unchanged. Local evidence calid-critical-full36-verification.json and hero-owner-specialization-live.json. Next: positive specializations and remaining branches.

## 2026-10-04 — repeatable hero and skill control

The test driver accepts an existing hero and ordered skill grants for one Polygon/Superadmin load. Ownership, each grant's acceptance, queues and increasing mastery are checked; steps are retained in JSON. Ordinary-mode policy is unchanged. Four invalid configurations were rejected before launch.

The normal Calid6/6/6/60/91 command, without an in-memory function change, freezes baseline36 at10/4 and an exact complete7/7 forecast; the game closes. FrozenSHA/time/both snapshots/current driver hash are independently checked. DLL31cc03e0 unchanged; the earlier273 series stays tied to its older driver. Local evidence calid-critical-cli-verification.json. Next: the complete polygon with the skill and specialization controls.

Availability clarification, October 8,2026: the former reproduction link did not provide that public README section. Local evidence remains unpublished; this entry does not supply a complete reproduction procedure. Original observations and verification limits are retained.

## 2026-10-04 — positive Critical Strike control

Skill granting requires a valid hero and dependencies. On the existing Inferno hero Calid, ordinary commands granted Attack through3, Demonic Strike and Critical Strike in sequence; each command's acceptance and mastery were verified. HasHeroSkill confirmed Critical Strike enabled.

Before Start the level1 hero score is36 at horizons10/4, agreeing with base24 plus the50% Universe bonus. There is no paired pre-grant measurement of this same hero. The complete seven-stack forecast matches7/7 and the game closes; frozenSHA/time/both actual snapshots are independently verified. Hero selection used a temporary research function change in memory, explicitly recorded; map/tool/DLL files unchanged. Local evidence calid-critical-strike-live.json and calid-critical-strike-verification.json. Next: persistent authored hero/skill control parameters and specialization tests.

## 2026-10-04 — binding predicates to the hero owner

Actual hero predicate addresses were captured before Start. The skill predicate calls owner method174 and returns true only for a positive signed result; the second predicate forwards to owner method190. These original forwarders now execute in the oracle; five skill-result boundaries are added,1/1 PASS2.901s. The second owner's deeper implementation remains unverified.

The Critical Strike grant attempt did not produce a positive control: the command is exposed but HasHeroSkill stayed0→0. The experiment stopped before Start; an earlier boolean RPC error is also retained. A separate baseline-only control then preserved the exact7/7 forecast, baseline24 and normal game exit. This does not verify an enabled bonus. Local evidence hero-critical-strike-live.json and hero-baseline-live-methods.json; DLL31cc03e0 unchanged. Next: grant conditions or a suitable authored hero and a positive control.

## 2026-10-04 — testing the replacement Universe stage

576 synthetic target and null-target calls match while executing the original uni.dll stage. It accumulates a float bonus from three predicates: half the score, level×coefficient×score, and level×4. The total is then converted to an integer and clamped to at least1. Original rounding order and HP reads remain intact.

The first256 bytes of previously captured live code exactly match the pinned uni.dll after PE relocation. This does not verify all runtime data or the remaining tail. Real skill-predicate semantics remain open. The existing test1/1 PASS2.871s retains earlier EXE checks; the first new-test failure came from stale emulator instructions, fixed by explicit cache invalidation after patching. DLL31cc03e0 unchanged, no new game launch. Local evidence hero-baseline-universe-verification.json; [reproducible test](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py).

## 2026-10-04 — live correction: record format and Universe patch

The earlier12-byte record inference is corrected: seven live stacks have a current16-byte record. The getter reads end−8. For undamaged stacks its value agrees with HP of one creature: multiplying by independently observed quantity gives stack HP in all7 cases. Damaged behavior remains unverified. The first array-validation failure is retained; the retry forecast frozen before Start matches7/7 and the game closes normally.

Loaded-byte comparison finds a JMP atbc1d09 to uni.dll RVA37d10. Therefore earlier180/864 complete caller comparisons prove stock EXE arithmetic, not the replacement Universe stage. The new code accumulates bonuses through three predicates; its rounding and semantics still need an oracle. Other checked helper/scalar/getter ranges match the EXE. The record fixture is corrected,1/1 PASS2.689s; DLL31cc03e0 unchanged. Local evidence: target-floor-live-verification.json and hero-baseline-live-patch.json; next step is testing the Universe patch.

## 2026-10-04 — source of the score floor

Target getter1d4 returns the second word of the last12-byte record in an internal list. An empty list uses a zero sentinel. The word's meaning remains unproven; the quantity observer uses a different getter1d8.

The existing [native test](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py) replaces the1d4 stub with original instructions.864 target cases and5 list boundaries pass;1296 interpolation cases and180 null-target calls remain covered:1/1 PASS2.517s. This is PE/emulator evidence, not live lists. DLL31cc03e0/sourcef8e9ba97 unchanged; the next control must compare the list with independently observed quantities and HP in an owned game.

## 2026-10-04 — hero score with a target

864 synthetic complete target-call cases match original instructions. The table index comes from one of two target interfaces or defaults to3; the original getter calculates remaining HP of one creature. When additional checks qualify, after the specialization bonus the result becomes the maximum of twice the score and target getter1d4; the original-level multiplier follows.

Both sides of the getter1d4 comparison are covered. Its meaning and skill-predicate semantics remain unproven; call modes other than0 are not covered. External characteristics are substituted; these are not864 live battles. The existing [native test](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py) also retains1296 interpolation cases and180 null-target calls:1/1 PASS2.404s. DLL31cc03e0/sourcef8e9ba97 unchanged, no game launch; local timings saved.

## 2026-10-04 — bonus order in the initial hero score

The complete null-target calculation matches original game instructions in180 combinations. A bonus first adds3 to the interpolation level; two specialization codes then add half the integer result; the final multiplier uses the original hero level. Native rounding, minimum1 and FPU restoration are preserved.

The existing test now checks180 complete calls and1296 interpolation cases:1/1 PASS in2.152s. Previously captured exact tables are reused; external hero characteristics are substituted. Flag combinations are synthetic arithmetic coverage, not bonuses available together to one hero. Virtual predicate semantics, loaded-code equivalence and the target-present call remain open. DLL31cc03e0/sourcef8e9ba97 unchanged; no new game launch. Reproduction: [native test](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py), `test_hero_baseline_interpolation_matches_original_tier_level_and_scalar_boundaries`; local timing journal retained.

## 2026-10-04 — target scalar meaning in the hero score

The target scalar is tied to HP of one creature, not stack quantity. The getter obtains maximumHP, accounts for fractional damage, adds0.5 before integer conversion and clamps to at least1. Original x87 rounding order is preserved.63 original-instruction comparisons with a supplied max-HP value pass; fraction boundaries are synthetic, not63 observed battles.

Seven real objects in an owned game confirm the interface chain and maximum-HP getter address. These reads occur after Start for research only. The forecast frozen before Start independently matches pack15 exactly7/7 and the game closes. Local evidence accuracy-campaign-20261004T090443Z-50576-polygon-admin.json, PID32688, target-scalar-live-chain.json. DLL31cc03e0/sourcef8e9ba97 unchanged. Maximum-HP modifiers and the full hero caller still need verification.

## 2026-10-04 — hero melee tables in the live game

Exact float32 words of two hero-score tables were read before Start in an owned game. Values match stock HeroDamageLevel1/HeroDamageLevel30 in DefaultStats.xdb; matching content does not prove archive precedence. Hero baseline24 agrees with row3 at level1 and scalar30. Pack15 forecast matches completely7/7 and the game closes.

Oracle coverage expands to synthetic and loaded tables:1296 original-instruction comparisons pass with FPU control word/reference restoration. Local report accuracy-campaign-20261004T084718Z-41500-polygon-admin.json, PID48664, supplement hero-baseline-live-settings.json. DLL31cc03e0/sourcef8e9ba97 unchanged. Complete hero modifiers and target scalar meaning still need verification.

## 2026-10-04 — hero initial-score arithmetic

The original hero-baseline interpolation helper clamps the index of two tables to1…8 and linearly changes their value with level using float32 coefficient0.033333335. Level31 is the upper table reference; rounding can differ from that endpoint. Levels above31 continue without a clamp. The result is multiplied by the target scalar and converted to an integer with the original x87 operation/rounding order.

648 original-instruction comparisons against independent arithmetic pass with synthetic tables and the x87 control word set to 24-bit precision and rounding toward zero; resource references and control word are restored. Only external resource getters are substituted, not arithmetic. Persistent test_hero_baseline_interpolation_matches_original_tier_level_and_scalar_boundaries passes1/1. This verifies a helper formula; loaded tables, scalar meaning and complete hero modifiers remain unconfirmed. DLL31cc03e0/sourcef8e9ba97 unchanged.

## 2026-10-04 — full cycle drops from80.18 to26.33min

The full273-battle campaign on the same DLL31cc03e0/sourcef8e9ba97 with optimized tools takes1579.579s instead of4810.981s. These two complete runs save3231.402s,53.86min, with a3.0457x time ratio. They cover the same selected scope and DLL, but use separate RNG/loads without statistically isolating each change.

Accuracy remains273/273 complete forecasts frozen before Start, mixed213/213,solo60/60. All ten games close normally and the current-hash strict verifier passes. Local report accuracy-campaign-20261004T075852Z-41916-rotation-admin.json, SHA `ba4f72a40076c9ba89f7990044f5fc878881e2fc7fd9c78b5c87efc0d685bf6f`; separate strict-verification record. Old CLI exit1 is an unconditional Superadmin terminal error, not a real mismatch. Algorithm edge cases and native DLL HMR remain unfinished.

## 2026-10-04 — complete short-cycle comparison

The same three selected packs pass in two fresh loads:25.334s with separate CLI processes and21.285s with the reused client. Both reports give3/3 complete pre-/post-Start matches and normal game closure. This is one pair with different RNG and startup times; whole long-campaign speedup is not established.

Local reports accuracy-campaign-20261004T074547Z-46036-polygon-admin.json and accuracy-campaign-20261004T074613Z-46036-polygon-admin.json. Final client error-boundary regression passes. The current speed phase is complete; algorithm work resumes, while native DLL HMR is a separate research TODO.

## 2026-10-04 — command client in one process

The harness reuses the existing canonical SDK dispatcher without starting Python for every command. PID, process creation, signatures and readiness are still validated on each call. Game handles are not retained between loads; CLI and serve remain available. Full SDK46/46 and three consecutive live forecasts3/3 pass, with normal game closure.

Identical day reads on one map give median0.165s through CLI and0.068s in-process. This speeds up that query, not the whole campaign. Local report accuracy-campaign-20261004T073153Z-42336-polygon-admin.json, PID5124, DLL31cc03e0/sourcef8e9ba97;22.820s complete cycle includes10 comparison queries. Tool hashes changed; older reports keep their original version scope.

## 2026-10-04 — completed-battle cache and combined army reads

The harness serializes completed battle records once, after final comparison. Later saves stream those cached records while updating the active battle and headers. Full JSON stays compatible; atomic replacement and lock handling remain. On identical273-battle data repeated save drops from0.7618 to0.0244s, with complete parsed equality. Initial cache population takes0.9912s separately.

Day and army counts are read in one query. Injected10→7→10 restoration passes with an exact7/7 forecast (accuracy-campaign-20261004T065752Z-41424-polygon-admin.json). Three consecutive battles with the new persistence match3/3 and preserve all prior evidence (accuracy-campaign-20261004T070426Z-42936-polygon-admin.json). Games closed. DLL31cc03e0 unchanged, driver7f5471b5 new. These measurements do not establish whole long-campaign speedup.

## 2026-10-04 — complete reduced forecast without deadline waiting

The harness immediately accepts a complete plan with fewer models when model count matches validated planned_models and the unplaced-record mask. Incomplete forecasts still wait; ordinary mode stays strict. The regression passes and two live controls preserve an exact BlackDragon10 forecast at[13,2] before Start and confirm1/1 afterward. Maps are restored and games closed.

On one window the new helper takes2.896s including initial readiness, then the old helper10.125s on the already-ready window; forecasts match. Paired report accuracy-campaign-20261004T062443Z-46832-polygon-admin.json, PID47616; separate production control accuracy-campaign-20261004T062130Z-41328-polygon-admin.json, PID44840. DLL31cc03e0/sourcef8e9ba97 unchanged, helper3221→9dc6. This optimization phase is finished; algorithm edge cases remain next.

## 2026-10-04 — faster saves and ranged-hero verification

New reports use compact JSON with the existing atomic replacement and lock handling. Saving the same full273-battle report drops from5.527 to0.699s and218.9 to56.3MB; all parsed data matches. This measures one save, not the entire campaign. The old report and its driver are retained by hash.

Current DLL31cc03e0/sourcef8e9ba97 passes fullPolygon with100 Archers in the hero army:36/36 complete matches, mixed30/30,solo6/6. Report accuracy-campaign-20261004T060800Z-42664-polygon-admin.json, PID20704, SHA `e929219016f6f86dd3a51beb0814a5ad2c1ade89753b28968d1d750058cf1ebb`,240.918s. Exact tuples, freeze before Start and normal closure are independently checked; new driverd603 differs from previous9f5, while the DLL remains unchanged.

## 2026-10-04 — ten loads of the current DLL:273/273

Current DLL31cc03e0/sourcef8e9ba97 passes ten fresh Polygon and both RMG loads:273/273 exact whole-pack forecasts, mixed213/213,solo60/60. Creature types, quantities and cells, prediction freeze before Start, build/map/tool hashes and normal closure of all ten games were checked. The independent strict verifier passes. This proves the tested sample, not reconstruction of every algorithm branch.

Local evidence: accuracy-campaign-20261004T044050Z-51896-rotation-admin.json, SHA `caf4165889599d115d76ed44f7e42b8cf94288e5854901efc83d36e76d7e8879`; separate strict-verification JSON records scope and goal_complete=false. Runtime4810.981s (~80.18min). The old driver returns exit1 due to an unconditional Superadmin rejection; it is not a forecast mismatch, and the original report stays unchanged. Exact threshold equality and remaining open cases need separate controls.

## 2026-10-04 — six arenas on the current DLL

The80-Peasant,35-Footman,12-Priest army matches completely on Grass_Big_01,Dirt_Small_01,Sand_Big_01,Snow_01,Lava_Small_01 andRiver_Grass_Big_01:6/6 battles,18/18 units. Cells differ across arenas; every forecast is frozen before Start and original scripted types/quantities are separately verified. Projection models release and six games close normally directly after the Start snapshot.

Local report arena-placement-20261004T043701Z-admin.json, DLL31cc03e0/sourcef8e9ba97, SHA `7a0abe47f62502f680389e8b030cd3af06bbd04015398aa5cf37bd4d1bc9f6b9`. Per-case elapsed total61.910s. This placement-only control does not verify results, level dialogs or hero return; it does not replace the ten-load protocol or remaining algorithm branches.

## 2026-10-04 — current DLL on RMG-B

All19 selected WorkshopRmgTaggedB packs match completely: mixed13/13,solo6/6. Required packs were independently derived from map XML; creature types, quantities, cells, hashes and prediction freeze before Start were checked. Vegeyr returned after battles and the game closed normally.

Local report: accuracy-campaign-20261004T043014Z-49124-rmg_b-admin.json, PID37808, DLL31cc03e0/sourcef8e9ba97,184.882s. SHA256: `64c7c119c5f75e79e8ea02a3257573e5f8b2c84a9de2d0f41d5f1aaa48934ce9`. Current Polygon/RMG-A/RMG-B have three separately verified loads; the ten-load protocol and full algorithm remain unfinished.

## 2026-10-04 — current DLL on RMG-A

All24 selected packs on WorkshopRmgTaggedA match completely: mixed18/18,solo6/6. Required packs were independently derived from map XML; creature types, quantities, cells, hashes and prediction freeze before Start were checked. Hero9 returned after battles and the game closed normally. Cases rmg_a_071/133 pass; the historical hero-loss cause remains unknown.

Local report: accuracy-campaign-20261004T042413Z-36388-rmg_a-admin.json, PID45020, DLL31cc03e0/sourcef8e9ba97,233.449s. SHA256: `32efe3fdffaab170350a3e78d09234d3e2362ef218d1a0c199bb917331248ecd`. This verifies one RMG-A load; RMG-B, ten-load control and remaining algorithm branches still require current-DLL verification.

## 2026-10-04 — new DLL on both threshold sides

Seven-stack pack15 matches completely with two mixed hero armies:1400/1800 Peasants,10 Angels and100 Archers. Ratios frozen before Start,5250/9404=0.558273 and5338/10996=0.485449, fall above and below loaded threshold0.54999995. The corresponding native comparisons match forecast bits exactly. Later rows from another calculation phase do not replace the original operands.

Local reports: accuracy-campaign-20261004T042026Z-34568-polygon-admin.json (PID48348) and accuracy-campaign-20261004T042042Z-43512-polygon-admin.json (PID36360), DLL31cc03e0/sourcef8e9ba97. Each7/7 units, normal closure;15.280/15.300s. These are two separate loads, not exact threshold equality or three values tested from the same state.

## 2026-10-04 — broad control after the DLL fix

New DLL31cc03e0/sourcef8e9ba97 passes all36 authored packs with the original Angel10 hero army: mixed30/30,solo6/6. Creature types, quantities and cells, prediction hashes, freeze before Start and normal game closure were independently checked. This is one load with this army; other armies, arenas, RMG and the ten-load protocol remain unverified for the new DLL.

Local report: accuracy-campaign-20261004T041313Z-11904-polygon-admin.json, PID46572,268.463s. SHA256: `ba5c163056112b6a50159dd6740927a01f1c6f13cabd3b1b374f0baa2b655a0e`.

## 2026-10-04 — forecast of placed large stacks fixed

The control with20 original Dragons confirms one placed10-Dragon stack at[13,2], with no merge into20. The old empty forecast is retained as incomplete in a diagnostic report. The new DLL preserves successful anchors and quantities, removes unplaced records from display and does not recalculate rows after compaction. Their mask does not imply an engine859b40 exclusion call or adventure-army deletion.

Full native58/58 and live pre-Start forecast1/1 pass. DLL31cc03e0/sourcef8e9ba97; report accuracy-campaign-20261004T041000Z-6096-polygon-admin.json, PID51456, SHA7962d300c60002618fad10851a6ac19f44d1a6c5b6096adaa5e28676462efdbb. Game closed, map restored;21.614s. Broad results of the previous DLL do not transfer to this one.

## 2026-10-04 — insufficient space for multiple large stacks

The authored BlackDragon20 versus Angel100 control with fixed obstacles produced public2/models0 and failed projection readiness before Start. No saved forecast or final cells exist; this is a predictor failure, not a completed accuracy sample. The game closed normally, temporary map and manifest were restored, and obstacles removed. Local report: accuracy-campaign-20261004T035629Z-25968-polygon-admin.json, PID41664, DLL baca8975/source13ae9b,20.809s.

Static tracing shows that the simple-placement dispatcher invokes the initial placement pass, runs the simple-path fallback once on failure, then releases its placement context and returns. The extended merge/exclusion retry is absent here. After-Start handling of the remaining unplaced stack is still unverified; prediction must not add exclusion without that evidence.

## 2026-10-04 — current DLL with Peasants in the hero army

All36 authored packs matched completely with1000 Peasants in the hero army: mixed30/30, solo6/6. Creature types, quantities, cells, the prediction hash frozen before Start and normal game closure were checked. Pack19 contains one neutral Peasant1000 stack at[13,6], versus four stacks in the previous100-Archer hero control. This tests changed splitting with a different known hero army.

Local evidence: accuracy-campaign-20261004T034843Z-34716-polygon-admin.json, PID24144, DLL baca8975/source13ae9b,262.590s. SHA256: `d93c03716dbcfe0e8efa97c7bb1187fbfbf1685d19ce306b2c634ff558ae5084`. One load does not complete the ten-load protocol or reconstruction of the full algorithm.

## 2026-10-04 — current DLL with a ranged hero army

All36 authored neutral compositions matched completely with100 Archers in the hero army: mixed30/30, solo6/6. Every creature type, exact quantity and cell was checked, alongside the prediction hash and its freeze before Start; the game closed normally. This is one load of current DLL baca8975, not completion of the ten-load protocol or the full algorithm.

Local evidence: accuracy-campaign-20261004T034054Z-10192-polygon-admin.json, PID25584, source13ae9b, duration272.228s. Report SHA256: `5c7ba899cdcaf41c87633130c609a1ff3ba1a670e01f191f650f1a47eb930dd4`.

## 2026-10-04 — large stack in live fallback

- Sandbox ordinary pack19 temporarily becomes BlackDragon1 with the previous fixed-obstacle fixture. This is an ordinary neutral attack, not a scripted extended-placement path. Forecast[84×1,13,2,size2] saved before Start matches exact1/1 afterward; direct entry into the simple-path fallback on side 0 confirms fallback after simple failure.
- At fallback entry the stack is unplaced; large helper writes its2×2 footprint in free front cells. Return/normal exit succeed. Hash/time/tuple/entry independently checked; map/manifest restored byte-for-byte and temporary H5U removed.
- One-large/two-column/melee scope does not prove third-column or split-large join/remove behavior. DLL baca89 unchanged; raw JSON/derived map/manifest stay local and game resources are not published. [Predictor](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp).

## 2026-10-04 — live fallback with fixed obstacles

- Sandbox uses the stock ArenaObstaclesGroup/FixedObstacles/blockedTiles format: X12/13,Y3..10 blocked, front two rows free. Temporary resource H5U belongs in UserMODs; the first erroneous data-directory installation did not apply obstruction and is not counted.
- Ordinary single-source Peasant1000 andArcher40 invoke direct entry into the simple-path fallback on side 0 after partial simple placement. First stack already occupies[13,2], others remain unplaced. Forecasts before Start match2/2 battles and6/6(type,quantity,cell) units, retaining that first cell; melee and shooter-first column priority differ as in the game.
- Return/normal exit succeed; exact owned overlay removed after hash verification. A supplemental manifest links immutable reports to overlay hash/setup. Derived game resources/raw JSON stay local and are not published. Third-column/2x2/remaining branches need separate controls. [Predictor](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp), [path observer](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## 2026-10-04 — direct entry into the simple-path fallback and unsuitable scripted control

- Passive path journal now records the simple-path fallback itself; shared column-helper calls do not substitute for caller proof. New observer installs successfully on a normal Peasant1000 control with3/3 exact forecast and normal exit; the simple-path fallback was not invoked.
- Single BlackDragon20 on specified Grass_Big_01 matches1/1 exact forecast before Start, returns and exits normally. The native route uses extended placement and its general pass rather than the target simple fallback. This scripted pack therefore does not count as live coverage of the simple-path fallback and is not blindly repeated over scenes.
- Next needs an ordinary single-source neutral attack with authored obstruction geometry and direct entry into the simple-path fallback. Production DLL unchanged; driver hash changed. Internal JSON/hash/time evidence retained but unpublished. [Observer](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## 2026-10-04 — broad control of the new fallback DLL

- Current DLL baca89 with Angels10 completes all36 authored cases:36/36 exact(type,quantity,cell),mixed30/30,solo6/6. Forecasts before Start, hashes/timing order and exact counters independently checked. Return and normal exit succeed; full cycle261.870s.
- Recorded path set does not contain the simple-path fallback; shared column-helper calls do not prove forced fallback. Synthetic240-case/selector checks remain a separate evidence scope. Other armies/arenas/RMG, live fallback and remaining branches stay open. Earlier273/273 is not transferred to this DLL. Internal JSON retained but unpublished. [Harness](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## 2026-10-04 — simple placement fallback implemented

- DLL baca89 adds source-simple fallback following the original simple-path fallback: source order, partial placed mask/occupancy, shooter-gated large/small passes, cursor reset per helper. Width2/3 comes from the army deployment rectangle; unsupported right-side/full-height geometry is not guessed.
- C++ matches original instructions on240 synthetic mixed two/three-column cases. Selector separately reproduces partial failure and[13,2],[13,1],[12,1]. Full native58/58 pass without skips.
- Live Archer40→twoArcher20 control matches2/2 and exits normally. It did not require fallback; forced live fallback remains pending.273/273 belongs to previous DLL a8d794; new broad matrix is still needed. Internal JSON/archives/timings retained but unpublished. [C++](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp), [native tests](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py).

## 2026-10-04 — uncovered fallback pass

- The original initial simple-placement pass and its fallback were tested on a synthetic field: three identical ranged1x1 stacks, two columns, local rows0/1 free and2..9 blocked. Simple placement writes the first stack[13,2] then fails; fallback preserves it and writes remaining[13,1],[12,1].
- This exposes a specific gap in current source-simple prediction, which stops after failure. Completed273/273 does not cover it; no live miss claimed here. Native regression passes; production DLL is unchanged.
- The source-record copy function preserves input order rather than sorting; the temporary-reference cleanup function releases those references. The test substitutes getters/copy for identical records; placement passes run original instructions. Mixed records and optional third-column mode remain incomplete. Internal fixture/log retained but unpublished. [Tests](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/tests/test_native_preview.py).

## 2026-10-04 — strict ten-load control

- Current DLL a8d794 completes273/273 exact(type,quantity,cell) matches across ten fresh loads: mixed213/213,solo60/60. Polygon144/144,RMG-A72/72,RMG-B57/57. Every game exits normally; no return failures in this series.
- Independent strict verification checks current source/DLL/tool/map hashes, expected packs/load order, prediction hashes, storage before Start/observation and exact counters. PASS applies to this dataset; goal_completefalse keeps complete-algorithm verification separate. Legacy CLI exit1 is its old Superadmin acceptance flag, not a miss in this series.
- Live equality/same-state thresholds, effects/linked/dispatcher/baseline/null-hero/simple-path fallback and complete RNG boundaries remain open. One clean series does not explain earlier hero loss. Full cycle4800.185s; report217989320bytes. Whole-JSON rewrites warrant profiling, not a claim that they caused all elapsed time. Internal JSON/hash evidence is retained but unpublished. [Verifier](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/check.py).

## 2026-10-04 — current DLL on both RMG maps

- DLL a8d794 matches all24/24 selected RMG-A and19/19 RMG-B battles; mixed18/18 and13/13,solo6/6 on each. Predictions frozen before Start; exact(type,quantity,cell), hashes and timing independently checked. Return and normal exit succeed.
- A Stronghold hero completes previously problematic pack133; a positive control does not explain an earlier different hero's disappearance. B case094 matches creatures and cells. Older-DLL failures remain separate evidence.
- Three current Polygon profiles plus two RMG loads total151/151 complete battles(mixed121/121,solo30/30). Five fresh loads are not the ten-load protocol or the entire algorithm. RMG cycles took245.027s and185.380s. Live equality, remaining branches and earlier hero loss stay open. Internal JSONs are unpublished. [Harness](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## 2026-10-04 — ranged army and threshold sides

- Current DLL a8d794 with Archer100 completes all36 authored cases:36/36 exact(type,quantity,cell) matches, mixed30/30,solo6/6. Combined with the other two profiles on this DLL,108/108 battles complete. Return and normal exit checked; JSON hashes and before/after Start ordering independently verified.
- Mixed Peasant1400/1800+Angel10+Archer100 pack15 controls each match7/7. Frozen large/total melee scores5250/9398 and5244/10647 yield0.55863 and0.49253 across loaded0.549999952; first native comparisons agree. Later comparisons may describe a different state and must not replace the initial snapshot.
- These are separate fresh loads, not equality or a same-state triple. Live equality, current RMG/ten-load series and remaining branches stay open. No new code/DLL change in this experiment; internal JSONs are retained but unpublished. [Harness](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## 2026-10-04 — native level dialog and complete Polygon controls

- Devkit now observes CLevelUpBox construction/destruction instead of inferring absence from empty OCR. A live control shows the object exists while GetHeroLevel remains1; choosing destroys it and commits level2. Production cleanup handled a real forced modal with one choice and closed state; combat boundaries were stubbed in this separate UI experiment.
- Current DLL a8d794 full Angels10 and Peasant1000 series match **72/72 exact** battles: mixed60/60,solo12/12. Predictions are frozen before Start; types/quantities/cells, hashes and timing order independently checked. Adventure return and normal exit succeed. Neither series opened a level dialog; positive dialog evidence remains the separate control.
- Native55/55 and SDK45/45 tests pass without skips. Full36-battle cycles took263.507s and264.510s, measurements rather than a general benchmark. Screenshots remain unreliable and their guard remains. Ten loads, other armies/thresholds/RNG/branches and earlier Stronghold hero loss stay open. Internal logs are unpublished. [SDK](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game_control.py), [mod check](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/native-preview-check.py).

## 2026-10-04 — forecasts on six named arenas

- DLL a8d794 matches original scripted arguments to descriptors captured as primitive inputs and binds them to a checked placement window. Ambiguous/stale/unsupported data are rejected. Source modifiers, hero and geometry are accounted for before Start; final positions are not inputs.
- Six fresh controls: Grass_Big_01,Dirt_Small_01,Sand_Big_01,Snow_01,Lava_Small_01,River_Grass_Big_01. Fixed army: Peasant80, Footman35, Priest12. Forecasts saved before Start match6/6 battles and18/18(type,quantity,cell) tuples. Each game exits normally directly after its Start snapshot; projection release checked.
- This verifies placement, not results/adventure return or ten rotated loads. Main campaign still stops on blank results captures. A foreground-owned client DC fallback was also blank and reverted. Native54/54 pass; full current-DLL matrix remains unverified. Internal JSON/hash/time evidence is retained but unpublished. [Source](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp).

## 2026-10-03 — production capture of original scripted inputs

- New DLLfb8e74 explicitly captures original StartCombat arguments in Superadmin. Live control retained exact80/35/12, input generation1 and56 primitive rows. Argument-level modifiers remain unknown; placement binding and a finished scripted forecast are not implemented.
- Final54/54 native tests passed. A normal three-stack attack matched all3 exact(type,quantity,cell) tuples against a forecast frozen before Start, but results checking failed on a blank capture. The run is incomplete and the game closed normally. Earlier aggregate accuracy does not apply to this DLL.
- SourceTrace ABI7 distinguishes map-neutral/scripted provenance and modifier availability. Ordinary mode receives no new hidden inputs. Full algorithm, six named arenas and ten loads remain open. Internal logs/source archive are retained but unpublished. [Source](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp).

## 2026-10-03 — original scripted army before placement construction

- Correction to the previous control: original-source generation0 does not establish absent scripted entry. A checked arena-call return and separate placement generation0→1 prove native placement-window construction. Visibility/non-minimization were checked; rendered deployment remains unproven.
- On the pinned build, an owned temporary observer at the StartCombat call captured its original arguments: Peasant80, Footman35, Priest12. They matched the authored army and preceded combat construction, without consuming final positions. Original code restored; normal game exit confirmed.
- The DLL's ordinary attack handler does not run on this path. Scripted source/generation support is still unimplemented; named-arena prediction accuracy remains unproven. The console VM separately lacks type/pcall; the earlier type query timed out. Internal logs/decompilation are retained but unpublished. [DLL source](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp).

## 2026-10-03 — blank capture does not establish game phase

- On the pinned Universe build, a scripted Grass_Big_01 control yielded no saved forecast: original-source generation0 and public/models0. PrintWindow succeeded but returned a blank black/white surface. Combat entry remains unproven; this is not an accuracy sample.
- Devkit retains PNG and rejects at most two colours sampled on a32×32 grid before OCR. A retained blank frame was rejected; an adventure frame passed. All9 SDK tests passed without skips. Passing the heuristic does not establish phase, freshness or correct rendering.
- Screenshot failure no longer suppresses separate native failure diagnostics in the predictor harness; its targeted regression passed. Missing original source and earlier hero disappearance remain unexplained. Internal logs are retained but unpublished; no new full accuracy campaign was completed. Sources: [shared capture](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game-ui.ps1), [harness](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/scripts/accuracy-campaign.py).

## October3 — separate strict verification and incomplete campaign

Superadmin report verification now checks current hashes, the complete selected pack set, ten normally closed loads, prediction before observation and exact creatures/quantities/cells. Spatial-only matches or incomplete campaigns cannot pass. All52 tests passed. Passing this set alone does not establish full algorithm branch coverage.

The new campaign retained210 fully compared matches and one additional correct four-stack snapshot. After the last battle, the driver could not find its selected adventure hero, so cleanup and ten loads remain unverified. The cause is unknown; all eight games closed normally and evidence is retained. No hero was automatically recreated or replaced. Internal logs distinguish accurate prediction from cleanup failure.

## October3 — level-up modal stopped the campaign

All101 completed battles in the new current-DLL series matched completely. The next battle never started because an adventure level-up modal remained open. This is a test-driver failure, not a measured placement miss; ten loads did not complete.

Checking hero level alone was insufficient: the API returns the old level until a skill is selected. The driver now recognizes the real dialog and sends addressed selection/OK events. A separate live UI control confirmed1→2, modal disappearance and normal closure; its combat stages were mocked, so it is not an accuracy battle. All51 tests passed; initial failed controls remain retained. OCR adds latency; direct devkit modal detection remains to implement.

## October3 — current DLL:151/151 complete sets

With unchanged94f0e7,108 Polygon battles across three hero armies,24 battles on the first generated map and19 on the second matched completely:151/151, with121/121 mixed. These are five fresh loads. Creatures, quantities, cells, prediction hashes and pre-Start preservation were checked separately; all games closed normally.

Exact tested source bytes are retained in a SHA-256 archive. The ten-load series, specified arenas and remaining special branches still need verification. This does not complete the overall goal; internal logs retain earlier misses.

## October3 — overlapping Cyclops roles

A Cyclops paired with Goblins can be a physical shooter despite zero ordinary ammo. Ordinary deployment processes large units before special shooters, whereas defence begins with shooters. One shooter flag does not replace category order.

The first correction produced a new0/2 miss with hero Angels while the Peasant control matched; the failure remains retained. DLL94f0e7 stores physical capability separately, uses the selected role for row choice, and passed50 native tests and2/2 fresh controlled battles. Both new fields differ from the original negatives. Retained obstacle-vector checks reproduce rows7 and4 but do not replay complete arenas. A full new series remains necessary; raw logs are internal.

## October3 — ten loads:269/273 and two additional rules

DLL e4d4c6 matched269/273 complete battles across ten fresh Polygon/two-generated-map loads:209/213 mixed and60/60 solo. Predictions were saved before Start and all games closed normally.272/273 occupied-cell-set matches do not replace creature/quantity verification.

Three misses of one pack exchanged two melee units under defence plus spread. The game used ordinary movement-aware ordering; the mod selected power ordering. DLL384e08 corrects comparator selection and passes49 native tests and3 fresh targeted battles, including defence without spread. Its complete series has not run.

The fourth miss remains:40 Goblins and3 Cyclopes. The game classifies the Cyclops as a physical shooter in this composition despite a recorded ordinary ammo count of zero. Both predicted rows differed from the actual rows. Exact classification and its use remain to fix; the full algorithm is not yet proven. Raw logs remain internal.

## October3 — exact source identity, RMG-A24/24

The previous failure is explained: public identification yielded type89 (Black Knight), whereas the original army contained90 (Death Knight). No quantity matched89, so calculation stopped before world capture. The placement-binding hypothesis was refuted: frame guards,16×12 field and obstacle buffer were valid.

Superadmin now uses exact original types and order before calculated splits/grades. This is not a knight-specific exception; ordinary mode retains public inputs. DLL `e4d4c655c72ff5be2e21e77213d964f7c6b7457442eba5404a4c29afb807679d` passed the targeted battle2/2 and the complete first generated-map set24/24:18 mixed and6 solo. Predictions were saved before Start, games closed normally, and49 native tests passed. Earlier Polygon108/108 and second-map19/19 belong to another DLL.

Operation timing has started. The corrected one-case run took20 seconds and the complete24-battle set232 seconds; individual analysis intervals took minutes. Test duration does not prove accuracy, and one successful map set does not complete the overall goal. Raw diagnostic logs remain internal.

## October3 — three hero armies and generated maps

With unchanged DLL `c14548e7855da4f1ba13b664937703406a56381265887a222328ab1491b632de`, Polygon matched108/108 complete battles:36 compositions each with10 hero Angels,1000 Peasants and100 Archers. A separate series on the second generated map matched19/19, including composition, quantities and cells. Predictions were saved before Start and test games closed normally.

A10-Titan control matched the target seven-stack pack7/7: large ranged troops were excluded from both melee groups, with24/24 matching native scores. Two mixed armies matched7/7 each with ratios0.492 below the approximately0.55 threshold and0.558 above it. Exact equality was tested at the arithmetic boundary; a live equality army remains to prepare. Intermediate inputs differ between these loads, so they are not a controlled change of just one variable.

The first generated map remains incomplete:7 battles matched, then the next case stopped before Start. A screenshot shows deployment on a lava arena, but the forecast did not render and its calculation world was not captured. Placement-frame binding remains unexplained; the previous battle's stale observation is not this case's result. Successful series do not close this separate forecast-start failure. Raw logs remain internal; the overall goal is not complete.

## October3 — ground retry fixed, ranged series36/36

DLL `c14548e7855da4f1ba13b664937703406a56381265887a222328ab1491b632de` retries unplaced small support troops together with all small melee units using a joint sorted list. A fresh complete series with100 hero Archers matched36 of36 packs:30 of30 mixed and6 of6 solo. The previous counterexample's Swordsmen now matched(12,8); its Archers matched(13,6). Predictions were saved before Start, actual composition/quantities/cells captured afterward. The game closed normally.

All49 native tests passed. The first intermediate build displayed no models before Start because a new iterator was not reset between planning and rendering. The failure was retained, the reset fixed and tested separately. Passing native tests alone had not proved live operation. Other hero armies, arenas, thresholds and RMG remain necessary;36/36 does not complete the overall goal. Raw logs remain internal.

## October3 — complete ranged series and ground retry

With DLL `0cb7c5ef4bd169c8d56d26a1f9d76f07d28d13ec234842c29b8ccb3f32b489b4` and100 hero Archers,35 of36 packs matched completely:29 of30 mixed and6 of6 solo. The sole miss was15 Swordsmen: predicted(13,1), actual(12,8). The same pack's40 Archers matched(13,4), and placement mode agreed. The original algorithm retries unplaced small melee units in the general ground placement pass after support placement. Our code omits this retry; the exact cell choice remains to reproduce.

A separate hero control with100 Peasants+10 Angels+100 Archers matched7/7. Owned large/all-melee scores5243/5498, calculated before Start, exactly matched the later native comparison. All48 native tests passed without skips. Both games closed normally. This verifies specific branches; the complete goal and new miss remain open. Raw logs are internal; a public input-field dataset is not yet published.

## October3 — hero contribution to large melee strength

In the investigated Universe build, large melee strength is compared with all melee strength. Both estimates include the hero contribution and use the complete opposing army as the reference. An army of100 Archers therefore yielded24/24=1 despite having no creatures in either selected group. After-Start observations confirmed zero selected creature damage/health and hero contribution24. The earlier estimate based on the health share of large creatures missed this contribution.

Corrected DLL `0cb7c5ef4bd169c8d56d26a1f9d76f07d28d13ec234842c29b8ccb3f32b489b4` calculated24/24 before Start. One fresh battle against a mixed seven-stack pack matched all7 creatures, quantities and cells, followed by normal game closure. Earlier6/7 and4/7 misses remain retained. Their original arenas have not been replayed, and the complete series has not run on this DLL. This does not establish100% overall accuracy. Raw logs remain internal; a public example containing the original input fields is not yet published.

## 3 October — new counterexample with a ranged hero army

The test driver now accepts explicit hero armies with composition readback before combat. The first control with100 Archers matched6/7 exact pairs in the seven-stack pack: types and quantities were correct, one cell differed. Defence and spread matched the game.

A fresh repeat matched7/7, but the negative control remains open. Diagnostics recorded a1.0 fraction against a threshold near0.55 for neighbouring-row handling. Reconstruct the exact fraction inputs before correcting the implementation. All games closed; the earlier two-army72/72 does not extend to ranged conditions. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — new DLL matches all72 Polygon battles

All36 compositions were checked again with two hero armies:72/72 complete matches, mixed60/60 and solo12/12. Composition, quantities, upgrades/splitting and cells matched; forecasts were frozen before Start. Both games closed normally.

A separate calculation replay from the old miss's saved inputs restored17 enemy aggregate numeric fields exactly. However, the earlier defensive-positive state did not recur live. Ranged hero armies, threshold controls, arenas, RNG, full RMG coverage and other algorithm gaps remain. Two Polygon loads do not complete the full goal; post-Start explanations remain a separate task. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — complete campaign with two hero armies

All36 compositions were checked across two fresh loads: baseline army36/36, second army35/36. Total71/72 exact battles including composition, quantities, upgrades and cells; mixed59/60,solo12/12. After-Start observations are now saved before leaving combat. Both games closed normally.

One miss involved an unsupported shooter flag that halves its entire action factor. The correction matched220 original-function comparisons and all47 tests of the new DLL passed. Two fresh target controls matched, but the earlier defensive-positive state did not recur. Repeat the full campaign on the new DLL, then complete other hero armies, arenas, thresholds, RNG and RMG. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally; the full goal is unfinished.

## 3 October — quick combat obstructed placement verification

Observed subsequent startups did not reproduce the earlier access violation. A screenshot of a separate failure showed a different cause: the strong hero received quick-combat results without entering placement. Test maps now disallow quick combat for their objects; armies/positions and the player's saved profile are preserved.

The first new control matched completely, including splitting and an upgrade. A broader run completed11 exact battles before a report-write failure; brief Windows locks now receive bounded atomic-replacement retries. The latest run completed four exact battles and stopped reading the hero after leaving the next battle. The full Polygon and second hero army remain unverified; the original crash is unexplained. All games closed. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — late spread passes corrected

The row filter incorrectly bypassed later ground and support placement passes. After correction all44 tests passed, and the problematic mixed pack on the second RMG map matched completely across three fresh spread-on loads. This verifies correction of that specific miss.

The full Polygon campaign with two hero armies failed during startup before its first battle. The access violation cause remains unknown; neither Granny nor the new DLL is established as its cause. Capture exception context before retry. All processes are closed; the complete goal and post-Start explanations remain open. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — spread mode reconstructed, cells still differ

Actor area properties are frozen before Start;768 arithmetic checks matched original branches. The owned calculation now correctly enables spread, but three fresh battles of the problematic RMG pack still differ in cells. Candidate and row selection need diagnosis. All43 tests of the current DLL passed; the goal remains unfinished.

Following the owner's report, visible automation now chooses the current player's hero, asks the game to validate approach cells, and follows the camera after verified teleport. A separate control image shows the hero and selected portrait; the game closed. The original intermittent disappearance was not independently reproduced, so no single proven cause is claimed. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally; post-Start explanations remain pending.

## 3 October — area estimate inputs frozen before Start

The new capture saved26 army and spell property records before Start. No overflow or unsupported records occurred, and they did not change after Start. All42 tests passed. A fresh battle matched completely with spread off; the owned denominator101 matched the game.

The hero value24 came from the caster baseline property rather than its sole listed spell, which was neither damaging nor area eligible. The property's internal formula still needs reconstruction. Next are the remaining actor area properties and complete numerator; earlier spread-on misses remain open. The sandbox closed normally. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — spell scoring for spread

Spell power calculation from availability, damage, resources and available casts was reconstructed;776 original-function comparisons matched. Four-turn and ten-turn estimates differ: damage97 with resources for one cast yields24 versus9. Therefore the completed aggregate estimate cannot substitute for the spread numerator.

Spell fields still need capture before Start and integration with other army area properties. The new calculation is built but not deployed; no live accuracy improvement is claimed. The cause of the observed hero value24 remains unproven. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally; explanations remain pending.

## 3 October — owned power calculation for spread

The area-attack ratio denominator was ported to C++;664 original-instruction comparisons matched. In a fresh battle both prediction and game produced97, and the entire pack matched. The hero had Battle Frenzy and the game selected spread off. This is a separate positive control; the preceding three spread-on misses remain open because the exact numerator still needs capture and calculation before Start. The game closed; the goal is unfinished. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — category clarified and remaining miss

The special category argument places a unit in the shooter group only with two additional flags. Exclusion, shooter, flying and ground priority was reconstructed;64 original-instruction checks passed. The new DLL calculates both armies.

Three fresh controls of the problematic mixed pack on the second RMG map still produced0/3 complete matches: prediction does not yet calculate the spread chosen by the game. Capture primitive area-attack properties before Start and compute their relative power; after-Start observation remains validation only. Earlier36/36 belongs to the previous DLL. All test games closed; explanations remain pending. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are being prepared locally.

## 3 October — first complete Polygon match {#integrated-polygon-2026-10-03}

Computed composition is now connected to projections. Split solo packs use their own sequential placement pass, preserving order and quantities.64 cell cases matched the original function and all39 tests passed. Three fresh targeted loads matched whole packs.

The new full Polygon load produced36/36 exact battles: mixed30/30,solo6/6. This covers one load/profile. Three selected encounters matched on the first RMG map; two of three matched on the second. The miss involves spread selection with a currently unsupported hero-army category. A separate driver error expecting the original stack count was fixed and retained.

The goal remains incomplete: that mismatch, the full profile/arena/RNG/RMG matrix and remaining fallback branches need work. Games were closed. All-player post-Start explanations remain open. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; the new candidate is unpublished.

## 3 October — composition computed before Start {#owned-composition-2026-10-03}

Owned C++ determines stack count, RNG draws, interior upgrade and quantities from early inputs.2352 cases matched original instructions. Three fresh loads matched composition3/3, including upgrade substitution.

Rendered cells still use the previous forecast: only1/3 whole battles matched. All38 tests passed and games were closed. Placement integration is next. All-player post-Start explanations remain a separately open task. [Sources](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; new evidence is unpublished.










## 3 October — early strength and RNG inputs captured in the DLL {#source-input-runtime-2026-10-03}

C++ now captures early source-stack stats, context flags, coefficients and extended initiative, then computes strength with owned code. RNG state is separately captured before the splitting draw. Completed engine decisions and cells are never prediction inputs.

Three fresh loads with default and small hero armies matched all nine distinct numeric results on each load. Hero and target inputs are scoped separately from other map armies. The early seed matched independent observation and reproduced its draw. All37 tests passed without skips.

Initial journals overflowed with repeated queries; those failures were retained. Identical inputs now deduplicate, changed inputs remain separate, and verification stops at the freeze boundary. These results prove inputs and arithmetic, not composition prediction. Army sums, stack count, grades, quantities and their separate placement path are next. Games were closed and original game files unchanged. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; the new candidate is unpublished.


## 3 October — preserving initiative input precision {#source-initiative-precision-2026-10-03}

Before integration, an input-format difference was found: the engine receives extended initiative, subtracts the integer baseline and only then rounds the difference. Storing the getter directly as float could change the result. The C++ input now preserves the extended value before subtraction.

1936 numerical cases matched the original function, including pairs proving that early narrowing changes final strength. All37 tests passed without skips. An initial extended-number fixture normalization error was retained and corrected; it is not counted as an engine defect.

Actual stat capture still needs integration. A new build is prepared while the sandbox retains the previous DLL; no game was launched for these checks. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally and new results are unpublished.


## 3 October — owned source strength in C++ {#owned-source-strength-2026-10-03}

Owned numerical source-stack strength was implemented with ordered integer conversions, modifiers and context corrections. It receives stat values and coefficients without reading the engine's completed decision. x87 precision and intermediate stores preserve the verified order.

1920 compiled C++ cases matched the original function: actual coefficients, two FPU modes, shooter bonus, context penalty and large integer values. The full37/37 checks passed without skips. This proves the numeric core within the tested domain, not a new in-game result.

Early input capture and composition generation still need integration. A new build is prepared, the test game is closed and the sandbox DLL remains the prior version. [Source and tests](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; the candidate is unpublished.


## 3 October — strength calculation order for splitting {#split-strength-order-2026-10-03}

The source-stack strength arithmetic was reconstructed: base value, ordered stat additions, modifiers and multiplication by quantity. The engine converts to an integer after each addition and multiplier; moving all conversions to the end changes the algorithm.

108 controlled cases matched the original function under two FPU modes. These test arithmetic with supplied inputs and binary-exact coefficients. Context branches, shooter bonuses and rounding with actual coefficients still require verification. An initial fixture field-type error was retained and corrected against original instructions.

A live control confirmed the function bytes and froze loaded-build coefficients. The DLL was unchanged and the solo pack still split differently from its forecast. Own strength and composition calculation from early inputs is next. The game was closed; [tool sources](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally and new raw evidence is unpublished.


## 3 October — capturing RNG at the split draw {#split-rng-timing-2026-10-03}

The late preview RNG state does not reproduce splitting rolls. A passive trace captured state immediately before the draw: independent arithmetic matched all four measured cases. Splitting and initial initiative use the same RNG, with state captured at different times.

This does not yet implement composition prediction. Strength calculation, stack-count boundaries, grade selection and quantities remain to reconstruct. Three fresh controls of the unchanged DLL yielded2/3 matches because two random outcomes retained one stack; these are not an improvement. A Python driver failure was preserved and fixed before successful measurements, and games were closed. [Tools](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; new evidence is unpublished.


## 3 October — residual passes implemented in C++ {#owned-residuals-2026-10-03}

The Superadmin predictor now places remaining large and small units after primary groups. Original source order is kept separately from strength sorting and already placed units are skipped. Full occupied footprints are checked and the free-row cursor persists between units. Ordinary mode is unchanged.

The new DLL matched pack7 completely across three fresh loads with default, small and default hero armies. A separate36-composition load then produced32/36 full matches: mixed30/30, solo2/6. Four misses involve composition splitting that is not yet predicted, including grade substitution. One Polygon load does not establish100% across profiles, arenas and RMG.

All36 native tests passed without skips; cell tests gained residual and exhausted-space cases. Games were closed and original game files unchanged. Predictions were saved before Start; observations served as verification. [Predictor sources](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; the new candidate and raw evidence are unpublished.


## 3 October — why shooter support is skipped {#leftover-chronology-2026-10-03}

A passive trace showed that the support pass generates neighbours of the shooter's world cell, then tests them against local deployment bounds. All eight candidates were outside those bounds in the measured battle. The unicorn remains unplaced until the large leftover pass, after the pixie and shooter. This pinned-build behaviour still needs reconstruction in C++.

Three fresh loads with different hero armies produced1/3 whole matches; the small-army control matched. The new causal control remains0/1 because the DLL was unchanged. Instrumentation-install, initial field-label and context-offset errors were retained and corrected evidence verified separately. Measurement replaces the previous hypothesis about placement before primary attempts. Documents were repaired after a Cyrillic pipeline encoding error; JSON reports remain unchanged.

Games were closed and game files unchanged. Diagnostic cells are never forecast inputs. [Predictor tools](https://github.com/Xaaalera/heroes5-deployment-preview) are prepared locally; new raw evidence is unpublished.

## 3 October — health and exact unit assignments {#health-defensive-order-2026-10-03}

A conditional health transformation is reconstructed from a coefficient frozen from the loaded game before Start. Owned code repeats multiplication precision, integer conversion and the inactive case.42 original-instruction cases match and36 tests pass. The alternative branch is verified offline only; other effects remain unfinished.

The first live control matched all occupied cells but swapped two units, so strict prediction failed. Mode-specific sorting is corrected: defence compares strength, while ordinary placement retains ground/flying ordering. Three fresh controls then match whole packs. New complete load gives31/36 strict, mixed29/30 and solo2/6; large leftovers and composition changes remain. One load does not establish100% or full RMG/profile scope. Games close normally and counterexamples are retained. Oracles are in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw data unpublished.

## 3 October — seven-stack resource corrections {#resource-factor-2026-10-03}

Three current/maximum counter pairs are frozen before Start and replayed in C++ in native order. Positive maxima use1+0.1×current/maximum. Full, partial and ignored ratios match original instructions bit-for-bit across100 cases in two FPU environments;35 tests pass. Resource names remain to verify without assuming mana/ammo.

The seven-stack pack matches in four fresh controls across defensive and ordinary modes. A new complete36-composition run gives30 strict matches, mixed28/30 and solo2/6. This is neither100% acceptance nor a controlled regression comparison against the previous different load. A separate mixed-pack health effect, large leftovers and composition transforms remain. Games close normally; oracle is in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview), raw data unpublished and full goal active.

## 3 October — defensive prediction and36 compositions {#defensive-prediction-36-2026-10-03}

The DLL now selects defence from aggregates and unit properties frozen before Start. Threshold comparisons and opponent-capability checks are reconstructed for supported inputs; specialized power/ability evaluations retain declared native-helper provenance. Defensive phase mapping and large-unit column/row retries are corrected. Unsupported effects do not count as a complete calculation.

One complete load tests36 compositions:31 strict type/quantity/cell matches, mixed28/30 and solo3/6.35 tests pass and the game closes normally. This is progress, not100% acceptance across profiles/arenas/RMG. Remaining misses involve composition changes, large-stack leftovers and resource corrections in the seven-stack pack. It matched7/7 in an earlier load but4/7 in the new one; both results remain recorded without a universal claim. Two earlier campaigns stopped on research-observer overflow and zero models, with corrections and negative evidence retained. Raw reports are unpublished; tests are in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview).

## 3 October — auxiliary power provenance {#auxiliary-power-input-2026-10-03}

The additional24 comes from the hero evaluator; physical-unit evaluations are zero in this pack. It contributes to ranged advantage. The DLL now freezes that native evaluator result before Start as an explicit input and accumulates matching records itself. The evaluator's complete mechanics are not yet implemented in owned code.

Live control matches17 of18 words for both aggregates; the remaining word is an internal pointer the owned calculation does not create. This verifies one pack's numeric inputs, not complete effects or placement accuracy.34 tests pass, frozen data is unchanged after Start and the game closes normally. Defensive policy is still unconnected and the battle remains a strict miss. Tests are in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw game data is unpublished.

## 3 October — hero correction from primitive integers {#hero-scalar-replay-2026-10-03}

The conditional hero correction is reconstructed: two integers are summed and multiplied by0.05, then1+that value scales the army factor. Stat names and guard meaning still require verification. The DLL freezes primitive inputs before multiplication and calculates the correction with pass/generation binding.

Owned arithmetic matches original instructions bit-for-bit across ten cases. Live values1 and1 produce all13 matching numeric fields for both armies before Start. Auxiliary scoring and defensive policy remain unfinished, so the battle is still a strict miss.33 tests pass and the game closes normally. Oracle is in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw evidence remains unpublished and full goal open.

## 3 October — owned runtime aggregates {#owned-runtime-aggregates-2026-10-03}

Frozen inputs now drive owned aggregate calculation in the DLL before Start. Repeated observations are separated by army/pass; order is preserved and ambiguous duplicates or unsupported effects are rejected. Live control verifies13 bit-exact neutral numeric fields. The own army matches12 of13, with hero correction to the action factor still unfinished.

FPU-state preservation and post-Start immutability are verified;31 tests pass. Grouping oracle is in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview) and raw evidence remains unpublished. Defensive policy is not yet connected, so the control battle remains a strict miss. Auxiliary score fields, abilities and full coverage remain open. The game closes normally.

## 3 October — owned early collector {#owned-early-collector-2026-10-03}

Pre-Start attribute capture now runs in the C++ DLL. The bounded snapshot is tied to an attack and frozen before combat. Corrected live control retains42 rows;20 fields per row match independent observations and remain unchanged after Start. Unsupported effects are explicit and final occupied cells are absent.

The first candidate crashed after reset changed an existing handler's input register. The defect is localized, corrected and covered by a regression test; negative evidence is retained. The control game closes normally. Capture is not yet connected to defensive policy and the battle remains a strict miss. Aggregate integration and hero corrections come next; tests are in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview) and raw game records remain unpublished.

## 3 October — early inputs and rounding {#early-inputs-fpu-2026-10-03}

Early observation confirms the same forecast world contains both armies during calculation, while late vectors are empty. Types, quantities and actual attributes are retained before Start. Independent C++ replay initially differed from live float bits: the game uses24-bit x87 precision with rounding toward zero.

Reproducing that environment matches all42 factors. An initial numerator seed1 was also restored, after which13 neutral numeric aggregate fields match. Hero correction, auxiliary fields and group ordering remain unfinished. This verifies core arithmetic on frozen inputs, not an active predictor or100% acceptance. Games close normally and defensive-mode misses remain. The three relevant oracle tests are in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw replay is unpublished.

## 3 October — input capture timing {#forecast-input-lifetime-2026-10-03}

A live control confirms both forecast-world army interfaces, but the next finds both unit vectors empty at prediction-freeze time. Late reading of these vectors does not provide complete calculation inputs. Earlier observed factors were computed before Start; whether those temporary actors belong to the same world remains unverified.

Next is earlier attribute/context capture with generation checks. Both control battles remain strict defensive-mode misses and games close normally. Snapshot size/lifetime checks extend `test_superadmin_source_requires_opt_in_and_expires_with_placement` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw records remain unpublished. The negative result is retained.

## 3 October — health and distinct defence weights {#health-accumulation-2026-10-03}

Owned C++ accumulates health and defence weights. Total and gated-subset defence can differ: the verified doubling applies to the total, while the subset uses the raw value. A temporary remaining-health label is replaced with a neutral subset name; the complete meaning of its eligibility gate remains to verify.

Seven sequential inputs and final normalization match original EXE instructions bit-for-bit. Evidence: `test_owned_health_accumulation_matches_native_subset_and_distinct_defence` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview). Earlier health effects are neutralized in this oracle; complete input capture and defensive-policy integration remain unfinished. No game launched and placement accuracy has not changed.

## 3 October — army damage accumulation {#damage-accumulation-2026-10-03}

Owned C++ accumulates damage and weighted sums for shooters, flying, ground and category-excluded units. Eight sequential inputs match original EXE instructions bit-for-bit, including float rounding, zero damage and integer overflow. Subsequent normalization also matches.

Evidence: `test_owned_damage_accumulation_matches_original_categories_and_rounding` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview). This oracle stops before health and status processing. Complete input collection and defensive-policy integration remain unfinished; no game launched and placement accuracy has not increased.

## 3 October — army-strength normalization {#aggregate-normalization-2026-10-03}

Weighted normalization is reconstructed: attack uses damage, defence uses health and categories have separate denominators. Zero denominators preserve prior fields. The intermediate action-factor sum is float, correcting an inaccurate decompiler type.

Owned C++ matches original EXE instructions bit-for-bit across ten complete18-field inputs. Evidence: `test_owned_aggregate_normalization_matches_original_words_and_zero_gates` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview). Exact input collection and defensive-policy integration remain unfinished. No game launched this pass; placement accuracy is unchanged.

## 3 October — conditional bonus and C++ arithmetic {#conditional-action-factor-2026-10-03}

The counter-origin hypothesis for1.1 is disproved for the tested pack: measured counters are zero. A different original property/flag condition activates the bonus. Adding this branch explains42 measured factors within rounding precision. Exact property/flag names still require verification; this is not a universal constant multiplier.

Baseline arithmetic is implemented in C++ with x87 intermediate precision. Ten cases match original EXE instructions bit-for-bit. The oracle extends `test_native_initial_action_factor_includes_initiative_speed_and_atb` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview). Full defensive policy is not yet connected to this calculation; both control battles remain strict misses. Raw data is unpublished and games closed normally.

## 3 October — calculation timing and attributes {#action-factor-inputs-2026-10-03}

A new observer shows that factors in the tested mixed pack are calculated before Start. Reading a buffer later does not prove computation happened after Start; a separate pre-Start prefix is now retained. Actual morale, luck, initiative, speed and ATB are measured. The shooter speed-factor exemption is verified; the source of an additional1.1 multiplier remains under investigation.

Four controls remain strict defensive-mode misses. Observer x87/bounds test: `test_action_factor_observer_preserves_x87_inputs_and_bounds` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview). Raw game records remain unpublished, and observations do not feed the predictor. Games closed normally.

## 3 October — live generator control {#live-atb-rng-2026-10-03}

Three fresh loads of one mixed pack verify that the preview-world RNG state frozen before Start begins the sequence creating three actual actors. Active Universe uses ATB0…0.1 while the disk EXE contains0…0.25. This corrects the previous static conclusion without rewriting historical evidence.

All three predictions remain strict misses due to defensive-mode selection. Exact battle inputs, subsequent ATB corrections and abilities remain unfinished; this experiment does not verify splitting, grades or RMG. Games closed normally. Observer checks extend `test_native_battle_rng_uses_two_steps_and_signed_shift` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); raw game JSON remains unpublished.

## 3 October — initial ATB generator {#initial-atb-rng-2026-10-03}

The shared combat-actor constructor samples initial ATB in [0,0.25]. Generator arithmetic uses two state steps and a signed-shift mixer. Original-instruction emulation checks six seeds,30 integer cases and48 ATB samples; float results and resulting state match bit-for-bit. Evidence: `test_native_battle_rng_uses_two_steps_and_signed_shift` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); working decompilation is not published.

Pre-Start state capture timing and consumption order during transformations and creation of both armies remain unverified. Abilities can subsequently change ATB. No game launched this pass; arithmetic verification does not establish live predictor accuracy.

## 3 October — initial battle factors {#initial-battle-factor-2026-10-03}

Executing the pinned build's original arithmetic verifies that baseline battle strength depends on initiative, speed, morale, luck and initial ATB. Six cases check initiative/ATB boundaries and the selected-unit exemption. Attack and defence account for native terrain; army accumulation adds its own unit offset.

Abilities, statuses and reproducing initial ATB/RNG before Start remain unfinished. No fresh game launched this pass. Evidence: `test_native_initial_action_factor_includes_initiative_speed_and_atb` in the [predictor repository](https://github.com/Xaaalera/heroes5-deployment-preview); source game records and decompilation are not yet published. After-Start observations remain verification, not predictor inputs.

This page preserves **experiments, original results and corrections**. [Articles](research-index.md) explain the current understanding; diary entries record its basis.

September 21–23 entries were reconstructed on **September 24, 2026**. This begins the journal; entries identify source data that remain unpublished.

Experiments below use the [pinned Universe build](universe-build.md) unless stated otherwise.

## September 26: sheltered formation and prediction limits {#placement-defence-2026-09-26}

**October 2, 2026 follow-up:** work resumed to reconstruct the complete algorithm and achieve fully matching Superadmin predictions frozen before Start. Ordinary-mode policy will be discussed separately. Exact source quantities are available to Superadmin, but automatic strategy, composition transformations and special adjacency are not fully reproduced.

Twenty theory compositions were added locally to the polygon, bringing the total to36. Cases cover1×1/2×2 footprints, shooter support, Goblin/Shaman/Cyclops links, a missing partner, reversed input order, seven large stacks and duplicate types. A new40-Goblin/8-Shaman control matched1/2 exact pairs: the Shaman matched, but the engine placed the Goblin beside it while the prediction chose another row under the same strategy. Special-category adjacency is a cause hypothesis to verify. Two source Peasant stacks of10 and20 matched2/2 cells; final quantities were not checked. Full local logs are unpublished; these controls do not establish100% Superadmin accuracy.

The sandbox startup was restored by changing import order only in the owned process's memory, preserving on-disk game files. This validates test tooling, not a changed player installation. Record every discrepancy and then verify its branch; one successful case does not complete a mechanism.

A seven-large-type control exposed an incomplete prediction: seven public types but five created projections. The test stopped before Start and closed the game normally; no actual cells were recorded. Deployment capacity and leftover passes are hypotheses for the next check, not a measured5/7 result.

**Later correction that day:** a separate research control froze the partial prediction before Start and then recorded actual deployment. The engine also deployed only five units from seven source types. All five occupied cells matched, but only2/5 type/cell pairs matched; source selection and ordering remain unresolved. Missing projections alone therefore do not prove the earlier capacity hypothesis.

Goblin linkage is now implemented in C++: a previously placed large carrier still participates in adjacency, and upgraded Goblins are identified by base type. The observer captures actual quantities after Start, while exact-quantity predictions are saved and hashed before Start. Two fresh controls, Goblin/Shaman and two source Peasant stacks, matched types, quantities and cells. These are individual experiments, not100% acceptance; full logs remain local.

Verification exposed two SDK checkouts at different versions. The workshop now has one working checkout per subrepo, with repeated mod dependencies linked to the shared SDK and a command checking origins/versions. SDK edits are immediately visible to both mods. Algorithm research was paused by the owner; no new DLL was published.

**After goal resumption:** non-shooter ordering was checked separately: ground units before flyers, speed takes priority when reaching the distance between armies, then strength is compared. C++ matched original-instruction execution on108 combinations; these are not108 live battles. Source speed/flight are frozen before army transformations.

Live observation explained the five-stack selection: after the first failed attempt the engine excluded eight Genies, then five Hydras after the second, even though the Hydras had already been placed. Placement is then recalculated. Prediction still lacks the complete exclusion/retry cycle; matching five occupied cells with different creatures is not a complete forecast. Full logs remain unpublished and the100% goal remains open.

**Next verified step:** owned dry planning, weakest-source exclusion and occupancy restoration were added to the DLL. Another arena then exposed a further rule: a2×2 unit may try the next row while retaining the original candidate score. After reproducing it, three fresh loads of the problematic pack fully matched types, quantities and cells. Predictions were computed before Start; observation only verified them.

A completed36-composition load matched28 exact formations:24/30 mixed and4/6 solo. Two split cases, five defensive-mode decisions and one large-unit leftover pass remain wrong. Other profiles, arenas and RMG are not yet verified with this candidate. This is intermediate evidence, not a100% guarantee. All20 native checks pass, the game is closed and the new DLL is unpublished.

The next investigation compared raw army aggregation with battle aggregation. The source-descriptor builder was connected after fixing its calling convention; the first incorrect experiment crashed and is recorded separately. Two corrected controls matched total damage/health but differed in attack/defence and multiplier: one army differed by+1, the other by+2, with different multipliers. The causes are not yet established. Raw input is frozen before Start; battle aggregation is observed only for verification after Start. Exact formation choice requires those transformations; local evidence remains unpublished and the100% goal is unfinished.

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

**Method:** ordinary DLL loading, WorkshopPolygon, pack_8 → pack_12 → pack_15. Predictions were saved before Start; GetUnitPosition recorded positions separately. An additional observer captured placement-context parameters before formation selection; these records were read after combat and never supplied to the predictor. Random state was not fixed between runs.

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

**Research Superadmin:** an explicitly enabled DLL returned RMG source `(92,18),(98,8)` **before Start**; ordinary startup returned an empty list. In one four-stack control, manually selecting spread and using hidden counts matched **all four occupied cells**, but only **one of four exact creature+cell pairs**. This isolates parts of the rules, not an automatic exact mode: a different manually forced spread series matched only6/19, then4/19 when the engine chose another policy. The100/100 target has not been reached.

[Numerical records and build hashes](../../assets/preview/rmg-accuracy-2026-09-25.json) · [technical mechanism](placement-internals.md). Complete logs and RMG map archives remain local. The final ten-load campaign and≥70% complete matches among **mixed** packs have not passed; newer DLL changes need fresh validation.

**Later September25 control:** one RMG-A pass, with the player's own army restored to its starting composition before each battle, fully matched10/18 mixed packs. All eight misses used another native branch: five spread, three defensive. On RMG-B,0/13 mixed packs fully matched: the engine spread twelve and used defensive plus spread for one. Neutral compositions were unchanged, but arenas and random decisions varied between passes. These two loads do not replace the required ten.

**Next September25 candidate:** the DLL now reads qualitative count bands from stock public cards, never exact neutral quantities, and uses them to estimate spread and defensive selection. Separate fresh loads matched all cells in13/18 mixed RMG-A packs and11/13 mixed RMG-B packs. On the polygon, one defensive seven-stack battle against a small hero army matched all seven creature+cell pairs. With10 Angels, the DLL often falsely enables defence that the game suppresses; the exception is still under study. Reconstructed spread arithmetic matched205/205 native calls **after Start**, but those observations never feed ordinary prediction. These are separate experiments, not the required ten-load campaign or the independent pre-publication review.

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
| The CombatSize field is creature tier | Registration/XML loading identify CombatSize, range 1…2 | Do not substitute tier into CombatSize>2 |
| Equal scores retain input order | Ordinary sorting selects the right lane on equality; 10 equal rows yield 8,4,6,10,2,7,3,5,9,1 | Preserve native ordering instead of arbitrary stable sorting |
| Spread evenly rounds rows | Integer division gives {0,4,9} for R=10,N=3 | Rounding to {0,5,9} changes the result |
| Crowded stacks always merge | The inner loop of the apparent same-type merging function is unreachable for tested valid vectors N=0,1,2,3,7,64 | A branch name does not establish merging |

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

**Algorithm check:** 16 authored fields matched execution of the original movement-cost propagation function in an emulator. Allocation/free were substituted and the source EXE hash was checked. Cases covered diagonals, a wall, flight/landing, a 2×2 corridor, boundaries and buffer guards. This is the preserved September 23 result, not a new September 24 run.

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

**Next experiment:** a temporary entry counter in the army-list renderer, without reading actual guards.

| Action | Cumulative counter |
|---|---:|
| Before hovering | 0 |
| Hovering bank and neutral pack | 47 |
| Then bank and empty ground only | 51 |

**Conclusion:** the bank tooltip path invokes the renderer. The four additional calls cannot be separated into show/hide events; no frame recording exists for this experiment. Invocation does not establish safe integration of a new reference model.

**Static refinement:** the model's virtual methods supply the population condition, element count and indexed access. The inspected implementation uses a 24-byte record stride: its count method reports the number of entries and its indexed-access method obtains one entry. An entry carries texture, numeric and string labels. This describes one implementation, not a ready ABI for arbitrary objects.

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
