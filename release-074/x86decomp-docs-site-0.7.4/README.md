# x86decomp documentation site 0.7.4

Open `index.html` directly, or serve the directory locally:

```bash
python serve.py
```

Then visit `http://127.0.0.1:8000`.

Run the bundled completeness and link checks:

```bash
python verify_site.py
```

Coverage pinned by `coverage-manifest.json`:

- 140 toolkit root commands and 280 toolkit runnable paths
- 5 verification-harness commands
- 33 canonical groups and 173 canonical routes
- 137 feature modules across both packages
- 983 functions and methods across both packages
- 215 tests
- 93 schemas
- 31 adapters

The site uses no external web assets or search service.
