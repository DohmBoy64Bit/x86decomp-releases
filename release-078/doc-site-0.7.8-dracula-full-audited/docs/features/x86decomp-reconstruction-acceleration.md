---
title: x86decomp.reconstruction.acceleration
description: Source module reference for x86decomp.reconstruction.acceleration.
---

# `x86decomp.reconstruction.acceleration`

**Source path:** `src/x86decomp/reconstruction/acceleration.py`  
**SHA-256:** `acada93918527df17da324b8697e7e5f6f6259238790526d8b6daecaa26ae396`  
**Documented symbols:** 70

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `_safe_rel` | function | 32 | 39 | no docstring declared |
| `_read_text_if_exists` | function | 42 | 43 | no docstring declared |
| `_body_ranges` | function | 46 | 57 | no docstring declared |
| `_contiguous_single_range` | function | 60 | 67 | no docstring declared |
| `_read_range_bytes` | function | 70 | 85 | no docstring declared |
| `_read_mnemonics` | function | 88 | 116 | no docstring declared |
| `_function_name` | function | 119 | 124 | no docstring declared |
| `llm_job_from_function_packet` | function | 127 | 210 | Create one local-LLM job from a verified function artifact directory. |
| `llm_job_from_range` | function | 213 | 284 | Create one local-LLM job from an explicitly supplied file offset/RVA range. |
| `llm_batch_create` | function | 287 | 312 | no docstring declared |
| `llm_batch_match` | function | 315 | 338 | no docstring declared |
| `candidate_promote` | function | 341 | 367 | no docstring declared |
| `source_map_annotate` | function | 370 | 385 | no docstring declared |
| `source_map_verify` | function | 388 | 402 | no docstring declared |
| `module_assign` | function | 405 | 413 | no docstring declared |
| `module_suggest` | function | 416 | 431 | no docstring declared |
| `type_propagate` | function | 434 | 443 | no docstring declared |
| `header_synthesize_project` | function | 446 | 462 | no docstring declared |
| `vtable_recover` | function | 465 | 467 | no docstring declared |
| `class_scaffold` | function | 470 | 484 | no docstring declared |
| `diff_explain` | function | 487 | 498 | no docstring declared |
| `triage_next` | function | 501 | 509 | no docstring declared |
| `playability_smoke_plan` | function | 512 | 517 | no docstring declared |
| `asset_inventory` | function | 520 | 528 | no docstring declared |
| `mod_branch_init` | function | 531 | 534 | no docstring declared |
| `regression_compare` | function | 537 | 541 | no docstring declared |
| `_json_out` | function | 570 | 573 | no docstring declared |
| `_read_any_text` | function | 576 | 580 | no docstring declared |
| `_file_report` | function | 583 | 585 | no docstring declared |
| `function_discover` | function | 588 | 628 | Discover candidate function entry offsets using architecture profiles. |
| `function_boundary_reconcile` | function | 631 | 650 | no docstring declared |
| `function_list_sort` | function | 653 | 669 | no docstring declared |
| `sort_key` | function | 660 | 666 | no docstring declared |
| `function_list_classify` | function | 672 | 692 | no docstring declared |
| `pattern_catalog` | function | 695 | 697 | no docstring declared |
| `pattern_scan` | function | 700 | 722 | no docstring declared |
| `pattern_generate` | function | 725 | 741 | no docstring declared |
| `pattern_match` | function | 744 | 751 | no docstring declared |
| `pattern_promote` | function | 754 | 758 | no docstring declared |
| `image_text_compose` | function | 761 | 805 | no docstring declared |
| `_pe_section` | function | 808 | 826 | no docstring declared |
| `text_swap_plan` | function | 829 | 837 | no docstring declared |
| `text_swap_inject` | function | 840 | 860 | no docstring declared |
| `text_swap_verify` | function | 863 | 871 | no docstring declared |
| `text_swap_build` | function | 874 | 879 | no docstring declared |
| `progress_reconcile` | function | 882 | 898 | no docstring declared |
| `project_health` | function | 901 | 910 | no docstring declared |
| `source_stage_classify` | function | 913 | 937 | no docstring declared |
| `ghidra_mcp_probe` | function | 940 | 949 | no docstring declared |
| `_json_rpc` | function | 952 | 956 | no docstring declared |
| `ghidra_mcp_functions` | function | 959 | 962 | no docstring declared |
| `ghidra_mcp_decompile` | function | 965 | 968 | no docstring declared |
| `ghidra_mcp_batch_decompile` | function | 971 | 982 | no docstring declared |
| `ghidra_mcp_sync_names` | function | 985 | 993 | no docstring declared |
| `compiler_rule_learn` | function | 996 | 1002 | no docstring declared |
| `compiler_rule_report` | function | 1005 | 1008 | no docstring declared |
| `compiler_compare_flags` | function | 1011 | 1017 | no docstring declared |
| `runtime_identify` | function | 1020 | 1030 | no docstring declared |
| `runtime_quarantine` | function | 1033 | 1040 | no docstring declared |
| `runtime_match_library` | function | 1043 | 1046 | no docstring declared |
| `subsystem_detect` | function | 1049 | 1060 | no docstring declared |
| `state_machine_detect` | function | 1063 | 1073 | no docstring declared |
| `project_doctor_paths` | function | 1076 | 1087 | no docstring declared |
| `script_port_audit` | function | 1090 | 1102 | no docstring declared |
| `toolchain_hash_tree` | function | 1105 | 1109 | no docstring declared |
| `toolchain_verify_local` | function | 1112 | 1121 | no docstring declared |
| `toolchain_redact_package` | function | 1124 | 1135 | no docstring declared |
| `decompiler_cleanup` | function | 1138 | 1156 | no docstring declared |
| `candidate_search` | function | 1159 | 1167 | no docstring declared |
| `release_goal_moddable_source` | function | 1170 | 1174 | no docstring declared |
