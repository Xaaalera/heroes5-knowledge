# Contributions / Вклад в базу

## RU

### Обязательный стандарт содержания

Применяется ко всем статьям `docs/` и их переводам. Основа: [Diátaxis](https://diataxis.fr/), [Good Docs: инструкции](https://www.thegooddocsproject.dev/template/how-to), [справка](https://www.thegooddocsproject.dev/template/reference), [Google: процедуры](https://developers.google.com/style/procedures), [Factorio: игровые страницы](https://wiki.factorio.com/Factorio:Style_guide). Это адаптация для базы Heroes, а не требование этих проектов.

1. **Назначение.** Одна страница отвечает на конкретный вопрос или решает одну задачу. Начало даёт ответ/результат и границы. Заголовок не обещает больше, чем текст выполняет.
2. **Конкретность.** Абзац содержит факт, действие, объяснение причины, пример или существенное ограничение. Удалять общие вступления, самопохвалу и пересказ заголовка. Не сокращать необходимые объяснения ради объёма.
3. **Воспроизводимость.** В инструкции указаны среда, точные действия, пути/кнопки/команды и ожидаемый результат. Подстановки подписаны. Ссылка «следуй инструкции автора» не заменяет обещанную процедуру.
4. **Применимость.** Различать игру, дополнение, мод и сборку. Не переносить проверку одной сборки Universe на все Heroes V. Редактирование текста не означает повторной проверки игры.
5. **Доказательства.** Спорные и версионные факты сопровождаются источником рядом с утверждением либо воспроизводимым опытом. Статические определения не доказывают все варианты поведения в игре. Гипотеза, наблюдение и подтверждённый механизм обозначаются отдельно.
6. **Данные.** Указывать единицы, условия, исключения; нативные адреса и вызовы привязывать к точной сборке/хешу. Не выдумывать числа, пути и поддержку версий ради заполнения шаблона.
7. **Связность.** У факта/таблицы один основной источник в базе; другие статьи ссылаются на него. Допустим краткий контекст. Термины и игровые названия единообразны; RU/EN сообщают одинаковые факты.
8. **Доступность.** Публичная статья не требует доступа к приватному журналу. Подготовить публичное доказательство или обозначить ограничение. Скриншоты нужны для действия/сравнения, а не вместо объяснения.

### Виды страниц и каркас

| `content_type` | Назначение | Что читатель должен получить |
|---|---|---|
| `tutorial` | Обучение на одном примере | Подготовка, управляемые шаги, контрольные точки, завершённый результат |
| `how-to` | Решение конкретной задачи | Предусловия, действия, проверка результата, известные сбои/откат при необходимости |
| `reference` | Точные сведения | Определение, таблица/структура, единицы/значения, исключения, происхождение данных |
| `explanation` | Объяснение механизма | Краткий ответ, причинная связь, пример, границы и неизвестное |
| `landing` | Входная страница | Навигация по реально существующим материалам |
| `meta` | О базе и участии | Действующие правила и точные способы участия |

Первые четыре — типы статей Diátaxis. Последние два обозначают служебные страницы. Тип не обязывает создавать отдельный пункт меню. Названия разделов выбираются по содержанию; пустые заголовки запрещены.

### Метаданные и статус

- Каждая страница задаёт `content_type` и `status`: `draft`, `verified` или `outdated`. `draft` разрешён в предварительном показе, но не считается соответствием всем содержательным требованиям.
- Для `verified` и `outdated` статей первых четырёх типов обязательны: `scope` (непустое описание применимости), `verified_on` (дата реальной проверки, YYYY-MM-DD) и `sources` (непустой список HTTPS-ссылок на публичные источники/воспроизводимые отчёты). Старую дату у `outdated` не обновлять без проверки.
- Служебные `landing`/`meta` не требуют искусственной игровой версии или научных источников. Их факты и ссылки всё равно проверяются редактором.
- `lang`, `translation`, `faction`, `content_type`, `status` согласуются в RU/EN-паре. `translation` — адрес от корня сайта, обратная ссылка ведёт к исходной странице. Применимость и доказательства перевода должны соответствовать оригиналу.
- Любое изменение технического поведения требует повторной проверки затронутого материала либо статуса `draft`/`outdated`. Старые наблюдения сохраняются как исторические, а не переписываются под новый результат.

### Приёмка

**Машина:** `npm run check` проверяет метаданные, связи RU/EN, даты/источники проверенных статей, ссылки/якоря и границу публичного содержимого. Неизвестные статусы, битые пары и неполные verified-записи блокируют проверку. Вывод отдельно считает черновики и устаревшие страницы; зелёная сборка не означает, что они проверены по существу.

**Редактор:** для каждой изменённой статьи docs-review фиксирует: вопрос читателя; выполнено ли обещание заголовка; какие существенные утверждения сверены и с чем; можно ли выполнить действия; соответствуют ли версии и RU/EN; какие ограничения остались. Указывает пути проверенных статей. Неточные факты, невыполнимая процедура и неподтверждённое `verified` блокируют приёмку. Отдельно перечисляет черновики, а не выдаёт им знак готовности.

Перед статусом `verified` инструкция проходит выполнение другим читателем/проверяющим без устных подсказок. Для справки сверяются ключевые значения и источники; для объяснения — логика и пример. Количество заголовков/слов, отсутствие запрещённых слов или положительная оценка ИИ не заменяют эту проверку. Автор не объявляет собственную статью проверенной лишь по факту генерации.

Текущие стартовые страницы — `draft`. Перерабатывать их по этому стандарту, начиная с трёх эталонов: инструкция, справка, объяснение. Полнота сайта не достигается созданием пустых разделов.


Исправления и дополнения принимаются через issues и pull requests. Начни с одной страницы и одного проверяемого изменения. Укажи версию игры и способ проверки технического утверждения.

Парные страницы RU/EN должны сообщать одинаковые факты. `translation` в метаданных — URL соответствующей страницы от корня сайта; `section` выбирает раздел навигации. Ссылки в Markdown ведут на относительные `.md`-файлы. Ссылки в метаданных главной страницы — URL от корня сайта. Не вставляй частные рабочие журналы вместо подготовленных статей.

Перед PR выполнить команды сборки и проверки из README. Изменения темы проверять на широком и узком экране, с клавиатурой, а также при недоступном поисковом индексе. Не добавлять трекеры, удалённые шрифты или сбор личных данных.

Перед push владелец изменения получает независимые оценки по пяти линзам `.claude/review.config.json`. Каждая линза проверяет точный diff от заданной базы: craft — ясность и дублирование; architecture — границы и переносимость; tests — достаточность проверок; docs — факты/переводы/инструкции; security — публикация, ввод, доступ и утечки. После исправлений повторно проверяется финальный diff.

`npm run review:info` показывает базу и hash. Реальные результаты `{ "craft": {"score": 10, "verdict": "PASS"}, ... }` передаются в `npm run review:attest -- <results.json>`; пример задаёт только форму, не готовые оценки. Аттестация коммитится отдельно. `npm run review:gate` проверяет её и детерминированные проверки. По умолчанию база закреплена на начальном коммите; `--base <sha>` позволяет явно выбрать другую. CI использует закреплённую базу, поэтому обновлять её нужно согласованно с ревью.

## EN

### Mandatory content standard

Applies to every `docs/` article and translation. The shared source links in RU identify Diátaxis, Good Docs how-to/reference templates, Google procedures and Factorio's style guide. These rules adapt those ideas for Heroes.

1. One page answers a specific question or completes one task. Its opening states the answer/outcome and scope. Deliver the title's promise.
2. Each paragraph adds a fact, action, cause, example or material limitation. Remove generic introductions, self-praise and repetition; retain necessary explanations.
3. Procedures provide environment, exact actions/paths/controls/commands, labelled placeholders and expected results. Referring readers to an author's guide does not fulfil a promised procedure.
4. Distinguish game, expansion, mod and build. Never generalize one Universe build to all Heroes V. Editing is not runtime verification.
5. Attach evidence to disputed/version-sensitive claims. Distinguish hypotheses, observations and confirmed mechanisms. Static definitions alone do not prove every runtime outcome.
6. Provide units, conditions and exceptions. Tie native addresses/calls to exact builds/hashes. Never invent data to fill a template.
7. Keep a canonical source for facts/tables and link to it. Brief context is allowed. Use consistent terms and matching RU/EN facts.
8. Public articles must not depend on inaccessible private logs. Publish usable evidence or state the limitation. Screenshots assist actions/comparisons rather than replacing explanation.

### Page types and shape

- `tutorial`: a learning outcome, prepared environment, controlled example, checkpoints and a completed result.
- `how-to`: a concrete task, prerequisites, actions, result verification and relevant failures/rollback.
- `reference`: definitions, structured values/units, exceptions and provenance.
- `explanation`: an answer, causal mechanism, example and limits/unknowns.
- `landing`: navigation to existing content; `meta`: current project and contribution information. These two are service-page types, not extra Diátaxis modes.

Types do not require matching menu sections. Choose useful headings and omit empty sections.

### Metadata and status

Every page declares `content_type` and `status`: `draft`, `verified` or `outdated`. Drafts may appear in the design preview but do not thereby meet all editorial criteria.

For verified/outdated articles of the first four types, require nonempty `scope`, actual verification date `verified_on` (YYYY-MM-DD), and a nonempty `sources` list of public HTTPS sources/reproducible reports. Outdated articles retain their historical verification date. Landing/meta pages need accurate information and links, not invented game versions or citations.

RU/EN pairs must have corresponding `lang`, reciprocal site-root-relative `translation`, and matching `faction`, `content_type` and `status`. Their scope and evidence must agree. Technical behavior changes require rechecking affected claims or marking the page draft/outdated. Preserve historical observations.

### Acceptance

**Machine:** `npm run check` validates metadata, reciprocal language pairs, verified article dates/sources, local links/anchors and the public-content boundary. Invalid statuses, broken pairs and incomplete verified records fail. Draft/outdated counts are reported separately; a green result does not certify their content.

**Editor:** for each changed article, docs-review records its path, reader question, whether the title's promise is met, which material claims were checked against what, whether procedures are executable, version/translation consistency and remaining limits. False facts, unusable procedures or unsupported verified status block acceptance. List drafts separately without certifying them as ready.

Before verified status, another reader/reviewer executes a procedure without verbal help; reference values/sources and explanation logic/examples are checked as applicable. Word counts, headings, banned-word checks or a positive AI score do not substitute for this. Generating an article never verifies it.

All initial pages are draft. Improve them using three exemplars (procedure, reference, explanation), without empty scaffolding.


Use issues and pull requests. Start with one page and one verifiable change. State the game version and verification method for technical claims.

Keep RU/EN pairs factually aligned. `translation` is the counterpart's site-root-relative URL; `section` selects navigation. Markdown links use relative `.md` paths; homepage metadata links use site-root-relative URLs. Prepare articles rather than pasting private work logs.

Run README build/check commands before a PR. Test theme changes on wide and narrow screens, with keyboard navigation and an unavailable search index. Do not add trackers, remote fonts, or personal-data collection.

Before a push, obtain independent judgments for the five configured lenses: craft, architecture, tests, docs and security. Each reviews the exact base-to-HEAD diff; after fixes, review the final diff again. Review info reports the base/hash. Pass actual judgment JSON to review:attest; the example above is a format example, not real scores. Commit the resulting attestation separately and run review:gate.

The default review base is pinned to the initial commit; an explicit --base may override it. CI uses the pinned base, so any baseline update must be coordinated with review.
