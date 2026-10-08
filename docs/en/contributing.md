---
content_type: meta
status: draft
faction: inferno
title: Suggest an edit
lang: en
kicker: ADD TO THE CODEX
translation: contributing/
description: Report a mistake or propose an article for Xaaalera’s knowledge base.
updated: 2026-10-08
---
# Suggest an edit

Start with a typo, a version clarification, or a small example. You do not need to write a complete guide.

## Report a problem

[Open a GitHub issue](https://github.com/Xaaalera/heroes5-knowledge/issues/new). Include the page, the disputed statement, and what you observe in your game. For technical problems, add the version and reproduction steps.

## Edit an article

The “Edit on GitHub” link at the bottom of an article opens its source. GitHub guides you through a branch or fork and a pull request. A GitHub account is required.

Primary articles live in `docs/`; English versions are in `docs/en/`. Update both when changing a fact, or explicitly note in the PR that translation is still needed.

## Where documentation lives

Publish guides, references and explanations for our mods, xkit and Game API on this site. Article source must belong to the knowledge repository. Each project's README should briefly introduce it and link to the relevant site pages. Remove the previous living copy when migrating documentation; do not maintain the same instructions in several repositories.

AGENTS.md holds agent working rules; licenses remain beside source code. Dated research and private logs preserve verification history. They do not replace a current article and must not bring personal paths, game distributions or technical memory addresses onto the site.

## Write for a person

Start with the reader's task: what they will be able to do or understand. Choose one primary format: a guided example, a task procedure, a reference or an explanation. Keep development history out of the first steps; the research diary has its own place.

- State the intended reader and the prerequisites.
- Explain unfamiliar terms on first use. Describe actions in familiar words.
- Provide repeatable commands, where to enter them and when to wait for completion.
- Show the expected result and how to check it. Explain what to do after a refusal.
- Separate implemented behavior from plans and observations from assumptions. Check technical claims against code and reproducible results.
- Update Russian and English together. Numbers, limits and the meaning of actions must agree.

The approach draws on [Diátaxis](https://diataxis.fr/start-here/) and [Google's procedure guidelines](https://developers.google.com/style/procedures). A page type helps shape the writing; it does not verify facts.

## Review each article with five critics

Every new or changed article receives five independent critiques using the [critique method](https://github.com/Xaaalera/claude-skills/blob/main/plugins/critique/skills/critique/SKILL.md). Knowledge maintainers organize them: contributors submit a PR with sources and a description of the change. For a typo, checks can be brief, but must cover the final text. The author cannot count as an independent critic of their own text.

| Area | What the critic checks |
|---|---|
| Newcomer clarity | Goal, terms and first actions are understandable without the author or AI |
| Technical accuracy | Commands and limits agree with code, sources and observations |
| Reproducibility | Preparation, steps and result checks are sufficient to repeat the task |
| Structure and navigation | Answers are easy to find, links work and unnecessary repetition is absent |
| Terminology and translation | Names, examples, numbers and meaning agree across RU/EN |

A finding identifies its location, concrete defect, consequence, severity and evidence. A style preference without a reader problem is not a defect. Verify testable claims against sources or a small safe probe.

Collect findings in one JSON: page and content hash, critic and area, defect location, evidence, severity, disposition and fix verification. Deduplicate by location while preserving independent agreement. Freeze text within a round and recheck corrected locations afterward. Cap review at three rounds per article. Fix confirmed substantial defects before publication and mark uncertain claims as unverified. Critique does not replace the site build, link checks or rendered-page inspection.

## Support technical conclusions

Separate observations from assumptions. Include the game version, scenario, and a small example. Do not upload game distributions, others' private material, tokens, or personal data.

Screenshots should show the result itself. Check for unrelated windows and personal information before adding them.

For a reproducible experiment, start with the [xkit and test-copy guide](modding/devkit.md). The [console article](modding/console.md) explains command entry, suggestions, replies and the journal.

## Site structure

Markdown is the only article source. Presentation lives in `theme/` and `styles/`; do not edit or commit generated `site/` or compiled CSS. The site builds independently of the private workshop.

### Article metadata and status

Declare `content_type`, `status`, `lang`, `translation` and `faction` at the start of the file. Types are `tutorial` for a learning example, `how-to` for a task procedure, `reference` for lookup and `explanation` for understanding. `landing` and `meta` serve navigation and project information. Do not add empty sections to satisfy a template.

`translation` is the counterpart's site-root-relative address. RU/EN must agree on type, status and faction, with reciprocal translation links. Internal Markdown links use relative `.md` paths.

Start with `draft`: full editorial acceptance remains incomplete. For `verified` or `outdated` pages of the first four types, declare verification scope in `scope`, an actual `verified_on` date and a nonempty `sources` list of public HTTPS sources. Outdated pages retain their historical verification date. Editing text is not a new game test.

Before `verified`, another reader executes the procedure without verbal help; reference values and sources or explanation logic and examples are checked as applicable. A green build, heading count or positive AI judgment is insufficient.

### Preserve research

Add dated experiments to the [diary](reference/research-diary.md): build and date, question, inputs and actions, observation, inference or hypothesis, limits and available evidence. Label retrospective summaries with their reconstruction date. State when original logs are private; articles need accessible explanations or explicitly limited conclusions.

A corrected technical conclusion receives a dated correction linked to the earlier entry. Do not replace a past observation with a new one. Check download hashes against published bytes: local line endings can differ.

For spatial mechanics, show the full field, both armies, obstacles, creature footprints and X/Y axes. Generate repeated grids from data and distinguish measured cells from hypotheses. Examples connect inputs, intermediate decisions and checked results; a final screenshot alone does not explain causes. Label code as original source, reconstruction or pseudocode.

### Build the site locally

You need Git, Python 3.10+ and Node.js 22+. Clone the [knowledge repository](https://github.com/Xaaalera/heroes5-knowledge), open a terminal in its directory and create an environment:

```text
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in Windows PowerShell or `source .venv/bin/activate` on Linux/macOS. Then run:

```text
python -m pip install -r requirements.txt
npm ci
npm run build
npm run check
npx playwright install chromium
npm test
python -m mkdocs serve --watch-theme
```

The last command keeps a local preview server running; the terminal shows its address and Ctrl+C stops it. After SCSS changes, run `npm run styles` in a second terminal. MkDocs watches articles and the theme. Browser tests use a separate server on port 8769.

On Linux, Chromium also needs system dependencies: replace the browser installation command with `npx playwright install --with-deps chromium`. OS package installation may require administrator rights; see the [Playwright documentation](https://playwright.dev/docs/browsers).

`npm run check` validates metadata, translations, links, diagrams and public-data boundaries, reporting drafts separately. Browser tests cover navigation, search, languages and overflow at five widths. Also inspect interface changes with keyboard navigation and unavailable search. Do not add trackers, remote fonts or personal-data collection. Keep asset provenance and licenses in NOTICE.

### Review and publish a change

Repository maintainers perform this stage. To propose an article, submit a GitHub PR; contributors need not create review results or attestations themselves. The maintainer obtains JSON from independent reviewers for the lenses in `.claude/review.config.json`, including the docs report and five article critics. `<results.json>` below is the path to that received file, not a file supplied by the repository. If it is missing, organize review first; do not fill in scores on behalf of reviewers.

`npm ci` installs the Git pre-push gate. Before pushing, obtain independent reviews of the exact diff for the configured craft, architecture, tests, docs and security lenses. They complement the five article critics. `npm run review:info` reports the base, hash and article list; after edits, reviews must match the final bytes.

Commit source and article changes first: the gate checks commits and refuses uncommitted edits. The [review adapter](https://github.com/Xaaalera/heroes5-knowledge/blob/main/scripts/review-check.mjs) checks the received JSON format: top-level fields name the five lenses, each with actual `verdict` and `score`. `docs.review` contains the report's reviewer, covered files, eight criteria with evidence, findings and `articleCritiques`. The [report validator](https://github.com/Xaaalera/heroes5-knowledge/blob/main/scripts/review-docs.mjs) defines the complete nested field contract; [test fixtures](https://github.com/Xaaalera/heroes5-knowledge/blob/main/scripts/review-docs.test.mjs) illustrate its shape but are not actual review results.

Pass actual results JSON to `npm run review:attest -- <results.json>`, commit the generated attestation separately and run `npm run review:gate`. A docs score alone is insufficient: its report covers eight criteria and every changed Markdown file, including the agent index `docs/llms.txt`. Each changed article needs five independent critics and its current hash. An explicit `--base` does not override the separate article-policy adoption boundary; do not change bases to bypass checks.

The repository workflow publishes GitHub Pages. Local success does not mean the article is live: verify the workflow result and published RU/EN pages.

### Data and presentation

`faction` selects the background and accent from `docs/assets/worlds/`; names live in `mkdocs.yml`. Placement diagram coordinates live in `docs/assets/placement/observations.json`; `npm run figures` generates SVGs. Edit data or the generator, not individual SVG cells. The downloadable `placement_walkthrough.py` reconstruction has its own tests and explicit assumptions; do not present it as the game's complete algorithm.

`docs/llms.txt` points agents to source and evidence. Pages link to it and their GitHub Markdown sources; this does not promise automatic discovery by every client. Main can precede the deployed site, so record the revision being checked. Python caches and bytecode are excluded from publication.
