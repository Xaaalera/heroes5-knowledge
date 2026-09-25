---
content_type: explanation
status: draft
faction: fortress
title: Наш стенд разработки модов
lang: ru
section: modding
kicker: HEROES V · UNIVERSE
translation: en/modding/devkit/
description: Наш стенд разработки модов
updated: 2026-09-24
---
# Наш стенд разработки модов

[**Heroes V Mod Devkit на GitHub**](https://github.com/Xaaalera/heroes5-mod-devkit) собирает H5U, создаёт отдельную копию игры и управляет тестовым процессом через команды. Исходники стенда вынесены в самостоятельный репозиторий; это те общие инструменты, которыми мы пользуемся при разработке модов.

Python и PowerShell обслуживают разработку и проверку. Сам предиктор остаётся C++ DLL и в этот репозиторий не входит. Нативные команды рассчитаны на [конкретную сборку Universe](../reference/universe-build.md).

## Что входит

| Часть | Что делает | Результат |
|---|---|---|
| [mod-dev.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/mod-dev.py) | Собирает, устанавливает и откатывает ресурсный мод | H5U и журнал собственных хешей |
| Песочница | Копирует файлы установленной игры без hardlink | `.local/test-game/` |
| [test-map.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/test-map.py) | Создаёт полигон из ресурсов своей игры | WorkshopPolygon.h5m |
| [native-probe.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/native-probe.py) | Запускает свой процесс и подключает командный канал | PID и проверяемое состояние канала |
| [game_control.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game_control.py) | Читает состояние, двигает героя, запускает и завершает бои | Ответ команды и проверка результата |
| [game-ui.ps1](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/scripts/game-ui.ps1) | Сохраняет кадр, распознаёт текст, выполняет адресный ввод | PNG и OCR-данные |
| [inspect_universe.py](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/inspect_universe.py) | Сравнивает архивы и извлекает тексты для анализа | Локальная инвентаризация |

Файлы мода, копия игры и журналы лежат в **рабочей папке**, отдельно от исходников devkit. Мастерская подключает devkit как submodule; старые команды в её `scripts/` сохранены через переходники к единственной реализации.

## Развернуть стенд

Нужны Windows 10/11, Git, Python 3.10+ x64 и установленная Heroes V: Повелители Орды с Universe. Закрой игру и редактор. Копии потребуется место под игровые архивы, музыку и видео.

В новом каталоге:

```powershell
git clone https://github.com/Xaaalera/heroes5-mod-devkit.git
cd heroes5-mod-devkit
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
$env:H5_WORKSPACE = [IO.Path]::GetFullPath('../heroes5-workspace')
$env:H5_GAME_DIR = (Resolve-Path '../HeroesV-Universe').Path
New-Item -ItemType Directory -Path "$env:H5_WORKSPACE/mods" -Force | Out-Null
Copy-Item examples/menu-marker "$env:H5_WORKSPACE/mods/menu-marker" -Recurse
python -X utf8 scripts/mod-dev.py prepare --sandbox
```

Замени `../HeroesV-Universe` путём существующей установки. Рабочую папку выбирай отдельно от игры. Пример мода копируется один раз; в новом PowerShell нужно заново задать переменные. `prepare` откажется перезаписывать уже существующую тестовую копию.

## Первый цикл: метка в меню

```powershell
python -X utf8 scripts/mod-dev.py build --sandbox --mod menu-marker
python -X utf8 scripts/mod-dev.py deploy --sandbox --mod menu-marker
python -X utf8 scripts/mod-dev.py launch --sandbox --menu
```

Проверь появление `[DEV: menu-marker]`. После выхода из игры выполни:

```powershell
python -X utf8 scripts/mod-dev.py rollback --sandbox --mod menu-marker
```

Следующий запуск должен показать меню без метки. Это короткий контроль всей цепочки: рецепт → H5U → установка → наблюдение → откат. [Почему выбран именно такой опыт](resource-overrides.md).

`--sandbox` здесь обязателен: без него сборщик работает с исходной установкой. Deploy проверяет неизменность входных ресурсов и бинарников; rollback не удалит пакет, изменённый извне.

## Быстрые бои через команды

```powershell
python -X utf8 scripts/test-map.py
python -X utf8 scripts/native-probe.py launch --map WorkshopPolygon --control
python -X utf8 scripts/game_control.py status
python -X utf8 scripts/game_control.py heroes
```

Не считай появление PID готовностью карты. Дождись загрузки и ответа со списком героев. Затем можно подготовить обычное нападение:

```powershell
python -X utf8 scripts/game_control.py teleport Brem 14 50
python -X utf8 scripts/game_control.py interact Brem pack_8
```

Когда виден экран расстановки, `confirm` начинает бой. Для тестового завершения служат `finish --winner 0` и `results`; возврат на карту проверяется через `hero Brem`. Закрытие — `quit`. Это команды вида `python scripts/game_control.py <команда>`, а не горячие клавиши.

Ответ `dispatched` означает отправку, а не завершение. Не повторяй нападение при таймауте вслепую. [Все команды и ограничения](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md).

Полигон содержит восемь фракций, 12 хранилищ, 16 нейтральных армий и шесть сценарных арен. [Скачать уже собранную карту и посмотреть расположение объектов](test-maps.md). Генератор в devkit не требует наших модов и не содержит экспериментальной подписки UniverseTrigger.

## Что проверено при переносе

- 37 тестов devkit: упаковка, хеши и владение файлами, XML, terrain, командный канал в эмуляторе, внешняя рабочая папка.
- 48 прежних проверок мастерской прошли через переходники; общий код не продублирован.
- Полигон собран в пустой рабочей папке без каталога наших модов: 60 объектов, шесть арен, целый ZIP.
- Отдельного живого запуска выделенного комплекта пока не было. Исторические игровые результаты сохранены в [дневнике](../reference/research-diary.md).

Нативные инструменты проверяют хеши четырёх игровых файлов и отказываются работать с другой сборкой. Полная изоляция записей профиля не доказана; запуск EXE может кратко получить фокус. Адресный ввод и физическая мышь — разные проверки. Сам devkit не поставляет предиктор, универсальный SDK плагинов или подтверждение всех арен.

Для работы с этой базой через агента есть [указатель llms.txt](../llms.txt) и [инструкции devkit для агента](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/AGENTS.md).

## Сборка наших модов {#mod-sources}

Эти инструкции предназначены разработчикам, а не игрокам:

- [Предиктор: сборка C++ и запуск](https://github.com/Xaaalera/heroes5-deployment-preview#readme).
- [Справочник хранилищ: сборка H5U и диагностический запуск](https://github.com/Xaaalera/heroes5-bank-reference#readme).

Оба репозитория закрепляют devkit как submodule. README содержат зависимости, точные команды, отключение и границы проверки. Готовых пользовательских выпусков пока нет.
