# x86decomp MkDocs site

This folder contains the style-preserving MkDocs documentation site for x86decomp-toolkit 0.7.5. It keeps the Dracula MkDocs theme from the supplied site baseline while updating the documentation content, references, release evidence, local-LLM guide, and generated source coverage to the 0.7.5 release.

## Build

```bash
python -m pip install -r requirements.txt
python -m mkdocs build --strict
python scripts/verify_end_user_site.py
```

On Windows PowerShell, you can also run:

```powershell
python -m pip install -r requirements.txt
.\build.ps1
```

If PowerShell blocks the script because the ZIP came from the internet, run:

```powershell
Unblock-File .\build.ps1
Unblock-File .\serve.ps1
```

## Serve locally

```bash
python -m mkdocs serve -a 127.0.0.1:8000
```

Or on Windows:

```powershell
.\serve.ps1
```

## Source of truth

The live documentation source is the `docs/` directory plus `mkdocs.yml`. Historical static-site migration archives are intentionally not included in this updated package, so older archived pages cannot be confused with the current 0.7.5 site.
