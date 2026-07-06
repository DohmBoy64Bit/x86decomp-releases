# x86decomp-toolkit 0.7.9 Full Code Review and Audit Report

Generated: 2026-07-05

## Scope and source of truth

Source artifact audited: `/mnt/data/x86decomp-toolkit-0.7.9-docstring-audit-release-bundle.zip`

- Release bundle SHA-256: `cdca1185562f7ceeba3c11e78508e72565402b946d82e0b43b7192ff99ff4d00`
- Matching 0.7.9 doc-site ZIP SHA-256 present locally: `968837c6b8b3be1908d01568ec34b96e2bfff5c402ec882cc259cdf53febb094`
- Clean extraction root: `/mnt/data/audit_079_clean/x86decomp-079-final/x86decomp-toolkit-0.7.9`
- Source tree was not edited during this audit.

## Audit coverage statement

I read every file in the clean extracted source tree by bytes and computed a SHA-256 inventory. There were no read errors.

- Total files read: **444**
- Code/config candidates included in static review: **393**
- Python files parsed and byte-compiled in memory: **207**
- Python parse errors: **0**
- Python in-memory compile errors: **0**
- JSON/TOML/CFG structured parse errors: **0**
- Shell scripts checked with `bash -n`: **3/3 passed**
- Root CLI commands discovered: **166**
- Canonical groups/routes discovered: **59 / 239**
- Missing root dispatch branches: **0**
- Duplicate canonical routes: **0**

The raw evidence file accompanying this report contains the full file inventory, hashes, static-scan hits, duplicate groups, unused-import candidates, and command-surface checks.

## Verification commands run

```bash
# Clean source extraction and full byte inventory were performed from the 0.7.9 ZIP.
python3 /mnt/data/run_audit079_clean.py

# Targeted release-contract/docstring tests on the extracted tree.
PYTHONPATH=src:test-suite/src pytest -q tests/test_docstring_audit.py tests/test_release_contract.py

# Full pytest attempt to observe failure mode.
PYTHONPATH=src:test-suite/src pytest -q -x

# Contract validator attempt to observe Java-parser dependency behavior.
PYTHONPATH=src python3 scripts/validate-contracts.py
```

Observed targeted result: **11 passed** for `tests/test_docstring_audit.py` and `tests/test_release_contract.py`.

Observed full pytest first failure: `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_angr_public_file_wrappers` fails when `angr` is absent because the test directly calls the optional `angr` backend.

## Confirmed non-issues / clean checks

These checks did not produce findings:

- No unreadable files in the clean extraction.
- No Python parse or in-memory compile failures across all 207 Python files.
- No JSON/TOML/CFG parse failures across structured config/schema/example files.
- No `shell=True`, `os.system`, or bare `except:` matches were found in the static scan.
- No missing dispatch branch was found for the 166 root commands; canonical groups are delegated through the canonical dispatcher.
- No duplicate canonical route was found among 239 canonical routes.
- No production function with only `pass`, ellipsis, or empty `return` body was found. The only stub-like bodies detected were test HTTP `log_message` suppressors.
- Placeholder-word hits in production source were mostly domain vocabulary (`stubs`) or explicit anti-placeholder policy/prompts; I did not classify those as unfinished implementation.

## Issue CR-079-001 — Full test-suite is not dependency-adaptive for optional `angr`

**Severity:** High for release verification accuracy; Medium for runtime functionality.

**Evidence:**

```text
151: def test_angr_public_file_wrappers(tmp_path: Path) -> None:
152:     """Verify angr public file wrappers.
153:     
154:     Parameters and return values follow the signature and runtime validation in the body.
155:     """
156:     target = tmp_path / "target.bin"
157:     candidate = tmp_path / "candidate.bin"
158:     target.write_bytes(b"\x31\xc0\xc3")
159:     candidate.write_bytes(b"\x31\xc0\xc3")
160:     assert angr_bounded_compare(target.read_bytes(), candidate.read_bytes(), max_steps=20, max_paths=4)["equivalent_within_completed_model"]
161:     assert angr_bounded_compare_files(target, candidate, max_steps=20, max_paths=4)["equivalent_within_completed_model"]
162:     harness = write_json(
163:         tmp_path / "memory.json",
164:         {
165:             "architecture": "x86",
166:             "regions": [{"name": "a", "pointer_register": "eax", "size": 4, "initial": "symbolic"}],
167:             "observed_regions": ["a"],
168:             "output_registers": ["eax"],
169:             "max_steps": 20,
170:             "max_paths": 4,
171:         },
172:     )
173:     report = angr_memory_alias_compare_files(target, candidate, harness)
174:     assert report["kind"] == "angr_memory_alias_comparison"
```

```text
18: def _load_angr() -> tuple[Any, Any]:
19:     """Load angr.
20:     
21:     Parameters and return values follow the signature and runtime validation in the body.
22:     """
23:     try:
24:         import angr  # type: ignore[import-not-found]
25:         import claripy  # type: ignore[import-not-found]
26:     except ImportError as exc:
27:         raise ExternalToolError("angr backend requires the optional 'angr' dependency") from exc
28:     return angr, claripy
```

The toolkit declares `angr` as an optional extra in `pyproject.toml`, but the public API contract test above calls `angr_bounded_compare`, `angr_bounded_compare_files`, and `angr_memory_alias_compare_files` unconditionally. In the audit environment, full pytest failed at this test with `ExternalToolError: angr backend requires the optional 'angr' dependency`.

**Why this is an issue:** The runtime wrapper behaves honestly by raising a clear optional-dependency error, but the test is not aligned with the packaging contract. A full test run in a minimal installation cannot complete, even though minimal install is valid according to the package metadata. This weakens release verification because “full pytest failed due optional dependency” becomes a recurring non-actionable blocker.

**Recommended modification:** Add `pytest.importorskip("angr")` at the start of this test, split it into an optional-adapter suite, or run it only when the test-suite capability detector reports `angr` installed. Keep a separate test like `tests/test_dynamorio.py::test_angr_backend_has_explicit_optional_dependency_error` to verify the missing-dependency error path.

**Why this fix:** It preserves honest optional dependency handling while allowing minimal and full-adapter verification to be distinguished instead of conflated.

## Issue CR-079-002 — Test-suite adapter catalog treats optional toolkit extras as mandatory

**Severity:** High for test-suite UX and adapter resolution consistency.

**Evidence:**

```text
20: dependencies = []
21: 
22: [project.optional-dependencies]
23: disassembly = ["capstone>=5.0.6,<6"]
24: dynamic = ["unicorn>=2.1.4,<3"]
25: symbolic = ["capstone>=5.0.6,<6", "z3-solver>=4.15,<5"]
26: angr = ["angr>=9.2,<10"]
27: service = ["fastapi>=0.128,<1", "uvicorn>=0.48,<1"]
28: full = ["capstone>=5.0.6,<6", "unicorn>=2.1.4,<3", "z3-solver==4.13.0.0", "fastapi>=0.128,<1", "uvicorn>=0.48,<1", "angr>=9.2,<10"]
29: pe = ["lief>=0.17,<0.18"]
30: dev = ["pytest>=8,<10", "jsonschema>=4.23,<5", "javalang>=0.13,<1", "PyYAML>=6,<7", "build>=1.2,<2"]
```

```text
80:         AdapterSpec(
81:             "capstone",
82:             "Capstone Python bindings",
83:             AdapterKind.PYTHON,
84:             ("disassembly", "matching", "symbolic"),
85:             python_modules=("capstone",),
86:             pip_requirement="capstone>=5.0.6,<6",
87:             optional=False,
88:         ),
89:         AdapterSpec(
90:             "unicorn",
91:             "Unicorn Python bindings",
92:             AdapterKind.PYTHON,
93:             ("dynamic", "functional"),
94:             python_modules=("unicorn",),
95:             pip_requirement="unicorn>=2.1.4,<3",
96:             optional=False,
97:         ),
98:         AdapterSpec(
99:             "z3",
100:             "Z3 Python bindings",
101:             AdapterKind.PYTHON,
102:             ("symbolic", "functional"),
103:             python_modules=("z3",),
104:             pip_requirement="z3-solver>=4.13,<5",
105:             optional=False,
106:         ),
107:         AdapterSpec(
108:             "angr",
109:             "angr",
110:             AdapterKind.PYTHON,
111:             ("angr", "symbolic-memory"),
112:             python_modules=("angr",),
113:             pip_requirement="angr>=9.2,<10",
114:             optional=False,
115:         ),
```

`pyproject.toml` declares `disassembly`, `dynamic`, `symbolic`, `angr`, `service`, and `pe` as optional extras. The test-suite adapter catalog marks several of those same dependencies as `optional=False`, including Capstone, Unicorn, Z3, angr, FastAPI, Uvicorn, and LIEF.

**Why this is an issue:** It makes the adapter capability model stricter than the package installation model. Users with a valid base installation are told required adapters are missing even when those adapters correspond to optional extras. This also explains why full-suite attempts immediately reach optional-adapter failures.

**Recommended modification:** Represent required-ness per suite/capability instead of globally. For example, keep `pytest`, `jsonschema`, Python, and core packaging tools as non-optional for baseline verification, but mark Capstone/Unicorn/Z3/angr/FastAPI/Uvicorn/LIEF as required only for suites that exercise their feature groups. Add a report section that states “blocked optional capability” instead of failing the whole baseline.

**Why this fix:** It preserves strictness for capability-specific gates without mislabeling a base install as incomplete.

## Issue CR-079-003 — Packaged harness self-tests drifted from source self-tests

**Severity:** Medium; High on Windows for packaged test-suite reliability.

**Evidence from source-tree test:**

```text
111: def test_path_detection_preserves_symlink_argv0(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
112:     """Verify path detection preserves symlink argv0.
113:     
114:     Parameters and return values follow the signature and runtime validation in the body.
115:     """
116:     if os.name == "nt":
117:         try:
118:             (tmp_path / "_sym_probe").symlink_to(tmp_path)
119:         except OSError:
120:             return  # Skip on Windows without Developer Mode
121:     target = tmp_path / "generic"
122:     target.write_text("#!/bin/sh\necho generic\n")
123:     target.chmod(0o755)
124:     alias = tmp_path / "special-link"
125:     alias.symlink_to(target)
```

**Evidence from packaged fallback self-test:**

```text
111: def test_path_detection_preserves_symlink_argv0(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
112:     """Verify path detection preserves symlink argv0.
113:     
114:     Parameters and return values follow the signature and runtime validation in the body.
115:     """
116:     target = tmp_path / "generic"
117:     target.write_text("#!/bin/sh\necho generic\n")
118:     target.chmod(0o755)
119:     alias = tmp_path / "special-link"
120:     alias.symlink_to(target)
121:     monkeypatch.setenv("PATH", str(tmp_path))
122:     spec = AdapterSpec("special", "Special", AdapterKind.EXECUTABLE, ("test",), commands=("special-link",), optional=False)
123:     result = detect_adapter(spec, _config(tmp_path))
124:     assert result.installed
125:     assert Path(result.path).name == "special-link"
```

The source test contains a Windows symlink capability guard before creating the symlink. The packaged fallback copy lacks that guard. Other mirrored self-test files differ only in module docstrings, but this file contains behavioral drift.

**Why this is an issue:** The harness chooses `test-suite/tests` when running from the source tree and falls back to packaged `x86decomp_testkit/self_tests` when installed. That means source verification and installed-package verification can behave differently on Windows.

**Recommended modification:** Make the packaged self-tests generated from the source tests during release, or import shared test bodies from one canonical location. Add a synchronization test that diffs the two copies while allowing only known intentional header/module-name differences.

**Why this fix:** It eliminates drift between source and installed test-suite behavior without removing packaged self-test capability.

## Issue CR-079-004 — Read-only FastAPI page uses `innerHTML` with unescaped project JSON

**Severity:** Medium security issue for local service UI; potentially High if serving untrusted project data to a browser.

**Evidence:**

```text
212:     @app.get("/", response_class=HTMLResponse)
213:     def index() -> str:
214:         """Implement index.
215:         
216:         Parameters and return values follow the signature and runtime validation in the body.
217:         """
218:         return """<!doctype html><html><head><meta charset='utf-8'><title>x86decomp</title>
219: <style>body{font:15px system-ui;margin:2rem;max-width:1100px}pre{background:#eee;padding:1rem;overflow:auto}.ok{color:green}.bad{color:#b00}</style></head>
220: <body><h1>x86decomp project</h1><p>This local interface is read-only. Mutations remain evidence-gated through the CLI/MCP transaction journal.</p>
221: <div id='app'>Loading…</div><script>
222: fetch('/api/project').then(r=>r.json()).then(p=>{
223:  const valid=p.verification.valid;
224:  document.getElementById('app').innerHTML=`<h2>Integrity: <span class='${valid?'ok':'bad'}'>${valid}</span></h2><p>${p.pipelines.length} durable pipeline(s)</p><pre>${JSON.stringify(p,null,2)}</pre>`;
225: });</script></body></html>"""
```

The index route builds a client-side page that inserts `JSON.stringify(p, null, 2)` into `innerHTML`. The JSON originates from project files, reports, workflows, and manifests, which may include strings derived from analyzed binaries or user-provided artifacts.

**Why this is an issue:** The service is read-only, but read-only does not prevent browser script execution. A crafted project string containing HTML/script-breaking content could be rendered through `innerHTML`. This is a local UI XSS risk and violates a defense-in-depth expectation for tooling that inspects untrusted reverse-engineering inputs.

**Recommended modification:** Replace the `innerHTML` assignment with DOM construction and `textContent` for the JSON block. Alternatively, HTML-escape JSON before insertion and add a restrictive Content Security Policy. A safe pattern is: create the status nodes explicitly, set CSS class names from booleans only, and assign `pre.textContent = JSON.stringify(p, null, 2)`.

**Why this fix:** It keeps the read-only UI behavior but prevents project-controlled text from becoming markup.

## Issue CR-079-005 — Redundant public command aliases overlap with canonical capability routes

**Severity:** Medium for CLI maintainability and user-facing command design.

**Evidence from command-surface audit:**

```json
[
  {
    "action": "generate",
    "flat": "hybrid-generate",
    "group": "hybrid",
    "owner": "assembly"
  },
  {
    "action": "check",
    "flat": "project-check",
    "group": "project",
    "owner": "assembly"
  }
]
```

The static command audit found no missing dispatch branches and no duplicate canonical routes. It did find two flat root commands whose names map directly onto canonical group/action routes: `hybrid-generate` and `project-check`.

**Why this is an issue:** The release model favors one executable and canonical capability groups. Parallel flat aliases for the same capability increase test/documentation burden and make the surface less intuitive, especially after the project moved away from version-specific or parallel command planes.

**Recommended modification:** Keep backward-compatible aliases for one release if needed, but declare the canonical commands (`x86decomp hybrid generate`, `x86decomp project check`) as primary. Internally route the flat aliases through the canonical dispatcher and document them as compatibility aliases, or remove them only after a tested compatibility plan.

**Why this fix:** It reduces redundant command surface while respecting the no-regression rule.

## Issue CR-079-006 — Duplicate subsystem helper logic should be centralized

**Severity:** Medium maintainability issue.

**Evidence — repeated CLI helpers:**

```text
29: def _json_arg(raw: str | None, default: Any) -> Any:
30:     """Implement json arg.
31:     
32:     Parameters and return values follow the signature and runtime validation in the body.
33:     """
34:     if raw is None:
35:         return default
36:     try:
37:         return json.loads(raw)
38:     except json.JSONDecodeError as exc:
39:         raise ContractError(f"invalid JSON argument: {exc}") from exc
40: 
41: 
42: def _emit(value: Any) -> None:
43:     """Emit the requested operation.
44:     
45:     Parameters and return values follow the signature and runtime validation in the body.
46:     """
47:     if hasattr(value, "__dict__"):
48:         value = value.__dict__
49:     print(json.dumps(value, indent=2, sort_keys=True, default=str))
50: 
```

```text
26: def _json(raw: str | None, default: Any) -> Any:
27:     """Implement json.
28:     
29:     Parameters and return values follow the signature and runtime validation in the body.
30:     """
31:     if raw is None: return default
32:     try: return json.loads(raw)
33:     except json.JSONDecodeError as exc: raise ContractError(f"invalid JSON argument: {exc}") from exc
34: 
35: 
36: def _json_file(path: str) -> Any:
37:     """Implement json file.
38:     
39:     Parameters and return values follow the signature and runtime validation in the body.
40:     """
41:     return json.loads(Path(path).read_text(encoding="utf-8"))
42: 
43: 
44: def _emit(value: Any) -> None:
45:     """Emit the requested operation.
46:     
47:     Parameters and return values follow the signature and runtime validation in the body.
48:     """
49:     if hasattr(value, "__dict__"): value = value.__dict__
50:     print(json.dumps(value, indent=2, sort_keys=True, default=str))
```

```text
55: def _json(raw: str|None, default: Any) -> Any:
56:     """Implement json.
57:     
58:     Parameters and return values follow the signature and runtime validation in the body.
59:     """
60:     if raw is None: return default
61:     try: return json.loads(raw)
62:     except json.JSONDecodeError as exc: raise ContractError(f'invalid JSON argument: {exc}') from exc
63: 
64: def _emit(value: Any) -> None:
65:     """Emit the requested operation.
66:     
67:     Parameters and return values follow the signature and runtime validation in the body.
68:     """
69:     if hasattr(value,'__dict__'): value=value.__dict__
70:     print(json.dumps(value,indent=2,sort_keys=True,default=str))
```

**Evidence — repeated store row JSON decoder:**

```text
116:     @staticmethod
117:     def decode(row: Any, *json_fields: str) -> dict[str, Any]:
118:         """Decode the requested operation.
119:         
120:         Parameters and return values follow the signature and runtime validation in the body.
121:         """
122:         result = dict(row)
123:         for field in json_fields:
124:             if field in result:
125:                 raw = result.pop(field)
126:                 result[field[:-5] if field.endswith("_json") else field] = (
127:                     None if raw is None else json.loads(raw)
128:                 )
129:         return result
```

```text
132:     def decode(row: Any, *json_fields: str) -> dict[str, Any]:
133:         """Decode the requested operation.
134:         
135:         Parameters and return values follow the signature and runtime validation in the body.
136:         """
137:         result = dict(row)
138:         for field in json_fields:
139:             if field in result:
140:                 raw = result.pop(field)
141:                 result[field[:-5] if field.endswith("_json") else field] = None if raw is None else json.loads(raw)
142:         return result
```

```text
183:     def decode(row: Any, *json_fields: str) -> dict[str, Any]:
184:         """Decode the requested operation.
185:         
186:         Parameters and return values follow the signature and runtime validation in the body.
187:         """
188:         result = dict(row)
189:         for field in json_fields:
190:             if field in result:
191:                 raw = result.pop(field)
192:                 result[field[:-5] if field.endswith('_json') else field] = None if raw is None else json.loads(raw)
193:         return result
```

The duplicate-body detector found exact or near-exact implementations for CLI JSON parsing/output helpers and row JSON-field decoding. The store `decode` method is duplicated across three store classes; CLI `_json`/`_json_arg` and `_emit` are duplicated across governance/native/reconstruction CLIs.

**Why this is an issue:** These are small functions, but they sit on command and persistence paths. Duplicating them makes error-message behavior, JSON serialization defaults, and future fixes easy to apply inconsistently.

**Recommended modification:** Move CLI helpers into a shared module such as `x86decomp.cli_utils` and row decode/encode helpers into a shared store base/mixin. Preserve public class names and command behavior; only move helper implementation.

**Why this fix:** It removes repeated logic without reducing features or altering the command surface.

## Issue CR-079-007 — Production source contains unused imports / dead import code

**Severity:** Low; Medium as a cleanup and lint-gate issue.

The AST unused-import pass found **32 production-source unused imports** after excluding `__init__.py` re-export modules. These are dead code in the import graph; they increase startup/import noise and make actual dependencies harder to audit.

| File | Line | Import module | Imported name | Bound name |
|---|---:|---|---|---|
| `src/x86decomp/assembly/materialize.py` | 12 | `tempfile` | `tempfile` | `tempfile` |
| `src/x86decomp/cli.py` | 68 | `worker` | `WorkerLimits` | `WorkerLimits` |
| `src/x86decomp/coff.py` | 17 | `dataclasses` | `field` | `field` |
| `src/x86decomp/coff.py` | 19 | `typing` | `Mapping` | `Mapping` |
| `src/x86decomp/compiler_worker.py` | 11 | `os` | `os` | `os` |
| `src/x86decomp/content_store.py` | 13 | `tempfile` | `tempfile` | `tempfile` |
| `src/x86decomp/cpp_recovery.py` | 9 | `collections` | `defaultdict` | `defaultdict` |
| `src/x86decomp/governance/cli.py` | 11 | `typing` | `Callable` | `Callable` |
| `src/x86decomp/harness_generator.py` | 12 | `abi` | `CallingConvention` | `CallingConvention` |
| `src/x86decomp/hybrid.py` | 5 | `json` | `json` | `json` |
| `src/x86decomp/image_match.py` | 17 | `util` | `sha256_bytes` | `sha256_bytes` |
| `src/x86decomp/integration.py` | 18 | `errors` | `ExternalToolError` | `ExternalToolError` |
| `src/x86decomp/linker_layout.py` | 15 | `typing` | `Sequence` | `Sequence` |
| `src/x86decomp/local_llm/matching.py` | 8 | `tempfile` | `tempfile` | `tempfile` |
| `src/x86decomp/local_llm/matching.py` | 18 | `x86decomp.util` | `sha256_bytes` | `sha256_bytes` |
| `src/x86decomp/local_llm/matching.py` | 21 | `prompts` | `build_messages` | `build_messages` |
| `src/x86decomp/msvc_metadata.py` | 19 | `errors` | `ContractError` | `ContractError` |
| `src/x86decomp/native/closed_loop.py` | 7 | `json` | `json` | `json` |
| `src/x86decomp/native/matching.py` | 7 | `json` | `json` | `json` |
| `src/x86decomp/project_state.py` | 23 | `errors` | `VerificationError` | `VerificationError` |
| `src/x86decomp/project_state.py` | 24 | `util` | `atomic_write_bytes` | `atomic_write_bytes` |
| `src/x86decomp/project_template.py` | 10 | `json` | `json` | `json` |
| `src/x86decomp/reconstruction/acceleration.py` | 13 | `subprocess` | `subprocess` | `subprocess` |
| `src/x86decomp/reconstruction/acceleration.py` | 17 | `typing` | `Iterable` | `Iterable` |
| `src/x86decomp/reconstruction/acceleration.py` | 24 | `x86decomp.util` | `sha256_bytes` | `sha256_bytes` |
| `src/x86decomp/reconstruction/generated_tests.py` | 7 | `pathlib` | `Path` | `Path` |
| `src/x86decomp/reconstruction/store.py` | 8 | `pathlib` | `Path` | `Path` |
| `src/x86decomp/reconstruction/store.py` | 11 | `x86decomp.contracts` | `canonical_json` | `canonical_json` |
| `src/x86decomp/reconstruction/store.py` | 11 | `x86decomp.contracts` | `utc_now` | `utc_now` |
| `src/x86decomp/release_gate.py` | 11 | `json` | `json` | `json` |
| `src/x86decomp/reproducibility.py` | 9 | `json` | `json` | `json` |
| `src/x86decomp/reproducibility.py` | 10 | `os` | `os` | `os` |

**Why this is an issue:** Unused imports are low-risk individually, but in a toolkit with optional adapters they can obscure whether a dependency is actually required. They also indicate the absence of a lint gate such as Ruff/Pyflakes in release verification.

**Recommended modification:** Remove the listed imports where confirmed unused, then add a lightweight lint step that ignores intentional `__init__.py` re-exports but fails on unused imports in implementation modules.

**Why this fix:** It reduces dead code without changing behavior.

## Issue CR-079-008 — `llm_batch_create` suppresses secondary manifest-ID read errors

**Severity:** Low error-handling diagnostic issue.

**Evidence:**

```text
327:     for manifest_path in sorted(functions_root.glob("*/function.json")):
328:         artifact = manifest_path.parent
329:         try:
330:             manifest = validate_function_manifest(load_json(manifest_path))
331:             rg = _contiguous_single_range(manifest)
332:             if rg["size"] > max_bytes:
333:                 raise ContractError(f"function body size {rg['size']} exceeds max_bytes {max_bytes}")
334:             out = output / f"{manifest['id'].replace(':', '_')}.json"
335:             report = llm_job_from_function_packet(artifact, out, architecture=architecture, image_base=image_base, max_attempts=max_attempts, overwrite=overwrite)
336:             created.append(report)
337:         except Exception as exc:
338:             fid = None
339:             try: fid = load_json(manifest_path).get("id")
340:             except Exception: pass
341:             blocked.append({"artifact_dir": str(artifact), "function_id": fid, "reason": str(exc)})
342:     report = {"schema_version": 1, "kind": "local_llm_batch_create_report", "created_at": utc_now(), "created_count": len(created), "blocked_count": len(blocked), "created": created, "blocked": blocked}
```

When processing a function manifest fails, the function tries to recover `id` for the blocked report. If that secondary `load_json` also fails, the code silently `pass`es and records `function_id: None`.

**Why this is an issue:** The primary error is preserved, so this is not an empty success path. However, suppressing the secondary failure loses useful diagnostic detail for corrupt or unreadable manifests.

**Recommended modification:** Capture the secondary exception into the blocked record, e.g. `function_id_error: str(id_exc)`, or avoid re-reading by initializing `manifest_id` only after a successful load. Use a narrow `except Exception as id_exc` with explicit diagnostic storage instead of `except Exception: pass`.

**Why this fix:** It keeps batch processing resilient while improving evidence quality.

## Issue CR-079-009 — Docstring coverage exists, but many generated docstrings are not semantically useful

**Severity:** Medium documentation/API maintainability issue.

**Evidence examples:**

```text
26: def _json(raw: str | None, default: Any) -> Any:
27:     """Implement json.
28:     
29:     Parameters and return values follow the signature and runtime validation in the body.
30:     """
31:     if raw is None: return default
32:     try: return json.loads(raw)
33:     except json.JSONDecodeError as exc: raise ContractError(f"invalid JSON argument: {exc}") from exc
```

```text
94:     @app.get("/api/health")
95:     def health() -> dict[str, Any]:
96:         """Implement health.
97:         
98:         Parameters and return values follow the signature and runtime validation in the body.
99:         """
100:         snapshot = service_snapshot(root)
101:         return {
102:             "toolkit_version": snapshot["toolkit_version"],
103:             "project_valid": bool(snapshot["verification"].get("valid")),
104:             "state_valid": None if snapshot["state_check"] is None else bool(snapshot["state_check"]["valid"]),
105:             "read_only": True,
```

The 0.7.9 release has complete docstring presence, and `tests/test_docstring_audit.py` passed. However, many docstrings are template-like (“Implement json”, “Parameters and return values follow the signature and runtime validation in the body”) rather than concise behavioral documentation.

**Why this is an issue:** Presence-only docstring coverage does not necessarily help a maintainer understand commands, persistence invariants, adapter behavior, or error contracts. This is not a runtime bug, but it is a quality gap for a release whose purpose is docstring audit coverage.

**Recommended modification:** Replace templated docstrings in public commands/classes and complex helpers with behavior-specific docstrings. Prioritize modules under `src/x86decomp/*/cli.py`, stores, optional-adapter loaders, security-sensitive worker/service code, and release-gate functions. Keep a docstring audit that checks presence, but add a heuristic or review checklist for template phrases.

**Why this fix:** It converts docstring coverage from a numeric gate into useful API documentation.

## Issue CR-079-010 — Mirrored corpus and example duplicates need explicit ownership rules

**Severity:** Low for current behavior; Medium for future drift risk.

Exact duplicate files found:

- `corpus/ground_truth_sources/aliasing.c`, `src/x86decomp/corpus/ground_truth_sources/aliasing.c`
- `corpus/ground_truth_sources/arithmetic.c`, `src/x86decomp/corpus/ground_truth_sources/arithmetic.c`
- `corpus/ground_truth_sources/bitfields.c`, `src/x86decomp/corpus/ground_truth_sources/bitfields.c`
- `corpus/ground_truth_sources/branches.c`, `src/x86decomp/corpus/ground_truth_sources/branches.c`
- `corpus/ground_truth_sources/calling_conventions.c`, `src/x86decomp/corpus/ground_truth_sources/calling_conventions.c`
- `corpus/ground_truth_sources/classes.cpp`, `src/x86decomp/corpus/ground_truth_sources/classes.cpp`
- `corpus/ground_truth_sources/eh_multiple.cpp`, `src/x86decomp/corpus/ground_truth_sources/eh_multiple.cpp`
- `corpus/ground_truth_sources/exceptions.cpp`, `src/x86decomp/corpus/ground_truth_sources/exceptions.cpp`
- `corpus/ground_truth_sources/floating_point.c`, `src/x86decomp/corpus/ground_truth_sources/floating_point.c`
- `corpus/ground_truth_sources/globals.c`, `src/x86decomp/corpus/ground_truth_sources/globals.c`
- `corpus/ground_truth_sources/indirect_calls.c`, `src/x86decomp/corpus/ground_truth_sources/indirect_calls.c`
- `corpus/ground_truth_sources/loops.c`, `src/x86decomp/corpus/ground_truth_sources/loops.c`
- `corpus/ground_truth_sources/member_pointers.cpp`, `src/x86decomp/corpus/ground_truth_sources/member_pointers.cpp`
- `corpus/ground_truth_sources/multiple_inheritance.cpp`, `src/x86decomp/corpus/ground_truth_sources/multiple_inheritance.cpp`
- `corpus/ground_truth_sources/static_initializers.cpp`, `src/x86decomp/corpus/ground_truth_sources/static_initializers.cpp`
- `corpus/ground_truth_sources/structs.c`, `src/x86decomp/corpus/ground_truth_sources/structs.c`
- `corpus/ground_truth_sources/switch_dense.c`, `src/x86decomp/corpus/ground_truth_sources/switch_dense.c`
- `corpus/ground_truth_sources/tail_calls.c`, `src/x86decomp/corpus/ground_truth_sources/tail_calls.c`
- `corpus/ground_truth_sources/templates.cpp`, `src/x86decomp/corpus/ground_truth_sources/templates.cpp`
- `corpus/ground_truth_sources/tls.c`, `src/x86decomp/corpus/ground_truth_sources/tls.c`
- `corpus/ground_truth_sources/unions.c`, `src/x86decomp/corpus/ground_truth_sources/unions.c`
- `corpus/ground_truth_sources/varargs.c`, `src/x86decomp/corpus/ground_truth_sources/varargs.c`
- `corpus/ground_truth_sources/vectorizable.c`, `src/x86decomp/corpus/ground_truth_sources/vectorizable.c`
- `corpus/ground_truth_sources/virtual_inheritance.cpp`, `src/x86decomp/corpus/ground_truth_sources/virtual_inheritance.cpp`
- `examples/integration/candidate.py`, `examples/integration/target.py`
- `examples/validators/add_stack_candidate.bin`, `examples/validators/add_stack_target.bin`
- `setup.cfg`, `test-suite/setup.cfg`

The 24 ground-truth corpus source files are intentionally mirrored between `corpus/ground_truth_sources` and `src/x86decomp/corpus/ground_truth_sources`; `tests/test_release_contract.py` verifies those mirrors are in sync. The duplicate integration demo scripts and validator binaries are also exact duplicate examples.

**Why this is an issue:** The ground-truth mirror has an explicit sync test, so I do not classify it as dead code. The risk is maintenance drift if new corpus/example files are added without a canonical generation/sync step. The exact duplicate `candidate.py`/`target.py` demo only tests the happy path; it does not exercise mismatch reporting.

**Recommended modification:** Keep one canonical source for corpus files and generate/package the mirror during release, or keep the current mirror but preserve the sync test. For integration demos, add a second negative scenario with an intentionally different candidate so the example suite demonstrates failure evidence as well as success evidence.

**Why this fix:** It preserves package-data availability while making duplication intentional and tested.

## Issue CR-079-011 — Z3 dependency constraints disagree across package extras and adapter catalog

**Severity:** Medium packaging/reproducibility issue.

**Evidence:**

```text
25: symbolic = ["capstone>=5.0.6,<6", "z3-solver>=4.15,<5"]
28: full = ["capstone>=5.0.6,<6", "unicorn>=2.1.4,<3", "z3-solver==4.13.0.0", "fastapi>=0.128,<1", "uvicorn>=0.48,<1", "angr>=9.2,<10"]
```

```text
99:         AdapterSpec(
100:             "z3",
101:             "Z3 Python bindings",
102:             AdapterKind.PYTHON,
103:             ("symbolic", "functional"),
104:             python_modules=("z3",),
105:             pip_requirement="z3-solver>=4.13,<5",
106:             optional=False,
107:         ),
```

`pyproject.toml` requires `z3-solver>=4.15,<5` for the `symbolic` extra, but the `full` extra pins `z3-solver==4.13.0.0`, and the test-suite adapter catalog accepts `z3-solver>=4.13,<5`.

**Why this is an issue:** The `full` extra should be a superset of symbolic capability dependencies, but its Z3 pin is lower than the symbolic lower bound. Installing combined extras such as `x86decomp-toolkit[full,symbolic]` can produce dependency conflicts, and the adapter catalog can report Z3 acceptable at a version the package’s symbolic extra does not accept.

**Recommended modification:** Choose one supported Z3 range and use it consistently in `symbolic`, `full`, and the adapter catalog. If `4.13.0.0` is intentionally pinned for solver determinism, lower the `symbolic` bound and document the pin. If `>=4.15` is required by code/tests, update `full` and the adapter catalog to match.

**Why this fix:** It makes packaging, adapter resolution, and reproducible test environments agree on the same solver contract.

## Additional duplicate-body observations

Selected duplicate function-body groups from the static detector:

- group `47493b05205a` (19 copies):
  - `src/x86decomp/assembly/pipeline.py:104` `AssemblyPipeline.__init__` (7 lines, normalized 225 bytes)
  - `src/x86decomp/native/closed_loop.py:23` `ClosedLoop.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/hybrid_composer.py:22` `HybridComposer.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/matching.py:99` `FunctionMatching.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/pe_reconstruction.py:85` `PEReconstruction.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/runtime.py:23` `RuntimeValidation.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/slots.py:63` `FunctionSlots.__init__` (7 lines, normalized 225 bytes)
  - `src/x86decomp/native/staging.py:34` `StagingBridge.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/native/windows_tools.py:58` `WindowsTools.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/abi_contracts.py:19` `ABIContracts.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/builds.py:19` `BuildManager.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/capsules.py:20` `Capsules.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/generated_tests.py:18` `GeneratedTests.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/headers.py:18` `HeaderManager.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/libraries.py:16` `LibraryRecognition.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/project_layout.py:19` `ProjectLayout.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/provenance.py:19` `ProvenanceLedger.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/security.py:17` `SecurityReview.__init__` (6 lines, normalized 225 bytes)
  - `src/x86decomp/reconstruction/semantic_changesets.py:17` `SemanticChangeSets.__init__` (6 lines, normalized 225 bytes)
- group `faf1f506bbc0` (8 copies):
  - `src/x86decomp/governance/campaigns.py:20` `CampaignEngine.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/consensus.py:20` `ConsensusEngine.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/hypotheses.py:84` `HypothesisLedger.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/knowledge_graph.py:20` `KnowledgeGraph.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/plugins.py:25` `PluginRegistry.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/proofs.py:28` `ProofLedger.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/reviews.py:21` `ReviewQueue.__init__` (7 lines, normalized 267 bytes)
  - `src/x86decomp/governance/workers.py:21` `WorkerRegistry.__init__` (7 lines, normalized 267 bytes)
- group `31c5340ab773` (3 copies):
  - `src/x86decomp/assembly/store.py:117` `AssemblyStore.decode` (13 lines, normalized 1196 bytes)
  - `src/x86decomp/native/store.py:132` `NativeStore.decode` (11 lines, normalized 1196 bytes)
  - `src/x86decomp/reconstruction/store.py:183` `ReconstructionStore.decode` (11 lines, normalized 1196 bytes)
- group `d01a1c5b3918` (3 copies):
  - `src/x86decomp/governance/cli.py:29` `_json_arg` (11 lines, normalized 654 bytes)
  - `src/x86decomp/native/cli.py:26` `_json` (8 lines, normalized 654 bytes)
  - `src/x86decomp/reconstruction/cli.py:55` `_json` (8 lines, normalized 654 bytes)
- group `07606bf9717a` (3 copies):
  - `src/x86decomp/governance/cli.py:42` `_emit` (8 lines, normalized 603 bytes)
  - `src/x86decomp/native/cli.py:44` `_emit` (7 lines, normalized 603 bytes)
  - `src/x86decomp/reconstruction/cli.py:64` `_emit` (7 lines, normalized 603 bytes)
- group `c160294d65f5` (2 copies):
  - `src/x86decomp/governance/cli.py:255` `main` (13 lines, normalized 1307 bytes)
  - `src/x86decomp/reconstruction/cli.py:476` `main` (9 lines, normalized 1307 bytes)
- group `ba95bb0feba8` (2 copies):
  - `src/x86decomp/cli.py:90` `_path` (6 lines, normalized 148 bytes)
  - `test-suite/src/x86decomp_testkit/cli.py:20` `_path` (6 lines, normalized 148 bytes)

I did not classify all duplicate bodies as defects. Many are constructor boilerplate, test mirrors, or intentional command wrappers. The confirmed modification targets are the shared CLI helpers and store decoding helpers above.

## Full-suite and environment limitations

- Full pytest was attempted and failed first on missing optional `angr`; the run was not a complete pass/fail enumeration of all possible optional-adapter failures.
- `scripts/validate-contracts.py` failed because `javalang` is not installed in this environment. The Java files were still byte-read and hashed; Java syntax/type validation was not claimed.
- Ghidra script runtime behavior was not executed because Ghidra APIs are not available in this environment.
- External adapters such as Ghidra, DynamoRIO, LM Studio, Ollama, vLLM, LocalAI, compilers, and Windows-native tooling were not live-executed.

## Recommended next release plan

1. Fix CR-079-001 and CR-079-002 first so baseline and full-adapter verification are separated cleanly.
2. Fix CR-079-003 before publishing another test-suite wheel, because packaged/source self-test drift can create platform-specific failures.
3. Fix CR-079-004 before encouraging use of the read-only FastAPI UI on untrusted projects.
4. Resolve CR-079-011 so `symbolic`, `full`, and adapter-catalog Z3 requirements agree.
5. Remove dead imports and centralize duplicate helpers under a no-regression test pass.
6. Decide whether flat aliases `project-check` and `hybrid-generate` remain supported compatibility aliases or are fully consumed into canonical command routes.
7. Improve docstrings semantically in high-value modules instead of relying on presence-only coverage.

## Raw evidence artifact

Raw audit evidence file: `/mnt/data/x86decomp_079_code_audit_clean_raw.json`

- Raw evidence SHA-256: `6d63ac335fcc1a4be7656e8e7aa2b7a935d4a490b0399f5bf6744a8c6ed9b007`
