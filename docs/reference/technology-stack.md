---
content_type: meta
status: draft
faction: academy
title: Технологии проекта
lang: ru
section: reference
kicker: РАЗРАБОТЧИКАМ
translation: en/reference/technology-stack/
description: Что уже используется в SDK, модах, исследованиях и на сайте.
updated: '2026-10-08'
---
# Технологии проекта

Перед добавлением инструмента или библиотеки проверь этот список и соответствующий код. Сначала используй существующий компонент; новую зависимость добавляй для конкретной задачи, которую он не решает. Обновляй список вместе с изменением зависимости.

## Уже используется

| Область | Технологии | Назначение |
|---|---|---|
| Игра и нативные модули | C++20, Windows API, x86 | DLL, процессы, ввод, игровые привязки и нативный SDK |
| Сборка DLL | MSVC, CMake | Сборка 32-битных модулей и изолированных проверок |
| Общая библиотека | Наш Game API | Проверки версии игры, известные hooks и общие привязки; сначала ищи нужное здесь |
| Перехват в SDK | MinHook | Уже подключён к нативному загрузчику SDK для hook справочника; это не завершённый перенос предиктора |
| Инструменты SDK | Python 3.10+ | Команды xkit, подготовка стенда, сборка, управление и наблюдение |
| Командная строка | Typer, Click, Rich | Команды, справка и читаемый вывод; Rich также используется через зависимости Typer |
| Локализация | gettext, Babel | Русские и английские сообщения; gettext входит в стандартную библиотеку Python |
| Журналы и блокировки | logging, structlog, concurrent-log-handler, portalocker | Структурированные события, ротация журналов и блокировки файлов |
| Нативная консоль | Dear ImGui, ImTerm, ImGuiColorTextEdit, DirectX 9 | Окно, терминал, редактор команд и отрисовка |
| Нативный JSON | nlohmann/json | Разбор структурированных сообщений консоли |
| Анализ и проверки | Keystone, Unicorn, pefile, Capstone | Машинный код, эмуляция, чтение PE и дизассемблирование |
| Сайт | MkDocs, Jinja, JavaScript, SCSS/Sass | Статические статьи, шаблоны, поиск и оформление |
| Изображения | Pillow, PNG, AVIF, SVG | Исходные фоны, сжатые копии и схемы; оригинальные PNG сохраняются |
| Проверки | unittest, CTest, Node.js, Playwright | Проверки Python/C++, ревью и браузерные сценарии |
| Проверка публикации | bladeforge-review-harness, Husky | Ревью перед push; Husky используется в корневой мастерской |
| Упаковка SDK | setuptools | Установка Python-пакета и команд xkit |
| Версии и публикация | Git, GitHub Actions, GitHub Pages | Канонические репозитории, проверки и выкладка сайта |
| Windows-автоматизация | PowerShell | Управление окнами и проверки физического ввода в собственной тестовой игре |

Это список инструментов разработчика. Он не означает, что игроку с готовым DLL/H5U-пакетом нужно устанавливать Python, Node.js или компилятор.

## Где закреплены версии

Не поддерживаем второй набор номеров вручную: точные версии и закреплённые ревизии задают манифесты.

- [Зависимости SDK](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/requirements.txt), [проверки SDK](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/requirements-dev.txt), [Python-пакет](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/pyproject.toml).
- [Зависимости нативной консоли](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/console_module.cmake): ревизии и хеши архивов.
- [Нативный SDK и MinHook](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/CMakeLists.txt): подключение, закреплённая ревизия и хеш архива.
- [Проверки предиктора](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/requirements-dev.txt).
- [Python-зависимости сайта](https://github.com/Xaaalera/heroes5-knowledge/blob/main/requirements.txt), [Node.js-инструменты сайта](https://github.com/Xaaalera/heroes5-knowledge/blob/main/package.json).
- [Происхождение изображений и лицензии](https://github.com/Xaaalera/heroes5-knowledge/blob/main/NOTICE.md).

## При изменении стека

1. Найди существующее решение в канонических репозиториях и стандартной библиотеке языка или Windows API.
2. Если нужна новая зависимость, запиши задачу, место использования и причину выбора. Проверь совместимость, лицензию и способ закрепления версии.
3. Обнови манифест, этот список и необходимую инструкцию в одной серии изменений. Удалённый инструмент убери из списка, когда код перестал его использовать.
4. До публикации проверь список по коду и манифестам. Изученный вариант не называй подключённой технологией.

**MinHook уже используется в SDK для hook справочника. Перенос всех hooks предиктора на этот механизм ещё не завершён. Microsoft Detours только исследован и не подключён.** Буфер состояния текущего прототипа использует Windows API.
