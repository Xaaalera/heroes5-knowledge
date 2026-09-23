---
faction: fortress
title: Installing and removing a mod
lang: en
section: players
kicker: PLAYERS · MODIFICATIONS
translation: players/installing-mods/
description: Distinguish archives, scripts, and native mods before installation.
updated: 2026-09-23
---
# Installing and removing a mod

Different mods use different installation methods. The author's instructions for your version determine file locations and whether a separate launcher is required.

## Check the package contents

| Package contents | What to establish |
|---|---|
| `.h5u` or `.pak` | Destination, version requirements, and resource conflicts |
| `.lua` files | Where scripts load and which game context runs them |
| `.dll` and a launcher | Compatible executable and launch procedure |

A file extension does not establish compatibility. See the [format reference](../reference/formats.md).

## Follow the installation instructions

1. Close the game.
2. Record the files being added or replaced.
3. Back up files being replaced.
4. Follow the author's instructions and run the verification scenario.

Do not infer archive precedence solely from filenames. When two mods change one resource, verify the ordering and result on the specific build.

## If the result is wrong

Restore original files or remove only the files added by that mod. Repeat the scenario without the change. Comparing before, after, and after rollback helps separate mod problems from game state.

A useful bug report includes the game version, mod list, reproduction steps, and a screenshot. Do not attach the entire game installation.
