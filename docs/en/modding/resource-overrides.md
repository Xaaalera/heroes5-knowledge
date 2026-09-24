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
updated: '2026-09-24'
---
# Test a resource override with a menu marker

This experiment adds `[DEV: menu-marker]` beside the main-menu version. It tests one resource override from a separate H5U without changing game balance.

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

## Observed result and scope

On September 21,2026 the user confirmed appearance and disappearance after installation/removal with restarts. The first test-copy launch exited unexpectedly; a repeat succeeded, with the initial cause unresolved.

The packer used the original member date plus two seconds. Identical inputs under the same compression environment produced identical output, not proof of universal newest-file priority, map precedence or hot reload.

XML clones additionally require valid nodes, href resolution and ObjectRecordID handling. [Formats](../reference/formats.md). Do not replace original UI text with normalized analysis UTF-8 without the required encoding conversion.
