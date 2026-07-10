# Per-file audit — src/x86decomp/compiler.py

## A. Identity
- Path: `src/x86decomp/compiler.py`
- SHA-256: `cd474dd4aa9c3ba80b6e5d1b50df0e2e2d460aae68b30bc63233531e730834bb`
- Size: 9946 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 238 lines)
Deterministic external-compiler execution + content-addressed cache keys. Version probe (timeout 10, OSError/Timeout→None), profile run (argv array, env, cwd=workdir tempdir, timeout from profile, check=False).

## C/H. Security
- Argument arrays; no shell. Env constructed explicitly. Deterministic cache via canonical_json_bytes+sha256. Compiler executable comes from a profile/toolchain registry (user-declared), run with timeout. No injection surface.
- Honors BLOCKED policy (returns None / raises ExternalToolError on absence).

## M. Verdict
High quality. Final status: Audited — complete.