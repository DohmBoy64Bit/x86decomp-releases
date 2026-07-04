---
title: Test Source Reference
description: Source-derived test file and test-node coverage for x86decomp 0.7.8.
---

# Test Source Reference

This index covers **59** test source files. It documents collected test definitions but does not claim every optional external adapter was available during the release environment.

| Test source | Test functions/classes |
| --- | ---: |
| [`test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py`](test-suite-src-x86decomp_testkit-self_tests-test_adapter_capabilities.md) | 4 |
| [`test-suite/src/x86decomp_testkit/self_tests/test_adapter_detection_resolution.py`](test-suite-src-x86decomp_testkit-self_tests-test_adapter_detection_resolution.md) | 6 |
| [`test-suite/src/x86decomp_testkit/self_tests/test_archive_security.py`](test-suite-src-x86decomp_testkit-self_tests-test_archive_security.md) | 4 |
| [`test-suite/src/x86decomp_testkit/self_tests/test_cli_and_installation.py`](test-suite-src-x86decomp_testkit-self_tests-test_cli_and_installation.md) | 2 |
| [`test-suite/src/x86decomp_testkit/self_tests/test_config_models.py`](test-suite-src-x86decomp_testkit-self_tests-test_config_models.md) | 2 |
| [`test-suite/src/x86decomp_testkit/self_tests/test_inventory_reports_process.py`](test-suite-src-x86decomp_testkit-self_tests-test_inventory_reports_process.md) | 4 |
| [`test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`](test-suite-src-x86decomp_testkit-toolkit_tests-test_public_api_contract.md) | 23 |
| [`test-suite/tests/test_adapter_capabilities.py`](test-suite-tests-test_adapter_capabilities.md) | 4 |
| [`test-suite/tests/test_adapter_detection_resolution.py`](test-suite-tests-test_adapter_detection_resolution.md) | 6 |
| [`test-suite/tests/test_architecture_maps.py`](test-suite-tests-test_architecture_maps.md) | 4 |
| [`test-suite/tests/test_archive_security.py`](test-suite-tests-test_archive_security.md) | 4 |
| [`test-suite/tests/test_cli_and_installation.py`](test-suite-tests-test_cli_and_installation.md) | 2 |
| [`test-suite/tests/test_config_models.py`](test-suite-tests-test_config_models.md) | 2 |
| [`test-suite/tests/test_inventory_reports_process.py`](test-suite-tests-test_inventory_reports_process.md) | 4 |
| [`tests/assembly/test_annotation_materialize.py`](tests-assembly-test_annotation_materialize.md) | 8 |
| [`tests/assembly/test_helpers_and_relocations.py`](tests-assembly-test_helpers_and_relocations.md) | 3 |
| [`tests/assembly/test_pipeline_cli_schemas.py`](tests-assembly-test_pipeline_cli_schemas.md) | 8 |
| [`tests/governance/test_core.py`](tests-governance-test_core.md) | 17 |
| [`tests/governance/test_governance_cli_schemas.py`](tests-governance-test_governance_cli_schemas.md) | 5 |
| [`tests/governance/test_proof_plugin_worker.py`](tests-governance-test_proof_plugin_worker.md) | 8 |
| [`tests/governance/test_worker_thread_safety.py`](tests-governance-test_worker_thread_safety.md) | 2 |
| [`tests/native/test_cli_schemas.py`](tests-native-test_cli_schemas.md) | 4 |
| [`tests/native/test_inventory_and_loops.py`](tests-native-test_inventory_and_loops.md) | 3 |
| [`tests/native/test_pe_hybrid.py`](tests-native-test_pe_hybrid.md) | 4 |
| [`tests/native/test_slots_matching.py`](tests-native-test_slots_matching.md) | 4 |
| [`tests/native/test_staging_loop_runtime_windows.py`](tests-native-test_staging_loop_runtime_windows.md) | 4 |
| [`tests/reconstruction/test_capsules_security_changesets.py`](tests-reconstruction-test_capsules_security_changesets.md) | 4 |
| [`tests/reconstruction/test_cli_schemas_retention.py`](tests-reconstruction-test_cli_schemas_retention.md) | 6 |
| [`tests/reconstruction/test_decomp_acceleration.py`](tests-reconstruction-test_decomp_acceleration.md) | 3 |
| [`tests/reconstruction/test_project_headers_builds.py`](tests-reconstruction-test_project_headers_builds.md) | 3 |
| [`tests/reconstruction/test_provenance_abi_tests.py`](tests-reconstruction-test_provenance_abi_tests.md) | 3 |
| [`tests/reconstruction/test_real_project_acceleration.py`](tests-reconstruction-test_real_project_acceleration.md) | 3 |
| [`tests/test_abi_disassembly.py`](tests-test_abi_disassembly.md) | 1 |
| [`tests/test_artifacts.py`](tests-test_artifacts.md) | 3 |
| [`tests/test_coff.py`](tests-test_coff.md) | 2 |
| [`tests/test_coff_archive.py`](tests-test_coff_archive.md) | 3 |
| [`tests/test_compiler.py`](tests-test_compiler.md) | 2 |
| [`tests/test_decompme_objdiff.py`](tests-test_decompme_objdiff.md) | 2 |
| [`tests/test_diffing.py`](tests-test_diffing.md) | 3 |
| [`tests/test_documentation.py`](tests-test_documentation.md) | 3 |
| [`tests/test_dynamic_symbolic.py`](tests-test_dynamic_symbolic.md) | 2 |
| [`tests/test_dynamorio.py`](tests-test_dynamorio.md) | 2 |
| [`tests/test_evidence.py`](tests-test_evidence.md) | 3 |
| [`tests/test_ghidra.py`](tests-test_ghidra.md) | 2 |
| [`tests/test_integration.py`](tests-test_integration.md) | 2 |
| [`tests/test_linker_metadata_corpus.py`](tests-test_linker_metadata_corpus.md) | 10 |
| [`tests/test_local_llm.py`](tests-test_local_llm.md) | 9 |
| [`tests/test_mcp.py`](tests-test_mcp.md) | 1 |
| [`tests/test_memory.py`](tests-test_memory.md) | 3 |
| [`tests/test_modes_and_db.py`](tests-test_modes_and_db.md) | 2 |
| [`tests/test_pdb.py`](tests-test_pdb.md) | 2 |
| [`tests/test_pe32.py`](tests-test_pe32.md) | 3 |
| [`tests/test_pe64_patch_hybrid.py`](tests-test_pe64_patch_hybrid.md) | 3 |
| [`tests/test_production.py`](tests-test_production.md) | 22 |
| [`tests/test_project.py`](tests-test_project.md) | 3 |
| [`tests/test_release_contract.py`](tests-test_release_contract.md) | 8 |
| [`tests/test_relink.py`](tests-test_relink.md) | 1 |
| [`tests/test_test_bundle.py`](tests-test_test_bundle.md) | 5 |
| [`tests/test_workqueue.py`](tests-test_workqueue.md) | 1 |
