# Audit baseline

- **Repository root:** `/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11`
- **Governing scope:** `GOVERNING_AUDIT_SPECIFICATION.txt`
- **Audit timestamp:** `2026-07-10T15:01:48-04:00` (`America/New_York`)
- **Input archive SHA-256:** `ec222b125e59987642c1685d9c1a1e44cc2c2c2d53e8500aed72ac96c9c7468a`
- **Repository state:** extracted source archive; `.git/` metadata is absent, so branch, commit, tracked/untracked, ignored status, submodule state, and original working-tree cleanliness are **Blocked from verification**.
- **Original repository files:** 543
- **UTF-8 text files:** 540
- **Binary files:** 3
- **Symlinks:** 0
- **Nested repositories/submodules:** none detectable without VCS metadata
- **Operating system:** Linux x86_64 (`uname` evidence recorded in RUN_LOG.md)
- **Python:** 3.13.5
- **pytest:** 9.0.2
- **Clang:** 17.0.0
- **GCC:** 14.2.0
- **Node:** 22.16.0
- **Build system:** setuptools via `pyproject.toml`; Makefile orchestration
- **Primary languages/formats:** Python, Markdown, JSON/JSON Schema, C/C++, Java, YAML, TOML, shell, PowerShell
- **Project purpose (verified from README and package metadata):** evidence-governed x86/x86-64 Windows binary analysis, reconstruction, validation, and reproducible release work.

## Safe commands identified

Read-only or disposable-clone checks included parser/AST/JSON validation, source-manifest verification, CLI help/error probes, exact pytest partitions, packaged self-tests, shell syntax checks, corpus synchronization, and malformed-input parser smoke tests. Commands that write reports, caches, build trees, or package artifacts were redirected to disposable clones or audit evidence paths.

## Environment limitations

- `mkdocs`, `javalang`, and `pyflakes` were not installed in the active environment. They were not installed because the review-only specification prohibits altering the project environment without authorization. Current executions of those gates are therefore **Blocked from verification in this environment**; prior sealed reports are historical corroboration only.
- The source archive lacks Git metadata, so Git-aware inventory fields are explicitly unavailable rather than guessed.
- Optional external integrations (Ghidra, DynamoRIO, model servers, commercial toolchains, network services) were not invoked.
- No coverage.py line/branch run was performed during this review-only audit; test execution counts must not be confused with code-coverage percentages.
