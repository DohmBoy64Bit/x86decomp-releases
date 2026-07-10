# Per-file audit — scripts/run-pytest-partitions.py

## A. Identity
- Path: `scripts/run-pytest-partitions.py`
- SHA-256: `9e19f2f989ee6d471c1cddbad44be24741abc0bb1519965dac2476986fb98179`
- Size: 6665 bytes | Type: text | Classification: build or packaging
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 162 lines)
Runs the test inventory in isolated per-file processes (ISOLATED_TEST_FILES for the two heavy ones), reconciles JUnit XML, aggregates. Exists specifically because monolithic pytest timed out (TEST-001).

## C. Correctness
Partitioning is a legitimate workaround, but it is also the mechanism by which cross-test-interference would be masked (TEST-001 impact). subprocess argv, env with PYTHONPATH + PYTEST_DISABLE_PLUGIN_AUTOLOAD. Sound.

## M. Verdict
Final status: Audited — complete.