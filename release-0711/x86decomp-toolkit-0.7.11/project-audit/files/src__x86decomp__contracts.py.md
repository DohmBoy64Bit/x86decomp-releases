# Per-file audit — src/x86decomp/contracts.py

## A. Identity
- Path: `src/x86decomp/contracts.py`
- SHA-256: `4031b2f069be4ba4d6fbdad241113e41d74e082c0cef43d59622ac49fbc98aca`
- Size: 5609 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 164 lines)
Foundational contract primitives: ContractError(ValueError); utc_now, canonical_json, sha256_bytes/file, stable_id (canonical-JSON+NUL-join hash), random_id, validate_id (regex ^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$), ensure_relative_path (string-based traversal rejection incl. backslash normalization and drive-letter check), atomic_write_bytes (chmod 0644), atomic_write_json, read_json, dedupe_preserve.

## C. Correctness
- ensure_relative_path: rejects absolute, .., drive-qualified — good for manifest-declared paths; does NOT resolve symlinks (a relative path pointing through a symlink inside the project can still escape). Whether that matters depends on call sites (governance/reconstruction stores) — flagged for B06 cross-check as SEC-candidate; symlink-based escape requires attacker ability to plant symlinks in a project dir. Possible; revisit.
- stable_id: 20 hex chars = 80 bits — collision-safe for project scale.
- atomic writer failure path unlinks temp only when replace failed — correct (except BaseException → unlink → re-raise).

## K. Duplication
Second half of DUP-002/ARC-001 (see util.py report).

## M. Verdict
Quality: high. Final status: Audited — complete.