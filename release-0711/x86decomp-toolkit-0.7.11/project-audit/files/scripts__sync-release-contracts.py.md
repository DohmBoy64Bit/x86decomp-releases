# Per-file audit — scripts/sync-release-contracts.py

## A. Identity
- Path: `scripts/sync-release-contracts.py`
- SHA-256: `2ce74c75d2b1fd60f1c290fdabe5e487e9844decb6a9e96923cda3d2505a857b`
- Size: 4388 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 126 lines)
Regenerates release inventories (command reference, feature catalog, surface counts) from the LIVE parser (canonical_routes/_build_parser) + testkit inventory/adapters. Writes docs/COMMAND_REFERENCE etc.

## C. Correctness
Derives contracts from live code (good — single source of truth). If run post-fix it would regenerate the now-stale COMMAND_REFERENCE/feature_catalog; the fact those artifacts + MANIFEST are stale (REPO-001) means this sync step was not re-run after the fix pass. Corroborates REPO-001 cause.

## M. Verdict
Final status: Audited — complete.