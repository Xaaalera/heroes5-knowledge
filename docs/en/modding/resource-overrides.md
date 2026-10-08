---
content_type: how-to
status: draft
faction: fortress
title: Test a resource override with a menu marker
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/resource-overrides/
description: Test a resource override with a menu marker
updated: '2026-10-08'
---
# Test a resource override with a menu marker

Add `[DEV: menu-marker]` beside the main-menu version through a separate H5U. If it appears after installation and disappears after removal, the game loaded the `UI/MainMenu2/Version.txt` override.

## Requirements

An isolated copy of the [investigated Universe build](../reference/universe-build.md), Python 3 and a closed game. The source resource must exist with UTF-16LE BOM. Check for other test-copy mods overriding the same path.

## Build

Save the code as make_marker.py in a separate working folder. It reads the source and writes version-marker.h5u beside the script invocation without editing the PAK. An existing output file of that name will be overwritten.

```python
from datetime import datetime, timedelta
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import sys

source = Path(sys.argv[1]) / 'data' / 'Universe_mod.pak'
name = 'UI/MainMenu2/Version.txt'
with ZipFile(source) as archive:
    raw = archive.read(name)
    stamp = datetime(*archive.getinfo(name).date_time) + timedelta(seconds=2)
if raw[:2] != b'\xff\xfe' or stamp.year > 2107:
    raise ValueError('Unexpected encoding or unsupported ZIP date')
payload = b'\xff\xfe' + (raw[2:].decode('utf-16-le') + ' [DEV: menu-marker]').encode('utf-16-le')
info = ZipInfo(name, stamp.timetuple()[:6])
with ZipFile('version-marker.h5u', 'w') as output:
    output.writestr(info, payload, compress_type=ZIP_DEFLATED)
```


```powershell
python make_marker.py "../HeroesV-test"
```

Replace the example path with your test installation. The ZIP member must be exactly `UI/MainMenu2/Version.txt`, without an extra files/ or package-name directory.

## Verify and remove

1. Launch without the package, confirm no marker, then close.
2. Copy the H5U into the test copy's UserMODs without replacing another person's file.
3. Relaunch and check for the marker.
4. Close and remove only your version-marker.h5u.
5. Relaunch and confirm its disappearance.

If absent, inspect the internal path, BOM, launched copy and competing overrides. Replacing the original PAK would change the experiment's meaning.

## What was checked

On the inspected build, the marker appeared after H5U installation and disappeared after removal with restarts. [Experiment record and failed first launch](../reference/research-diary.md#menu-marker).

The example uses the original ZIP-member timestamp plus 2 seconds. Identical inputs and compression environment produced identical packages. This did not test general archive/map precedence or resource hot reload.

XML clones additionally require checking edited nodes, relative `href` and `ObjectRecordID`. Text normalized to UTF-8 for analysis must be returned to its original encoding before packaging. [Formats and links](../reference/formats.md).

For ordinary development, use the [xkit guide](devkit.md) and [command reference](../reference/xkit-commands.md). Builder source: [mod-dev.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/mod-dev.py).

## xkit resource project recipe

`xkit new ui-example --resources` creates `mods/ui-example/mod.json`. Create a sibling `files` directory when adding your own resources. Edit the recipe, then run `xkit build ui-example`. Its `id` must match the project name. Archives come from the selected game's `data` directory; resources use their internal game paths.

| Recipe field | Purpose |
|---|---|
| `source_archive`, `source_path` | Required source archive and resource, hashed in the build report |
| `append` | Optional text appended to the main resource |
| `xml_patches` | XML template edits, each with required `source` and optional `archive` and `target` |
| `encode_texts: "utf-16-le"` | Convert your UTF-8 TXT files under `files` to UTF-16LE with BOM; otherwise preserve bytes |

For an XML edit, `archive` defaults to `source_archive` and `target` to `source`. Operations address existing elements using ElementTree paths:

| Operation | Effect |
|---|---|
| `clear`: list of paths | Clear the selected element's children, text and attributes |
| `text`: path to string mapping | Replace element text |
| `attributes`: path to attribute mapping | Add or replace the specified attributes |
| `append_xml`: path to XML-string list mapping | Append child elements from fragments |

Missing elements or invalid XML cause refusal rather than construction of a similar template. Cloning removes the root `ObjectRecordID` and resolves relative `href` links against their original directory. A new window file also needs a reference from game resources: packaging a clone alone does not make the game show it.

For example, add `xml_patches` to the generated recipe while retaining its required `id`, `source_archive` and `source_path`:

```json
{
  "xml_patches": [
    {
      "archive": "data.pak",
      "source": "UI/Tooltips/CommonAdvObjTooltip/ArmyWnd.(WindowSimple).xdb",
      "target": "UI/XkitExample/ArmyWnd.(WindowSimple).xdb",
      "text": { "./Visible": "true" }
    }
  ]
}
```

This is a recipe fragment, not a replacement for the entire `mod.json`. It creates a separate standard-panel clone and sets its existing `Visible` element. The original template and this operation were checked through the builder in memory; this example does not wire the new window into the interface. After `xkit build ui-example`, check the new internal H5U path, then verify game usage separately.

Files under `files` preserve game paths. Paths must remain inside the project; case-insensitive collisions are refused. XML/XDB is parsed for validity. Build reports record every consumed template's archive, path and SHA-256, and deployment rechecks those dependencies. ZIP dates account for the newest consumed template, without establishing game loading precedence.

## Deployment ownership and rollback

Ordinary `xkit start ui-example` manages the test session; player delivery uses `xkit release ui-example` and the package's README.txt. Low-level resource deployment journals ownership before replacement, then records installed state. Redeployment accepts only a known owned hash; foreign destination files are not overwritten.

Low-level `rollback` removes its owned installation, restoring absence of the mod rather than a previous version. External file edits cause refusal to delete it. Deployment and rollback require the game and editor closed; do not start the game externally while files are being written. After a crash, first confirm the recorded process has exited. Do not blindly remove unknown temporary files or locks.

These checks concern the resource builder and its isolated tests. A valid ZIP and successful installation do not prove that the game actually uses the chosen window or resource.
