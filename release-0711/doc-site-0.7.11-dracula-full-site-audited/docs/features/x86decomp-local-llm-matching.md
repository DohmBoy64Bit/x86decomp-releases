---
title: x86decomp.local_llm.matching
description: Module reference for x86decomp.local_llm.matching.
---

# `x86decomp.local_llm.matching`

- Area: `toolkit`
- Source path: `src/x86decomp/local_llm/matching.py`
- SHA-256: `9b392884b6a186206dd50705b4099157c8073aa77512c5b144a1a358991e8d66`
- Size: `19200` bytes
- Lines: `422`

## Module docstring

Local-model C generation and deterministic byte-match verification loop.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_parse_candidate` | 35 | Support parse candidate processing for internal toolkit callers. |
| function | `_prepare_output` | 91 | Support prepare output processing for internal toolkit callers. |
| function | `_feedback_from_compile` | 105 | Support feedback from compile processing for internal toolkit callers. |
| function | `_feedback_from_diff` | 116 | Support feedback from diff processing for internal toolkit callers. |
| function | `generate_candidate` | 130 | Generate and validate one uncompiled C proposal. |
| function | `run_match_loop` | 174 | Run bounded local generation, compilation, relocation, and exact comparison. |
| function | `verify_match_report` | 366 | Verify report invariants and every referenced accepted artifact hash. |
