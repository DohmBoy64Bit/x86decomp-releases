# Per-file audit — pyproject.toml

## A. Identity
- Path: `pyproject.toml`
- SHA-256: `060a452b2c4356e1db1de87cb85995f8d3442e9e6670518e07b560d394cfd4c5`
- Size: 1515 bytes | Type: text | Classification: configuration
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Package metadata for `x86decomp-toolkit` 0.7.11: setuptools>=75 backend, zero required runtime deps (stdlib-only core — Verified, `dependencies = []`), 8 optional extras (capstone/unicorn/z3/angr/fastapi/lief/dev), console script `x86decomp = x86decomp.cli:main`, src-layout, package-data for corpus ground-truth sources, ruff (line 100, py311) and pyright strict config.

## C/E. Review
- `requires-python = ">=3.11"` is consistent with CI matrix (3.11–3.13). Verified.
- Version pin style is disciplined (upper bounds on all extras). No license classifier mismatch (Apache-2.0 matches LICENSE).
- `[tool.setuptools.package-data] x86decomp = ["corpus/ground_truth_sources/*.c", ...]` — that path is relative to the package dir `src/x86decomp/`; repo-level `corpus/` lives at root. Whether a `src/x86decomp/corpus/` exists must be checked (open question OQ-7); if not, this glob matches nothing silently. Possible packaging defect — Unverified pending B05/B12.
- pyright strict is declared but no CI step runs pyright (ci.yml has contracts/pytest only) — declared-but-unenforced gate. Informational.

## D. Documentation
N/A (config). Keys self-describing.

## H. Security
No secrets. Dependencies pinned with ranges; no hash pinning (pip-audit adapter exists as a runtime command instead). Acceptable.

## I. Testing
Exercised by CI packaging job (build + clean install + `x86decomp --help`). Verified in ci.yml text; execution not verified in this audit yet (Phase 10 n/a — needs network).

## L. Findings
- Candidate: package-data glob possibly dead (OQ-7, Possible; tracked, verified in B05).

## M. Verdict
Quality: good. Correctness confidence: high except OQ-7. Priority: low. Final status: Audited — complete.