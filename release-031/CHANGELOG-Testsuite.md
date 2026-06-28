# Changelog

## 0.3.1 — 2026-06-28

### Integrated source layout and release hygiene

- Renamed the repository directory from the versioned
  `x86decomp-test-suite-0.3.0/` form to the stable `test-suite/` path.
- Updated package, runtime, catalog, tests, documentation, and HTTP user-agent version
  strings to 0.3.1.
- Removed generated run reports, coverage output, smoke-test virtual environments,
  downloaded adapter binaries, editable-install metadata, caches, and local absolute
  path configuration from the distributable source tree.
- Added a dedicated `.gitignore` so future runs remain outside release source.

### Normalized-source regression

- Combined repository regression: **109 passed, 0 failed, 0 skipped**.
- Harness tests: **17 passed**; packaged self-tests: **17 passed**; supplemental toolkit tests: **19 passed**.
- Pinned 0.3.1 inventory audit remained exact at 45 modules, 394 function/method bodies, 72 commands, 38 schemas, and 3 Ghidra scripts.

### Windows adapter detection

- Added `_prefer_windows_executable()` in `src/x86decomp_testkit/adapters/detection.py`
  so that `.bat`/`.exe` variants are preferred over bare filenames on Windows.
- Fixed `_ghidra_test()` in `src/x86decomp_testkit/live_adapters.py` to create
  `work`/`project` directories before the analyzer runs.
- Result: `ghidra:headless` test was **ERROR**, now **PASS**.

## 0.3.0

- Added exact feature catalog for x86decomp-toolkit 0.3.0.
- Added inventory drift enforcement for modules, commands, schemas, and Ghidra scripts.
- Added AST/coverage correlation for every public toolkit function and method.
- Added all-command CLI parse testing.
- Added no-pytest-skip JUnit enforcement.
- Added source-manifest, JSON Schema, Java syntax, skill-frontmatter, and compileall validation.
- Added clean wheel/source-distribution build and clean-wheel installation tests.
- Added detection-first adapter resolution with custom-path prompts only for missing tools.
- Added opt-in Python, package-manager, and official-release installation paths.
- Added live probes for Python libraries, compilers, linkers, Ghidra, DynamoRIO, objdiff, and build tools.
- Added detailed text, JSONL, JSON, Markdown, HTML, JUnit, and coverage logging.
- Added safe archive extraction and bounded download handling.
- Added harness self-tests covering configuration, detection, prompting, installers, archive safety, inventory, coverage, JUnit, reporting, process handling, and CLI behavior.
