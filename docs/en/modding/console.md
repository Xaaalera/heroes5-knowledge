---
content_type: how-to
status: draft
faction: academy
title: The xkit console in game
lang: en
section: modding
kicker: MOD DEVELOPMENT
translation: modding/console/
description: Open the xkit console, run a command, get suggestions and inspect the test game journal.
updated: 2026-10-08
---
# The xkit console in game

The console lets you control the test game, read command replies and inspect connected modules inside the Heroes V window. It is available in a development session started by xkit. A ready player mod does not require this console.

## Open the console

1. [Install xkit and create a project](devkit.md).
2. Start the test game with `xkit start project-name` in your Windows terminal.
3. Wait for game readiness and the SDK connection.
4. Click **Logs** near the upper-right of the game window. Choose **Commands** to enter a command.

If the button is absent, check that the game was started through `xkit start` and read that terminal's messages. An ordinary launch of an installed player mod does not create a development session.

## Run your first command

Enter this in the bottom field:

```text
help
```

Press **Ctrl+Enter** or click **Run**. The reply appears above the input field. Plain Enter inserts a line in the command editor.

`help` lists commands; `help army` shows help for one command. Selecting a suggestion or history entry fills the editor; you submit the command yourself.

Use a short command such as `heroes` inside the console. Its Windows terminal equivalent is `xkit game heroes`: open a second terminal while the first runs `xkit start`. The roster belongs to the current loaded map; use a name from that reply for hero commands.

## Suggestions, history and panel controls

| Action | How |
|---|---|
| Open completion choices | Press Tab or click the suggestions button |
| Restore an older command | Press Up or select a history entry |
| Move to a newer entry | Press Down |
| Clear command output | Run `clear` |
| Resize the panel | Drag an edge or corner |
| Hide the panel and continue playing | Click **Return to game** |

Tab suggests commands, parameters, maps, heroes and creature constants. Hero suggestions refresh from the test game and may take a moment while a map loads. Hiding the panel retains output and history. Click Logs to reopen it.

## Find the cause of an error

On **Logs**, select a message level and filter by part of the text. INFO shows ordinary events, WARNING warnings, ERROR failures and DEBUG additional details. Filtering changes visible rows; the complete journal stays in its file.

**Modules** helps inspect connection state. Commands sent from the terminal also appear in the shared session journal.

If a command does not complete successfully, read the reply and check `help command-name`. Run `xkit diagnostics` in the second terminal for diagnostics.

After `map` or `restart`, wait until the adventure map appears in the game window. Then request `heroes`: a successful reply shows that the hero roster is available. Until then, avoid army or level changes. A dispatched loading request and a `status` reply establish a connection, not map readiness. Do not blindly repeat an action with an uncertain outcome.

## Locate diagnostic files

Run `xkit diagnostics` in the terminal: it does not launch a game and shows paths to development journals, the latest SDK check and crash monitor. `xkit diagnostics --json` returns paths for scripts and IDEs. Older reports apply to their recorded sources; file existence does not establish a healthy current session.

Crash monitoring is optional. Download [Microsoft ProcDump](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump), extract `procdump.exe` and place it at the location shown by `xkit diagnostics`. On the next `xkit start` or `xkit check`, the SDK verifies the Microsoft signature and connects the monitor to its owned test game. Discovering an EXE does not mean its signature has already been checked. After a crash, request diagnostics again: a successful monitor exit does not cancel a game failure.

After a failed launch, xkit also attempts to retain a matching Windows Application Error event using the process identity, creation time and game path. Windows logging can be delayed or unavailable; no matching event does not prove that no crash occurred. Its module and timestamp are shown separately from the original session failure; they do not establish the crash cause by themselves.

## Control disk usage

| Terminal command | Purpose |
|---|---|
| `xkit storage status` | Show prepared installations and the shared cache |
| `xkit storage clean --keep 3` | Keep up to three installations, snapshot retired copies and share identical large resources |
| `xkit storage restore ARCHIVE` | Restore an installation from its saved `retired-game.zip` and shared cache |
| `xkit storage restore-dump FILE.dmp.gz` | Extract an archived dump for an external debugger |

Close the game and editor before cleanup. Replace `ARCHIVE` and `FILE.dmp.gz` with your file paths. `--keep` accepts 0 through 3; if the limit is occupied, free a slot before restoration. Do not manually remove the shared cache: saved snapshots reference its resources.

To find `ARCHIVE`, open `.local/test-state` in the retired test installation's workspace: the current snapshot is `retired-game.zip`, with older snapshots named `retired-game-….zip`. If you do not know that workspace, run `xkit diagnostics`, open its printed event journal and find `storage_cleaned`: `result.retired` lists `game` and `archive` pairs, with `archive` holding the full snapshot path. The brief cleanup reply and `storage status` do not list those paths.

Large immutable test resources use [NTFS hard links](https://learn.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions) into a separate cache, never into the installed game. Mutable files remain independent. Explorer's summed directory sizes can count shared bytes more than once.

Cleanup validates SDK ownership, build and path boundaries; unknown directories are not deleted. It verifies a snapshot before retiring a test copy. The two newest dumps remain uncompressed; older dumps are compressed without losing bytes and checked by hash. Journals and reports retain context. These commands manage test files; they are not commands inside the game.

## Verified scope

This guide describes xkit preview.5 on the supported Universe test build. Seven interface scenarios were checked; separate live controls verified Ctrl+Enter, history, Tab, resizing and separation of log scrolling from camera zoom. These checks do not cover every keyboard combination on every map.

Behavior was checked against the [console interface](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/native/console_module.cpp) and [command broker](https://github.com/Xaaalera/heroes5-mod-devkit/blob/v0.1.1-preview.5/scripts/sdk_console.py). The [research diary](../reference/research-diary.md) retains verification history.
