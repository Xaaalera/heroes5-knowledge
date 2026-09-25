# Repository instructions / Инструкции репозитория

## RU

- Пользователь запускает игру обычным способом через Heroes/Lobby. Наши моды подключаются через DLL; отдельный EXE для игрока запрещён владельцем. Диагностические EXE и Python-команды принадлежат только инструкциям разработчика. При смене поставки синхронизировать README, RU/EN wiki, devkit, инструкции агентам и release notes; прежние EXE-пакеты не публиковать.

### Быстрая проверка агентом

1. Для проверки утверждения читай метаданные статьи, указанную сборку, запись дневника и артефакт. Ссылки на исходники доступны через `docs/llms.txt`; HTML страниц содержит Markdown alternate. Не объявляй гипотезу подтверждённой по одному пересказу.
2. Для правки клона сначала выполни `git status --short` и `git rev-parse HEAD`, затем прочти CONTRIBUTING.md. Не включай чужие незавершённые изменения в свой коммит.
3. Подготовка сайта: `python -m pip install -r requirements.txt`, `npm ci`, `npx playwright install chromium` (в Linux может потребоваться системная установка зависимостей Chromium). Проверки: `npm run build`, `npm run check`, `npm test`.
4. Игровые инструменты проверяются в отдельном devkit по его AGENTS.md; тесты сайта не проверяют игру. Редактура не обновляет дату реального игрового опыта.
5. Итог проверки содержит ревизию, область, выполненные команды/коды выхода, результаты и пропуски, пути или ссылки на доказательства и явно непроверенные части. Сохраняй хеш опубликованных байтов, а не только Windows-копии текста.


- После значимого исследования или исправления вывода обновлять [дневник](docs/reference/research-diary.md) и EN-пару по CONTRIBUTING. Статьи ссылаются на записи; не переписывать старые технические наблюдения без датированной поправки. Ретроспективный пересказ не выдавать за сырой лог.

- Механика расположения требует полных 2D-схем по CONTRIBUTING. Сетки генерируются циклом из координат обеих армий и препятствий; не рисовать клетки вручную. Для статьи о расстановке источник — `docs/assets/placement/observations.json`, генератор — `npm run figures`.

- Перед каждым push выполнить протокол независимого агента из CONTRIBUTING: получить полный `docs.review` по восьми критериям и всем Markdown-файлам review:info. Без отчёта push запрещён; не обходить хук и не выдумывать PASS. `npm ci` устанавливает pre-push hook; отчёт хранится в аттестации.

- Обязательный стандарт статей — [CONTRIBUTING.md](CONTRIBUTING.md). Читать перед написанием и docs-review. Оценивать все изменённые статьи по его приёмке; зелёные машинные проверки не подтверждают факты. Не менять `draft` на `verified` без независимой содержательной проверки.

- Это публичная личная база знаний Xaaalera о Героях. Не называть её официальной вики или состоявшимся сообществом.
- Статьи — только `docs/`, английские пары — `docs/en/`. Общие факты менять в обеих версиях. UI-строки — `extra.labels` в `mkdocs.yml`.
- `theme/` и `styles/` отвечают за представление. Сохранять Markdown переносимым; не дублировать статьи в HTML.
- Не добавлять игровые архивы, чужие закрытые материалы, приватные пути, токены, профили и сырые рабочие журналы.
- Дизайн: оригинальный pixel art в иллюстрациях и декоре; обычный читаемый шрифт для длинного текста и кода. Контрольные ширины: 320, 390, 768, 1088, 1440 CSS px. Размеры интерфейса задавать в rem.
- Перед публикацией: `npm run build`, `npm run check`, `npm test`. Независимые read-only линзы craft, architecture, tests, docs, security проверяют точный diff; результаты записываются через `npm run review:attest -- <results.json>`, затем `npm run review:gate`. Не выдумывать оценки/аттестации.
- Изменение сборки или темы сопровождается обновлением README/CONTRIBUTING. Отправлять только файлы этой публичной репы.
- GitHub Pages — первый этап. Правки через GitHub, а не через встроенный wiki-редактор. Не обещать реализованный MCP или SDK.

## EN

- Players keep the ordinary Heroes/Lobby launch. Our mods load through DLLs; the owner rejects separate player launchers. Diagnostic EXEs and Python commands belong only in developer instructions. Delivery changes must update README, RU/EN wiki, devkit, agent instructions and release notes together; never publish the superseded EXE packages.

### Agent verification entry point

1. To assess a claim, read article metadata, build identity, diary entry and evidence artifact. `docs/llms.txt` links source documents and each HTML page exposes a Markdown alternate. A summary alone does not establish a hypothesis.
2. Before editing a checkout, run `git status --short` and `git rev-parse HEAD`, then read CONTRIBUTING. Preserve unrelated work.
3. Prepare with `python -m pip install -r requirements.txt`, `npm ci`, `npx playwright install chromium` (Linux may need Chromium system dependencies). Run `npm run build`, `npm run check`, `npm test`.
4. Check game tools separately under devkit AGENTS.md; site tests do not test gameplay. An editorial change does not change an experiment's actual date.
5. Report revision, scope, executed commands/exit codes, results/skips, evidence paths or links, and unverified parts. Hash published bytes rather than only a Windows text checkout.


- After significant research or a corrected conclusion, update the [diary](docs/en/reference/research-diary.md) and RU pair under CONTRIBUTING. Articles link to records; preserve prior technical observations through dated corrections. Never present a retrospective summary as a raw log.

- Spatial mechanics require complete 2D diagrams under CONTRIBUTING. Generate cells in loops from both armies and obstacles; never hand-place grid cells. Placement article data lives in `docs/assets/placement/observations.json`; regenerate with npm run figures.

- Before every push follow CONTRIBUTING’s independent-agent protocol: obtain full docs.review for all eight criteria and review:info Markdown paths. Never bypass the hook or fabricate PASS; missing review blocks push. npm ci installs the pre-push hook; the attestation stores the report.

- [CONTRIBUTING.md](CONTRIBUTING.md) owns the mandatory article standard. Read it before authoring and docs-review; assess every changed article against its acceptance criteria. Machine checks do not establish factual correctness. Never promote draft to verified without independent content verification.

- This is Xaaalera’s public personal knowledge base about Heroes. Do not present it as an official wiki or an established community.
- Articles live only in `docs/`, with English counterparts in `docs/en/`. Keep facts aligned in both languages. UI strings live in `mkdocs.yml` under `extra.labels`.
- `theme/` and `styles/` own presentation. Keep Markdown portable; do not duplicate articles in HTML.
- Do not add game archives, others' private content, private paths, tokens, profiles, or raw work logs.
- Design: original pixel art for illustrations and decoration; readable normal fonts for prose and code. Check 320, 390, 768, 1088 and 1440 CSS-pixel widths. Use rem for layout dimensions.
- Before publishing: run build, check and browser tests. Independent read-only craft, architecture, tests, docs and security reviews cover the exact diff; record actual judgments with review:attest, then run review:gate. Never fabricate reviews.
- Build/theme changes update README/CONTRIBUTING. Push only files belonging to this public repository.
- GitHub Pages is stage one. Contributions use GitHub, not direct wiki editing. Do not claim MCP or SDK is implemented.
