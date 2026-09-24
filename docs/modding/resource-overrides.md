---
content_type: how-to
status: draft
faction: fortress
title: Проверяем переопределение ресурса меткой в меню
lang: ru
section: modding
kicker: HEROES V · UNIVERSE
translation: en/modding/resource-overrides/
description: Проверяем переопределение ресурса меткой в меню
updated: '2026-09-24'
---
# Проверяем переопределение ресурса меткой в меню

Результат этого опыта — метка `[DEV: menu-marker]` рядом с версией в главном меню. Она проверяет, что игра приняла конкретный ресурс из отдельного H5U; игровой баланс не меняется.

## Что потребуется

Отдельная тестовая копия [исследованной сборки Universe](../reference/universe-build.md), Python 3 и закрытая игра. Архив должен содержать `UI/MainMenu2/Version.txt` с UTF-16LE BOM. До установки проверь, что в тестовой UserMODs нет другого мода, меняющего этот путь.

## Собрать пакет

Сохрани код в `make_marker.py` в отдельной рабочей папке. Он читает исходный ресурс и создаёт рядом `version-marker.h5u`; оригинальный PAK не изменяется. Существующий файл с таким именем в рабочей папке будет перезаписан.

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


Передай каталог тестовой игры аргументом:

```powershell
python make_marker.py "../HeroesV-test"
```

Путь в команде — пример, замени его на свою тестовую копию. Внутри ZIP должен быть ровно `UI/MainMenu2/Version.txt`, без дополнительной папки вроде `files/` или `version-marker/`.

## Проверка и откат

1. Запусти тестовую игру без пакета и проверь отсутствие метки. Закрой игру.
2. Скопируй полученный H5U в UserMODs тестовой копии. Не заменяй существующий чужой файл.
3. Запусти игру заново. В меню должна появиться метка.
4. Закрой игру и удали только установленный `version-marker.h5u`.
5. Снова запусти игру: метка должна исчезнуть.

Если метка не появилась, проверь внутренний путь, BOM, выбранную копию игры и другие переопределения этого же ресурса. Не переходи сразу к замене штатного PAK: тогда опыт перестанет проверять независимый пакет.

## Что доказал наш контроль

21 сентября2026 пользователь подтвердил появление метки после установки отдельного H5U и исчезновение после удаления с перезапусками. Первый запуск тестовой копии неожиданно завершился; повторный был успешен. Причина первого завершения не установлена.

Упаковщик использовал дату исходного ZIP-члена плюс 2 секунды. Одинаковые входы при той же среде сжатия давали одинаковый пакет. Это не доказывает универсальную победу самого нового архива, приоритет карт или hot reload.

Для интерфейсных XML-клонов дополнительно проверяются существование изменяемых узлов, относительные href и ObjectRecordID. [Разбор форматов](../reference/formats.md). Нормализованные UTF-8 файлы анализа не подставляются вместо исходных UI-текстов без обратного кодирования.
