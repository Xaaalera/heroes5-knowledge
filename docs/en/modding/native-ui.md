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

ArmyWnd already had Visible=true, yet the bank reference army was absent. A template describes layout; the game must also select the window, supply its model and fill children.

## Resources and model

`data.pak/UI/Tooltips/CommonAdvObjTooltip/` contains a197×110 ArmyWnd, ArmyText and seven CreatureFace slots. Each has a40×40 frame,34×34 CreatureIconPlace and CreaturesNumber; MonsterTooltip/CommonAdvObjTooltip already reference the container.

The renderer searches child names. Investigated model virtual slots+0x38/+0x3c/+0x40 correspond to population condition, count and indexed access. One implementation uses 24-byte entries containing a texture reference and numeric/string labels. This is not a universal C++ ABI.

## Separate root selection

1. A shared-renderer experiment found panels but did not establish complete filling/layout for all banks.
2. The working prototype registered a separate root in typedWindows of a Universe UIGameRoot copy.
3. Public object names select that root before native filling/layout; ordinary tooltips retain their original path.
4. Its table has 19 names for 12 families. Renames/name collisions remain limitations, not a proven Type dispatcher.

A separate demon-bank window was observed in-game. Other families/new rows did not all receive equivalent live validation.

## Distinct army UI mechanisms

ArmyWnd is the portrait/label list for an object. SCreatureInfoTooltip is the combat screen's single-type detailed card. Projection cards use a synthetic one-creature descriptor without hero or real combat stack; CScreenTooltipController owns display/RMB. Grade switching updates both retained references rather than just an icon. Details use an owned CSimpleCreaturesRotator; quantity 1 is reference data, not revealed enemy numbers.

## Lifecycle

Windows/projections are tied to owners and generations. Start/destruction releases references. An early second-battle crash came from clearing mask pointers while retaining dimensions; resetting the complete 24-byte structure fixed that regression. One successful opening cannot validate lifecycle behavior.

Strings/vtables are not ready APIs. Validate object identity, calling convention, reference ownership, active screen and execution thread separately.

| Investigated entry | Address |
|---|---|
| Army-list renderer | 0x5f8050 |
| Root selection before layout | 0x5f8800 |
| Combat tooltip source | 0x546f40 |
| Creature descriptor | 0x4bd550 |
| Rotator construction | 0x789010 |

**Evidence:** resources, call counter, separate bank window and later native card checks, September 21–23. Only the [pinned build](../reference/universe-build.md); not an SDK. Original game DLLs were not replaced by a generic loader.
