# Per-file audit — scripts/verify.sh

## A. Identity
- Path: `scripts/verify.sh`
- SHA-256: `324346ded8358e7fe227f69035deefa0365843e3735dbef904a7ce7387b5e853`
- Size: 359 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully)
compileall src/tests/scripts/test-suite → validate-contracts → pytest → test-suite pytest. `set -eu`. NOTE: this verify.sh does NOT run source_hashes verify (unlike `make verify` which does) — so verify.sh would pass on the current tree while make verify fails. Minor inconsistency between the two documented verification entry points. Informational (REPO-001-adjacent).

## M. Verdict
Final status: Audited — complete.