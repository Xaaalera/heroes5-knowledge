# База знаний Xaaalera о Героях

## RU

[Дневник исследований](docs/reference/research-diary.md) хранит датированные опыты и ссылки на исходные результаты; статьи дают отредактированное объяснение. Правила ведения — в CONTRIBUTING.

Подготовленные результаты исследования Heroes V Universe: игровые механики, ресурсы, скрипты, нативный интерфейс и воспроизводимые примеры. Вход по темам — [карта знаний](docs/reference/research-index.md).

- Сайт: https://xaaalera.github.io/heroes5-knowledge/
- Статьи: `docs/`; английские версии: `docs/en/`.
- Оформление: Jinja-шаблон `theme/main.html`, SCSS `styles/`, браузерный поиск `theme/assets/site.js`.
- Единственный источник статьи — Markdown. Сайт собирается самостоятельно, без приватной мастерской.

### Сборка

Нужны Python 3.10+ и Node.js 22+.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
npm ci
npm run build
npm run check
npx playwright install chromium
npm test
python -m mkdocs serve --watch-theme
```

`site/` и скомпилированный CSS не редактируются и не коммитятся. После правки SCSS выполнить `npm run styles`; MkDocs serve следит за статьями и темой. Публикация Pages выполняется workflow этой репы.

Обязательные требования к структуре, доказательствам, статусам и редакторской приёмке: [стандарт в CONTRIBUTING](CONTRIBUTING.md). Статус `draft` сохраняет явно указанные границы исследования; успешная сборка не подтверждает факты.

### Проверка и ограничения

Проверка сборки ищет сломанные ссылки, пропавшие переводы и приватные пути. Playwright проверяет навигацию, поиск, переключение языка и переполнение на пяти ширинах. Результаты скриншотов остаются локальными тестовыми артефактами.

Материалы не являются полной спецификацией движка. Фоны оригинальные; игровые кадры и их происхождение перечислены в NOTICE. Гостевого wiki-редактирования пока нет — предложения идут через GitHub.

Подробнее: [CONTRIBUTING](CONTRIBUTING.md), [AGENTS](AGENTS.md), [источники иллюстраций и шрифтов](NOTICE.md).

## EN

The [research diary](docs/en/reference/research-diary.md) stores dated experiments and links to source results; articles provide edited explanations. CONTRIBUTING defines the recording rules.

Xaaalera’s personal notes, research, and guides about Heroes V. Prepared findings cover game mechanics, resources, scripts, native UI and reproducible examples. Start with the [knowledge map](docs/en/reference/research-index.md).

The site URL and commands above apply to both languages. Requires Python 3.10+ and Node.js 22+. Markdown articles are the only content source; the site builds independently of any private workspace.

Presentation lives in `theme/` and `styles/`; generated `site/` and CSS are not committed. Run `npm run styles` after changing SCSS. MkDocs serve watches articles and the theme; this repo's Pages workflow publishes the site.

The mandatory article standard and editorial acceptance live in [CONTRIBUTING](CONTRIBUTING.md). Draft status retains stated research limits; successful builds do not verify factual claims.

Checks cover content metadata, local links, translations and private paths. Browser tests exercise navigation, search, language switching and overflow at five widths. Screenshots remain local test artifacts.

This is not a complete engine specification. Background art is original; game screenshots and provenance are listed in NOTICE. Direct wiki editing is not available; proposed changes use GitHub. See the shared contribution, agent and asset documentation links above.

### Фоны / Backgrounds

Восемь фракционных замков служат фоном всего окна. Поле `faction` в метаданных статьи выбирает изображение из `docs/assets/worlds/` и цветовой акцент. Фон меняется при навигации; обновление страницы и смена языка сохраняют фракцию. Названия фракций: `extra.worlds` в `mkdocs.yml`.

Eight faction castles fill the viewport behind the content. Article metadata `faction` selects an image from `docs/assets/worlds/` and its accent color. Navigation changes the background; reloads and language changes preserve the faction. Localized names live in `mkdocs.yml` under `extra.worlds`.

Перед push / Before push: `npm ci` installs the Git pre-push gate. Follow the independent agent protocol in [CONTRIBUTING](CONTRIBUTING.md): a docs score alone is insufficient; the hash-bound report must cover all eight criteria and changed Markdown files. / `npm ci` устанавливает pre-push gate. Одной оценки docs недостаточно: нужен независимый отчёт по восьми критериям и всем изменённым Markdown-файлам.

### Placement diagrams / Схемы расстановки

`docs/assets/placement/observations.json` owns recorded coordinates of both armies and blocked cells. `npm run figures` generates complete SVG grids with labelled X/Y axes; edit data/generator, not individual SVG cells. `npm run check` rejects stale diagrams and invalid/overlapping footprints. Screenshots are separate evidence; instructional overlays are labelled in the article.

JSON — единственный источник записанных координат обеих армий и препятствий. `npm run figures` строит полные SVG-сетки циклом; вручную SVG-клетки не править. Проверка отклоняет устаревшие схемы, выход за границы и пересечения фигур. Скриншоты дополняют схемы; учебные слои подписаны отдельно.

The placement article includes `docs/assets/placement/placement_walkthrough.py`, an executable, scoped reconstruction. Tests compare two recorded fields and all seven native attempts in the traced elemental case. The reconstruction never consumes recorded neutral target cells; they are independent comparison data. / Исполняемый разбор сверяется с двумя записанными полями и семью попытками игры. Итоговые клетки нейтралов служат только независимым результатом для сравнения, не входом расчёта.

The walkthrough distinguishes recorded mode flags from an explicit `assumed_context`. Missing flags without that argument fail; the older field comparison is conditional, not evidence of its selected branch. / Код различает записанный режим и явно заданное предположение. Отсутствующий режим без assumed_context вызывает отказ; совпадение клеток старого поля не доказывает выбранную игрой ветку.

Python bytecode/cache directories are excluded from MkDocs output and rejected by the generated-site check. The downloadable walkthrough `.py` remains a public source file. / Кэш и байткод Python исключены из сайта и запрещены проверкой сборки; скачиваемый `.py` остаётся доступным исходником.

Browser tests start a dedicated non-live-reloading server on port 8769 and do not reuse the interactive preview. / Браузерные проверки запускают отдельный сервер без live reload на 8769 и не переиспользуют интерактивный preview со старым CSS.

### Agent entry points / Входы для агентов

RU — `docs/llms.txt` — короткий указатель на исходный Markdown, devkit и доказательства. Шаблон страницы даёт `rel="describedby"` на этот файл и `rel="alternate" type="text/markdown"` на соответствующий исходник статьи в GitHub. Копии статей не храним. Ветка main может опережать развёрнутый сайт: при проверке фиксировать ревизию. AGENTS.md содержит порядок проверок. `docs/llms.txt` включён в обязательный docs-review наравне с Markdown-файлами. `npm run check` проверяет наличие llms.txt и локальные исходники его ссылок; браузерный тест проверяет обнаружение на RU/EN-страницах с префиксом Pages. Обнаружение указателя зависит от клиента; не обещаем автоматическое чтение каждым агентом.

EN — `docs/llms.txt` indexes source Markdown, devkit and evidence. Page metadata links it with describedby and links the corresponding GitHub Markdown source with alternate/type=text/markdown. No duplicate article copies are maintained. Main may precede a deployed site, so record revisions during verification. AGENTS.md defines check order. Mandatory docs-review includes `docs/llms.txt` alongside Markdown files. `npm run check` validates llms.txt and its own-repository source targets; a browser test checks discovery on RU/EN pages under the Pages prefix. Client discovery varies; automatic loading by every agent is not guaranteed.

Format references / описание форматов: [llms.txt proposal](https://llmstxt.org/) · [AGENTS.md](https://agents.md/).
