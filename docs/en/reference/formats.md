---
content_type: reference
status: draft
faction: necropolis
title: Heroes V archives, XDB and encodings
lang: en
section: reference
kicker: HEROES V · UNIVERSE
translation: reference/formats/
description: Heroes V archives, XDB and encodings
updated: '2026-09-24'
---
# Heroes V archives, XDB and encodings

**PAK, H5U and H5M in the inspected installation can be read as ZIP.** An override must preserve the internal resource path: `UI/MainMenu2/Version.txt` for the version text. An extra enclosing directory changes that path.

| Format | Observed behavior | Check |
|---|---|---|
| PAK | All eight local data archives opened as ZIP | Member paths, timestamps, sizes and bytes |
| H5U | A separate UserMODs ZIP overrode version text; rollback removed the marker | Before/install/remove with restarts |
| H5M | Test map ZIP contains map.xdb, terrain and script resources | Members and references; test loading separately |
| XDB/XML | XML definitions for creatures, objects and UI | XML parsing establishes syntax, not valid game links |
| TXT | Investigated UI text uses UTF-16LE with BOM | Inspect original bytes and decoding |
| Lua | Inspected combat-startup.lua handled as UTF-8 | Test the correct game context |
| DLL | Executable x86 code | PE/exports/calls; placing a DLL in H5U does not load it |

## Read a resource without extracting the game

Python 3, from the game directory; no installation or writes:

```python
from zipfile import ZipFile

with ZipFile('data/Universe_mod.pak') as archive:
    name = 'UI/MainMenu2/Version.txt'
    member = archive.getinfo(name)
    raw = archive.read(name)
    print(member.date_time, len(raw), raw[:2].hex())
    print(raw.decode('utf-16'))
```

This checked text starts with `fffe`. Do not apply this decoder to all members: XML has its declaration/BOM, and binary resources remain bytes.

## Create an archive comparison report

Use `inspect_universe.py` from the [xkit source repository](https://github.com/Xaaalera/heroes5-mod-devkit) for a full comparison. It requires Python 3.10+ and the studied installed build, with no extra Python packages. It reads the game and writes results to a separate research directory.

In PowerShell, from the xkit source directory, set your two paths:

```powershell
$env:H5_GAME_DIR = (Resolve-Path '../HeroesV').Path
$env:H5_WORKSPACE = Join-Path (Get-Location).Path '../HeroesV-research'
New-Item -ItemType Directory -Force -Path $env:H5_WORKSPACE
python -X utf8 inspect_universe.py
```

Replace the examples with your game and a separate research directory. The tool expects the baseline `data.pak`, `a2p1-data.pak`, `texts.pak`, `a2p1-texts.pak`, plus `Universe_mod.pak` and `universe_mod_texts_ru.pak`. Another installation may require changes to the tool.

| File in the research directory | Contents |
|---|---|
| `research/inventory.json` | Resource counts, file types, game DLL/EXE SHA-256 hashes and report status |
| `research/archive-diff.csv` | Universe resources classified as added, changed or identical to the selected baseline |
| `research/unpacked/` | Universe XDB, XML, Lua and TXT plus matching baseline files, normalized to UTF-8 |

The JSON starts with `status: incomplete`; only a finished analysis writes `complete`. After an error, do not treat the CSV or extraction as a complete snapshot. Fix the reported cause and rerun. Do not run two analyses into the same directory concurrently. Previous extracted files are not removed: choose a new research directory for another build. These copies are for reading, not installing in the game.

## Relative XDB links

`href="../Textures/icon.xdb#xpointer(/Texture)"` combines a resource path with an XML pointer. Moving the containing definition can change its target. Clone processing must resolve links against the original directory. The [devkit clone generator](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/mod-dev.py) also removes the root ObjectRecordID; missing expected template nodes fail instead of silently constructing substitutes.

## ZIP dates are not a complete precedence model

The [devkit inventory tool](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/inspect_universe.py) selected newer member dates for case-insensitive matching paths. That describes the analysis tool, not a proven complete loader order. Maps, UserMODs, loose files and native patches need separate treatment.

The marker established one override, not universal alphabetic priority or hot reload.

**Evidence:** ZIP inventory, encoding/reference tests and the September 21 live marker on the [pinned build](universe-build.md). UTF-8 analysis copies are not automatically installable game text. [Marker recipe](../modding/resource-overrides.md).

[Research record](research-diary.md#archive-inventory).
