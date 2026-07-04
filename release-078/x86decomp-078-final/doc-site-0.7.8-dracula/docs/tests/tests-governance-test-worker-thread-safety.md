---
title: tests/governance/test_worker_thread_safety.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/governance/test_worker_thread_safety.py`

**Collected nodes:** 2  
**Source SHA-256:** `053888fd3453b44860f529fec44c6d6f14824c09c1a381f66976bcc8fdd6f969`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_worker_uses_exec_wrapper_without_thread_unsafe_preexec`

No test docstring is declared.

**Direct call names in source:** `WorkerLimits`, `WorkerRequest`, `execute_worker_request`, `kwargs.get`, `monkeypatch.setattr`, `real_popen`  
**Node ID:** `tests/governance/test_worker_thread_safety.py::test_worker_uses_exec_wrapper_without_thread_unsafe_preexec`  
**Area:** Toolkit behavior  
**Source line:** 13

## `test_legacy_preexec_compatibility_callback_is_executable`

Retain and directly exercise the 0.4 private callback without forking.

**Direct call names in source:** `SimpleNamespace`, `WorkerLimits`, `_preexec`, `callback`, `calls.append`, `monkeypatch.setattr`, `monkeypatch.setitem`, `sessions.append`  
**Node ID:** `tests/governance/test_worker_thread_safety.py::test_legacy_preexec_compatibility_callback_is_executable`  
**Area:** Toolkit behavior  
**Source line:** 37
