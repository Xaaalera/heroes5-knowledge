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
updated: 2026-10-08
---
# Наш стенд разработки модов

## Начать с xkit

[xkit v0.1.1-preview.3](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.3) содержит готовый SDK: исходники, Game API и служебные DLL. Нужна установленная игра с Universe. Для ресурсного H5U C++-компилятор не нужен; нативные плагины требуют MSVC Build Tools.

Скачай `xkit-sdk.zip`, распакуй папку `xkit` и установи [uv](https://docs.astral.sh/uv/getting-started/installation/). В терминале внутри папки `xkit` выполни:

```text
uv tool install --editable .
uv tool update-shell
```

Открой новый терминал. `xkit setup` сохранит путь к установленной игре и папке проектов. Затем создай ресурсный проект, запусти его в тестовой копии и собери готовый H5U:

```text
xkit setup
xkit new demo --resources
xkit start demo
xkit release demo
```

Для нативного проекта используй `xkit new demo-native`. Сохранение поддерживаемого C++-кода запускает автоматическую сборку и замену DLL в той же игре. Проверены новое расширение функций/экспорта ядра, состояние, отключение callbacks и откат. Полная перекомпиляция игры не требуется; DLL-код всё равно компилируется.

После создания выполни `xkit start demo-native`. При завершении разработки `xkit release demo-native` собирает отдельный игровой DLL-пакет. Ресурсный `xkit start demo` не обещает автоматическую замену H5U в открытой карте. [Установка и ограничения этой версии](https://github.com/Xaaalera/heroes5-mod-devkit/blob/f5d9a7666635ca478c1481444b6b943d096c2efe/README.md).

### Управление и диагностика

| Команда | Результат |
|---|---|
| `xkit game map WorkshopPolygon` | Запрос загрузки тестовой карты |
| `xkit game restart WorkshopPolygon` | Запрос повторной загрузки указанной карты |
| `xkit game menu` | Запрос возврата в меню |
| `xkit game screenshot` | Новый снимок PNG и путь к файлу |
| `xkit diagnostics` | Состояние SDK и сведения для разбора ошибки |

В подключённом SDK доступны те же команды через игровую консоль. Отправленный запрос загрузки не подтверждает готовность карты. Снимок показывает текущий кадр: карту, меню или заставку. После ошибки захват не повторяется другим способом; диагностический клиент не отключает плагины при выходе. [Справка команд](https://github.com/Xaaalera/heroes5-mod-devkit/blob/f5d9a7666635ca478c1481444b6b943d096c2efe/docs/commands.md).

Каждый ресурсный мод выпускается отдельным H5U, нативный — своей DLL. Общая инфраструктура использует `dinput8.dll` и `d3d9.dll`; оригинальная графическая библиотека игры остаётся локально как `d3d9.universe.dll`. Старые предиктор и справочник не стали HMR-плагинами автоматически. При неподтверждённой очистке SDK останавливает обновления и сохраняет данные для восстановления.

Для справочника теперь добавлен отдельный адаптер разработки: `xkit start army-reference --map WorkshopPolygon`, `xkit build army-reference` и `xkit release army-reference`. В тестовой игре проверены карточка склепа и сохранение заполненного кеша при обновлении DLL и ядра. Несовместимые структуры данных отклоняются. Предиктор остаётся на паузе; этот адаптер не переносит его на HMR.

## Исторические прототипы и границы проверок

Ниже сохранены результаты прежних ревизий. Их оговорки о неопубликованном прототипе не описывают текущий релиз.

**Несколько плагинов:** режим `plugin-watch.py --plugins` следит за папками, подключает новые плагины в той же игре и отключает удалённые. Состояния и ошибки сборки раздельны; добавление cpp/header проверено живым сценарием. Удалённые UI/hooks очищаются, повторное подключение начинает новое состояние. Исходники SDK общие, у каждого плагина отдельный экземпляр собранного моста. Два готовых DLL-пакета также проверены при обычном совместном запуске.

Общие проверки сборки, каталог известных hooks и проверки собственного процесса теперь находятся в отдельной [библиотеке Game API](https://github.com/Xaaalera/heroes5-game-api). Она опубликована после пяти независимых ревью и успешного CI. Предиктор, справочник и devkit используют одну библиотеку без копий исходников. Настройка ревью входит в репозиторий библиотеки; игроку эти инструменты не нужны.

**Приёмка прототипа ABI3 завершена:** текущий код прошёл автоматическую смену функций, UI и проверенного engine CALL hook, сохранение состояния и откат ошибок, затем обычный запуск DLL-пакета из того же исходника. Последний save→UI2.101s; Python51/native4 PASS. Проверка повторяется командой plugin-check.py --live. Поддержанные границы и сохранённые отказы — в [дневнике](../reference/research-diary.md). Изменения ещё не опубликованы.

Локальный прототип от4октября2026 добавляет native watch: сохранение C++ автоматически пересобирает изменённые units и заменяет DLL в той же игре. Проверены оконные callbacks, числовой UI, состояние и откат ошибочной правки; save→UI2.162s в одном опыте. `plugin-watch.py --release` собирает из тех же исходников ZIP с `bin/Heroes5Mods/Plugins/<name>.dll` и общим `bin/dinput8.dll`; обычный запуск проверен без клиента разработки. Эти изменения ещё не опубликованы. Произвольные engine hooks и общий UI API пока не готовы. [Результаты и ограничения](../reference/research-diary.md).

Ресурсные и поддерживаемые игровым контекстом скриптовые моды могут поставляться H5U. Нативный SDK требует DLL/bootstrap; помещение DLL внутрь H5U не запускает её. Существующие предиктор и справочник сохраняют свои legacy-контракты и автоматически reloadable не становятся.

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
- 25 сентября командный стенд использован в пяти боях с автоматическим подключением обеих DLL. Загрузка, карточки и очистка проверены отдельно от точности прогноза; результаты и расхождения сохранены в [дневнике](../reference/research-diary.md#dll-delivery).

Нативные инструменты проверяют хеши четырёх игровых файлов и отказываются работать с другой сборкой. Полная изоляция записей профиля не доказана; запуск EXE может кратко получить фокус. Адресный ввод и физическая мышь — разные проверки. Сам devkit не поставляет предиктор, универсальный SDK плагинов или подтверждение всех арен.

Для работы с этой базой через агента есть [указатель llms.txt](../llms.txt) и [инструкции devkit для агента](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/AGENTS.md).

## Сборка наших модов {#mod-sources}

Эти инструкции предназначены разработчикам, а не игрокам:

- [Предиктор: сборка C++ и запуск](https://github.com/Xaaalera/heroes5-deployment-preview#readme).
- [Справочник хранилищ: сборка DLL и H5U](https://github.com/Xaaalera/heroes5-bank-reference#readme).

Оба репозитория закрепляют devkit как submodule. README содержат зависимости, точные команды, отключение и границы проверки. [Готовые DLL-пакеты](../players/mods.md) устанавливаются без инструментов разработки.

## Обычный запуск с DLL {#dll-autoload}

Общий [dinput8.dll из devkit](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/mod_loader.cpp) подключает известные DLL из bin/Heroes5Mods и передаёт DirectInput штатной библиотеке Windows. Отдельный EXE для игрока не используется. Ошибка инициализации отменяет запуск, чтобы игра не продолжала работу с частью модов.

Для тестового полигона и наблюдения Start используется `native-probe.py launch --map WorkshopPolygon --control --observe-deployment`. Это диагностическая подготовка обычного игрового процесса, не пользовательский способ установки. Не добавляй старый `--native-loader` поверх DLL-подключения.
