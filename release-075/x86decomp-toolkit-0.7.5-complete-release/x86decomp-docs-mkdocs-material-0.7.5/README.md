# x86decomp 0.7.5 documentation

This is the editable Material for MkDocs source for the x86decomp-toolkit 0.7.5 documentation site.

## Build

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs build --strict --clean
.\.venv\Scripts\python.exe .\scripts\canonicalize_site.py .\site
```

On Linux or macOS, replace `.\.venv\Scripts\python.exe` with `./.venv/bin/python`.

## Serve locally

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

## Verify

```powershell
.\.venv\Scripts\python.exe scripts\verify_end_user_site.py
.\.venv\Scripts\python.exe scripts\verify_built_site.py
```

The site is generated from the final 0.7.5 parser, source AST, collected tests, schemas, adapter catalog, source manifests, and Project Example evidence ledgers. The local-model feature is documented as an untrusted proposal path whose only matching acceptance gate is deterministic compilation plus exact relocation-resolved byte identity.

## Reproducibility

`canonicalize_site.py` rewrites the generated sitemap gzip with a fixed timestamp and no embedded filename. The verified release build is byte-reproducible across consecutive builds from the same source and dependency versions.
