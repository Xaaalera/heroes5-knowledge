---
content_type: explanation
status: draft
faction: inferno
title: 'Native UI: why Visible=true is insufficient'
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/native-ui/
description: 'Native UI: why Visible=true is insufficient'
updated: '2026-09-24'
---
# Native UI: why Visible=true is insufficient

An army tooltip needs **a window template, the selected root and a populated data model**. `ArmyWnd` already had `Visible=true`; the flag cannot fill an empty model.

## Army-panel elements

`data.pak/UI/Tooltips/CommonAdvObjTooltip/` contains:

| Element | Purpose and size |
|---|---|
| ArmyWnd | 197×110 container |
| ArmyText | Army text |
| CreatureFace.1–7 | Seven portrait cells |
| Cell frame / CreatureIconPlace | 40×40 / 34×34 |
| CreaturesNumber | Quantity label |

`MonsterTooltip` and `CommonAdvObjTooltip` already reference this container. The renderer finds child elements **by name**.

In the inspected model, virtual slots `+0x38/+0x3c/+0x40` supply the population condition, element count and element access. A 24-byte record contains a texture reference and numeric/string labels. These offsets describe one implementation, not a universal C++ ABI.

## Read ArmyWnd from your installation {#read-army-resource}

Use Python 3 and `data.pak` from the [inspected build](../reference/universe-build.md). Save this as `inspect_army_window.py`. It only reads ZIP/XML and does not launch the game.

```python
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree
import sys

archive_path = Path(sys.argv[1]) / 'data' / 'data.pak'
resource = 'UI/Tooltips/CommonAdvObjTooltip/ArmyWnd.(WindowSimple).xdb'
with ZipFile(archive_path) as archive:
    raw = archive.read(resource)
window = ElementTree.fromstring(raw)
size = window.find('.//Size/First')
print('sha256:', sha256(raw).hexdigest())
print('Visible:', window.findtext('.//Visible'))
print('Size:', size.findtext('x'), size.findtext('y'))
```

Replace `../HeroesV-test` with your installed game's directory:

```powershell
python inspect_army_window.py "../HeroesV-test"
```

Expected output for the inspected resource:

```text
sha256: 30a503de3aa0d28c29229a5d9d51cc98ea324ac32ea27a8388ebb8067bc1a2e9
Visible: true
Size: 197 110
```

A different hash means different resource bytes; compare contents first. The example inspects the `WindowSimple` **instance**. Its Shared file has size 0×0 and `Size/Second=false`; Shared alone does not establish a zero-sized panel. [September 24 repeat-check record](../reference/research-diary.md#army-resource-check).

## Selecting the prototype window

Switching the shared renderer found panels but did not provide suitable population and space for every bank.

The working path was:

1. Register a separate root in a copy of Universe `UIGameRoot`'s `typedWindows`.
2. Select it by the public object name **before** normal population and layout.
3. Keep other tooltips on their normal path.

The prototype table contains 19 names for 12 families. Renaming or duplicate names can break selection; a universal Type dispatcher is unconfirmed. The separate demon-bank window was seen in game; other families did not receive the same full check.

## Army list versus creature card

| Window | Display |
|---|---|
| Object-tooltip ArmyWnd | Several portraits and labels |
| Combat SCreatureInfoTooltip | Stats of one creature type |

A projection uses a reference descriptor for one creature, without a hero or real combat stack. `CScreenTooltipController` owns the card/RMB behavior; changing upgrade updates **both retained references**. Replacing the image alone is insufficient.

The detailed window uses `CSimpleCreaturesRotator`. Its displayed quantity of one is a reference value, not an enemy count.

## Why the second battle matters

Window and projection references belong to an owner and generation; Start or screen destruction releases them. An early mask reset cleared pointers but retained dimensions, causing the second battle to crash. The fix resets **all 24 bytes** of the mask structure.

Before a native call, check the window pointer, calling convention, reference ownership, active screen and execution thread. A function name or virtual-method table alone is insufficient.

## Addresses in the inspected build

| Purpose | Address |
|---|---|
| Army-list renderer | `0x5f8050` |
| Root selection before layout | `0x5f8800` |
| Combat tooltip source | `0x546f40` |
| Creature descriptor creation | `0x4bd550` |
| Rotator creation | `0x789010` |

**Scope:** the [pinned build](../reference/universe-build.md) only; no universal plugin API. The [devkit](devkit.md) contains development tools. Evidence: resources, call counter and game checks on September 21–23, 2026. Original game DLLs were not replaced with a generic loader.

[Research record](../reference/research-diary.md#army-tooltip-probe).

Inspection tools: [native-probe.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/native-probe.py) and [frame capture/OCR](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md#capture-input-and-shutdown). The predictor card implementation is not included in the devkit.

[Predictor card source](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/src/preview_plugin.cpp) and the [bank-reference recipe](https://github.com/Xaaalera/heroes5-bank-reference/blob/main/mod.json) now live in separate repositories.
