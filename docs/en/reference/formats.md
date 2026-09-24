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

A resource is identified by its **path inside the container**, not its extraction directory. A version-text override therefore retains `UI/MainMenu2/Version.txt`.

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

## Relative XDB links

`href="../Textures/icon.xdb#xpointer(/Texture)"` combines a resource path with an XML pointer. Moving the containing definition can change its target. Clone processing must resolve links against the original directory. Our clone generator also removes the root ObjectRecordID; missing expected template nodes fail instead of silently constructing substitutes.

## ZIP dates are not a complete precedence model

Our inventory comparison selected newer member dates for case-insensitive matching paths. That describes the analysis tool, not a proven complete loader order. Maps, UserMODs, loose files and native patches need separate treatment.

The marker established one override, not universal alphabetic priority or hot reload.

**Evidence:** ZIP inventory, encoding/reference tests and the September 21 live marker on the [pinned build](universe-build.md). UTF-8 analysis copies are not automatically installable game text. [Marker recipe](../modding/resource-overrides.md).
