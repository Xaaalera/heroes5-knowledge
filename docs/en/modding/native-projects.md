---
content_type: how-to
status: draft
faction: academy
title: Extend a C++ plugin and recover test files
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/native-projects/
description: Additional DLL exports and recovery of the bank adapter's test files in xkit.
updated: '2026-10-08'
---
# Extend a C++ plugin and recover test files

For developers with a working [first xkit C++ project](devkit.md), this guide covers an additional exported function and the separate case of bank-adapter file recovery after failed installation. Players using a released mod do not need these actions.

## Connect dependencies in a standalone clone

For a separate clone of our bank reference or predictor repository, open PowerShell in that clone's directory. In the shared workshop, use its `sync-subrepos` instead of this manual procedure.

Read the selected branch's `.gitmodules` first. The procedure below applies when both `devkit` and `game-api` are declared. The older published predictor branch currently declares only `devkit`: use `git submodule update --init devkit`, then follow its pinned SDK version's rules. Do not pass Git an undeclared submodule name or add a dependency solely to follow this guide.

```text
git submodule update --init devkit game-api
git -C devkit rev-parse HEAD:game-api
git -C game-api rev-parse HEAD
```

The last two commands show the Game API commit expected by the SDK and the actual checkout commit. They must match. If they differ, choose compatible pinned versions after review; do not update a dependency to main automatically.

`devkit/game-api` must reference the root `game-api` checkout. If it already contains files or is a link, do not replace it this way: establish its provenance first. Only an empty directory left by Git for an uninitialized submodule may be removed with `Remove-Item -LiteralPath devkit/game-api`. Then create the link:

```powershell
New-Item -ItemType Junction -Path devkit/game-api -Target (Resolve-Path game-api).Path
```

A junction exposes the same physical library checkout at another path. Do not initialize a nested Game API submodule, which would create another checkout. This preparation links sources; it does not prove modified-code HMR compatibility or player-release readiness.

## Add an exported function

An export is a function name available to another DLL module. It is not a new in-game console command: calling code must know the arguments, return value and calling convention. These agreements form the ABI; breaking them can crash the game even when compilation succeeds.

1. Add the function to your project's `plugins/project-name` sources. Preserve the mandatory xkit contract functions.
2. Create one `.def` file in that source tree, such as `exports.def`. Multiple definition files for one DLL are refused.
3. List the required names under `EXPORTS`. They must match functions actually included in the build. Account for C++ name decoration; a plain name typically uses `extern "C"` or maps to an internal symbol name. See [Microsoft EXPORTS](https://learn.microsoft.com/en-us/cpp/build/reference/exports?view=msvc-170) for syntax and symbol discovery.
4. Save the files while `xkit start project-name` is running. Wait for successful build and application. Adding or editing `.def` is watched; changing only export definitions relinks cached object files.
5. Check the function with an ABI-compatible consumer. An exported name alone does not prove correct invocation. A new export does not automatically register a console command.
6. Stop with Ctrl+C and run `xkit release project-name`. Release uses the same `.def`. Inspect the DLL from that package, for example with `dumpbin /exports DLL_PATH` in a Visual Studio Build Tools terminal.

Replace `project-name` and `DLL_PATH` with your project name and the DLL path from its extracted release. Compilation or linking failure does not mean the change was applied. Do not retain function pointers from an unloaded version; see [Game API](../reference/game-api.md) for callback removal and state transfer.

Startup bootstrap and graphics facade changes take effect at the next process launch. Use supported core or plugin contracts for development changes. Moving an older DLL into a project directory does not automatically make it HMR-compatible.

## Recover bank-adapter files

This section concerns the development adapter that temporarily installs the bank DLL and H5U into its owned test game. Before writing, xkit retains previous files and a `recovery.json` manifest. This is not a command for removing arbitrary mods from your main installation.

1. After failed installation or cleanup, retain the `recovery.json` path from the SDK journal. `xkit diagnostics` locates that journal; a recovery error also includes the manifest path.
2. Close the owned test game and confirm its process has exited. Do not move the test installation or workspace during recovery.
3. In a terminal using the same workspace configuration, run:

```text
xkit sdk recover-bank "MANIFEST_PATH"
```

Replace the placeholder with the full path to the saved `recovery.json`. Do not construct it manually or substitute a manifest from another workspace.

The command validates workspace identity, allowed destinations and file hashes. External changes or corrupted backups cause refusal. Preserve the material and read the error; do not delete backups to bypass it.

On success, xkit restores previous files, removes consumed backups and the manifest, then reports completion. A lease file left after process exit does not establish an active operation: the OS releases the lock.

## Verification limits

The procedure was checked against the [plugin builder](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/plugin-watch.py), [CLI](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/xalkit.py) and [runtime recovery](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/xalkit_runtime.py). It documents supported routes, not arbitrary ABI changes or recovery of relocated test copies.
