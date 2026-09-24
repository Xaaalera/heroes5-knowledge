---
content_type: reference
status: draft
faction: sylvan
title: 'Боевые скрипты: Prepare, Start и результат боя'
lang: ru
section: modding
kicker: HEROES V · UNIVERSE
translation: en/modding/combat-scripts/
description: 'Боевые скрипты: Prepare, Start и результат боя'
updated: '2026-09-24'
---
# Боевые скрипты: Prepare, Start и результат боя

Код приключенческой карты и боевой скрипт выполняются в разных контекстах. Поэтому отсутствие ответа приключенческого запроса во время боя не доказывает, что функция или терминальный канал сломаны.

## Когда наблюдать расстановку

| Событие | Момент | Подходящее наблюдение |
|---|---|---|
| Prepare | До ручной расстановки; расстановка ждёт завершения функции | Подготовка условий опыта |
| Start | После расстановки и перед ходами; бой ждёт завершения функции | Фактические стартовые координаты |
| COMBAT_RESULTS_TRIGGER | После завершения боя | Сохранённые составы/потери по combatIndex |

Длинная задержка внутри Start задерживает начало боя. Координаты после хода быстрого существа уже не являются стартовой расстановкой.

## Минимальная запись обеих армий

Этот код относится к **боевому скрипту карты**, а не к обычной консоли приключений:

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


На нашем полигоне ресурс `CombatScript.xdb` имеет вид:

```xml
<Script><FileName href="CombatScript.lua"/></Script>
```

У объекта нейтрала поле CombatScript ссылается на этот Script-ресурс. Сам файл Lua без такой привязки не является доказательством выполненного callback. В опытах вызовы и результаты GetUnitPosition дополнительно фиксировались наблюдателем; генератор простых `print` не является опубликованной системой сбора журнала.

## Результаты без чтения скрытых входов

Пример обработчика в скрипте карты, проверенный на непустой армии победителя:

```lua
function OnResults(combatIndex)
    local count = GetSavedCombatArmyCreaturesCount(combatIndex, 1);
    local creature, initial, died = GetSavedCombatArmyCreatureInfo(combatIndex, 1, 0);
    SetGameVar("last_battle", combatIndex .. "|" .. count .. "|" .. creature .. "|" .. initial .. "|" .. died);
end;
SetTrigger(COMBAT_RESULTS_TRIGGER, "OnResults");
```


Значение 1 выбирает армию победителя; индекс 0 — её первый стек. Контроль дал `0|1|13|10|0`: combatIndex 0, один стек победителя, тип 13, исходно 10, погибло 0. Для пустой армии прежде обращения к индексу 0 нужен отдельный путь обработки.

Эти данные появляются **после боя** и годятся для проверки. Они не должны возвращаться во входы прогноза до боя. [Граница публичных данных](public-information.md).

## Что известно о дополнительных событиях Universe

Названия UniverseTrigger и GetCombatStartedSnapshot исследовались отдельно. Регистрация/появление строки не равны проверенному содержимому snapshot во всех сценариях. Для исходной фиксации координат подтверждён прямой GetUnitPosition в Start.

**Основание:** поставляемый `HOMM5_A2_Script_Functions.pdf`, раздел Combat, страницы 60–71 и105–109; полигонные проверки 22–23 сентября на [закреплённой сборке](../reference/universe-build.md). [Расстановка с измерениями](../players/army-placement.md).
