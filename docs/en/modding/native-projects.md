---
content_type: how-to
status: draft
faction: academy
title: C++ mod architecture and extension
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/native-projects/
description: Required boundaries between the game, shared runtime, adapter and mod behavior; development, release and acceptance.
updated: '2026-10-09'
---
# C++ mod architecture and extension

This guide defines the required boundaries between our mods and xkit. It then covers standalone clones, DLL exports and test-file recovery. Start with the [xkit guide](devkit.md) for initial commands; players using a finished mod do not need these actions.

## Required architecture contract {#architecture-contract}

**Game behavior and UI belong to the mod. The development environment connects the mod through an adapter and does not define its behavior.** This contract applies when creating, extending or migrating mods. It states requirements; the text itself does not establish that current builds comply.

### Layer responsibilities

| Layer | Owns | Does not own |
|---|---|---|
| Game | World, battles, creatures, camera, native windows and engine rules | Mod development tools |
| [Game API](../reference/game-api.md) | Verified bindings to the supported game, game types and known hook sites | Predictor algorithm, bank-reference content or project management |
| Shared game loader/runtime | Mod connection, event delivery, safe callback invocation/retirement and the agreed state contract | Individual mod rules or UI |
| Individual mod adapter | Translating runtime events/data into mod calls, registering callbacks and transferring state/cleanup | A duplicate algorithm built for the SDK |
| Mod behavior and UI | Calculation, mod rules, models, cards, tooltips and state | Supervisor commands, build management and HMR mechanics |
| xkit tools | Projects, builds, file watching, developer commands, logs and packaging | A required service on a player's computer |

Runtime means code executing inside the game. An adapter is part of an individual mod's integration. The supervisor is the xkit process watching sources and managing development updates. These roles do not require a separate DLL for every table row: physical packaging can differ. Each mod still ships independently, with shared game dependencies listed in its package.

### Dependency direction

- The adapter depends on the public runtime contract and calls its mod's behavior. The shared runtime invokes registered callbacks through that contract.
- Mod behavior must not import its adapter, internal SDK types, runtime buffer layouts or development commands. Algorithm inputs have meaning in the mod's domain.
- Mod UI may use Game API and native game objects. Independence from xkit does not mean independence from the game itself.
- The shared runtime does not know predictor creature categories, placement formulas or army variants for a particular bank. These decisions remain in the mods.
- A shared library holds reusable bindings and mechanisms with an explicit purpose. Moving code there requires a real shared consumer; calling it “common” is insufficient.

**Predictor boundary example.** The runtime reports battle preparation. The adapter creates an allowed input and calls the existing predictor calculation. The predictor returns positions and UI data; the adapter connects necessary operations to the runtime lifecycle. Information disclosure policy is separate: research mode does not authorize hidden quantities, upgrades or the final neutral split in ordinary prediction.

| Allowed | Boundary violation |
|---|---|
| Adapter translates a game callback into mod input | Algorithm receives an internal SDK context and reads its buffers |
| Mod owns the reference-upgrade choice; adapter preserves it during reload | Upgrade choice exists only in the developer's Python process |
| Runtime safely invokes mod cleanup | Runtime has a special branch for Genie placement |
| Mod uses verified Game API bindings | Mod searches for xkit sources or workspace during play |
| New adapter invokes the previous algorithm and UI | SDK integration creates a simplified copy of the mod |

### Two operating modes

**Development through xkit:** mod sources → temporary DLL build → compatibility checks → safe version replacement in the test game. Developer tools and console help observe results. C++ still compiles; HMR automates building and connection.

**Finished mod for a player:** installed package → ordinary Heroes/Lobby startup → game loader/runtime → adapter → the same mod behavior. Separate xkit processes, Python/Node, sources, workspace and developer console are unnecessary. Resource mods ship their own H5U; native mods ship their own DLL; necessary shared game files are explicit.

Development and release use one behavior implementation. Connection and packaging may differ. Conditional compilation must not silently disable features in either mode. Copying an intermediate HMR DLL does not turn it into a finished player package.

### State, updates and cleanup

- The mod defines its state's meaning. The adapter transfers it through the agreed contract; runtime owns the provided storage lifetime. Transport types must not become the algorithm's data model.
- Contract and state-format compatibility are checked before replacement. Without established compatibility, reject the update with an understandable reason. Never silently reset state or reinterpret its meaning.
- A DLL must not unload while the game or another callback can invoke its functions. Retire callbacks through the agreed mechanism; release game objects and references on an allowed game thread.
- A rejected update should preserve the previous working version when state allows that to be established. This does not promise rollback of arbitrary game actions already performed.
- Loader, incompatible-state or resource changes may require a restart. Record its specific reason; ending a check or response does not justify closing the test game.

### Migration completion requirements

| Requirement | Necessary evidence |
|---|---|
| Source boundaries respected | Architecture review of dependencies and behavior ownership; violations block acceptance |
| Previous features retained | A pre-migration feature inventory and post-migration result for each feature, including UI and cleanup |
| Finished package correct | Checks of actual released files, DLL entry points, dependencies and installation paths |
| Development supports claimed HMR | Code, state, callback and rejection checks in one confirmed session |
| Player needs no development environment | Ordinary final-package startup without developer processes, sources or workshop paths, with mod behavior checked |
| Mods independent | Separate-package and coexistence checks; demand loading/stopping additionally tested when claimed |

Successful compilation, a module-list entry, static DLL validation and SDK operation establish different properties. None alone proves migration completion. The predictor's earlier accuracy campaigns do not transfer to a new build either: evidence must cover that build's calculation.

### Change control and current limits

Root, devkit and both mod AGENTS link to this contract. Architecture review must check dependency direction, absence of SDK implementation leakage and retained behavior. Changing the decision requires updating the contract and related acceptance criteria with a reason; bypassing it as a local implementation detail is unacceptable.

The development native packager already requires a [static player ZIP check](#player-package-check). It does not prove the absence of programmatically loaded dependencies or source-layer separation. Automatic checking of all dependencies between layers is not implemented; architecture review currently owns that check. Different packaging routes, including the bank reference, require their own acceptance. Full feature parity of the migrated predictor and ordinary startup of its new managed build remain unverified.

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

<span id="player-package-check"></span>

**Final DLL check during release.**

The development packager automatically checks DLL format, the entry point called by the loader, and normal/delayed dependencies before emitting a player ZIP. A missing-entry-point error may mean that a development payload was supplied instead of the finished mod. An undeclared-dependency error requires checking the build and package contents; installing the SDK on the player's computer is not a fix.

This check is not yet published. It does not launch the game or detect every dependency loaded programmatically. Ordinary final-package startup through Heroes/Lobby without developer processes, and verification that all features remain available, are separate readiness requirements.

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
