---
content_type: reference
status: draft
faction: haven
title: Из чего состоит исследованная сборка Universe
lang: ru
section: reference
kicker: HEROES V · UNIVERSE
translation: en/reference/universe-build/
description: Из чего состоит исследованная сборка Universe
updated: '2026-09-24'
---
# Из чего состоит исследованная сборка Universe

**Нативные адреса и опыты в этой базе относятся к четырём файлам с хешами ниже.** Надписи «Universe 2.0» недостаточно: мод меняет ресурсы, интерфейс и исполняемый код. Перед повторением нативного опыта сравни SHA-256 своей установки.

## Почему недостаточно надписи «Universe 2.0»

В `UI/MainMenu2/Version.txt` найдена версия `HoMM V version 3.1 + Universe mod 2.0`, а в `uni.dll` — строка проверки PAK версии 1.8. Строка может быть устаревшей. Для адресов и native-экспериментов использована следующая точная связка:

| Файл | SHA-256 |
|---|---|
| `H5_Game.exe` | `88c9dc6107b9bced0649924a86360f1c56397ee00de0413f6f2b08f865ed5519` |
| `uni.dll` | `aa5211151d9e9a8c135e180ff8832908d128ccae08a5145162bcdae4946c18ee` |
| `um.dll` | `1956c00b371d22a3e1a644394ff3e7159b6ec36d660d5ffa36628fcf63fd0fc6` |
| `d3d9.dll` | `5eb152357f99d53397b764384d5cf9a0f6aece733ced30a34186ac57fb15be25` |

Все четыре — x86 PE, machine `0x14c`. ImageBase исследованного EXE — `0x400000`; адреса функций EXE в этих материалах указаны как абсолютные виртуальные адреса, не смещения от начала файла. Совпадение EXE не доказывает совпадение ресурсов, профиля и патчей других DLL.

Из каталога своей игры можно проверить файл командой PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\bin\H5_Game.exe
```

## Снимок ресурсов 21 сентября 2026

Все восемь исследованных `data/*.pak` открылись как ZIP. Сравнение учитывало локальные `data.pak`, `a2p1-data.pak`, `texts.pak`, `a2p1-texts.pak`; их чистота относительно оригинальной ToE отдельно не установлена.

| Архив | Всего ресурсов | Отличаются | Новые пути | Совпадают |
|---|---:|---:|---:|---:|
| `Universe_mod.pak` | 5159 | 1075 | 4047 | 37 |
| `universe_mod_texts_ru.pak` | 1771 | 605 | 942 | 224 |

В основном архиве насчитано 3767 ресурсов UI, 787 GameMechanics, 185 MapObjects и 61 RMG. Это количества файлов соответствующих разделов, не количество новых функций.

Примеры побайтово найденных изменений определений: у `Academy/Rakshasa_Rukh.xdb` DefenceSkill 20→25, Health 140→145; у `Dungeon/Assassin.xdb` WeeklyGrowth 7→8; у `Dungeon/Blood_Witch.xdb` 5→6. Это значения исследованных файлов, не обещание таких итоговых статов в любом бою.

Чтобы получить инвентаризацию своей установки, используй [inspect_universe.py из devkit](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/inspect_universe.py). Исходную игру и папку результатов задают [настройки рабочего каталога](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/README.md#где-что-хранится).

## Скачать исходную таблицу сравнения {#archive-diff}

[archive-diff.csv](../assets/archive-diff.csv) содержит **6930 записей** двух архивов из таблицы выше. Это имена ресурсов, результаты сравнения, размеры и даты ZIP-записей; содержимое игровых файлов в CSV не включено.

| Столбец | Значение |
|---|---|
| archive | Архив Universe |
| path | Путь ресурса внутри ZIP |
| status | `added` — пути нет в базе; `changed` — байты отличаются; `same` — совпадают |
| baseline_archive | Выбранный архив базы; пусто для added |
| bytes | Размер ресурса в байтах |
| member_date | Дата ZIP-записи, не дата исследования |

При совпадающем пути в нескольких базовых архивах отчёт выбирал более новую дату ZIP-члена; при равной дате оставлял первый. Пути сопоставлялись без учёта регистра. Это правило отчёта, **не доказанный приоритет загрузки игры**.

Чтобы пересчитать таблицу, скачай CSV в рабочую папку и выполни этот код Python 3 из той же папки:

```python
from collections import Counter
import csv

with open('archive-diff.csv', encoding='utf-8', newline='') as source:
    counts = Counter((row['archive'], row['status']) for row in csv.DictReader(source))
for (archive, status), count in sorted(counts.items()):
    print(archive, status, count)
```

```text
Universe_mod.pak added 4047
Universe_mod.pak changed 1075
Universe_mod.pak same 37
universe_mod_texts_ru.pak added 942
universe_mod_texts_ru.pak changed 605
universe_mod_texts_ru.pak same 224
```

SHA-256 скачиваемого CSV (UTF-8, LF): `81115018610632c94b9db9566b28cc85afa3e42b76cf2c37e3ffbfc4a5af4299`.

## Что нельзя заключить по DLL-строкам

Имена `UniverseTrigger` и событий `UNIVERSE_COMBAT_STARTED`, `UNIVERSE_WORLD_READY_AFTER_LOAD` найдены в бинарнике. Само наличие имени не устанавливает сигнатуру и доступность функции в конкретном Lua-контексте. Обнаруженные признаки proxy у `d3d9.dll` также не разрешают заменять её произвольным загрузчиком: цепочка загрузки должна сохраняться.

`RMG/MapScript.lua` из основного архива содержал лишь комментарий-заголовок. Поэтому описывать Universe как набор Lua-скриптов неверно.

**Основание:** ZIP-каталоги и сравнение содержимого, строки/PE-заголовки и SHA-256 установки; проверки 21–23 сентября 2026. Статистика не переносится на более позднюю сборку автоматически. [Как читать архивы](formats.md) · [Точки UI в этой сборке](../modding/native-ui.md).

[Запись исследования](research-diary.md#archive-inventory).

Проект Universe: [сайт UniverseTeam / Heroes V Lobby](https://h5lobby.com/), [сообщество](https://vk.com/h5universe). Совместимость скачанной версии с исследованными хешами проверяется отдельно.
