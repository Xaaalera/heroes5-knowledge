---
faction: dungeon
title: Verifying a change
lang: en
section: modding
kicker: MOD CREATORS · METHOD
translation: modding/verification/
description: Build identity, scenario, observation, and limits of a conclusion.
updated: 2026-09-23
---
# Verifying a change

A successful build proves the tool produced its output. Mod behavior needs a separate check in the game.

## Identify the build

Record game and mod versions. For native research, include the executable's SHA-256. In PowerShell, from the game directory:

```powershell
Get-FileHash -Algorithm SHA256 .\bin\H5_Game.exe
```

This path is an example for an installation with that layout; check your actual executable location.

## Choose a short scenario

Specify initial state, action, and expected result. “I played and it seemed fine” is useful feedback, but hard for someone else to reproduce.

Also test leaving the state: close and reopen the window, enter another battle, or restore original settings, as appropriate.

## Distinguish evidence types

| Check | What it establishes |
|---|---|
| Build and static validation | Output files meet the checked conditions |
| Automated test | A particular scenario passed in a specified environment |
| In-game observation | A recorded result appeared on screen |
| Physical mouse test | Behavior with actual user input |

A programmatically posted mouse message and a physical click are different verification methods. Do not present one as the other.

## State the limits

Explain what was checked and what remains unknown. A conclusion based on one creature type or one arena should say so. Later observations may refine earlier conclusions.
