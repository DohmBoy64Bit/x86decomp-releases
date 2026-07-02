---
title: About x86decomp and this site
description: Source identity and documentation policy
original_path: about.html
---

Section: About

# About x86decomp and this site

This site documents the sealed x86decomp-toolkit 0.7.4 release supplied in the current release bundle.

## Source of truth

Release bundle SHA-256: `7fae1658b0eccb980d54a3c80a5f91a6cf09f8eb4e2eb4ebcae3bd477f6d36e8`.

Deterministic source ZIP SHA-256: `f6d5f97454b405891dc89ad9329372e2005b91ea9ba0d8116df987023f834d8e`.

## Documentation policy

- Parser metadata is read from the actual command trees.
- Module, signature, line, and test inventories are read from the source AST.
- Function and test behavior is not inferred when source docstrings are absent.
- All schema facts are read from the JSON files.
- All packaged source paths are reconciled against `MANIFEST.sha256`.
- Unavailable integrations remain BLOCKED, never converted to pass or skip.
- Unfinished-content and insertion markers are not permitted anywhere in the published site.

## Authorization and safety

Use the toolkit only on binaries, systems, and environments you are permitted to analyze. Review generated changes and isolate native execution appropriately.
