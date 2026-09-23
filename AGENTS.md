# Repository instructions / Инструкции репозитория

## RU

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
