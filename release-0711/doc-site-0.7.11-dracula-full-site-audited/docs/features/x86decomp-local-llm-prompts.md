---
title: x86decomp.local_llm.prompts
description: Module reference for x86decomp.local_llm.prompts.
---

# `x86decomp.local_llm.prompts`

- Area: `toolkit`
- Source path: `src/x86decomp/local_llm/prompts.py`
- SHA-256: `03aa0e774538d41645426c911742ae8f710df75b7f1b126493428c166a347918`
- Size: `9726` bytes
- Lines: `204`

## Module docstring

Deterministic, injection-resistant prompts for C candidate generation.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_text` | 15 | Support text processing for internal toolkit callers. |
| function | `_integer` | 31 | Support integer processing for internal toolkit callers. |
| function | `_resolve_job_path` | 38 | Support resolve job path processing for internal toolkit callers. |
| function | `load_job` | 49 | Load and normalize a local-LLM generation/matching job. |
| function | `_evidence_block` | 131 | Support evidence block processing for internal toolkit callers. |
| function | `build_messages` | 146 | Build a deterministic two-message prompt with explicit trust boundaries. |
| function | `prompt_record` | 193 | Execute the prompt record operation for the current toolkit workflow. |
