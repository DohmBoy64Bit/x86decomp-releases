---
title: About
description: Source-of-truth policy for the 0.7.5 documentation.
---

# About x86decomp and this site

This site documents x86decomp-toolkit 0.7.5 and is regenerated from the release parser, source AST, schemas, adapters, manifests, tests, and maintained project examples.

## Documentation policy

- Parser metadata comes from the live command trees.
- Module names, signatures, lines, and docstrings come from the source AST.
- Test node IDs come from pytest collection.
- Schema facts come from the JSON files.
- Adapter and provider facts come from their declaration catalogs.
- Missing docstrings and help text are stated explicitly rather than replaced with inferred behavior.
- Unavailable integrations remain `BLOCKED`.
- No unfinished implementation markers are permitted.

## Authorization and safety

Use the toolkit only on binaries, systems, and environments you are permitted to analyze. Review model-generated source and isolate native execution.
