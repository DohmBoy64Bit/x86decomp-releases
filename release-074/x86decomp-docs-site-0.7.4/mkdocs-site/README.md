# x86decomp MkDocs site

This folder contains the MkDocs conversion of the original static x86decomp 0.7.4 documentation site.

## Build

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## Serve locally

```bash
mkdocs serve -a 127.0.0.1:8001
```

## Rebuild the end-user site from the converted docs

```bash
python scripts/refactor_end_user_site.py
mkdocs build --strict
```

## Verify the end-user site

```bash
python scripts/verify_end_user_site.py
```
