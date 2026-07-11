# Grouped audit — schemas/ (97), examples/ (26), corpus/ (24+24), test-suite meta (Bdata)

## schemas/ (97 JSON Schema files) — Audited — complete
- All 97 validated against Draft 2020-12 meta-schema (R-017: 97 valid, 0 invalid) AND validated by the product's own validate-contracts gate (R-018 PASS).
- One schema per capability output (evidence, claim, function, project, pipeline, coff-archive, pdb, msvc-metadata, symbolic/dynamic reports, release-gate, target-pack, mcp-mutation, etc.) — comprehensive, namespaced by capability (governance/native/reconstruction/assembly/local-llm subdirs + root). Additive-and-namespaced matches PROJECT_MEMORY policy.
- Each is data (not line-audited beyond structural validity + example conformance, which is machine-verified). No secrets. No findings.

## examples/ (26 files) — Audited — complete
- JSON examples (abi/benchmarks/compiler-profiles/contracts/integration/local-llm/release/relink/symbolic/test-bundle) all validated by validate-contracts (R-018 PASS) against their schemas — the CR-0710-006 fix added module docstrings to the 3 integration .py.
- Python fixtures (integration/candidate.py, candidate_mismatch.py, target.py): tiny, docstring'd stdin/stdout echo fixtures for integration scenarios; benign. (Their cpython-310 pyc are pre-existing, mtime Jul 6.)
- validators/*.bin + *.json: small binary fixtures + harness configs for symbolic/dynamic validation. Binary — inventoried with hash, not line-audited (fixture data). Belong in repo (test inputs).
- sample_source/add.c: trivial sample. No findings.

## corpus/ (root 24) + src/x86decomp/corpus/ (24, package-data) — Audited — complete
- Real deterministic C/C++ ground-truth sources (arithmetic/aliasing/bitfields/branches/calling_conventions/classes/exceptions/floating_point/globals/indirect/etc.) used by the ground-truth corpus builder + benchmarks. Genuine, compilable, purpose-built RE test material.
- The root corpus/ is duplicated into src/x86decomp/corpus/ as package-data (pyproject [tool.setuptools.package-data] glob) — standard src-layout pattern, resolves OQ-7 (glob is NOT dead). Duplication is intentional for wheel packaging (note DUP-005 Informational: two copies must stay in sync; the build could instead use a MANIFEST graft, but package-data-in-package is the conventional approach).
- No findings beyond the informational duplication note.

## test-suite/ meta files (README/CHANGELOG/INTEGRATION/MAINTENANCE/SECURITY/VERIFICATION.md, LICENSE, MANIFEST.in, MANIFEST.sha256, pyproject.toml, setup.cfg, .gitignore) — Audited — complete
- Mirror the root packaging for the standalone x86decomp_testkit distribution (its own pyproject/entry point x86decomp-test). test-suite/MANIFEST.sha256 verification FAILS (15 failures, part of REPO-001) — same stale-manifest issue as root. LICENSE Apache-2.0. No new findings; REPO-001 extends to the test-suite manifest.

## OQ resolutions
- OQ-7 RESOLVED: package-data corpus glob matches src/x86decomp/corpus/ground_truth_sources/*.c|cpp (24 files present). Not dead.
- DUP-005 (Informational): root corpus/ vs src/x86decomp/corpus/ duplicate the 24 ground-truth sources (intentional package-data).
