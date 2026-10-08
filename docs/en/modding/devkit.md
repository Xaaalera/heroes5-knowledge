---
content_type: how-to
status: draft
faction: fortress
title: Start developing with xkit
lang: en
section: modding
kicker: MOD SDK
translation: modding/devkit/
description: Install xkit, create a first mod, test it and release a player package.
updated: 2026-10-08
---
# Start developing with xkit

xkit is our toolkit for Heroes V Universe mod development. It prepares a test game, builds mods and helps check results. Playing with a ready mod needs no xkit, Python or compiler: start with the [mod catalogue](../players/mods.md). This guide is for mod authors.

## Prerequisites

- Windows 10/11 and Heroes V: Tribes of the East with Universe installed.
- 64-bit Python 3.10+ and [uv](https://docs.astral.sh/uv/getting-started/installation/) to install the command.
- A workspace outside the installed game for projects, the test game and journals.
- For C++ plugins, Visual Studio Build Tools with C++ tools and CMake. Install C++ CMake tools for Windows, or make CMake available on PATH. The resource example below needs no compiler: ready files accompany the SDK.

Native functions were checked on the [pinned Universe build](../reference/universe-build.md). Close the game and editor before first preparation.

## Install the command

1. Download `xkit-sdk.zip` from [preview.5](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.5).
2. Extract it into a permanent folder. Open a terminal inside the extracted xkit folder.
3. Run:

```text
uv tool install --editable .
uv tool update-shell
```

4. Open a new terminal and check `xkit --help`. You should see the command list.

This method requires `--editable`: the command uses the extracted source and neighboring ready runtime folder. Keep the SDK directory. If the command is missing, first open a new terminal; `xkit doctor` checks the environment.

## Select the game and workspace

```text
xkit setup
```

Select the installed game and a separate workspace. The game directory contains bin and data, with the executable inside bin. xkit saves the selection; each terminal does not need another setup. Development runs in a test copy, with the installation supplying files.

## First project: a menu marker

```text
xkit new demo --resources
```

The workspace now contains mods/demo. mod.json defines the recipe; files holds additional resources. The starter adds `[xkit: demo]` to the main-menu version label.

Start the test game:

```text
xkit start demo
```

On first use, xkit prepares the test game and deploys the mod. Wait for readiness and check the menu marker: this is the H5U's visible result. The original game archive is not edited.

This terminal stays occupied by the session. Open a second for [game commands](../reference/xkit-commands.md), or use the [in-game console](console.md). To stop, press Ctrl+C in the first terminal and wait for its test game to close.

## Release a mod

After stopping the session:

```text
xkit build demo
xkit release demo
```

`build` creates a separate H5U. `release` retains it and creates a player ZIP with the H5U, shared graphics DLL, notices and bilingual README.txt. It prints the output path; adjacent build.json is a developer report, not a game requirement.

<span id="dll-autoload"></span>

Players follow README.txt: on first installation retain the original graphics DLL, then copy the package bin and UserMODs folders. The mod connects during ordinary Heroes/Lobby startup. Keep shared DLLs while other mods need them. The separate H5U suits an already installed compatible graphics chain.

## Develop a C++ plugin

```text
xkit new demo-native
xkit start demo-native
```

Open `plugins/demo-native/plugin.cpp` in the workspace. Find `DisplayValue = 42` in the starter, change 42 to 77 and save. xkit builds an intermediate DLL and applies the edit in the same game. Wait for “Plugin updated”. In `.local/xalkit/logs/events.jsonl`, the new `applied` record should contain `observation.result` equal to 77; a failed build has no successful application record. This checks the starter function's result, not changes to game rules.

This is hot reload, or HMR. C++ still compiles; you do not move intermediate DLLs manually.

Added functions/core exports, state retention, old callback teardown and rollback on refusal were checked. Startup loaders and the graphics DLL update on the next game launch; put new functionality in the core or a separate plugin. Moving an existing predictor/reference folder alone does not migrate it to HMR.

Stop with Ctrl+C. `xkit release demo-native` creates a separate DLL package from the project's source. Each mod ships independently with its required shared files.

## Check the result and diagnose failures

| Symptom | Next step |
|---|---|
| xkit is missing | Open a new terminal after updating the environment; check `xkit --help` |
| Runtime files or translations are missing | Check the complete archive and installation with `--editable` |
| C++ build fails | Check Build Tools and compiler messages; refusal does not mean an edit was applied |
| Game does not reach readiness | Read launch messages and run `xkit diagnostics` in a second terminal |
| New behavior is absent | Inspect build/application messages, then the visible result |

Do not blindly repeat an action that may have run. Check state and the journal. See the [command reference](../reference/xkit-commands.md) for parameters and the [console guide](console.md) for in-game work.

## Verification and further reading

<span id="mod-sources"></span>

Project source: [SDK](https://github.com/Xaaalera/heroes5-mod-devkit), [Game API](https://github.com/Xaaalera/heroes5-game-api), [deployment predictor](https://github.com/Xaaalera/heroes5-deployment-preview) and [bank reference](https://github.com/Xaaalera/heroes5-bank-reference). Each repository can stand alone; shared documentation stays on this site.

Prepared preview.5 was installed outside the source checkout. Its short CLI released a resource ZIP without a compiler; the exact ZIP displayed its menu marker and exited normally. This checks the shared graphics dependency, not multiplayer or every installation variant.

- [Research diary](../reference/research-diary.md): observations and limits.
- [Resource overrides](resource-overrides.md): game resource selection.
- [Test maps](test-maps.md): repeatable experiments.
- [SDK source](https://github.com/Xaaalera/heroes5-mod-devkit): code and releases; this site holds the primary guides.
