---
faction: inferno
title: Suggest an edit
lang: en
kicker: ADD TO THE CODEX
translation: contributing/
description: Report a mistake or propose an article for Xaaalera’s knowledge base.
updated: 2026-09-23
---
# Suggest an edit

Start with a typo, a version clarification, or a small example. You do not need to write a complete guide.

## Report a problem

[Open a GitHub issue](https://github.com/Xaaalera/heroes5-knowledge/issues/new). Include the page, the disputed statement, and what you observe in your game. For technical problems, add the version and reproduction steps.

## Edit an article

The “Edit on GitHub” link at the bottom of an article opens its source. GitHub guides you through a branch or fork and a pull request. A GitHub account is required.

Primary articles live in `docs/`; English versions are in `docs/en/`. Update both when changing a fact, or explicitly note in the PR that translation is still needed.

## Support technical conclusions

Separate observations from assumptions. Include the game version, scenario, and a small example. Do not upload game distributions, others' private material, tokens, or personal data.

Screenshots should show the result itself. Check for unrelated windows and personal information before adding them.

## Site structure

Markdown is the only source for articles. Presentation lives in `theme/` and `styles/`. Build and check commands are in the [repository README](https://github.com/Xaaalera/heroes5-knowledge#readme).
