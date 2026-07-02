# x86decomp documentation site 0.7.4

This is the full source-audited documentation site for the sealed x86decomp-toolkit 0.7.4 release.

Open `index.html` directly, or serve the directory locally:

```bash
python serve.py
```

Then visit `http://127.0.0.1:8000`.

Run the bundled offline integrity, completeness, link, search, navigation, placeholder, and checksum checks:

```bash
python verify_site.py
```

Audit evidence:

- `FULL_DOCSITE_AUDIT.md` — human-readable source-to-site audit
- `FULL_DOCSITE_AUDIT.json` — machine-readable audit details for every check family
- `coverage-manifest.json` — exact expected and documented inventories
- `source-coverage.html` — all 411 root-manifest files and their hashes
- `PROJECT_EXAMPLES_SOURCE_AUDIT.json` — 95 exact source anchors supporting the 11 project examples
- `SHA256SUMS.txt` — hashes for every published site file except the checksum file itself

Coverage pinned by `coverage-manifest.json`:

- 140 toolkit root commands and 280 toolkit runnable paths
- 5 verification-harness commands
- 33 canonical groups and 173 canonical routes
- 137 Python modules across both packages
- 983 functions and methods across both packages
- 215 tests
- 93 JSON Schemas
- 31 adapters
- 3 Ghidra scripts
- 411 authenticated root-manifest files
- 2,183 search-index entries

The site uses no external web assets or search service. The sealed release test and coverage figures are reported as authenticated release evidence and are not presented as a newly executed full test run by the documentation audit.
