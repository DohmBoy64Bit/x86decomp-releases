---
title: x86decomp.integration
description: Manifest-driven integration scenario runner.
original_path: features/x86decomp-integration.html
---

<a id="function-require-string-list"></a>
<a id="function-resolve-existing"></a>
<a id="function-parse-stdin"></a>
<a id="function-copy-fixtures"></a>
<a id="function-substitute-command"></a>
<a id="function-bounded-output"></a>
<a id="function-run-side"></a>
<a id="function-observe-file"></a>
<a id="function-compare-stream"></a>
<a id="function-run-integration-scenarios"></a>

Section: Source-derived feature and function reference

# x86decomp.integration

Manifest-driven integration scenario runner.

Metadata: core · current · 10 functions/methods

**Source:** `src/x86decomp/integration.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `cb8157c8210544e2ed4730e8bdb01f0a77dc9d05f683d43154cba1bf93c1e845`.

## Functions and methods

Metadata: internal · line 24

### _require_string_list

No function or method docstring is declared in the v0.7.4 source.

```
def _require_string_list(value: Any, name: str, *, nonempty: bool = False) -> list[str]
```

**Catalog symbol:** `x86decomp.integration:_require_string_list`

Metadata: internal · line 32

### _resolve_existing

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_existing(base: Path, value: Any, name: str) -> Path
```

**Catalog symbol:** `x86decomp.integration:_resolve_existing`

Metadata: internal · line 41

### _parse_stdin

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_stdin(base: Path, value: Any) -> bytes
```

**Catalog symbol:** `x86decomp.integration:_parse_stdin`

Metadata: internal · line 63

### _copy_fixtures

No function or method docstring is declared in the v0.7.4 source.

```
def _copy_fixtures(base: Path, workdir: Path, fixtures: Any) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.integration:_copy_fixtures`

Metadata: internal · line 94

### _substitute_command

No function or method docstring is declared in the v0.7.4 source.

```
def _substitute_command(command: list[str], *, artifact: Path, workdir: Path) -> list[str]
```

**Catalog symbol:** `x86decomp.integration:_substitute_command`

Metadata: internal · line 108

### _bounded_output

No function or method docstring is declared in the v0.7.4 source.

```
def _bounded_output(data: bytes, limit: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:_bounded_output`

Metadata: internal · line 119

### _run_side

No function or method docstring is declared in the v0.7.4 source.

```
def _run_side(*, base: Path, scenario_id: str, side_name: str, spec: Any, wrapper_prefix: list[str], timeout_seconds: int, stdin_data: bytes, fixtures: Any, output_limit: int) -> tuple[dict[str, Any], Path]
```

**Catalog symbol:** `x86decomp.integration:_run_side`

Metadata: internal · line 197

### _observe_file

No function or method docstring is declared in the v0.7.4 source.

```
def _observe_file(workdir: Path, item: Any, *, side: str, index: int, output_limit: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:_observe_file`

Metadata: internal · line 251

### _compare_stream

No function or method docstring is declared in the v0.7.4 source.

```
def _compare_stream(name: str, mode: Any, target: bytes, candidate: bytes) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.integration:_compare_stream`

Metadata: public · line 273

### run_integration_scenarios

Execute and compare all declared integration scenarios.

```
def run_integration_scenarios(manifest_path: Path, *, allow_host_execution: bool = False, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.integration:run_integration_scenarios`
