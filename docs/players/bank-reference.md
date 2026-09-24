---
content_type: how-to
status: draft
faction: fortress
title: Справочник хранилищ — установка и карточки
lang: ru
section: players
kicker: HEROES V · UNIVERSE
translation: en/players/bank-reference/
description: Исходники, установка, чтение справки и удаление мода.
updated: 2026-09-24
---
# Справочник хранилищ — установка и карточки

[Исходники](https://github.com/Xaaalera/heroes5-bank-reference) · [Universe](https://h5lobby.com/) · [проверенный devkit](https://github.com/Xaaalera/heroes5-mod-devkit/tree/1b8934ac084491da460ce8bb145819e41e2cf888).

Мод показывает **возможные армии по тирам**, портреты, диапазоны и альтернативы. Фактическую скрытую охрану объекта он не раскрывает.

## Установка

Нужны Windows, Git, Python 3.10+ x64 и [поддерживаемая Universe](../reference/universe-build.md). Текущий прототип работает как **H5U плюс диагностический нативный запуск devkit**. Отдельного пользовательского DLL-установщика пока нет.

Закрой игру и редактор. В новом каталоге PowerShell:

```powershell
git clone --recursive https://github.com/Xaaalera/heroes5-bank-reference.git
cd heroes5-bank-reference
python -m venv .venv
.venv/Scripts/python -m pip install -r devkit/requirements.txt
$env:H5_WORKSPACE = [IO.Path]::GetFullPath('../bank-reference-workspace')
$env:H5_GAME_DIR = (Resolve-Path '../HeroesV-Universe').Path
.venv/Scripts/python devkit/scripts/mod-dev.py prepare --sandbox
.venv/Scripts/python devkit/scripts/mod-dev.py build --sandbox --mod army-reference --source .
.venv/Scripts/python devkit/scripts/mod-dev.py deploy --sandbox --mod army-reference
.venv/Scripts/python devkit/scripts/native-probe.py launch --army-layout --control
```

Замени пример пути своей установленной игрой и выбери отдельную рабочую папку. `prepare` выполняется один раз и не перезаписывает существующую копию. В новом PowerShell снова задай переменные. После правки рецепта сначала нужен build: deploy устанавливает готовый H5U.

Открой карту и наведи на поддерживаемое хранилище. В прежнем контроле тайник бесов показывал T1–T4 и 90–135 / 120–165 / 150–195 / 180–225. Последние правки оформления и остальные хранилища не получили такого же полного визуального подтверждения.

## Как читать справку

- T1/T2… обозначает возможный тир, а не разведанную охрану объекта.
- A/B разделяет альтернативные полные составы; их нельзя суммировать.
- Половинки портрета обозначают заменяющие друг друга виды. Процент применяется к отдельному отряду.
- Число под парой — диапазон всей группы, а не гарантированное количество каждого вида.

[Откуда берутся тиры и диапазоны](../reference/banks.md). Каталог содержит 13 семейств; 19 публичных названий сопоставлены с 12 подтверждёнными типами. Привязка OrcDeposit не найдена; переименованные объекты не поддерживаются выбором по имени.

## Удаление

Закрой тестовую игру и проверь выход процесса. В том же окружении:

```powershell
.venv/Scripts/python devkit/scripts/mod-dev.py rollback --sandbox --mod army-reference
```

Удаляется только собственный неизменённый H5U. Чужие моды и вся копия игры остаются. Обычный последующий запуск без `--army-layout` не устанавливает селектор новых окон.

## Что проверено

Отдельная сборка побайтно совпала с прежней: SHA-256 `824a14b48fbdadce9ea0475b49bc4d1f1f6d2ef112ef8294b63cc1ea4ebf7f1e`. Прошли четыре проверки рецепта и нативного селектора. Нового живого запуска после переноса не было; совместная работа с предиктором не проверена.

[Инструкция репозитория](https://github.com/Xaaalera/heroes5-bank-reference#readme) · [Оба мода и правила установки](mods.md) · [История подсказки](../reference/research-diary.md#army-tooltip-probe).
