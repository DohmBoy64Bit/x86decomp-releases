# Per-file audit — src/x86decomp/test_bundle.py

## A. Identity
- Path: `src/x86decomp/test_bundle.py`
- SHA-256: `e39fa02455b0bffa5ff85455eaf86bbaad76921df269e3b5cd8c7dc188cb8de3`
- Size: 19119 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, ~300 lines)
Hash-sealed authorized static test bundles: create_test_bundle (manifest + artifacts + authorization statement), inspect_test_bundle (_extract_safely with BundleLimits).

## C/H. Security — model zip handling
- _safe_member_path rejects backslash, absolute, empty/./.. parts, drive-qualified. _is_symlink rejects symlink members. _validate_archive_infos enforces max_files, per-member size, total uncompressed size, and compression-ratio (zip-bomb defense), rejects duplicate members and zero-compress-size-nonempty. _extract_safely re-checks resolved parent is within root (defense-in-depth beyond the path checks), streams with 'xb' (no overwrite), requires root manifest.
- This is a textbook-safe extractor and directly satisfies SECURITY.md's 'reject archive traversal, unsafe links, output paths outside declared roots'.

## M. Verdict
Exemplary. Final status: Audited — complete.