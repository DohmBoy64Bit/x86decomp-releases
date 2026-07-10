# Per-file audit — AGENTS.md

## A. Identity
- Path: `AGENTS.md`
- SHA-256: `63a01156035245a7636fdf8c71cde7e1911307cb40146c10bd26f0556fe73efc`
- Size: 2552 bytes | Type: text | Classification: documentation
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Operating rules for agents/contributors: single-release model, 12 non-negotiable engineering rules (no placeholders, evidence gates, deterministic outputs, single executables), required release gates, evidence vocabulary.

## C/E. Review
- Direct evidence the project is developed with AI agents in the loop (rules addressed to agents; 'Treat AI and analyst proposals as proposals'). This is provenance context for Section F assessments across the codebase — the boilerplate-docstring pattern is consistent with automated docstring generation, which this file implicitly sanctions under gates.
- Rule 12 requires a synchronized MkDocs site; no mkdocs.yml exists anywhere in the tree (verified: not in inventory). Declared gate with no corresponding artifact — inconsistency, DOC-002 candidate (verify in B08: maybe docs/ is the source without config).
- Release-gate list ('all tests with zero skips', 'line and branch coverage floors') is aspirational versus the admitted monolithic-pytest timeout (TEST-001).

## L. Findings
- DOC-002 (Low, Verified absence): MkDocs synchronization required by AGENTS.md rule 12 / PROJECT_MEMORY / SKILL.md, but no mkdocs.yml or site/ exists in the release tree.

## M. Verdict
Well-written policy doc; enforcement gaps are the story. Final status: Audited — complete.