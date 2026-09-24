---
content_type: explanation
status: draft
faction: dungeon
title: Inputs available for a public prediction
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/public-information/
description: Inputs available for a public prediction
updated: '2026-09-24'
---
# Inputs available for a public prediction

Type definitions, a visible quantity interval and the exact hidden composition are different sources. Rounding a hidden quantity after reading it does not make it public.

| Input | Supports | Does not establish |
|---|---|---|
| Ordinary tooltip portrait | Match a known type to a definition | Combat stack count after splitting |
| Visible quantity interval | Evaluate an eventual model at its bounds | Exact quantity |
| Creature XDB | Reference traits | Actual hidden upgrade |
| Bank AG_INFO/DefaultStats | Possible guards | The object's selected tier |
| Combat Start positions | After-the-fact comparison | Honest precombat prediction input |

Unknown/ambiguous portraits or a mismatched target invalidate the input. The inspected integration binds target information to the new grid of the attack command; stale hovering is not a current target.

## Why Danger is not our model

MonsterTooltip/Danger.(WindowTextView).xdb links ARMY_DANGER_* labels. Finding their display does not establish where all evaluation inputs originate.

The experimental Assess button accepted clicks and displayed a diagnostic response. It did not validate a victory, loss or probability model. Evaluating lower/upper quantity bounds and returning “risky” remained a proposal, not an implemented battle assessor.

## OCR is not ground truth

Recognizing “Imps 20–30” in a synthetic image did not measure accuracy on the game font. A full-frame OCR pass over a readable golem card once returned only “00.”; crop-based recognition recovered its title/fields. Missing recognized text does not prove missing UI. Reject a reversed 40–32 interval rather than silently swapping it.

**Evidence:** MonsterTooltip/AG_INFO analysis, diagnostic-button and OCR controls, September 21–23. [Creature definitions](../reference/creatures.md) · [Banks](../reference/banks.md) · [Projection meaning](../players/deployment-preview.md).
