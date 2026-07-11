# Review remediation changelog

## Scope

This change set fixes every open finding in the July 10, 2026 review-only audit. It does not rewrite the historical review evidence; closure evidence is stored in this separate directory.

## Major changes

1. Deterministic, non-mutating release verification and explicit report regeneration.
2. Python 3.11.0-compatible validated backup extraction.
3. Complete Apache-2.0 license and NOTICE payloads in both distributions.
4. Replacement of all 364 generic docstrings plus an expanded semantic quality gate.
5. Complete generated documentation for 405 live command nodes.
6. Normalized-AST synchronization for six duplicated test pairs.
7. Reproducible Ruff and Pyright gates in dependencies, Makefile, and CI.
8. `x86decomp --version`.
9. Complete active-tree trailing-whitespace and transient-cache cleanup.

## Additional defects exposed and corrected

Enforcing the type gate found and corrected a `.to_dict()` call on an already serialized claim-verification result, access to a nonexistent COFF archive `symbols` attribute, unsafe package-metadata access, and several narrower annotation/contract mismatches. These were fixed and covered by the full regression replay.
