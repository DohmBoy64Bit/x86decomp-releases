---
title: Full Docsite Hash and Parity Audit
description: Source-to-documentation parity audit for x86decomp 0.7.8.
---

# Full Docsite Hash and Parity Audit

Status: **PASS**  
Errors: **0**

This audit compares the current Dracula MkDocs site against the current x86decomp 0.7.8 source tree without changing the site theme or templates.

## Coverage summary

| Area | Count |
| --- | ---: |
| Markdown pages | 465 |
| Markdown SHA-256 entries | 465 |
| Built HTML pages | 467 |
| Root commands | 166 |
| Canonical groups | 59 |
| Canonical routes | 239 |
| JSON Schemas | 97 |
| Unique source-manifest paths | 433 |
| Root manifest entries verified | 433 |
| Test-suite manifest entries verified | 63 |
| Python modules documented | 145 |
| Python AST symbols documented | 1299 |
| Test source files documented | 59 |

## Verified gates

- Every root command has a command page.
- Every canonical group has a command page.
- Every canonical route action is present in its generated command page.
- Every JSON Schema path and SHA-256 digest is documented.
- Every source-manifest path and SHA-256 digest is documented and re-hashed.
- Every Python module in toolkit and test-suite source roots has a feature page.
- Every AST class/function/async-function symbol from those modules is included in the function index or module pages.
- Every test source file in the toolkit and test-suite test roots is documented with a source hash.
- Every Markdown source page has a SHA-256 entry in `DOCSITE_MARKDOWN_HASHES.json`.
- Local links and Markdown fragments resolve.
- MkDocs strict build output contains all published Markdown pages.
- The MkDocs search index contains every published Markdown page.
- No pre-0.7.8 version tag remains in the active site Markdown, README, or MkDocs configuration.
- `theme.name` remains `dracula`.

## Important boundary

This is a documentation/source parity audit. It proves source coverage, hash coverage, command/schema/module/test documentation coverage, link integrity, search indexing, and stale-version scanning for the docsite. It does not claim a new full optional adapter-aware runtime harness pass.

The machine-readable report is available at `FULL_DOCSITE_HASH_PARITY_AUDIT.json` and includes the checked command, schema, source-manifest, module, test-source, and Markdown-hash entry lists.
