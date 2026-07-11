# Review-only audit index

This directory contains a fresh, exhaustive review-only audit of the 543-file input archive. It does not replace or modify the historical audit artifacts in the parent directory.

Start with:

1. `FINAL_AUDIT_REPORT.md`
2. `FINDINGS_REGISTER.md`
3. `COVERAGE_REPORT.md`
4. `FILE_INVENTORY.csv` and `AUDIT_LEDGER.csv`
5. `COMMAND_SYSTEM_AUDIT.md`, `DOCUMENTATION_AUDIT.md`, `CROSS_FILE_ANALYSIS.md`, and `REVERSE_ENGINEERING_PRACTICES.md`
6. `files/` for one A–M report per baseline file
7. `evidence/` for machine-readable scans, command output, logs, and JUnit results

The final self-excluding `AUDIT_ARTIFACT_MANIFEST.sha256` seals every artifact in this directory.
