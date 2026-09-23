# База знаний Xaaalera о Героях

## RU

Личные заметки, исследования и руководства по Heroes V. Предварительный показ оформления; статьи — стартовые черновики, содержание дорабатывается. Материалы для игроков, первые шаги моддинга и справочник файлов.

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
python -m mkdocs serve
```

`site/` и скомпилированный CSS не редактируются и не коммитятся. После правки SCSS выполнить `npm run styles`; MkDocs serve следит за статьями и темой. Публикация Pages выполняется workflow этой репы.

### Проверка и ограничения

Проверка сборки ищет сломанные ссылки, пропавшие переводы и приватные пути. Playwright проверяет навигацию, поиск, переключение языка и переполнение на пяти ширинах. Результаты скриншотов остаются локальными тестовыми артефактами.

Начальные статьи не являются полным справочником движка. Дизайн не копирует игровые ресурсы. Гостевого wiki-редактирования пока нет — предложения идут через GitHub.

Подробнее: [CONTRIBUTING](CONTRIBUTING.md), [AGENTS](AGENTS.md), [источники иллюстраций и шрифтов](NOTICE.md).

## EN

Xaaalera’s personal notes, research, and guides about Heroes V. This is a design preview with initial draft articles; the content is being developed. The site includes player guides, first modding steps, and a file reference.

The site URL and commands above apply to both languages. Requires Python 3.10+ and Node.js 22+. Markdown articles are the only content source; the site builds independently of any private workspace.

Presentation lives in `theme/` and `styles/`; generated `site/` and CSS are not committed. Run `npm run styles` after changing SCSS. MkDocs serve watches articles and the theme; this repo's Pages workflow publishes the site.

Checks cover local links, translations and private paths. Browser tests exercise navigation, search, language switching and overflow at five widths. Screenshots remain local test artifacts.

The initial articles are not a complete engine reference. Art is original, not extracted game resources. Direct wiki editing is not available; proposed changes use GitHub. See the shared contribution, agent and asset documentation links above.

### Фоны / Backgrounds

Восемь фракционных замков служат фоном всего окна. Поле `faction` в метаданных статьи выбирает изображение из `docs/assets/worlds/` и цветовой акцент. Фон меняется при навигации; обновление страницы и смена языка сохраняют фракцию. Названия фракций: `extra.worlds` в `mkdocs.yml`.

Eight faction castles fill the viewport behind the content. Article metadata `faction` selects an image from `docs/assets/worlds/` and its accent color. Navigation changes the background; reloads and language changes preserve the faction. Localized names live in `mkdocs.yml` under `extra.worlds`.
