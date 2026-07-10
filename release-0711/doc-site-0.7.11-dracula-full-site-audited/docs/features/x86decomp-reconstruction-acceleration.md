---
title: x86decomp.reconstruction.acceleration
description: Module reference for x86decomp.reconstruction.acceleration.
---

# `x86decomp.reconstruction.acceleration`

- Area: `toolkit`
- Source path: `src/x86decomp/reconstruction/acceleration.py`
- SHA-256: `70942db2fd66b84d8c33439d7bf5b9cd50be38d28a8f068ea284036c95ce78e3`
- Size: `72229` bytes
- Lines: `1247`

## Module docstring

Human-readable decompilation acceleration helpers.

These helpers deliberately create reviewable manifests, source annotations, and
triage reports.  They do not claim original source recovery or validator success;
state-changing commands require concrete input reports and emit auditable JSON.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_safe_rel` | 31 | Support safe rel processing for internal toolkit callers. |
| function | `_read_text_if_exists` | 42 | Support read text if exists processing for internal toolkit callers. |
| function | `_body_ranges` | 47 | Support body ranges processing for internal toolkit callers. |
| function | `_contiguous_single_range` | 62 | Support contiguous single range processing for internal toolkit callers. |
| function | `_read_range_bytes` | 73 | Support read range bytes processing for internal toolkit callers. |
| function | `_read_mnemonics` | 92 | Support read mnemonics processing for internal toolkit callers. |
| function | `_function_name` | 124 | Support function name processing for internal toolkit callers. |
| function | `llm_job_from_function_packet` | 133 | Create one local-LLM job from a verified function artifact directory. |
| function | `llm_job_from_range` | 219 | Create one local-LLM job from an explicitly supplied file offset/RVA range. |
| function | `llm_batch_create` | 293 | Execute the llm batch create operation for the current toolkit workflow. |
| function | `llm_batch_match` | 329 | Execute the llm batch match operation for the current toolkit workflow. |
| function | `candidate_promote` | 356 | Execute the candidate promote operation for the current toolkit workflow. |
| function | `source_map_annotate` | 386 | Execute the source map annotate operation for the current toolkit workflow. |
| function | `source_map_verify` | 405 | Execute the source map verify operation for the current toolkit workflow. |
| function | `module_assign` | 423 | Execute the module assign operation for the current toolkit workflow. |
| function | `module_suggest` | 435 | Execute the module suggest operation for the current toolkit workflow. |
| function | `type_propagate` | 454 | Emit a type-propagation plan without silently editing source files. |
| function | `header_synthesize_project` | 466 | Execute the header synthesize project operation for the current toolkit workflow. |
| function | `vtable_recover` | 486 | Execute the vtable recover operation for the current toolkit workflow. |
| function | `class_scaffold` | 492 | Execute the class scaffold operation for the current toolkit workflow. |
| function | `diff_explain` | 510 | Execute the diff explain operation for the current toolkit workflow. |
| function | `triage_next` | 525 | Execute the triage next operation for the current toolkit workflow. |
| function | `playability_smoke_plan` | 537 | Execute the playability smoke plan operation for the current toolkit workflow. |
| function | `asset_inventory` | 546 | Execute the asset inventory operation for the current toolkit workflow. |
| function | `mod_branch_init` | 558 | Execute the mod branch init operation for the current toolkit workflow. |
| function | `regression_compare` | 565 | Execute the regression compare operation for the current toolkit workflow. |
| function | `_json_out` | 599 | Support json out processing for internal toolkit callers. |
| function | `_read_any_text` | 606 | Support read any text processing for internal toolkit callers. |
| function | `_file_report` | 614 | Support file report processing for internal toolkit callers. |
| function | `function_discover` | 620 | Discover candidate function entry offsets using architecture profiles. |
| function | `function_boundary_reconcile` | 663 | Execute the function boundary reconcile operation for the current toolkit workflow. |
| function | `function_list_sort` | 686 | Execute the function list sort operation for the current toolkit workflow. |
| function | `sort_key` | 694 | Execute the sort key operation for the current toolkit workflow. |
| function | `function_list_classify` | 707 | Execute the function list classify operation for the current toolkit workflow. |
| function | `pattern_catalog` | 731 | Execute the pattern catalog operation for the current toolkit workflow. |
| function | `pattern_scan` | 737 | Execute the pattern scan operation for the current toolkit workflow. |
| function | `pattern_generate` | 763 | Execute the pattern generate operation for the current toolkit workflow. |
| function | `pattern_match` | 783 | Execute the pattern match operation for the current toolkit workflow. |
| function | `pattern_promote` | 794 | Execute the pattern promote operation for the current toolkit workflow. |
| function | `image_text_compose` | 802 | Execute the image text compose operation for the current toolkit workflow. |
| function | `_pe_section` | 850 | Support pe section processing for internal toolkit callers. |
| function | `text_swap_plan` | 872 | Execute the text swap plan operation for the current toolkit workflow. |
| function | `text_swap_inject` | 884 | Execute the text swap inject operation for the current toolkit workflow. |
| function | `text_swap_verify` | 908 | Execute the text swap verify operation for the current toolkit workflow. |
| function | `text_swap_build` | 920 | Execute the text swap build operation for the current toolkit workflow. |
| function | `progress_reconcile` | 929 | Execute the progress reconcile operation for the current toolkit workflow. |
| function | `project_health` | 949 | Execute the project health operation for the current toolkit workflow. |
| function | `source_stage_classify` | 962 | Execute the source stage classify operation for the current toolkit workflow. |
| function | `ghidra_mcp_probe` | 990 | Execute the ghidra mcp probe operation for the current toolkit workflow. |
| function | `_json_rpc` | 1003 | Support json rpc processing for internal toolkit callers. |
| function | `ghidra_mcp_functions` | 1011 | Execute the ghidra mcp functions operation for the current toolkit workflow. |
| function | `ghidra_mcp_decompile` | 1018 | Execute the ghidra mcp decompile operation for the current toolkit workflow. |
| function | `ghidra_mcp_batch_decompile` | 1025 | Execute the ghidra mcp batch decompile operation for the current toolkit workflow. |
| function | `ghidra_mcp_sync_names` | 1040 | Execute the ghidra mcp sync names operation for the current toolkit workflow. |
| function | `compiler_rule_learn` | 1052 | Execute the compiler rule learn operation for the current toolkit workflow. |
| function | `compiler_rule_report` | 1062 | Execute the compiler rule report operation for the current toolkit workflow. |
| function | `compiler_compare_flags` | 1069 | Execute the compiler compare flags operation for the current toolkit workflow. |
| function | `runtime_identify` | 1079 | Run time identify for the current toolkit workflow. |
| function | `runtime_quarantine` | 1093 | Run time quarantine for the current toolkit workflow. |
| function | `runtime_match_library` | 1104 | Run time match library for the current toolkit workflow. |
| function | `subsystem_detect` | 1111 | Execute the subsystem detect operation for the current toolkit workflow. |
| function | `state_machine_detect` | 1126 | Execute the state machine detect operation for the current toolkit workflow. |
| function | `project_doctor_paths` | 1140 | Execute the project doctor paths operation for the current toolkit workflow. |
| function | `script_port_audit` | 1155 | Execute the script port audit operation for the current toolkit workflow. |
| function | `toolchain_hash_tree` | 1171 | Execute the toolchain hash tree operation for the current toolkit workflow. |
| function | `toolchain_verify_local` | 1179 | Execute the toolchain verify local operation for the current toolkit workflow. |
| function | `toolchain_redact_package` | 1192 | Execute the toolchain redact package operation for the current toolkit workflow. |
| function | `decompiler_cleanup` | 1207 | Execute the decompiler cleanup operation for the current toolkit workflow. |
| function | `candidate_search` | 1229 | Execute the candidate search operation for the current toolkit workflow. |
| function | `release_goal_moddable_source` | 1241 | Execute the release goal moddable source operation for the current toolkit workflow. |
