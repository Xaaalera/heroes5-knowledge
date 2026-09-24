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

Добавим `[DEV: menu-marker]` рядом с версией в главном меню через отдельный H5U. Если метка появляется после установки и исчезает после удаления, игра подхватила переопределение `UI/MainMenu2/Version.txt`.

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

## Что проверено

На исследованной сборке метка появлялась после установки и исчезала после удаления H5U с перезапусками. [Запись опыта и неудачный первый запуск](../reference/research-diary.md#menu-marker).

Дата ZIP-записи в примере — исходная плюс 2 секунды. При одинаковых входах и среде сжатия получался одинаковый пакет. Общий приоритет архивов, карт и перезагрузка ресурсов без перезапуска этим не проверены.

Для XML-клонов отдельно проверяются изменяемые узлы, относительные `href` и `ObjectRecordID`. Тексты после анализа в UTF-8 нужно вернуть в исходную кодировку перед упаковкой. [Форматы и ссылки](../reference/formats.md).

Для повторного цикла используй [установку devkit](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/README.md#быстрый-старт) и [команды build/deploy/rollback](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md#ресурсный-цикл). Исходник сборщика — [mod-dev.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/mod-dev.py).
