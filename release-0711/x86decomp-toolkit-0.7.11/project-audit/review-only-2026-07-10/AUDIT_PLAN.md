# Review-only audit plan

## Scope

The baseline is the 543-file extracted archive. Every baseline file is inventoried, hashed, completely read at byte level, classified, cross-referenced, assigned a final ledger status, and linked to one A–M per-file report. All 540 UTF-8 files received complete-content structural and semantic review. The three binary fixtures received full byte/hash inventory and limited purpose/security review without execution.

New artifacts created by this audit are isolated under `project-audit/review-only-2026-07-10/`; they are not added to the baseline denominator. Existing repository files, including the historical `project-audit/` record, must remain byte-identical.

## Repository-specific risks

1. Untrusted PE/COFF/PDB/archive parsing and resource bounds.
2. Evidence provenance, claim levels, and reproducibility.
3. Command-surface breadth and documentation drift.
4. File/path/process/network trust boundaries.
5. Packaging and deterministic manifest integrity.
6. Duplicated source/package test logic.
7. Optional-tool behavior and explicit blocked states.

## Review order and methods

1. Establish byte-identical baseline and deterministic manifests.
2. Parse every Python and JSON file; fully ingest every text file; record binary hashes and context.
3. Build architecture, command, dependency, duplicate, documentation, and test maps.
4. Review risk-bearing implementations and corroborating tests/documentation.
5. Execute safe checks only in disposable clones or with outputs redirected to audit paths.
6. Triple-check important findings using direct evidence, corroboration, and consistency review.
7. Generate per-file reports sequentially and reconcile ledger/inventory counts.
8. Rehash every original file, seal all audit artifacts, and package the reviewed tree.

## Prohibited actions

No source edits, formatting, renames, dependency updates, global installs, network-dependent integration runs, destructive commands, Git operations, or fix-mode tools. No finding may rely on conversational memory or unsupported inference.

## Completion criteria

- 543/543 baseline inventory rows have final statuses.
- 543/543 per-file reports exist and contain sections A–M.
- 540/540 text files are marked completely read; 3/3 binaries have documented limited-review reasons.
- Command and canonical-route inventories reconcile to runtime parser counts.
- Exact tests and checks are recorded with outputs and limitations.
- Every original SHA-256 digest matches the baseline.
- No Pending, Unread, Unknown, or unexplained hash discrepancy remains.
- Audit artifacts are sealed by a self-excluding SHA-256 manifest.
