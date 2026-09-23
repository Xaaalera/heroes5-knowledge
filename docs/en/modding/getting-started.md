---
faction: academy
title: Your first experiment
lang: en
section: modding
kicker: MOD CREATORS · FIRST STEPS
translation: modding/getting-started/
description: Choose the right layer and run a small, verifiable experiment.
updated: 2026-09-23
---
# Your first experiment

Start with one change whose result is visible in a short run, such as an original interface text or one resource parameter.

## Choose the layer

| Layer | Purpose | Main check |
|---|---|---|
| Resources and XDB | Descriptions, object definitions, interface | Was the modified resource actually loaded? |
| Lua | Scenarios and logic exposed by the game API | Is the function available in this context? |
| Native code | Executable behavior changes | Do the build, ABI, and identified mechanism match? |

Use resources or scripts when they can solve the task. Native changes require a separate investigation of the executable.

## Locate the source

Record the resource path and archive. Preserve original text encoding. Follow XDB `href` references: the relevant value may live in another definition.

Editing an extracted copy does not mean the game used it. Verifying that it loads is a separate step.

## Record the experiment

A short record can look like this:

```text
Task: verify that custom text loads
Change: one resource
Expected: text appears in a particular window
Check: open that window in the test game
Rollback: remove the package and repeat
```

This is an example plan, not a report of a completed test.

## Preserve the result

Record the path, version, action, and observed result. See [verifying a change](verification.md) for the full procedure.
