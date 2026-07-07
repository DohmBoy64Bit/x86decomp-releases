# Test-suite changelog

## 0.7.11

- Replaced release-baseline and delta verification with one recursive current-surface catalog.
- Added recursive module, function/method, and nested-schema discovery.
- Removed version-specific coverage auditors, executable-shim tests, installer tests, and upgrade-report checks.
- Pinned one toolkit executable and one test-suite executable.
- Added historical-reference, upgrade-artifact, placeholder, documentation, and exact-entry-point gates.
- Preserved adapter detection, safe installation, process isolation, no-silent-skip behavior, reporting, packaging checks, and coverage floors.
- Fixed `safe_extract_archive` to copy single `.exe` release assets directly instead of raising "unsupported release archive format".
- Fixed `install_github_release` to rename single extracted `.exe` to match the first declared command name.
- Fixed `_candidate_from_root` and `_path_for` to fall back to `{command}.exe` on Windows when the bare command name is not found.
- Fixed objdiff release asset patterns to select the CLI binary (`objdiff-cli-*`) over the GUI binary.
- Fixed Ghidra auto-install path in `x86decomp-test.json` to point through the version-named extraction subdirectory.
- Fixed `_verify_manifest` to skip `MANIFEST.sha256` self-entry, avoiding chicken-and-egg hash mismatches.
- Fixed symlink test to early-return on Windows without Developer Mode instead of calling `pytest.skip()`.
- Fixed `validate-contracts.py` to exclude `.x86decomp-test-tools` from structure validation.
- Fixed `test_release_contract.py` to include `.x86decomp-test-tools` and `test-results` in `ignored_parts`.
