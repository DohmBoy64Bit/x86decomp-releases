---
title: x86decomp_testkit.self_tests.test_adapter_detection_resolution
description: Module reference for x86decomp_testkit.self_tests.test_adapter_detection_resolution.
---

# `x86decomp_testkit.self_tests.test_adapter_detection_resolution`

- Area: `test-suite`
- Source path: `test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py`
- SHA-256: `f5088b0b7ffcea762bf15990d087f76b782ae7d2ad88316aa0f532e5620c5cd3`
- Size: `5236` bytes
- Lines: `114`

## Module docstring

Provide the installed test-suite implementation for the `x86decomp_testkit.self_tests.test_adapter_detection_resolution` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_config` | 15 | Support config processing for internal toolkit callers. |
| function | `test_installed_adapter_never_prompts` | 22 | Verify installed adapter never prompts behavior. |
| function | `prompt` | 28 | Execute the prompt operation for the current toolkit workflow. |
| function | `test_missing_adapter_prompts_custom_path_then_accepts` | 38 | Verify missing adapter prompts custom path then accepts behavior. |
| function | `prompt` | 48 | Execute the prompt operation for the current toolkit workflow. |
| function | `test_missing_noninteractive_is_explicit_unresolved` | 60 | Verify missing noninteractive is explicit unresolved behavior. |
| function | `test_environment_and_configured_root_detection` | 69 | Verify environment and configured root detection behavior. |
| function | `test_path_detection_preserves_symlink_argv0` | 87 | Verify that adapter detection keeps a symlinked argv0 path when supported. |
| function | `test_missing_python_adapter_accepts_custom_interpreter` | 105 | Verify missing python adapter accepts custom interpreter behavior. |
