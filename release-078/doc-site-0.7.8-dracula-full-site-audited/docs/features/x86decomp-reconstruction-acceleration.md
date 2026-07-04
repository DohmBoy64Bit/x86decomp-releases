---
title: x86decomp.reconstruction.acceleration
description: Source module reference for x86decomp.reconstruction.acceleration.
---

# `x86decomp.reconstruction.acceleration`

**Source path:** `src/x86decomp/reconstruction/acceleration.py`  
**Documented symbols:** 70

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `_safe_rel` | function | 32 | 39 | — |
| `_read_text_if_exists` | function | 42 | 43 | — |
| `_body_ranges` | function | 46 | 57 | — |
| `_contiguous_single_range` | function | 60 | 67 | — |
| `_read_range_bytes` | function | 70 | 85 | — |
| `_read_mnemonics` | function | 88 | 116 | — |
| `_function_name` | function | 119 | 124 | — |
| `llm_job_from_function_packet` | function | 127 | 210 | Create one local-LLM job from a verified function artifact directory. |
| `llm_job_from_range` | function | 213 | 284 | Create one local-LLM job from an explicitly supplied file offset/RVA range. |
| `llm_batch_create` | function | 287 | 312 | — |
| `llm_batch_match` | function | 315 | 338 | — |
| `candidate_promote` | function | 341 | 367 | — |
| `source_map_annotate` | function | 370 | 385 | — |
| `source_map_verify` | function | 388 | 402 | — |
| `module_assign` | function | 405 | 413 | — |
| `module_suggest` | function | 416 | 431 | — |
| `type_propagate` | function | 434 | 443 | — |
| `header_synthesize_project` | function | 446 | 462 | — |
| `vtable_recover` | function | 465 | 467 | — |
| `class_scaffold` | function | 470 | 484 | — |
| `diff_explain` | function | 487 | 498 | — |
| `triage_next` | function | 501 | 509 | — |
| `playability_smoke_plan` | function | 512 | 517 | — |
| `asset_inventory` | function | 520 | 528 | — |
| `mod_branch_init` | function | 531 | 534 | — |
| `regression_compare` | function | 537 | 541 | — |
| `_json_out` | function | 570 | 573 | — |
| `_read_any_text` | function | 576 | 580 | — |
| `_file_report` | function | 583 | 585 | — |
| `function_discover` | function | 588 | 628 | Discover candidate function entry offsets using architecture profiles. |
| `function_boundary_reconcile` | function | 631 | 650 | — |
| `function_list_sort` | function | 653 | 669 | — |
| `sort_key` | function | 660 | 666 | — |
| `function_list_classify` | function | 672 | 692 | — |
| `pattern_catalog` | function | 695 | 697 | — |
| `pattern_scan` | function | 700 | 722 | — |
| `pattern_generate` | function | 725 | 741 | — |
| `pattern_match` | function | 744 | 751 | — |
| `pattern_promote` | function | 754 | 758 | — |
| `image_text_compose` | function | 761 | 805 | — |
| `_pe_section` | function | 808 | 826 | — |
| `text_swap_plan` | function | 829 | 837 | — |
| `text_swap_inject` | function | 840 | 860 | — |
| `text_swap_verify` | function | 863 | 871 | — |
| `text_swap_build` | function | 874 | 879 | — |
| `progress_reconcile` | function | 882 | 898 | — |
| `project_health` | function | 901 | 910 | — |
| `source_stage_classify` | function | 913 | 937 | — |
| `ghidra_mcp_probe` | function | 940 | 949 | — |
| `_json_rpc` | function | 952 | 956 | — |
| `ghidra_mcp_functions` | function | 959 | 962 | — |
| `ghidra_mcp_decompile` | function | 965 | 968 | — |
| `ghidra_mcp_batch_decompile` | function | 971 | 982 | — |
| `ghidra_mcp_sync_names` | function | 985 | 993 | — |
| `compiler_rule_learn` | function | 996 | 1002 | — |
| `compiler_rule_report` | function | 1005 | 1008 | — |
| `compiler_compare_flags` | function | 1011 | 1017 | — |
| `runtime_identify` | function | 1020 | 1030 | — |
| `runtime_quarantine` | function | 1033 | 1040 | — |
| `runtime_match_library` | function | 1043 | 1046 | — |
| `subsystem_detect` | function | 1049 | 1060 | — |
| `state_machine_detect` | function | 1063 | 1073 | — |
| `project_doctor_paths` | function | 1076 | 1087 | — |
| `script_port_audit` | function | 1090 | 1102 | — |
| `toolchain_hash_tree` | function | 1105 | 1109 | — |
| `toolchain_verify_local` | function | 1112 | 1121 | — |
| `toolchain_redact_package` | function | 1124 | 1135 | — |
| `decompiler_cleanup` | function | 1138 | 1156 | — |
| `candidate_search` | function | 1159 | 1167 | — |
| `release_goal_moddable_source` | function | 1170 | 1174 | — |
