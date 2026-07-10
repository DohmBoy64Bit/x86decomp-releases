---
title: x86decomp.linker_reconstruction
description: Module reference for x86decomp.linker_reconstruction.
---

# `x86decomp.linker_reconstruction`

- Area: `toolkit`
- Source path: `src/x86decomp/linker_reconstruction.py`
- SHA-256: `e2485c40df661dea95be2a879a8a91ff185ed25b859d8683c969e922cf1dc79c`
- Size: `6788` bytes
- Lines: `155`

## Module docstring

Evidence-driven linker reconstruction plans.

Plans are generated only from supplied PE/MAP/COFF/archive evidence.  Unknown
placement, runtime library, linker flag, and import decisions remain explicit
unresolved items rather than inferred facts.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `build_linker_reconstruction_plan` | 21 | Build linker reconstruction plan for the current toolkit workflow. |
| function | `write_relink_manifest_from_plan` | 146 | Write relink manifest from plan for the current toolkit workflow. |
