# Documentation Audit — x86decomp-toolkit 0.7.11

Evidence: full read of README + all root docs (B02) + docs/ (Bdocs) + COMMAND_REFERENCE diff (R-019) + docstring quality scan (R-006).

## Installation / setup / dependencies / platforms — ACCURATE
- README install (wheel + extras) matches pyproject; requires-python 3.11 consistent with CI; optional-dependency groups documented. Platforms (Windows x86/x64 PE targets; toolkit runs on the CI matrix) clear via supported-scope.md. Minor: no uninstall/upgrade section.

## Quick-start usability — GOOD
- README "First project" gives runnable init/inspect/commands flow. BUT the documented `make verify` and harness init-config examples (a) currently fail on the shipped tree (REPO-001) and (b) write byproducts into the repo root that aren't gitignored (REPO-004). A new user following the README verbatim hits a failing verify and a polluted tree.

## Command coverage — EXCELLENT (structurally)
- docs/COMMAND_REFERENCE_0.7.11.{json,md} is an EXACT match to the live 239-route/59-group/166-command surface (R-019) with plan-only annotations. This is the strongest doc artifact.
- BUT `--help` for 78/106 flat commands shows bare names (CLI-003) — so interactive discoverability lags the reference file.

## API / docstring coverage — PRESENT but LOW QUALITY (DOC-001)
- Presence: 100% (DOCSTRING_AUDIT + my scan agree — every module/class/function has a docstring).
- Quality: 555/1,614 defs (34%) carry template boilerplate ("... for the current toolkit workflow." / "Support X processing for internal toolkit callers."), incl. 36 degenerate repeated-verb non-sentences ("Append append...", "Verify verify..."). The post-fix edited files (util/contracts/cli_utils/canonical/pe/pe32) have GOOD Args/Returns/Raises docstrings — the boilerplate concentrates in coff.py (34), pdb.py (19), synthetic_corpus, assembly, governance. Docstring QUALITY contradicts the CHANGELOG's "professional docstrings" claim.

## Configuration coverage — GOOD
- Schemas (97) fully documented as JSON Schema + validated; contracts.md + evidence-and-claims.md + target-packs docs cover the data plane. Env vars (API key envs, GHIDRA_HOME) documented in local-llm.md / ghidra-integration.md.

## Troubleshooting / error explanations — THIN
- Little dedicated troubleshooting; error messages themselves are descriptive, but there's no "common errors" guide. SECURITY.md reporting lacks a channel (UX-001).

## Security & RE-workflow guidance — STRONG
- SECURITY.md, guardrails.md, supported-scope.md, source-basis.md, test-bundle.md, ghidra-integration.md, local-llm.md give concrete, accurate guidance matching the code. Consent/isolation posture well documented.

## Examples — CORRECT
- All JSON examples validate against their schemas (validate-contracts R-018 PASS). Integration python fixtures have module docstrings (CR-0710-006). Real usage, not name-echoes.

## Terminology / versioning / links — CONSISTENT
- Evidence vocabulary consistent across AGENTS/SKILL/PROJECT_MEMORY/evidence-and-claims. Version 0.7.11 consistent everywhere. Internal doc references resolve (docs/architecture.md etc. exist). DUP-001: some paragraphs duplicated verbatim across 4 root docs (drift risk).

## Architecture / release / migration docs — GOOD except MkDocs gap
- architecture.md + ARCHITECTURE_MAP(.md/_ASCII) + FEATURE_PARITY accurate. Single-release model documented. DOC-002: AGENTS/PROJECT_MEMORY/SKILL require a synchronized MkDocs Material site that does not exist in the tree (no mkdocs.yml/site/).

## Command-documentation coverage matrix (canonical routes)
| Attribute | Coverage |
|---|---|
| One-line summary | 239/239 (COMMAND_REFERENCE) |
| Detailed explanation | canonical routes yes; flat commands via reference |
| Argument docs | in COMMAND_REFERENCE; NOT in `--help` for 78 flat commands (CLI-003) |
| Option docs | as above |
| Expected output | JSON contract implicit + schemas |
| Error behavior | documented generally (exit 0/2); CLI-001/002 diverge from docs in practice |
| ≥1 valid example | README + examples/ + docs cover major flows; not per-command |
| Realistic use case | yes (README first-project, local-llm.md, target-packs) |
| Safety notes | SECURITY.md + guardrails + per-command consent flags |
| Test/verification ref | test_release_contract + COMMAND_REFERENCE regen from live parser |

## Verdict
Documentation is ABOVE AVERAGE: honest about scope/limits, a command reference that is mechanically in sync with code, and strong security/RE guidance. The weaknesses are (1) docstring QUALITY (boilerplate, DOC-001) contradicting the "professional docstrings" release claim, (2) the missing MkDocs site the governance docs mandate (DOC-002), (3) quick-start steps that fail/pollute on the shipped tree (REPO-001/004), and (4) interactive `--help` discoverability (CLI-003).
