---
title: x86decomp.synthetic_corpus
description: Module reference for x86decomp.synthetic_corpus.
---

# `x86decomp.synthetic_corpus`

- Area: `toolkit`
- Source path: `src/x86decomp/synthetic_corpus.py`
- SHA-256: `432382a2bab467462c312306adf333e3151c8a28ae2ece0f4e7f6afd42bc5358`
- Size: `13970` bytes
- Lines: `380`

## Module docstring

Deterministic ground-truth source corpus generation.

The generator expands a small, reviewed family of source templates into a
configurable set of C and C++ translation units.  Every generated file is
content-hashed and described by parameters in a manifest.  The output is
source evidence only: generation does not claim that any compiler, optimization
level, or resulting binary has been tested until ``ground-truth-build`` records
a successful build.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_symbol` | 25 | Support symbol processing for internal toolkit callers. |
| function | `_c_arithmetic` | 35 | Support c arithmetic processing for internal toolkit callers. |
| function | `_c_branches` | 49 | Support c branches processing for internal toolkit callers. |
| function | `_c_loop` | 66 | Support c loop processing for internal toolkit callers. |
| function | `_c_switch` | 84 | Support c switch processing for internal toolkit callers. |
| function | `_c_struct_alias` | 100 | Support c struct alias processing for internal toolkit callers. |
| function | `_c_bitfield` | 124 | Support c bitfield processing for internal toolkit callers. |
| function | `_c_float` | 144 | Support c float processing for internal toolkit callers. |
| function | `_c_indirect` | 158 | Support c indirect processing for internal toolkit callers. |
| function | `_cpp_virtual` | 170 | Support cpp virtual processing for internal toolkit callers. |
| function | `_cpp_multiple_inheritance` | 194 | Support cpp multiple inheritance processing for internal toolkit callers. |
| function | `_cpp_exception` | 211 | Support cpp exception processing for internal toolkit callers. |
| function | `_cpp_template` | 228 | Support cpp template processing for internal toolkit callers. |
| function | `generate_synthetic_corpus` | 256 | Generate deterministic source cases and a compiler-corpus input manifest. |
| function | `verify_synthetic_corpus` | 344 | Verify synthetic corpus for the current toolkit workflow. |
