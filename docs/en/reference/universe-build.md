---
content_type: reference
status: draft
faction: haven
title: The investigated Universe build
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/universe-build/
description: The investigated Universe build
updated: '2026-09-24'
---
# The investigated Universe build

Universe changes resources, UI and executable behavior. An XDB edit does not establish DLL behavior, and the menu version does not identify all four binaries.

## Resource snapshot, September 21, 2026

All eight inspected data PAKs opened as ZIP. The comparison baseline was the local data, a2p1-data, texts and a2p1-texts archives, not an independently authenticated clean ToE installation.

| Archive | Resources | Changed | Added paths | Identical |
|---|---:|---:|---:|---:|
| `Universe_mod.pak` | 5159 | 1075 | 4047 | 37 |
| `universe_mod_texts_ru.pak` | 1771 | 605 | 942 | 224 |

The main archive contained 3767 UI, 787 GameMechanics, 185 MapObjects and 61 RMG resources. These count files, not features.

Definition examples: `Academy/Rakshasa_Rukh.xdb` DefenceSkill 20→25 and Health 140→145; `Dungeon/Assassin.xdb` WeeklyGrowth 7→8; `Dungeon/Blood_Witch.xdb` 5→6. These are file values, not universal final battle stats.

## Exact native baseline

`UI/MainMenu2/Version.txt` says `HoMM V version 3.1 + Universe mod 2.0`; a uni.dll string checks PAK version 1.8. The string may be stale. Native observations use these hashes:

| File | SHA-256 |
|---|---|
| `H5_Game.exe` | `88c9dc6107b9bced0649924a86360f1c56397ee00de0413f6f2b08f865ed5519` |
| `uni.dll` | `aa5211151d9e9a8c135e180ff8832908d128ccae08a5145162bcdae4946c18ee` |
| `um.dll` | `1956c00b371d22a3e1a644394ff3e7159b6ec36d660d5ffa36628fcf63fd0fc6` |
| `d3d9.dll` | `5eb152357f99d53397b764384d5cf9a0f6aece733ced30a34186ac57fb15be25` |

All are x86 PE, machine 0x14c. The inspected EXE ImageBase is `0x400000`; function addresses in these articles are absolute virtual addresses, not file offsets. EXE equality does not establish resource/profile/runtime-patch equality. From your game directory:

```powershell
Get-FileHash -Algorithm SHA256 .\bin\H5_Game.exe
```

## Limits of string evidence

UniverseTrigger and event names such as UNIVERSE_COMBAT_STARTED and UNIVERSE_WORLD_READY_AFTER_LOAD appear in the binary. Names alone do not prove callable signatures or availability in a Lua context. Proxy indicators in d3d9.dll do not make replacement with an arbitrary loader compatible.

The main archive's RMG/MapScript.lua contained only a comment header; Universe is not explained by Lua scripts alone.

**Evidence:** local ZIP catalogs, byte comparisons, PE headers/strings and binary hashes, September 21–23,2026. Recheck later builds. [Archive inspection](formats.md) · [Native UI](../modding/native-ui.md).
