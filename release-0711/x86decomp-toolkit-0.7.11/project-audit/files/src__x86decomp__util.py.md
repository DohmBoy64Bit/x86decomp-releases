# Per-file audit — src/x86decomp/util.py

## A. Identity
- Path: `src/x86decomp/util.py`
- SHA-256: `92a8de9229078f873769f36804676ab02b66c1f7a95ae5f9f3bbced632f67ed5`
- Size: 6644 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 217 lines)
'Small, dependency-free utilities shared by all modules': utc_now, sha256_bytes/file, canonical_json_bytes, load_json, atomic_write_bytes/text, write_json, copy_file_atomic, ensure_relative_path(root,candidate) resolve-based escape check, require_mapping/require_string/require_int. Raises errors.ContractError.

## C. Correctness
- atomic_write_bytes: correct temp+fsync+os.replace pattern; `finally: unlink(temp)` after successful replace relies on FileNotFoundError pass — correct but wasteful one syscall; no chmod (mkstemp 0600 default persists!) — files written via util atomic writer are 0600 while contracts.atomic_write_bytes chmods 0644. Divergent permissions for sibling writers (part of DUP-002); on-disk project artifacts get inconsistent modes depending on which module wrote them. Verified by read.
- ensure_relative_path resolves symlinks (candidate.resolve()) — robust vs symlink escape; contracts.ensure_relative_path is string-based (no resolution, but rejects absolute//../drive) — DIFFERENT semantics under the SAME NAME (one takes (root,candidate), other takes (value)). Callers must know which they imported. Part of DUP-002.
- require_int correctly rejects bool. Good edge-case handling.

## D. Documentation
Good post-fix docstrings (in 68-file edit set).

## K. Duplication — DUP-002 (verified)
util.py vs contracts.py parallel implementations: utc_now (identical semantics, different construction), sha256_bytes, sha256_file, canonical_json_bytes vs canonical_json (bytes vs str), load_json vs read_json, atomic_write_bytes (different failure/permission semantics), write_json vs atomic_write_json (trailing-newline + ensure_ascii differences), ensure_relative_path (different signatures AND validation strategies), plus two ContractError classes (ARC-001). Import census: 67 modules import util, 49 import contracts — both foundational, neither canonical.

## L. Findings
- DUP-002 (Medium, Verified): duplicated foundational helper layer with behavioral drift (permissions, path-validation semantics, JSON formatting); consolidation direction: fold contracts.py primitives into util.py (or vice versa) and alias ContractError once.

## M. Verdict
Quality: high per-function; systemic duplication is the issue. Final status: Audited — complete.