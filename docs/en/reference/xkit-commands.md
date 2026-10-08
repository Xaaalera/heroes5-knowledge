---
content_type: reference
status: draft
faction: academy
title: xkit commands
lang: en
section: reference
kicker: SDK REFERENCE
translation: reference/xkit-commands/
description: Development and game-console commands, parameters, examples and execution conditions.
updated: 2026-10-08
---
# xkit commands

Windows terminal commands start with `xkit`. In the [in-game console](../modding/console.md), omit `xkit game` from game commands: use `heroes` instead of `xkit game heroes`.

Open a second terminal while the first runs `xkit start`. Help is available through `xkit --help`, `xkit game --help` and `xkit game army --help`. In game, use `help` and `help army`.

## Development and release

| Terminal command | Purpose |
|---|---|
| `xkit setup` | Select the installed game and project workspace |
| `xkit new demo --resources` | Create a resource mod |
| `xkit new demo-native` | Create a native C++ plugin |
| `xkit start demo` | Start the test game and development session |
| `xkit start demo --map WorkshopPolygon` | Start a session with the named test map |
| `xkit build demo` | Build a project; resource mods produce H5U |
| `xkit release demo` | Release a player package; resource ZIPs retain a separate H5U |
| `xkit diagnostics` | Read current session diagnostics |
| `xkit doctor` | Check the development environment |
| `xkit language ru` / `xkit language en` | Select the message language |
| `xkit check --console` | Check seven console scenarios in the test game |
| `xkit check --player` | Check player delivery in the test game |

Omit the project name from `build`, `release` or `start` when a project is already selected. A `start` session keeps running; Ctrl+C stops it and closes its own test game. See the [SDK guide](../modding/devkit.md) for installation and your first project.

Before `xkit check`, stop the current session with Ctrl+C and close other game/editor windows: the check starts its own test game. Run `--console` and `--player` separately.

## Game commands

Enter these commands in the game console. Add `xkit game` before each one in the terminal. Uppercase words such as `HERO`, `CREATURE` and `NAME` are placeholders for your values, not text to copy.

| Syntax | Action and conditions |
|---|---|
| `status` | Check the connection to the current test game; does not establish map readiness |
| `heroes` | Read hero names on the loaded adventure map |
| `army HERO CREATURE` | Read the hero's total creatures of one type |
| `army HERO CREATURE --count N` | Set the final total, from 0 to 1,000,000 |
| `level HERO TARGET` | Raise a hero to level 1–40; does not lower levels |
| `resource PLAYER KIND` | Read a participating player's resource; player number 1–8 |
| `resource PLAYER KIND --amount N` | Set the final amount, from 0 to 100,000,000 |
| `teleport HERO X Y [--floor N]` | Move a hero to map coordinates; floor defaults to 0 |
| `interact HERO TARGET` | Send a hero to the object with the specified game name |
| `map NAME` | Request a map from the test game's Maps folder |
| `restart NAME` | Reload the explicitly named map |
| `menu` | Request the main menu |
| `screenshot` | Save a fresh frame and print its PNG path |
| `trace [--level LEVEL] [--after N] [--limit N]` | Read records from the shared diagnostic bus |

Tab helps choose heroes, maps and creature constants such as `CREATURE_ARCHER`. Use a hero name returned by `heroes` and an object name from your test-map data. Quote names containing spaces.

For armies, `--count 100` sets the **total to 100**, rather than adding another 100. Seven occupied slots may prevent adding a new creature type. The level command handles available level-up dialogs automatically; its public interface currently provides no skill-choice parameter.

## Hero examples

If `heroes` returns `Brem`, you can enter:

```text
army Brem CREATURE_ARCHER
army Brem CREATURE_ARCHER --count 100
level Brem 20
```

The first command reads the army; the next two change the test game. Terminal example: `xkit game level Brem 20`. `hero-level` is not registered, and `army` does not accept a count as a third positional argument.

## Resource numbers

| KIND | Resource |
|---|---|
| 0 | Wood |
| 1 | Ore |
| 2 | Mercury |
| 3 | Crystals |
| 4 | Sulfur |
| 5 | Gems |
| 6 | Gold |

For example, `resource 1 6 --amount 5000` sets player 1's gold to 5000. Values were checked against shipped game scripts. Preview.5 help swaps the crystal and sulfur labels; this table has the correct order, and the label fix is prepared in SDK source.

## Map loading and the journal

`restart` requires a name: `restart WorkshopPolygon`. It does not infer the current map. After `map` or `restart`, wait for the map to appear in game, then check `heroes`. A dispatched command and `status` establish a connection; wait for the visible map and available roster before army or level changes.

`trace` defaults to level `info`, journal start `--after 0`, and a limit of 16 records. Levels are `debug`, `info`, `warning` and `error`; the limit is 1–64. Use `--after` to continue from the position in a previous reply. Additional `--console` requests output in the stock game console too; visibility of that output has not been independently verified.

Local `clear` clears the internal xkit console output, not the journal file. `--json` provides structured output in the terminal, for example `xkit game heroes --json`. The in-game console retains its human-readable reply.

### Install the example map

Normal preparation of a new project does not create WorkshopPolygon. First start and stop a test session to prepare its game copy. Download [WorkshopPolygon.h5m](../../assets/WorkshopPolygon.h5m) and copy it without extraction into `.local/test-game/Maps` inside the selected xkit workspace. Back up an existing copy first. Then use `xkit start demo --map WorkshopPolygon` or `map WorkshopPolygon` in an open session. See the [test-map article](../modding/test-maps.md) for its contents and release limitations.

## SDK maintenance

These commands serve tool authors and the workspace. Players using a ready mod do not need them.

| Group | Purpose |
|---|---|
| `xkit storage status` | Show test-file storage state |
| `xkit storage clean` | Clean obsolete SDK-owned data under its retention rules |
| `xkit storage restore --help` | Explain saved-state restoration |
| `xkit storage restore-dump --help` | Explain archived dump extraction |
| `xkit sdk build` | Build ready runtime files from SDK source |
| `xkit sdk release` | Build the complete SDK archive for mod authors |
| `xkit sdk recover-bank --help` | Explain recovery of an interrupted bank-reference test session |

Read `--help` before file-changing actions. A successful request does not replace a result check. If an action may already have run, inspect state before deciding to submit it again.

## Sources and scope

Game commands and parameters were checked against the [SDK CLI](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/scripts/xalkit.py), [game-command backend](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/scripts/game_control.py) and [console help](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/scripts/sdk_console_commands.py). The [research diary](research-diary.md) records interface checks and live-test limits. This reference does not promise every command works during combat or map loading.
