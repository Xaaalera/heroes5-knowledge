# Repository instructions / Инструкции репозитория

## Problem-solving order

Current release / Текущий выпуск: [xkit preview.4](https://github.com/Xaaalera/heroes5-mod-devkit/releases/tag/v0.1.1-preview.4), SDK `0c406f4`, Game API `a71985c`, hosted CI37726287809 success. Exact public archive installation, source HMR and same-source native release passed; latest diary preserves timings and original no-SDK resource baseline failure. Bank preview.4 has a separate one-Crypt/RU1024×768 player-card check after ordinary startup; diagnostic positioning is disclosed. Preserve older dated entries below. Do not transfer this scope to all maps, banks, input gestures or no-SDK H5U acceptance.

For every problem, first search our logs, research, backlog and handoff for prior occurrences, attempts, solutions and their verified conditions. Then research the web when needed for causes, documentation, existing solutions and libraries. Only then choose an approach and act. Repeat known experiments only for a new hypothesis or changed conditions. Record links, conclusions and verification limits in the existing log.

RU, 2026-10-07: xkit 0.1.0 опубликован с готовым SDK. Новый нативный плагин выпускается своей DLL, ресурсный мод — своим H5U. Общие dinput8.dll/d3d9.dll обеспечивают подключение, исходная графическая библиотека остаётся локально как d3d9.universe.dll. Существующие предиктор/справочник не переведены на HMR автоматически. Старые записи о wsock32 и неопубликованном прототипе сохраняют историческую область.
EN: xkit 0.1.0 is published with a ready SDK. Native plugins ship separately as DLLs and resource mods as H5U. Shared dinput8.dll/d3d9.dll retain the game original locally as d3d9.universe.dll. Existing predictor/reference plugins are not automatically migrated to HMR. Older wsock32/unpublished-prototype records retain historical scope.


[Game API](https://github.com/Xaaalera/heroes5-game-api) — shared C++ game bindings / общая библиотека привязок к игре.


## Public projects / Публичные проекты

- [Deployment Preview / Предиктор](https://github.com/Xaaalera/heroes5-deployment-preview): native placement projections.
- [Bank Reference / Справочник армий](https://github.com/Xaaalera/heroes5-bank-reference): possible bank armies.
- [Mod Devkit / Девкит](https://github.com/Xaaalera/heroes5-mod-devkit): shared tools used to build and test both DLL mods.
- [Knowledge / База знаний](https://github.com/Xaaalera/heroes5-knowledge) · [public site / сайт](https://xaaalera.github.io/heroes5-knowledge/).
- [Author / Автор — Xaaalera](https://github.com/Xaaalera) · [email](mailto:dampirsimpl@gmail.com) · [personal Telegram / личный Telegram](https://t.me/Victima).
- [Heroes V Universe / Heroes Lobby](https://h5lobby.com/).

RU: эти проекты принадлежат автору; база знаний и моды не являются официальными продуктами Universe. Общие факты и контакты обновлять во всех канонических репозиториях. EN: These are the author's projects, not official Universe products. Keep shared facts and contact links consistent across canonical repositories.

## RU

- При работе внутри связанной мастерской каждый сабрепозиторий имеет один канонический checkout. Общие зависимости используются через ссылки каталогов; не клонировать второй SDK и не переносить правки между копиями. Перед работой из корня мастерской выполнять `scripts/sync-subrepos.ps1 -Check`. Для самостоятельного клона этой базы процедура мастерской не требуется.

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

- Inside a linked workshop, each subrepo has one canonical checkout and repeated dependencies use directory junctions. Never clone another SDK or copy edits between checkouts. Run the workshop's `scripts/sync-subrepos.ps1 -Check` before work. Standalone knowledge clones do not need workshop setup.

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

## Standalone use / Работа вне мастерской

RU: этот репозиторий можно использовать отдельно. Начни с его README и AGENTS.md; глобальная папка мастерской не обязательна. Если есть .gitmodules, выполни `git submodule update --init --recursive` после клонирования. В связанной мастерской используй её sync-subrepos вместо создания вторых checkout.
EN: This repository can be used independently. Start with its README and AGENTS.md; the global workshop is optional. If .gitmodules exists, initialize pinned dependencies with `git submodule update --init --recursive`. In a linked workshop use its canonical dependency synchronization.

- [Devkit commands / команды SDK](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/docs/commands.md).
- [Game API contracts / контракты библиотеки](https://github.com/Xaaalera/heroes5-game-api/blob/main/docs/mechanisms/game-bindings.md).
- [Research index / карта исследований](https://xaaalera.github.io/heroes5-knowledge/reference/research-index/).

## Code standards / Стандарты кода

RU: перед новой правкой применяй подходящие установленные скиллы из [маркетплейса автора](https://github.com/Xaaalera/claude-skills). Имена переменных/параметров должны объяснять смысл; не использовать непрозрачные сокращения. C++ сохраняет calling convention, lifetime и ABI; Python использует описательные snake_case имена. Обязательные имена API/protocol/register и общепринятые PID/DLL/ABI сокращения допустимы. JS правила не переносить механически на C++/Python.
EN: Load the applicable guides before coding/reviewing. Use descriptive names, small functions with one responsibility, canonical dependencies and no speculative abstractions. Preserve native ABI/protocol compatibility during readability changes. Existing code is changed when relevant, not mass-renamed by this policy.

- All code: [solid](https://github.com/Xaaalera/claude-skills/blob/main/plugins/meta/skills/solid/SKILL.md), [ockham](https://github.com/Xaaalera/claude-skills/blob/main/plugins/meta/skills/ockham/SKILL.md).
- JS/TS only: [conventions](https://github.com/Xaaalera/claude-skills/blob/main/plugins/frontend-js/skills/conventions/SKILL.md).
- Tests: Codex alias `tests-architecture`, upstream [tests:architecture](https://github.com/Xaaalera/claude-skills/blob/main/plugins/tests/skills/architecture/SKILL.md).
- Documents: [standard](https://github.com/Xaaalera/claude-skills/blob/main/plugins/docs/skills/standard/SKILL.md), [lean-writing](https://github.com/Xaaalera/claude-skills/blob/main/plugins/meta/skills/lean-writing/SKILL.md), [wittgenstein](https://github.com/Xaaalera/claude-skills/blob/main/plugins/meta/skills/wittgenstein/SKILL.md).
- Changed user-facing UI: [ui-strings](https://github.com/Xaaalera/claude-skills/blob/main/plugins/i18n/skills/ui-strings/SKILL.md), [responsive-layout](https://github.com/Xaaalera/claude-skills/blob/main/plugins/frontend-css/skills/responsive-layout/SKILL.md).
- New public JSON error boundaries: [format](https://github.com/Xaaalera/claude-skills/blob/main/plugins/error/skills/format/SKILL.md); version changes explicitly, do not silently reinterpret native status words.
- Reviewers load every applicable guide listed in .claude/review.config.json. If a guide is not installed, read the canonical source above and report availability honestly. Do not vendor independent copies of these standards.

## Human-usable functionality / Использование человеком

RU/EN: No raw memory addresses, pointer/structure byte offsets or address-derived disassembler labels in published human documents. Use meaningful names and explain function/event/type roles. Numeric evidence stays in code/private logs. Owner authorizes readability edits to historical articles: preserve complete private originals and dated conclusions. Enforce this in docs review.

RU/EN: infrastructure descriptions must identify the standard language facility or maintained library actually used. Do not describe an unimplemented integration as available. SDK logging records need contextual structured events plus readable diagnostics; raw output belongs in linked local artifacts.

RU: весь функционал проекта должен быть пригоден для самостоятельного использования человеком без AI. Основной сценарий требует понятного входа, справки, разумных настроек по умолчанию, видимого состояния и ошибок с действием для исправления. Цепочка внутренних Python/PowerShell/RPC команд не заменяет пользовательский интерфейс. Разработчик должен уметь подготовить окружение, создать/запустить/обновить плагин и получить готовый мод по документации самостоятельно.
EN: Every feature must be usable by a person without an AI agent. Provide a clear entry point, help, sensible defaults, observable progress and actionable errors. Internal scripts/RPC sequences may support diagnostics but do not satisfy the main user workflow. Acceptance includes following the documented workflow as a human; never document a planned friendly command as already implemented. This is a project rule, not a new skill.

RU: правило также относится к README, документации, справке, описаниям, примерам и сообщениям. Писать для указанной аудитории простым языком: зачем функция нужна, как начать, какой результат ожидается, как исправить ошибку. Объяснять термины при первом использовании; внутренние механизмы выносить в документацию разработчика. Инструкция не должна требовать AI для расшифровки или поиска пропущенных шагов.
EN: Apply the same rule to README, documentation, help, descriptions, examples and messages. Explain purpose, starting steps, expected result and recovery in language appropriate to the reader. Define unfamiliar terms on first use; keep internals in developer documentation. A person must be able to follow the instructions without AI filling missing steps.
