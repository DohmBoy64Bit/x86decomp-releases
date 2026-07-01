# Documentation site verification

This static documentation site was generated from the sealed x86decomp-toolkit 0.7.4 release bundle and checked independently against its source tree.

## Coverage

- 140 toolkit root commands
- 280 runnable toolkit command paths
- 5 verification-harness commands
- 285 total documented command paths
- 33 canonical capability groups
- 173 canonical routes
- 137 feature modules
- 983 functions and methods
- 215 tests
- 93 schemas
- 31 integrations
- 340 HTML pages
- 1,760 search-index entries

## Passed checks

- Every command path has purpose, usage, arguments, and a concrete parser-valid example.
- Every feature module and function or method is documented exactly once.
- Every collected test is documented exactly once with its purpose and primary coverage.
- Every documented command example and workflow command parses with the real 0.7.4 parser.
- All local links and anchors resolve.
- Search contains every command, function or method, and test identifier.
- JavaScript syntax checks pass.
- A local HTTP server smoke test passed for the home, command, search-index, and test pages.
- The internal SHA-256 file manifest verifies every packaged site file.
- No unfinished markers, sample filler, or coming-soon content appears in visible documentation.
- The recorded source-bundle SHA-256 matches the uploaded source of truth.

See `SITE_VERIFICATION.json` and `coverage-manifest.json` for the machine-readable inventories.
