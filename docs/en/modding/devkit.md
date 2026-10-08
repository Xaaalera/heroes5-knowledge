---
content_type: explanation
status: draft
faction: fortress
title: Our mod development environment
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/devkit/
description: Our mod development environment
updated: 2026-10-08
---
# Our mod development environment

## Start with xkit

[xkit v0.1.1-preview.3](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.3) includes sources, Game API and ready SDK DLLs. An installed game with Universe is required. Resource H5U projects need no C++ compiler; native plugins require MSVC Build Tools.

Download `xkit-sdk.zip`, extract `xkit` and install [uv](https://docs.astral.sh/uv/getting-started/installation/). In a terminal inside `xkit`, run:

```text
uv tool install --editable .
uv tool update-shell
```

Open a new terminal. `xkit setup` saves the installed game and workspace paths. Then create a resource project, run it in the test copy and build its ready H5U:

```text
xkit setup
xkit new demo --resources
xkit start demo
xkit release demo
```

For a native project use `xkit new demo-native`. Saving supported C++ code automatically builds and replaces its DLL in the same game. Added functions/core exports, state transfer, callback teardown and rollback are verified. The game itself needs no rebuild; DLL code still compiles.

After creation, run `xkit start demo-native`. When development is finished, `xkit release demo-native` builds a separate player DLL package. Resource `xkit start demo` does not promise automatic H5U replacement in an open map. [Setup and version limits](https://github.com/Xaaalera/heroes5-mod-devkit/blob/f5d9a7666635ca478c1481444b6b943d096c2efe/README.md).

### Controls and diagnostics

| Command | Result |
|---|---|
| `xkit game map WorkshopPolygon` | Request to load the test map |
| `xkit game restart WorkshopPolygon` | Request to reload the named map |
| `xkit game menu` | Request to return to the menu |
| `xkit game screenshot` | A new PNG capture and its file path |
| `xkit diagnostics` | SDK status and failure diagnostics |

A connected SDK also exposes these commands through its in-game console. A loading request does not establish map readiness. A screenshot shows the current frame: map, menu or intro. Failed capture is not replayed through another route; exiting the diagnostic client does not stop plugins. [Command reference](https://github.com/Xaaalera/heroes5-mod-devkit/blob/f5d9a7666635ca478c1481444b6b943d096c2efe/docs/commands.md).

Each resource mod ships as its own H5U and each native plugin as its own DLL. Shared infrastructure uses `dinput8.dll` and `d3d9.dll`; the game original stays local as `d3d9.universe.dll`. Existing predictor/reference plugins are not automatically migrated to HMR. Unconfirmed cleanup stops updates and preserves recovery data.

Bank reference now has a dedicated development adapter: `xkit start army-reference --map WorkshopPolygon`, `xkit build army-reference` and `xkit release army-reference`. The owned test game verifies crypt-card rendering and populated cache continuity through bank DLL and SDK core updates. Incompatible data structures are rejected. Predictor work remains paused; this adapter does not migrate the predictor to HMR.

## Historical prototypes and verification limits

The observations below belong to earlier revisions. Their unpublished-prototype caveats do not describe the current release.

**Multiple plugins:** `plugin-watch.py --plugins` observes directories, adds new plugins to the same running game and removes deleted ones. State and compiler failures are separate; cpp/header additions were live-tested. Removal clears UI/hooks, and re-add starts fresh state. SDK source is shared while each plugin owns a compiled bridge instance. Two player DLL packages also passed ordinary simultaneous startup.

Shared build verification, known hook catalog and owned-process guards now live in the separate [Game API library](https://github.com/Xaaalera/heroes5-game-api), published after five independent reviews and successful CI. Predictor, bank reference and devkit consume one library without source copies. Review configuration is included in the library repository; players do not need those tools.

**ABI3 prototype acceptance is complete:** current code passes automatic function/UI/validated engine CALL-hook updates, state preservation and error rollback, followed by ordinary startup of a same-source player DLL package. Latest save→UI2.101s; Python51/native4 PASS. Repeat with plugin-check.py --live. Supported boundaries and retained failures are in the [diary](../reference/research-diary.md). Changes are not published yet.

The local October4,2026 prototype adds native watch: saving C++ automatically recompiles changed units and replaces the DLL in the same game. Window callbacks, numeric UI, state and rejected-update rollback are verified; one save→UI sample took2.162s. `plugin-watch.py --release` builds the same sources into a ZIP with `bin/Heroes5Mods/Plugins/<name>.dll` and shared `bin/dinput8.dll`; ordinary startup passed without the developer client. These changes are not published yet. Arbitrary engine hooks and a general UI API remain open. [Evidence and limits](../reference/research-diary.md).

Resource mods and scripts supported by the relevant game context can use H5U. The native SDK requires DLL/bootstrap; putting a DLL inside H5U does not execute it. Existing predictor/reference plugins keep their legacy contracts and do not become reloadable automatically.

[**Heroes V Mod Devkit on GitHub**](https://github.com/Xaaalera/heroes5-mod-devkit) builds H5U packages, creates a separate game copy and controls a test process through commands. Its source now lives in an independent repository containing the shared tools used in our mod development.

Python and PowerShell handle development/testing. The predictor remains a C++ DLL and is not bundled. Native commands target the [pinned Universe build](../reference/universe-build.md).

## Included tools

| Component | Purpose | Output |
|---|---|---|
| [mod-dev.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/mod-dev.py) | Build, install and roll back resource mods | H5U and ownership hashes |
| Sandbox | Copy installed files without hardlinks | `.local/test-game/` |
| [test-map.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/test-map.py) | Generate a polygon from installed resources | WorkshopPolygon.h5m |
| [native-probe.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/native-probe.py) | Launch an owned process with a control channel | PID and validated channel state |
| [game_control.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game_control.py) | Inspect state, move heroes, start/finish battles | Command response and result check |
| [game-ui.ps1](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game-ui.ps1) | Capture, OCR and addressed input | PNG and OCR data |
| [inspect_universe.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/inspect_universe.py) | Compare archives and extract analysis text | Local inventory |

Mod files, copied game and logs belong to a **workspace**, separate from devkit source. The workshop consumes the devkit as a submodule; compatibility entry points preserve its old commands while calling one canonical implementation.

## Set up the environment

Use Windows 10/11, Git, Python 3.10+ x64 and an installed Heroes V: Tribes of the East with Universe. Close game/editor and reserve disk space for game archives, music and video.

In a new directory:

```powershell
git clone https://github.com/Xaaalera/heroes5-mod-devkit.git
cd heroes5-mod-devkit
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
$env:H5_WORKSPACE = [IO.Path]::GetFullPath('../heroes5-workspace')
$env:H5_GAME_DIR = (Resolve-Path '../HeroesV-Universe').Path
New-Item -ItemType Directory -Path "$env:H5_WORKSPACE/mods" -Force | Out-Null
Copy-Item examples/menu-marker "$env:H5_WORKSPACE/mods/menu-marker" -Recurse
python -X utf8 scripts/mod-dev.py prepare --sandbox
```

Replace `../HeroesV-Universe` with your existing installation. Choose a workspace separate from the game. Copy the example once and set the variables again in a new shell. Preparation refuses to overwrite an existing test copy.

## First cycle: menu marker

```powershell
python -X utf8 scripts/mod-dev.py build --sandbox --mod menu-marker
python -X utf8 scripts/mod-dev.py deploy --sandbox --mod menu-marker
python -X utf8 scripts/mod-dev.py launch --sandbox --menu
```

Verify `[DEV: menu-marker]` appears, then exit the game and run:

```powershell
python -X utf8 scripts/mod-dev.py rollback --sandbox --mod menu-marker
```

The next launch should show no marker. This checks recipe → H5U → installation → observation → rollback. [Why this experiment is useful](resource-overrides.md).

Always pass `--sandbox` here; omission targets the original installation. Deployment checks resource/binary hashes, and rollback refuses externally modified packages.

## Command-driven battles

```powershell
python -X utf8 scripts/test-map.py
python -X utf8 scripts/native-probe.py launch --map WorkshopPolygon --control
python -X utf8 scripts/game_control.py status
python -X utf8 scripts/game_control.py heroes
```

A PID does not establish map readiness. Wait for loading and a hero-list response, then prepare an ordinary attack:

```powershell
python -X utf8 scripts/game_control.py teleport Brem 14 50
python -X utf8 scripts/game_control.py interact Brem pack_8
```

Once the deployment screen is visible, `confirm` starts combat. `finish --winner 0` and `results` provide a test shortcut to finish; check return to the map through `hero Brem`. Use `quit` to close. These are `python scripts/game_control.py <command>` calls, not hotkeys.

`dispatched` only means dispatch. Do not blindly repeat an attack after a timeout. [Full command reference and limits](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md).

The polygon contains eight factions, 12 banks, 16 neutral armies and six scripted arenas. [Download the built map and object layout](test-maps.md). The devkit generator needs no project mods and excludes the experimental UniverseTrigger subscription.

## Extraction checks

- 37 devkit tests cover packaging/ownership, XML, terrain, emulated control and external workspaces.
- 48 existing workshop checks passed through compatibility entry points; shared implementations are not duplicated.
- A polygon built in an empty workspace without our mod directory: 60 objects, six arenas, valid ZIP.
- On September 25, the command environment ran five battles with both DLLs automatically loaded. Startup, cards and cleanup are checked separately from prediction accuracy; results and discrepancies are in the [diary](../reference/research-diary.md#dll-delivery).

Native tools validate four game-file hashes and reject other builds. Complete profile isolation is unproven and EXE startup can briefly take focus. Addressed input and physical mouse behavior are different checks. The devkit does not bundle the predictor or a universal plugin SDK, nor certify every arena.

For agent-assisted work, use the [llms.txt index](../../llms.txt) and [devkit agent instructions](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/AGENTS.md).

## Build our mods {#mod-sources}

These instructions are for developers, not players:

- [Predictor: C++ build and launch](https://github.com/Xaaalera/heroes5-deployment-preview#readme).
- [Bank reference: DLL and H5U build](https://github.com/Xaaalera/heroes5-bank-reference#readme).

Both repositories pin devkit as a submodule. Their READMEs contain dependencies, exact commands, disabling and validation limits. [Ready DLL packages](../players/mods.md) require no player development tools.

## Ordinary startup with DLLs {#dll-autoload}

The shared [devkit dinput8.dll source](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/mod_loader.cpp) initializes known DLLs under bin/Heroes5Mods and forwards DirectInput to Windows. There is no separate player EXE. Initialization failure cancels startup instead of continuing with only part of the mods.

For the test polygon and Start observation use `native-probe.py launch --map WorkshopPolygon --control --observe-deployment`. This instruments the ordinary game process for development, not player installation. Do not combine legacy --native-loader injection with DLL autoloading.
