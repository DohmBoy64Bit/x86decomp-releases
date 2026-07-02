---
title: tests/governance/test_worker_thread_safety.py
description: 2 exact current test nodes
original_path: tests/tests-governance-test-worker-thread-safety.html
---

<a id="test-test-worker-uses-exec-wrapper-without-thread-unsafe-preexec"></a>
<a id="test-test-legacy-preexec-compatibility-callback-is-executable"></a>

Section: Source-derived test reference

# `tests/governance/test_worker_thread_safety.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `053888fd3453b44860f529fec44c6d6f14824c09c1a381f66976bcc8fdd6f969`.

Metadata: Toolkit behavior · line 13

### `test_worker_uses_exec_wrapper_without_thread_unsafe_preexec`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `monkeypatch.setattr`, `WorkerRequest`, `execute_worker_request`, `kwargs.get`, `real_popen`, `WorkerLimits`

**Node ID:** `tests/governance/test_worker_thread_safety.py::test_worker_uses_exec_wrapper_without_thread_unsafe_preexec`

Metadata: Toolkit behavior · line 37

### `test_legacy_preexec_compatibility_callback_is_executable`

Retain and directly exercise the 0.4 private callback without forking.

**Direct call names in source:** `WorkerLimits`, `_preexec`, `SimpleNamespace`, `monkeypatch.setitem`, `monkeypatch.setattr`, `callback`, `sessions.append`, `calls.append`

**Node ID:** `tests/governance/test_worker_thread_safety.py::test_legacy_preexec_compatibility_callback_is_executable`
