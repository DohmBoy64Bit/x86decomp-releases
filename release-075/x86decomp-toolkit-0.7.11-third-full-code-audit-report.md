# x86decomp-toolkit 0.7.11 third full code audit report

Source of truth: uploaded `x86decomp-toolkit-0.7.11-second-audit-fix-release-bundle(1).zip`.

## Executive summary

- Files read and hashed from ZIP: **455/455**.
- Code/config candidates reviewed: **439**.
- Python parsed: **213** files, **160** classes, **1451** functions/methods, **0** parse errors.
- Source hash verification: **PASS**.
- `compileall`: **PASS**.
- Production pyflakes: **PASS**.
- Whole-codebase pyflakes including tests: **FAIL**.
- Contract/schema validation: **PASS**.
- Command surface: **166** root commands, **59** canonical groups, **239** canonical routes, **0** noncanonical missing dispatch branches.

Confirmed findings: **9**.

## Confirmed findings

### AUDIT-0711-01: Whole-codebase pyflakes fails on test and test-suite files while production lint is clean

- Severity: **medium**
- Category: **test/lint hygiene**
- Why it matters: The project declares pyflakes as a dev gate, but the gate currently stays green only when tests are excluded. Unused imports and an unused local assignment in tests reduce signal quality and can hide future real regressions.
- How I would modify it: Remove the unused imports, remove or assert the unused local `result`, then make the release lint gate cover tests and test-suite tests as well as production sources.
- Evidence:

```json
[
  "tests/test_coff.py:2:1: 'pathlib.Path' imported but unused",
  "tests/test_dynamic_symbolic.py:3:1: 'pathlib.Path' imported but unused",
  "tests/test_local_llm.py:21:1: 'x86decomp.util.load_json' imported but unused",
  "tests/test_mcp.py:4:1: 'json' imported but unused",
  "tests/test_production.py:21:1: 'x86decomp.orchestrator.JobState' imported but unused",
  "tests/test_relink.py:6:1: 'subprocess' imported but unused",
  "tests/assembly/test_annotation_materialize.py:5:1: 'json' imported but unused",
  "tests/assembly/test_annotation_materialize.py:13:1: 'x86decomp.assembly.annotation.render_annotated_assembly' imported but unused",
  "tests/governance/test_core.py:4:1: 'json' imported but unused",
  "tests/governance/test_proof_plugin_worker.py:5:1: 'os' imported but unused",
  "tests/native/test_staging_loop_runtime_windows.py:3:1: 'os' imported but unused",
  "tests/native/test_staging_loop_runtime_windows.py:21:57: local variable 'result' is assigned to but never used",
  "tests/reconstruction/test_provenance_abi_tests.py:9:1: 'x86decomp.governance.proofs.ProofLedger' imported but unused",
  "test-suite/tests/test_cli_and_installation.py:7:1: 'json' imported but unused",
  "test-suite/tests/test_inventory_reports_process.py:13:1: 'x86decomp_testkit.logging_utils.JsonlEventLogger' imported but unused",
  "test-suite/tests/test_inventory_reports_process.py:14:1: 'x86decomp_testkit.models.TestResult as HarnessResult' imported but unused"
]
```

### AUDIT-0711-02: `generate_project_from_target_pack` exposes unused `overwrite_empty` parameter

- Severity: **medium**
- Category: **API contract / dead parameter**
- Why it matters: The function signature advertises behavior that does not exist. The body always rejects a non-empty output project, so callers cannot rely on `overwrite_empty=True` to change behavior. This is dead API surface and a foot-gun.
- How I would modify it: Either remove the parameter and update feature catalogs/tests, or implement it explicitly by allowing only safe replacement of empty/known generated directories with clear data-loss protections.
- Evidence:

```json
[
  {
    "line": 356,
    "path": "src/x86decomp/target_pack.py",
    "text": "overwrite_empty: bool = False,"
  }
]
```

### AUDIT-0711-03: Static dead-code scan still reports unused protocol parameters and the real unused target-pack parameter

- Severity: **low**
- Category: **dead-code cleanup**
- Why it matters: The `__exit__` parameters are protocol-required but should be named with leading underscores to avoid dead-code noise. The `overwrite_empty` report is a real API issue covered separately. Keeping avoidable noise makes future dead-code scans less actionable.
- How I would modify it: Rename intentionally ignored protocol parameters to `_exc_type`, `_exc`, `_traceback`/`_tb`, and fix or remove `overwrite_empty`.
- Evidence:

```json
[
  "src/x86decomp/analysis_db.py:88: unused variable 'exc_type' (100% confidence)",
  "src/x86decomp/analysis_db.py:88: unused variable 'traceback' (100% confidence)",
  "src/x86decomp/mcp.py:146: unused variable 'exc_type' (100% confidence)",
  "src/x86decomp/mcp.py:146: unused variable 'traceback' (100% confidence)",
  "src/x86decomp/orchestrator.py:234: unused variable 'exc_type' (100% confidence)",
  "src/x86decomp/orchestrator.py:234: unused variable 'traceback' (100% confidence)",
  "src/x86decomp/project_state.py:117: unused variable 'exc_type' (100% confidence)",
  "src/x86decomp/project_state.py:117: unused variable 'traceback' (100% confidence)",
  "src/x86decomp/target_pack.py:356: unused variable 'overwrite_empty' (100% confidence)",
  "test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py:466: unused variable 'exc_type' (100% confidence)",
  "test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py:466: unused variable 'tb' (100% confidence)"
]
```

### AUDIT-0711-04: Tests contain skip decorators despite repository rule requiring zero skips in release gates

- Severity: **medium**
- Category: **release-gate policy**
- Why it matters: AGENTS.md says release gates require verifier tests with zero skips. The test tree contains skip decorators for external tool availability. That can be practical locally, but it makes the release-gate contract ambiguous unless these tests are separated from the zero-skip gate or converted into explicit BLOCKED evidence.
- How I would modify it: Move optional external-tool cases into an integration suite that records BLOCKED adapter evidence, or replace skips with deterministic tests of the unavailable-tool error path. Keep the zero-skip release gate limited to tests that must always run.
- Evidence:

```json
[
  {
    "line": 14,
    "path": "tests/test_coff_archive.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang\") is None or shutil.which(\"llvm-ar\") is None, reason=\"LLVM tools unavailable\")"
  },
  {
    "line": 55,
    "path": "tests/test_coff_archive.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang\") is None or shutil.which(\"llvm-ar\") is None, reason=\"LLVM tools unavailable\")"
  },
  {
    "line": 85,
    "path": "tests/test_coff_archive.py",
    "text": "@pytest.mark.skipif("
  },
  {
    "line": 14,
    "path": "tests/test_compiler.py",
    "text": "@unittest.skipUnless(shutil.which(\"gcc\"), \"gcc is unavailable\")"
  },
  {
    "line": 131,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang++\") is None or shutil.which(\"lld-link\") is None, reason=\"LLVM tools unavailable\")"
  },
  {
    "line": 168,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang\") is None, reason=\"clang unavailable\")"
  },
  {
    "line": 192,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"python\") is None, reason=\"python unavailable\")"
  },
  {
    "line": 221,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang\") is None, reason=\"clang unavailable\")"
  },
  {
    "line": 253,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang\") is None or shutil.which(\"clang++\") is None, reason=\"clang unavailable\")"
  },
  {
    "line": 294,
    "path": "tests/test_linker_metadata_corpus.py",
    "text": "@pytest.mark.skipif(shutil.which(\"clang++\") is None or shutil.which(\"lld-link\") is None, reason=\"LLVM tools unavailable\")"
  },
  {
    "line": 21,
    "path": "tests/test_pdb.py",
    "text": "@pytest.mark.skipif("
  },
  {
    "line": 15,
    "path": "tests/test_relink.py",
    "text": "@pytest.mark.skipif(shutil.which(\"lld-link\") is None, reason=\"lld-link unavailable\")"
  }
]
```

### AUDIT-0711-05: Packaged self-tests duplicate repository test bodies instead of using a generated/single-source mechanism

- Severity: **medium**
- Category: **duplication / drift risk**
- Why it matters: The installed test-suite self-tests intentionally package runnable checks, but exact duplicated bodies across two directories create maintenance drift risk. A future fix can update one copy while leaving the installed harness stale.
- How I would modify it: Generate packaged self-tests from repository tests during release, import shared helpers, or add a hash/sync check that fails if mirrored tests diverge unexpectedly.
- Evidence:

```json
[
  [
    {
      "line": 54,
      "name": "test_junit_process_logging_and_reports",
      "normalized_ast_length": 5180,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py"
    },
    {
      "line": 63,
      "name": "test_junit_process_logging_and_reports",
      "normalized_ast_length": 5180,
      "path": "test-suite/tests/test_inventory_reports_process.py"
    }
  ],
  [
    {
      "line": 41,
      "name": "test_lm_studio_http_satisfies_openai_capability_without_product_aliasing",
      "normalized_ast_length": 4294,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py"
    },
    {
      "line": 56,
      "name": "test_lm_studio_http_satisfies_openai_capability_without_product_aliasing",
      "normalized_ast_length": 4294,
      "path": "test-suite/tests/test_adapter_capabilities.py"
    }
  ],
  [
    {
      "line": 32,
      "name": "test_inventory_catalog_and_public_coverage",
      "normalized_ast_length": 3025,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py"
    },
    {
      "line": 38,
      "name": "test_inventory_catalog_and_public_coverage",
      "normalized_ast_length": 3025,
      "path": "test-suite/tests/test_inventory_reports_process.py"
    }
  ],
  [
    {
      "line": 69,
      "name": "test_environment_and_configured_root_detection",
      "normalized_ast_length": 2822,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py"
    },
    {
      "line": 90,
      "name": "test_environment_and_configured_root_detection",
      "normalized_ast_length": 2822,
      "path": "test-suite/tests/test_adapter_detection_resolution.py"
    }
  ],
  [
    {
      "line": 11,
      "name": "test_config_roundtrip_and_relative_resolution",
      "normalized_ast_length": 2778,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_config_models.py"
    },
    {
      "line": 14,
      "name": "test_config_roundtrip_and_relative_resolution",
      "normalized_ast_length": 2778,
      "path": "test-suite/tests/test_config_models.py"
    }
  ],
  [
    {
      "line": 103,
      "name": "test_recursive_inventory_includes_capability_packages_and_nested_schemas",
      "normalized_ast_length": 2725,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py"
    },
    {
      "line": 118,
      "name": "test_recursive_inventory_includes_capability_packages_and_nested_schemas",
      "normalized_ast_length": 2725,
      "path": "test-suite/tests/test_inventory_reports_process.py"
    }
  ],
  [
    {
      "line": 14,
      "name": "test_safe_zip_and_tar_extraction",
      "normalized_ast_length": 2711,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_archive_security.py"
    },
    {
      "line": 17,
      "name": "test_safe_zip_and_tar_extraction",
      "normalized_ast_length": 2711,
      "path": "test-suite/tests/test_archive_security.py"
    }
  ],
  [
    {
      "line": 84,
      "name": "test_suite_schemas_and_catalog_are_valid",
      "normalized_ast_length": 2647,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py"
    },
    {
      "line": 96,
      "name": "test_suite_schemas_and_catalog_are_valid",
      "normalized_ast_length": 2647,
      "path": "test-suite/tests/test_inventory_reports_process.py"
    }
  ],
  [
    {
      "line": 34,
      "name": "test_rejects_traversal_and_links",
      "normalized_ast_length": 2420,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_archive_security.py"
    },
    {
      "line": 40,
      "name": "test_rejects_traversal_and_links",
      "normalized_ast_length": 2420,
      "path": "test-suite/tests/test_archive_security.py"
    }
  ],
  [
    {
      "line": 87,
      "name": "test_path_detection_preserves_symlink_argv0",
      "normalized_ast_length": 2390,
      "path": "test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py"
    },
    {
      "line": 111,
      "name": "test_path_detection_preserves_symlink_argv0",
      "normalized_ast_length": 2390,
      "path": "test-suite/tests/test_adapter_detection_resolution.py"
    }
  ]
]
```

### AUDIT-0711-06: Root CLI help and command catalog are slow because the parser eagerly constructs the full command surface

- Severity: **medium**
- Category: **CLI performance / command architecture**
- Why it matters: A basic help command should be near-instant. The current CLI imports all subsystems and registers all canonical command parents before parsing, making help/catalog commands pay full startup cost.
- How I would modify it: Lazily import command implementations inside dispatch branches, cache canonical route computation, and split top-level parser construction from canonical leaf parser generation so `--help` and `commands` avoid building every leaf parser.
- Evidence:

```json
{
  "parser_build_seconds": 6.252,
  "x86decomp --help seconds": 8.81,
  "x86decomp commands seconds": 9.33
}
```

### AUDIT-0711-07: Many docstrings remain mechanically generic rather than behavior-specific

- Severity: **low**
- Category: **documentation quality**
- Why it matters: Coverage is complete, but phrases such as “current toolkit workflow” and “internal toolkit callers” do not explain arguments, behavior, return values, or side effects. They satisfy presence checks while providing weak maintainer value.
- How I would modify it: Replace generic generated docstrings with behavior-specific documentation for public functions/classes first, then internal helpers. Add a style gate for known weak phrases.
- Evidence:

```json
{
  "count": 1039,
  "examples": [
    {
      "docstring": "Support environment processing for internal toolkit callers.",
      "kind": "function",
      "line": 22,
      "name": "_environment",
      "path": "scripts/run-pytest-partitions.py"
    },
    {
      "docstring": "Support collect processing for internal toolkit callers.",
      "kind": "function",
      "line": 33,
      "name": "_collect",
      "path": "scripts/run-pytest-partitions.py"
    },
    {
      "docstring": "Support partitions processing for internal toolkit callers.",
      "kind": "function",
      "line": 53,
      "name": "_partitions",
      "path": "scripts/run-pytest-partitions.py"
    },
    {
      "docstring": "Support junit counts processing for internal toolkit callers.",
      "kind": "function",
      "line": 67,
      "name": "_junit_counts",
      "path": "scripts/run-pytest-partitions.py"
    },
    {
      "docstring": "Run run for the current toolkit workflow.",
      "kind": "function",
      "line": 77,
      "name": "run",
      "path": "scripts/run-pytest-partitions.py"
    },
    {
      "docstring": "Support is ignored processing for internal toolkit callers.",
      "kind": "function",
      "line": 32,
      "name": "_is_ignored",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Support digest processing for internal toolkit callers.",
      "kind": "function",
      "line": 49,
      "name": "_digest",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Execute the manifest text operation for the current toolkit workflow.",
      "kind": "function",
      "line": 58,
      "name": "manifest_text",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Write manifest for the current toolkit workflow.",
      "kind": "function",
      "line": 67,
      "name": "write_manifest",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Support read manifest processing for internal toolkit callers.",
      "kind": "function",
      "line": 75,
      "name": "_read_manifest",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Verify manifest for the current toolkit workflow.",
      "kind": "function",
      "line": 91,
      "name": "verify_manifest",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Generate all for the current toolkit workflow.",
      "kind": "function",
      "line": 115,
      "name": "generate_all",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Verify all for the current toolkit workflow.",
      "kind": "function",
      "line": 129,
      "name": "verify_all",
      "path": "scripts/source_hashes.py"
    },
    {
      "docstring": "Write write for the current toolkit workflow.",
      "kind": "function",
      "line": 22,
      "name": "write",
      "path": "scripts/sync-release-contracts.py"
    },
    {
      "docstring": "Execute the root commands operation for the current toolkit workflow.",
      "kind": "function",
      "line": 27,
      "name": "root_commands",
      "path": "scripts/sync-release-contracts.py"
    },
    {
      "docstring": "Execute the module area operation for the current toolkit workflow.",
      "kind": "function",
      "line": 34,
      "name": "module_area",
      "path": "scripts/sync-release-contracts.py"
    },
    {
      "docstring": "Load load for the current toolkit workflow.",
      "kind": "function",
      "line": 16,
      "name": "load",
      "path": "scripts/validate-contracts.py"
    },
    {
      "docstring": "Validate schema files for the current toolkit workflow.",
      "kind": "function",
      "line": 21,
      "name": "validate_schema_files",
      "path": "scripts/validate-contracts.py"
    },
    {
      "docstring": "Validate examples for the current toolkit workflow.",
      "kind": "function",
      "line": 27,
      "name": "validate_examples",
      "path": "scripts/validate-contracts.py"
    },
    {
      "docstring": "Validate skill frontmatter for the current toolkit workflow.",
      "kind": "function",
      "line": 83,
      "name": "validate_skill_frontmatter",
      "path": "scripts/validate-contracts.py"
    },
    {
      "docstring": "Validate current release shape for the current toolkit workflow.",
      "kind": "function",
      "line": 120,
      "name": "validate_current_release_shape",
      "path": "scripts/validate-contracts.py"
    },
    {
      "docstring": "Provide the current runtime implementation for the `x86decomp.assembly.annotation` module.",
      "kind": "module",
      "line": 1,
      "name": "<module>",
      "path": "src/x86decomp/assembly/annotation.py"
    },
    {
      "docstring": "Validate symbol for the current toolkit workflow.",
      "kind": "function",
      "line": 15,
      "name": "validate_symbol",
      "path": "src/x86decomp/assembly/annotation.py"
    },
    {
      "docstring": "Parse byte directives for the current toolkit workflow.",
      "kind": "function",
      "line": 40,
      "name": "parse_byte_directives",
      "path": "src/x86decomp/assembly/annotation.py"
    },
    {
      "docstring": "Support chunk comments processing for internal toolkit callers.",
      "kind": "function",
      "line": 63,
      "name": "_chunk_comments",
      "path": "src/x86decomp/assembly/annotation.py"
    }
  ]
}
```

### AUDIT-0711-08: Assembly and native CLI schema tests duplicate leaf-command traversal helpers

- Severity: **low**
- Category: **test duplication**
- Why it matters: This is small but real duplication. If CLI parser traversal behavior changes, duplicated helpers can drift and make schema coverage inconsistent.
- How I would modify it: Move `_leaf_commands`/`walk` helper logic into a shared test helper module used by both assembly and native CLI schema tests.
- Evidence:

```json
[
  [
    {
      "line": 29,
      "name": "_leaf_commands",
      "normalized_ast_length": 1801,
      "path": "tests/assembly/test_pipeline_cli_schemas.py"
    },
    {
      "line": 14,
      "name": "_leaf_commands",
      "normalized_ast_length": 1801,
      "path": "tests/native/test_cli_schemas.py"
    }
  ],
  [
    {
      "line": 32,
      "name": "walk",
      "normalized_ast_length": 1375,
      "path": "tests/assembly/test_pipeline_cli_schemas.py"
    },
    {
      "line": 17,
      "name": "walk",
      "normalized_ast_length": 1375,
      "path": "tests/native/test_cli_schemas.py"
    }
  ]
]
```

### AUDIT-0711-09: No completed monolithic pytest run was produced during this audit

- Severity: **informational**
- Category: **verification limitation**
- Why it matters: This is not itself a code defect, but it limits the strength of audit evidence. The report must not claim all-at-once pytest success.
- How I would modify it: Keep deterministic segmented partitions, record each partition, and only restore the monolithic claim after CI proves that the full run completes within a declared timeout.
- Evidence:

```json
"The sandboxed audit did not complete a full all-at-once pytest run. The release history already avoids claiming monolithic pytest success and relies on segmented/file-level evidence."
```

## Checks that passed / non-issues

- **All ZIP files read and hashed**: 455/455 files
- **Python AST parse**: 213 files, 0 errors
- **Python compileall**: 0
- **Production pyflakes**: 0
- **Contract/schema validation with dev dependencies**: 0
- **Source hash manifests**: 0
- **JSON/TOML/YAML/Java parse**: {"java": {"count": 3, "errors": []}, "json": {"count": 124, "errors": []}, "toml": {"count": 2, "errors": []}, "yaml": {"count": 1, "errors": []}}
- **Command dispatch coverage**: {"canonical_groups": 59, "canonical_roots": 60, "canonical_routes": 239, "exact_handlers": 106, "noncanonical_missing_dispatch": [], "noncanonical_roots": 106, "parser_build_seconds": 6.252, "root_commands": 166, "startswith_handlers": ["db-", "work-", "mcp-", "pipeline-"]}
- **Known previous runtime paths**: {"llm_prompt_help": {"elapsed_seconds": 8.59, "returncode": 0, "stdout_head": "usage: x86decomp llm prompt [-h] job output\n\nmaterialize the deterministic prompt without contacting a model\n\npositional arguments:\n  job\n  output\n\noptions:\n  -h, --help  show this help message and exit\n"}, "plugin_validate_help": {"elapsed_seconds": 8.98, "returncode": 0, "stdout_head": "usage: x86decomp plugin validate [-h] manifest\n\npositional arguments:\n  manifest\n\noptions:\n  -h, --help  show this help message and exit\n"}}

## Explicit limitations

- This audit does **not** claim a completed monolithic `pytest tests` run.
- Static dead-code results involving protocol-required `__exit__` parameters are cleanup/noise findings, not behavioral failures.
- Dynamic behavior requiring unavailable external tools was not executed unless represented by deterministic local checks.

## Artifact hashes
```text
94dcb42ccf07a19d09ccce09bdba2d7fc2ff004a58f2e9897ba75a70fe5e467c  x86decomp-toolkit-0.7.11-third-full-code-audit-report.md
4c4f9a814ea4a17d5342cebc190d5594aeb9c2c9e16a2feb00b773bdf43eb4c2  x86decomp-toolkit-0.7.11-third-code-audit-evidence.json
f30a7c0f77d31f88f1cf82941907ee4d5495f01b989ebcaec4786a32d2828666  x86decomp-toolkit-0.7.11-third-all-file-manifest.json
f736a270969b2696dc353638a6b28669a5bc0fc3237fbccd784127426a11bea3  x86decomp-toolkit-0.7.11-third-code-audit-report-and-evidence.zip
```
