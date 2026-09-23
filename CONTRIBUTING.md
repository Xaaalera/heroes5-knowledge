# Contributions / Вклад в базу

## RU

Исправления и дополнения принимаются через issues и pull requests. Начни с одной страницы и одного проверяемого изменения. Укажи версию игры и способ проверки технического утверждения.

Парные страницы RU/EN должны сообщать одинаковые факты. `translation` в метаданных — URL соответствующей страницы от корня сайта; `section` выбирает раздел навигации. Ссылки в Markdown ведут на относительные `.md`-файлы. Ссылки в метаданных главной страницы — URL от корня сайта. Не вставляй частные рабочие журналы вместо подготовленных статей.

Перед PR выполнить команды сборки и проверки из README. Изменения темы проверять на широком и узком экране, с клавиатурой, а также при недоступном поисковом индексе. Не добавлять трекеры, удалённые шрифты или сбор личных данных.

Перед push владелец изменения получает независимые оценки по пяти линзам `.claude/review.config.json`. Каждая линза проверяет точный diff от заданной базы: craft — ясность и дублирование; architecture — границы и переносимость; tests — достаточность проверок; docs — факты/переводы/инструкции; security — публикация, ввод, доступ и утечки. После исправлений повторно проверяется финальный diff.

`npm run review:info` показывает базу и hash. Реальные результаты `{ "craft": {"score": 10, "verdict": "PASS"}, ... }` передаются в `npm run review:attest -- <results.json>`; пример задаёт только форму, не готовые оценки. Аттестация коммитится отдельно. `npm run review:gate` проверяет её и детерминированные проверки. По умолчанию база закреплена на начальном коммите; `--base <sha>` позволяет явно выбрать другую. CI использует закреплённую базу, поэтому обновлять её нужно согласованно с ревью.

## EN

Use issues and pull requests. Start with one page and one verifiable change. State the game version and verification method for technical claims.

Keep RU/EN pairs factually aligned. `translation` is the counterpart's site-root-relative URL; `section` selects navigation. Markdown links use relative `.md` paths; homepage metadata links use site-root-relative URLs. Prepare articles rather than pasting private work logs.

Run README build/check commands before a PR. Test theme changes on wide and narrow screens, with keyboard navigation and an unavailable search index. Do not add trackers, remote fonts, or personal-data collection.

Before a push, obtain independent judgments for the five configured lenses: craft, architecture, tests, docs and security. Each reviews the exact base-to-HEAD diff; after fixes, review the final diff again. Review info reports the base/hash. Pass actual judgment JSON to review:attest; the example above is a format example, not real scores. Commit the resulting attestation separately and run review:gate.

The default review base is pinned to the initial commit; an explicit --base may override it. CI uses the pinned base, so any baseline update must be coordinated with review.
