# x86decomp-toolkit 0.7.11 release verification

Second-audit fix release for the current unified toolkit surface.

## Surface

- root_commands: 166
- canonical_groups: 59
- canonical_routes: 239
- schemas: 97
- adapters: 37

## New or changed

- Fixed all nine concrete issues from the second 0.7.10 audit report.
- Added `x86decomp.binary_reader.BinaryReader` and moved PE/COFF bounded-reader behavior to the shared helper.
- Added pyflakes as a declared dev dependency and hard validation gate.
- Added command-level tests for `plugin validate`, `llm prompt`, `llm generate --report`, `llm cpp-generate --report`, and reconstruction CLI JSON error handling.
- Added module docstrings to the integration Python examples.
- Clarified plan-only CLI contracts and synchronized command/docs/architecture artifacts.

## Verification performed

- compileall: PASS for `src`, `test-suite/src`, `tests`, and `scripts`.
- pyflakes: PASS for `src`, `scripts`, and `test-suite/src`.
- validate-contracts: PASS.
- source manifests: PASS; root 449/449 and test-suite 63/63 after final report files were written.
- segmented pytest: PASS for the file-level root toolkit, test-suite, self-test, and public API contract files recorded in `SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json`.
- wheels/sdists: built for toolkit and test-suite.
- clean install and `pip check`: PASS.
- final extracted ZIP verification: PASS for source manifests, compileall, pyflakes, and validate-contracts.

## Not claimed

- A single monolithic `pytest tests` completion is not claimed because all-at-once/sequential sandbox runs timed out even though individual files passed.
- Live external local-model runtime availability or model quality is not claimed.
