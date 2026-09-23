---
faction: necropolis
title: PAK, H5U, XDB and other formats
lang: en
section: reference
kicker: REFERENCE · FILES
translation: reference/formats/
description: Basic resource, script, and native modification formats in Heroes V.
updated: 2026-09-23
---
# PAK, H5U, XDB and other formats

A short map of files encountered when working with Heroes V. This introductory reference does not guarantee that every game version supports every file.

| Format | Meaning | What to check |
|---|---|---|
| `.pak` | ZIP resource archive | Internal paths and which archive loads |
| `.h5u` | ZIP-format mod package | Support and install location in the target version |
| `.xdb` | XML game-resource definition | Object type, fields, and `href` references |
| `.lua` | Lua script | Execution context and available functions |
| `.txt` | Text resource | Encoding, markup, and references from definitions |
| `.dll` | Native library | Loader, architecture, and compatible build |

## Paths are part of an archive

The resource's path inside the archive matters. Changing it during packaging may make the game miss the resource or continue using the original definition.

Do not combine archives blindly: matching internal paths can indicate a resource conflict.

## XDB references

`href` links definitions to other resources. When moving your own definition, check its relative references too: they are interpreted relative to the file's location.

Text search and an XML parser are useful research tools. Verify encoding and structure after saving.

## Different layers need different checks

A resource mod needs a loading check. Lua needs execution in the intended context. A native library needs executable compatibility checks and in-game observation.

Continue with [your first experiment](../modding/getting-started.md) and [verification](../modding/verification.md).
