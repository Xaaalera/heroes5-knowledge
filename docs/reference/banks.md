---
content_type: reference
status: draft
faction: stronghold
title: 'Хранилища: типы, тиры и диапазоны охраны'
lang: ru
section: reference
kicker: HEROES V · UNIVERSE
translation: en/reference/banks/
description: 'Хранилища: типы, тиры и диапазоны охраны'
updated: '2026-09-24'
---
# Хранилища: типы, тиры и диапазоны охраны

**У одного тира хранилища может быть несколько составов охраны.** Например, у склепа восемь вариантов на четыре тира. Для справки нужно сопоставить варианты с тирами; номер записи в массиве для этого не подходит. Ниже — каталог и два примера расчёта численности.

## Привязка ресурсов

В проверенных PAK сопоставлены 25 определений объектов для 12 подтверждённых Type. В AG_INFO13 семейств: привязка OrcDeposit к XDB пока не найдена. Внутренний ключ BUILDING_ORC_DEPOSIT из раннего прототипа нельзя выдавать за установленный Type игры.

| Type / ключ | AG_INFO | Таблица / table | Тиры / tiers |
|---|---|---|---|
| BUILDING_CRYPT | 01 | BankCrypt | 1–4 |
| BUILDING_DWARVEN_TREASURE | 02 | BankDwarvenTreasure | 1–4 |
| BUILDING_GARGOYLE_STONEVAULT | 03 | BankGargoyleStonevault | 1–4 |
| BUILDING_PYRAMID | 04 | BankPyramid | 1–3 |
| BUILDING_SUNKEN_TEMPLE | 05 | BankSunkenTemple | 1–4 |
| BUILDING_BLOOD_TEMPLE | 06 | BankBloodTemple | 1–4 |
| BUILDING_UNKEMPT | 07 | BankUnkempt | 1–5 |
| BUILDING_CYCLOPS_STOCKPILE | 08 | BankElementalsStockpile | 1–4 |
| BUILDING_NAGA_BANK | 09 | BankMagiVault | 1–3 |
| BUILDING_TREANT_THICKET | 10 | BankTreantThicket | 1–3 |
| BUILDING_DEMOLISH | 11 | BankDemolish | 1–4 |
| OrcDeposit: Type не установлен / unresolved | 12 | BankNagaTemple | 1–3 |
| BUILDING_DRAGON_UTOPIA | 13 | BankDragonUtopia | 1–5 |

Названия не всегда однозначны. BUILDING_SUNKEN_TEMPLE объединяет старый затонувший храм и Universe-тайник бесов; BUILDING_CYCLOPS_STOCKPILE используется башней элементалей. BUILDING_UNKEMPT встречается у корабельных объектов и Магистрата Порядка, BUILDING_DEMOLISH — у остовов судов и Особняка мертвецов. Выбирать первую модель по алфавиту только по Type нельзя.

Точки проверки: `MapObjects/Universe_mod/Demonbank.(AdvMapBuildingShared).xdb`, `Monasterybank.(AdvMapBuildingShared).xdb`, `NecroEstate.(AdvMapBuildingShared).xdb`; также `MapObjects/MagiVault.xdb`, `Elemantal_Stockpile.(AdvMapBuildingShared).xdb` (именно такое написание), `WitchBank.(AdvMapBuildingShared).xdb`.

## Почему индекс варианта не равен тиру

В DefaultStats у склепа 8 вариантов на4 тира, у сокровищницы магов 5 на3, у утопии 7 на5. Номер элемента массива нельзя напрямую подписать T1,T2,T3…: один тир может иметь несколько составов.

При подготовке справки сопоставляются **армия варианта, награды и панель AG_INFO**. Одинаковые типы внутри одного варианта можно агрегировать. Взаимоисключающие замены нельзя складывать как одновременную армию.

## Пример: сколько существ в тайнике бесов

В `UI/AGINFO/05_01_SIZE.txt`…`05_04_SIZE.txt` описаны 5 групп по3 слота: всего 15 записей охраны.

| Тир | Количество в слоте | Всего по15 слотам |
|---|---|---|
| T1 | 6–9 | 90–135 |
| T2 | 8–11 | 120–165 |
| T3 | 10–13 | 150–195 |
| T4 | 12–15 | 180–225 |

Это диапазоны полного состава по тиру, а не сумма минимумов отдельных видов из разных вариантов. Ранний минимум «8 бесов» возник именно из такого смешения и был отброшен. Замены видов остаются внутри своих групп; таблица не раскрывает фактическую охрану посещённого объекта.

## Башня элементалей

Четыре варианта содержат по5,10,15 или 20 существ **каждого из четырёх видов**. Число 15 в одном варианте не означает суммарно 15 элементалей: при четырёх видах это 60 существ до дополнительных правил. Эта таблица ресурсов сама по себе не проверяет изменения DLL или конкретной карты.

## Ресурсы на земле — отдельный механизм

В исследованных AdvMapTreasureShared: дерево/руда MinResource=4, MaxResource=7; редкие ресурсы 2–4; золото 5–10 внутренних единиц. Пересчёт золота ×100 не был подтверждён нашим контролируемым опытом, поэтому не превращаем эту строку в готовую таблицу выплаты 500–1000.

**Основание:** MapObjects, UI/AGINFO и Banks в `GameMechanics/RPGStats/DefaultStats.xdb`, проверки 21 сентября2026 и исправление группировки. Число слотов сверено для 13 семейств; полная сверка всех вероятностей, названий и runtime-правил не выполнена. [Публичные данные](../modding/public-information.md) · [Сборка](universe-build.md).

[Запись исследования](research-diary.md#banks).

Группировка отрядов и формирование справочного текста реализованы в [object_reference.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/object_reference.py). Это компилятор рецептов; рецепты конкретных модов не поставляются вместе с devkit.
