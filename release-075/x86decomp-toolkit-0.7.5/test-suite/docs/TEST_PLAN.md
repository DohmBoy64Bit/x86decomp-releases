# Comprehensive test plan — 0.7.5

## Exact current inventory

The feature catalog pins 113 Python modules, 879 function and method bodies, 141 root commands, 34 canonical groups, 181 canonical routes, 97 schemas, 3 Ghidra scripts, and 36 adapter contracts.

## Required suites

1. Recursive inventory and catalog equality
2. Historical-reference and forbidden-artifact scan
3. Exactly one toolkit and one test-suite executable
4. Compilation, import, schema, example, skill, and Java syntax checks
5. All toolkit tests with zero skips
6. All standalone verifier tests with zero skips
7. Every root command and canonical route help/process probe
8. Every current function and method body execution audit
9. Line and branch coverage floors
10. Adapter detection, configured path, custom path, installation, and BLOCKED behavior
11. Safe archive and subprocess tests
12. Wheel and source-distribution build and clean-install tests
13. Extracted source archive verification
14. Deterministic archive reproduction and SHA-256 validation
15. Final release-bundle extraction and checksum verification

No release-delta or source-tree migration suite exists in the current contract.
