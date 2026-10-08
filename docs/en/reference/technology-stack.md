---
content_type: meta
status: draft
faction: academy
title: Project technologies
lang: en
section: reference
kicker: DEVELOPERS
translation: reference/technology-stack/
description: Technologies already used by the SDK, mods, research and website.
updated: '2026-10-08'
---
# Project technologies

Check this list and the relevant code before adding a tool or library. Reuse an existing component first; add a dependency for a concrete need it cannot meet. Update this list with the dependency change.

## In use

| Area | Technologies | Purpose |
|---|---|---|
| Game and native modules | C++20, Windows API, x86 | DLLs, processes, input, game bindings and the native SDK |
| DLL builds | MSVC, CMake | Building 32-bit modules and isolated checks |
| Shared library | Our Game API | Build checks, known hooks and shared bindings; look here first |
| SDK interception | MinHook | Already connected to the native SDK loader for the bank-reference hook; this does not establish completed predictor migration |
| SDK tools | Python 3.10+ | xkit commands, workspace preparation, builds, control and observation |
| Command line | Typer, Click, Rich | Commands, help and readable output; Rich is also provided through Typer dependencies |
| Localization | gettext, Babel | Russian and English messages; gettext is part of Python's standard library |
| Logs and locks | logging, structlog, concurrent-log-handler, portalocker | Structured events, rotating logs and file locks |
| Native console | Dear ImGui, ImTerm, ImGuiColorTextEdit, DirectX 9 | Window, terminal, command editor and rendering |
| Native JSON | nlohmann/json | Parsing structured console messages |
| Analysis and checks | Keystone, Unicorn, pefile, Capstone | Machine code, emulation, PE parsing and disassembly |
| Website | MkDocs, Jinja, JavaScript, SCSS/Sass | Static articles, templates, search and styling |
| Images | Pillow, PNG, AVIF, SVG | Original backgrounds, compressed copies and diagrams; original PNGs are retained |
| Checks | unittest, CTest, Node.js, Playwright | Python/C++ checks, review and browser scenarios |
| Publication checks | bladeforge-review-harness, Husky | Pre-push review; Husky is used in the root workshop |
| SDK packaging | setuptools | Python-package installation and xkit command entry points |
| Versions and publication | Git, GitHub Actions, GitHub Pages | Canonical repositories, checks and website deployment |
| Windows automation | PowerShell | Window control and physical-input checks in the owned test game |

These are developer tools. The list does not require players installing a ready DLL/H5U package to install Python, Node.js or a compiler.

## Version sources

Manifests define exact versions and pinned revisions; we do not maintain a second set of version numbers here.

- [SDK dependencies](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/requirements.txt), [SDK checks](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/requirements-dev.txt), [Python package](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/pyproject.toml).
- [Native console dependencies](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/console_module.cmake): revisions and archive hashes.
- [Native SDK and MinHook](https://github.com/Xaaalera/heroes5-mod-devkit/blob/main/native/CMakeLists.txt): integration, pinned revision and archive hash.
- [Predictor checks](https://github.com/Xaaalera/heroes5-deployment-preview/blob/main/requirements-dev.txt).
- [Website Python dependencies](https://github.com/Xaaalera/heroes5-knowledge/blob/main/requirements.txt), [website Node.js tools](https://github.com/Xaaalera/heroes5-knowledge/blob/main/package.json).
- [Image provenance and licenses](https://github.com/Xaaalera/heroes5-knowledge/blob/main/NOTICE.md).

## Changing the stack

1. Look for an existing solution in canonical repositories, the language's standard library or Windows API.
2. For a new dependency, record its purpose, code location and selection reason. Check compatibility, licensing and version pinning.
3. Update its manifest, this inventory and the relevant instructions together. Remove a technology from the list when the code stops using it.
4. Check the inventory against code and manifests before publication. A researched candidate is not an installed technology.

**MinHook is already used by the SDK bank-reference hook. Migration of all predictor hooks to that mechanism remains unfinished. Microsoft Detours has only been researched and is not connected.** The current state-buffer prototype uses Windows API.
