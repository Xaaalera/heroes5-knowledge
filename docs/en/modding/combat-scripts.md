---
content_type: reference
status: draft
faction: sylvan
title: 'Combat scripts: Prepare, Start and battle results'
lang: en
section: modding
kicker: HEROES V · UNIVERSE
translation: modding/combat-scripts/
description: 'Combat scripts: Prepare, Start and battle results'
updated: '2026-09-24'
---
# Combat scripts: Prepare, Start and battle results

Record initial positions with `GetUnitPosition` in **combat `Start`, before the first turn**. Read results and losses separately, after battle, through `COMBAT_RESULTS_TRIGGER`.

| Event | Timing | Useful observation |
|---|---|---|
| Prepare | Before manual placement; placement waits for it | Test setup |
| Start | After deployment, before turns; combat waits for it | Actual starting coordinates |
| COMBAT_RESULTS_TRIGGER | After battle | Saved army/loss information indexed by combatIndex |

A long Start delay delays battle start. Positions after a fast unit's move are no longer initial deployment.

## Record both armies

Use in the **map's combat script**, not the ordinary adventure console:

```lua
function Start()
    for index, unit in GetAttackerCreatures() do
        local x, y = GetUnitPosition(unit);
        print("ATTACKER", unit, GetCreatureType(unit), x, y);
    end;
    for index, unit in GetDefenderCreatures() do
        local x, y = GetUnitPosition(unit);
        print("DEFENDER", unit, GetCreatureType(unit), x, y);
    end;
end;
```


Our map uses this CombatScript.xdb resource:

```xml
<Script><FileName href="CombatScript.lua"/></Script>
```

Bind the neutral object's `CombatScript` field to this Script resource; a Lua file in the archive alone is insufficient. The code prints each stack's type and coordinates; it does not include a log collector. The published experiments also recorded `GetUnitPosition` results with a separate observer.

## After-battle results

Map-script handler checked with a nonempty winning army:

```lua
function OnResults(combatIndex)
    local count = GetSavedCombatArmyCreaturesCount(combatIndex, 1);
    local creature, initial, died = GetSavedCombatArmyCreatureInfo(combatIndex, 1, 0);
    SetGameVar("last_battle", combatIndex .. "|" .. count .. "|" .. creature .. "|" .. initial .. "|" .. died);
end;
SetTrigger(COMBAT_RESULTS_TRIGGER, "OnResults");
```


Argument 1 selects the winner's army; index 0 selects its first stack. The observed string `0|1|13|10|0` means battle index 0, one winning stack, type 13, initial 10 and died 0. Handle empty armies before querying index 0.

These are after-battle assertions, never precombat predictor inputs. [Public information boundary](public-information.md).

Adventure-map and combat scripts run in different contexts. An adventure query can time out during combat; that alone does not prove the function is broken.

## Additional Universe events

UniverseTrigger/GetCombatStartedSnapshot names were investigated separately. Registration or a string match does not validate every snapshot scenario. Direct GetUnitPosition in Start is the confirmed coordinate observation path.

**Evidence:** shipped `HOMM5_A2_Script_Functions.pdf`, Combat pages 60–71 and 105–109; September 22–23 polygon checks on the [pinned build](../reference/universe-build.md). [Measured placement explanation](../players/army-placement.md).
