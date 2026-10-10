---
content_type: reference
status: draft
faction: academy
title: Game API for C++ plugins
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/game-api/
description: Shared game bindings, build checks and callback lifetime rules.
updated: '2026-10-10'
---
# Game API for C++ plugins

Game API is the shared C++ library used by our mods and xkit. It holds supported-build checks and known game integration points. Use it instead of copying bindings from another plugin. For your first project, start with the [xkit guide](../modding/devkit.md).

## Connect the library

You need Windows 10/11, MSVC targeting x86, C++20 and CMake 3.21+. The game and its DLLs remain 32-bit. The library supports the [studied Universe build](universe-build.md); matching an EXE name is insufficient.

Place the [Game API sources](https://github.com/Xaaalera/heroes5-game-api) in your CMake project's `game-api` dependency directory. In the workshop, use the existing canonical dependency. Add these lines after declaring your `my_plugin` target:

```cmake
add_subdirectory(game-api)
target_link_libraries(my_plugin PRIVATE heroes5_game_api)
```

This is a header library, with no separate Game API DLL. Its CMake target provides `include`, C++20 and the Windows `bcrypt` library for hash checks. These lines do not install game hooks or make an older plugin compatible with HMR.

## Available building blocks

| Header | Purpose | Calling code must |
|---|---|---|
| `h5/build.hpp` | `VerifyGame`: check supported installation binary names and SHA-256 hashes | Check before using bindings; stop on refusal |
| `h5/process.hpp` | `OpenOwnedProcess`: open the specific process from your launch and verify creation time, path and build | Supply your launch provenance; close a successful handle with `CloseHandle` |
| `h5/hooks.hpp` | Named integration points for bank army selection, placement rendering, attack entry, hovering, scripts and exit | Verify the signature and calling contract; the catalog does not install a hook |
| `h5/actor_input.hpp` *(local research version; not published yet)* | Army-input records; `ReadActorRunicInputs` reads individual rune states, `ReadCombatRosterCount` reads the actual unit-list size | Matching live callback only; hidden inputs require explicit research mode. Runic scoring belongs to the mod; post-Start results serve verification |
| `h5/console.hpp` | `DispatchConsoleCommand` and `DispatchGameText`: dispatch a stock command, event or adventure script | Call on your game's window thread; verify the action's effect separately |
| `h5/script_observers.hpp` | Shared subscriptions to the game's script dispatcher | Remove your callback before unloading or replacing its DLL |
| `h5/camera_input.hpp` | Subscriptions to suppress camera input over a panel | Change subscriptions on the validated game thread; preserve map control outside the panel |
| `h5/adventure_input.hpp` | Isolate verified key presses while the console has focus | Preserve original handling when hidden; this does not capture every input kind |
| `h5/graphics_lifetime.hpp` | Repair the graphics wrapper lifetime in process memory | Startup only, before graphics initialization, with all owned child threads stopped; never continue startup after refusal |
| `h5/image_placement.hpp` | Validate a loaded DLL's file and placement without memory changes | Stop your loader at its DLL-load event and retain the original file handle |

`OpenOwnedProcess` neither discovers games automatically nor authorizes attachment to another person's process. On refusal, it closes the handle it opened. Build checks do not modify game files.

## Dispatch an event or script

`DispatchGameText` takes the existing `ConsoleCommandRequest` and a request kind:

| Kind | Accepted text |
|---|---|
| 1: named event | ASCII letters, digits and underscore; up to 127 characters |
| 2: adventure script | Printable ASCII characters; up to 4095 characters |

Kind 0 belongs to the separate `DispatchConsoleCommand`, which accepts a wide string. Empty text, incorrect request size or version, unknown kinds and calls from another thread are refused. The game's window thread constructs and releases the string using the game's own facilities.

Successful dispatch does not prove that the action happened. After a screenshot, verify a new file; after an army change, read its state. For supported actions, use [xkit commands](xkit-commands.md) rather than constructing a script unnecessarily.

## Subscribe and safely update a DLL

The script dispatcher supports up to 64 subscribers. `FindScriptObservers` validates the known shared dispatcher contract; `AddScriptObserver` and `RemoveScriptObserver` add and remove individual callbacks. Creating the shared handler and publishing the interception require the original signature to be checked; preparing storage alone does not install an interception.

Registration, removal and invocation run on the same validated game thread. A callback follows `cdecl void()`: it returns normally, does not re-enter the same runtime and does not retain pointers to temporary payload or plugin state.

When replacing a plugin:

1. Stop new calls and wait for current calls to finish.
2. Confirm removal of every callback from the old DLL.
3. Transfer the state specified by its contract.
4. Load the new DLL, restore state and register new callbacks.

The shared handler remains in the process until game exit; with no subscribers it calls the original function. Stopping one plugin must not remove another's subscriptions. This is a trusted in-process contract, not protection against other code already able to modify game memory.

## Graphics chain: loader use only

`VerifyGraphicsFiles` accepts the original Universe graphics library by default. For the SDK chain, calling code explicitly supplies the trusted facade SHA-256 from its verified build; the unchanged original must remain at `d3d9.universe.dll`. An unrelated hash file in the game directory does not establish trust.

`VerifyOwnedImagePlacement` checks a DLL's file and mapping before use. The loader retains the file handle from its load event: verification hashes that open file, rather than reopening a path. This function does not continue the load event, transfer handle ownership or modify process memory.

`RepairOwnedGraphicsProxyLifetime` modifies executable process memory so the device wrapper remains alive while references remain. At zero references, its original release behavior is retained. Game files are unchanged. The repair is restricted to the supported build, before graphics initialization and with all owned child threads stopped; it is not for HMR or an active map.

Writes and rollback verify bytes, page protection and image ownership. On refusal, startup must not continue, including after an attempted rollback. The SDK facade's internal route is likewise restricted to first initialization of the verified original DLL, before graphics objects are created and the factory reaches the game. Transaction tests with substituted memory operations do not replace live loader verification.

## Verification limits

For native tests, open a terminal in a separate Game API checkout with MSVC configured and run:

```text
cmake -S . -B .local/build -A Win32
cmake --build .local/build --config Release
ctest --test-dir .local/build -C Release --output-on-failure
```

These commands build the library test rather than launch the game. If the CMake generator does not support `-A Win32`, select an installed Visual Studio generator. Do not mix x64 and x86 in one build directory. Repository structure is checked separately with `python -X utf8 scripts/docs-check.py --structure-only`; that mode does not check whether code changes update the article.

Named integration points were extracted from existing mods and the SDK. Catalog inclusion is not a new live check of every hook. Thread affinity, calling convention, register preservation and callback lifetime remain part of the consumer's contract.

Native library checks cover hashes, wrong-build and process refusals, shared subscriptions, computational state preservation and specific graphics/input checks. Retained live SDK experiments exercised two subscribers, core and plugin replacement, rollback and independent removal. Results belong to particular sources and scenarios; they do not certify every map, every input kind or multiplayer.

Before adding a binding, confirm its signature, calling contract, thread and lifetime, then retain a reproducible test with its verification limits. Label unverified hypotheses explicitly. Numeric bindings belong in the [library sources](https://github.com/Xaaalera/heroes5-game-api/tree/main/include/h5); human descriptions use meaningful names and purposes.
