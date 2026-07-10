---
title: x86decomp.errors
description: Module reference for x86decomp.errors.
---

# `x86decomp.errors`

- Area: `toolkit`
- Source path: `src/x86decomp/errors.py`
- SHA-256: `5bb50a4d169960abdc486866d2e68c894d8c13da401361931d86991ff9f8030d`
- Size: `576` bytes
- Lines: `22`

## Module docstring

Typed errors used by the toolkit.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `X86DecompError` | 4 | Base class for user-facing toolkit errors. |
| class | `FormatError` | 8 | Raised when an input binary or document violates its contract. |
| class | `ContractError` | 12 | Raised when structured data violates a toolkit contract. |
| class | `VerificationError` | 16 | Raised when integrity or evidence verification fails. |
| class | `ExternalToolError` | 20 | Raised when a configured external tool cannot be executed successfully. |
