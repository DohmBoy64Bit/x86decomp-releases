---
title: Function Index
description: AST symbol index for x86decomp 0.7.11.
---

# Function Index

This page indexes classes, functions, and methods discovered by AST parsing source and test-suite modules.

Symbol count: **1290**

| Kind | Name | Module | Line | Docstring summary |
| --- | --- | --- | --- | --- |
| class | `CallingConvention` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 15 | Coordinate calling convention behavior for the current toolkit workflow. |
| class | `FloatMode` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 25 | Coordinate float mode behavior for the current toolkit workflow. |
| class | `ABIContract` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 35 | Store validated a b i contract fields used by toolkit reports and adapters. |
| function | `from_dict` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 49 | Execute the from dict operation for the current toolkit workflow. |
| function | `optional_nonnegative` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 61 | Execute the optional nonnegative operation for the current toolkit workflow. |
| function | `load_abi_contract` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 92 | Load abi contract for the current toolkit workflow. |
| function | `analyze_abi` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 97 | Execute the analyze abi operation for the current toolkit workflow. |
| function | `validate_abi` | [`x86decomp.abi`](../features/x86decomp-abi.md) | 160 | Validate abi for the current toolkit workflow. |
| class | `AnalysisDatabase` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 70 | Coordinate analysis database behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 72 | Initialize the instance with validated constructor state. |
| function | `close` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 80 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 84 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 88 | Exit the managed runtime context and release owned resources. |
| function | `upsert_entity` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 96 | Execute the upsert entity operation for the current toolkit workflow. |
| function | `add_reference` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 126 | Execute the add reference operation for the current toolkit workflow. |
| function | `add_type_constraint` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 145 | Execute the add type constraint operation for the current toolkit workflow. |
| function | `detect_constraint_conflicts` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 167 | Execute the detect constraint conflicts operation for the current toolkit workflow. |
| function | `accept_constraint` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 183 | Execute the accept constraint operation for the current toolkit workflow. |
| function | `ingest_function_artifact` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 196 | Execute the ingest function artifact operation for the current toolkit workflow. |
| function | `query` | [`x86decomp.analysis_db`](../features/x86decomp-analysis-db.md) | 252 | Execute the query operation for the current toolkit workflow. |
| function | `_load_angr` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 18 | Support load angr processing for internal toolkit callers. |
| function | `_arch_name` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 28 | Support arch name processing for internal toolkit callers. |
| function | `_summaries` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 37 | Support summaries processing for internal toolkit callers. |
| function | `_counterexample` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 113 | Support counterexample processing for internal toolkit callers. |
| function | `angr_bounded_compare` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 132 | Execute the angr bounded compare operation for the current toolkit workflow. |
| function | `angr_bounded_compare_files` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 178 | Execute the angr bounded compare files operation for the current toolkit workflow. |
| function | `_load_memory_harness` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 187 | Support load memory harness processing for internal toolkit callers. |
| function | `_memory_summaries` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 215 | Support memory summaries processing for internal toolkit callers. |
| function | `_memory_counterexample` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 383 | Support memory counterexample processing for internal toolkit callers. |
| function | `angr_memory_alias_compare` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 413 | Execute the angr memory alias compare operation for the current toolkit workflow. |
| function | `angr_memory_alias_compare_files` | [`x86decomp.angr_backend`](../features/x86decomp-angr-backend.md) | 452 | Execute the angr memory alias compare files operation for the current toolkit workflow. |
| function | `function_id_from_rva` | [`x86decomp.artifacts`](../features/x86decomp-artifacts.md) | 16 | Execute the function id from rva operation for the current toolkit workflow. |
| function | `validate_function_manifest` | [`x86decomp.artifacts`](../features/x86decomp-artifacts.md) | 23 | Validate function manifest for the current toolkit workflow. |
| function | `import_function_artifact` | [`x86decomp.artifacts`](../features/x86decomp-artifacts.md) | 47 | Execute the import function artifact operation for the current toolkit workflow. |
| function | `verify_function_artifact` | [`x86decomp.artifacts`](../features/x86decomp-artifacts.md) | 78 | Verify function artifact for the current toolkit workflow. |
| function | `validate_symbol` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 15 | Validate symbol for the current toolkit workflow. |
| function | `render_byte_assembly` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 22 | Render the original compatibility form. This output intentionally preserves byte-form assembly semantics. |
| function | `parse_byte_directives` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 40 | Parse byte directives for the current toolkit workflow. |
| function | `_chunk_comments` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 63 | Support chunk comments processing for internal toolkit callers. |
| function | `render_annotated_assembly` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 74 | Render byte-identical directives with idempotent Capstone comments. |
| function | `annotate_source` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 96 | Execute the annotate source operation for the current toolkit workflow. |
| function | `byte_directive_lines` | [`x86decomp.assembly.annotation`](../features/x86decomp-assembly-annotation.md) | 121 | Execute the byte directive lines operation for the current toolkit workflow. |
| function | `_json_file` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 21 | Load and parse JSON content from a filesystem path. |
| function | `_json_array` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 29 | Support json array processing for internal toolkit callers. |
| function | `_int` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 42 | Support int processing for internal toolkit callers. |
| function | `_emit` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 47 | Support emit processing for internal toolkit callers. |
| function | `build_parser` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 54 | Build the argparse parser for this command surface. |
| function | `dispatch` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 143 | Dispatch parsed command arguments to the matching implementation. |
| function | `main` | [`x86decomp.assembly.cli`](../features/x86decomp-assembly-cli.md) | 246 | Run the command-line entry point and return its process status. |
| class | `AssemblerError` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 21 | Assembler failure with source line numbers retained for focused fallback. |
| function | `__init__` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 24 | Initialize the instance with validated constructor state. |
| class | `InstructionCandidate` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 31 | Store validated instruction candidate fields used by toolkit reports and adapters. |
| function | `end` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 43 | Execute the end operation for the current toolkit workflow. |
| function | `_capstone` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 48 | Support capstone processing for internal toolkit callers. |
| function | `_safe_symbol` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 58 | Support safe symbol processing for internal toolkit callers. |
| function | `_preferred_addresses` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 63 | Support preferred addresses processing for internal toolkit callers. |
| function | `_replace_address_token` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 81 | Support replace address token processing for internal toolkit callers. |
| function | `_instruction_candidates` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 94 | Support instruction candidates processing for internal toolkit callers. |
| function | `_render_source_with_line_map` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 190 | Support render source with line map processing for internal toolkit callers. |
| function | `_render_source` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 225 | Support render source processing for internal toolkit callers. |
| function | `discover_assembler` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 244 | Discover assembler for the current toolkit workflow. |
| function | `assemble_coff` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 268 | Execute the assemble coff operation for the current toolkit workflow. |
| function | `_unit_for_offset` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 321 | Support unit for offset processing for internal toolkit callers. |
| function | `verify_existing_source` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 326 | Assemble an existing source file and verify its resolved bytes exactly. |
| function | `materialize_function` | [`x86decomp.assembly.materialize`](../features/x86decomp-assembly-materialize.md) | 384 | Materialize readable assembly and prove exact bytes, falling back per instruction. |
| function | `_load_json` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 26 | Support load json processing for internal toolkit callers. |
| function | `_resolve_path` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 34 | Support resolve path processing for internal toolkit callers. |
| function | `_function_bytes` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 40 | Support function bytes processing for internal toolkit callers. |
| function | `_symbol_map` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 60 | Support symbol map processing for internal toolkit callers. |
| class | `AssemblyPipeline` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 84 | Coordinate assembly pipeline behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 86 | Initialize the instance with validated constructor state. |
| function | `batch` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 91 | Execute the batch operation for the current toolkit workflow. |
| function | `report` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 319 | Execute the report operation for the current toolkit workflow. |
| function | `list_runs` | [`x86decomp.assembly.pipeline`](../features/x86decomp-assembly-pipeline.md) | 336 | Execute the list runs operation for the current toolkit workflow. |
| class | `SymbolAddress` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 25 | Store validated symbol address fields used by toolkit reports and adapters. |
| function | `safe_name` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 34 | Execute the safe name operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 38 | Return a serializable dictionary representation. |
| function | `normalize_symbol_map` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 49 | Normalize symbol map for the current toolkit workflow. |
| function | `supported_relocations` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 100 | Execute the supported relocations operation for the current toolkit workflow. |
| function | `_read_addend` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 121 | Support read addend processing for internal toolkit callers. |
| function | `_write_value` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 128 | Support write value processing for internal toolkit callers. |
| function | `_object_symbol_target` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 139 | Support object symbol target processing for internal toolkit callers. |
| function | `_resolve_target` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 161 | Support resolve target processing for internal toolkit callers. |
| function | `_compute_value` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 187 | Support compute value processing for internal toolkit callers. |
| class | `RelocationResolver` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 245 | Resolve COFF relocation fields under an explicit original-RVA symbol map. |
| function | `inspect` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 248 | Execute the inspect operation for the current toolkit workflow. |
| function | `resolve` | [`x86decomp.assembly.relocations`](../features/x86decomp-assembly-relocations.md) | 269 | Resolve resolve for the current toolkit workflow. |
| class | `AssemblyStore` | [`x86decomp.assembly.store`](../features/x86decomp-assembly-store.md) | 49 | Additive relocation-aware assembly schema layered on the current native reconstruction state. |
| function | `initialize` | [`x86decomp.assembly.store`](../features/x86decomp-assembly-store.md) | 52 | Initialize initialize for the current toolkit workflow. |
| function | `check` | [`x86decomp.assembly.store`](../features/x86decomp-assembly-store.md) | 74 | Check check for the current toolkit workflow. |
| function | `decode` | [`x86decomp.assembly.store`](../features/x86decomp-assembly-store.md) | 108 | Decode configured JSON columns from a SQLite row. |
| function | `classification_metrics` | [`x86decomp.benchmarks`](../features/x86decomp-benchmarks.md) | 17 | Execute the classification metrics operation for the current toolkit workflow. |
| function | `_resolve` | [`x86decomp.benchmarks`](../features/x86decomp-benchmarks.md) | 35 | Support resolve processing for internal toolkit callers. |
| function | `run_benchmark_corpus` | [`x86decomp.benchmarks`](../features/x86decomp-benchmarks.md) | 42 | Run benchmark corpus for the current toolkit workflow. |
| class | `BinaryReader` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 10 | Read little-endian binary structures while enforcing file bounds. |
| function | `__init__` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 13 | Store immutable input bytes for bounded reads. |
| function | `require` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 17 | Raise ``FormatError`` when a requested byte range is outside the file. |
| function | `unpack` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 24 | Unpack a structure after validating that the entire range exists. |
| function | `u16` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 30 | Read an unsigned little-endian 16-bit integer. |
| function | `u32` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 34 | Read an unsigned little-endian 32-bit integer. |
| function | `u64` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 38 | Read an unsigned little-endian 64-bit integer. |
| function | `c_string` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 42 | Read a bounded NUL-terminated UTF-8 string. |
| function | `optional_u16` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 51 | Read a relative 16-bit field when it is present in a bounded record. |
| function | `optional_u32` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 55 | Read a relative 32-bit field when it is present in a bounded record. |
| function | `optional_u64` | [`x86decomp.binary_reader`](../features/x86decomp-binary-reader.md) | 59 | Read a relative 64-bit field when it is present in a bounded record. |
| function | `_subparsers` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 65 | Support subparsers processing for internal toolkit callers. |
| function | `_source_parsers` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 73 | Support source parsers processing for internal toolkit callers. |
| function | `_group_parsers` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 81 | Support group parsers processing for internal toolkit callers. |
| function | `_leaf_parsers` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 90 | Support leaf parsers processing for internal toolkit callers. |
| function | `_route_owner` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 99 | Support route owner processing for internal toolkit callers. |
| function | `canonical_routes` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 120 | Execute the canonical routes operation for the current toolkit workflow. |
| function | `canonical_groups` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 132 | Execute the canonical groups operation for the current toolkit workflow. |
| function | `command_catalog` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 137 | Execute the command catalog operation for the current toolkit workflow. |
| function | `register_canonical_commands` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 161 | Execute the register canonical commands operation for the current toolkit workflow. |
| function | `dispatch` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 205 | Dispatch parsed command arguments to the matching implementation. |
| function | `build_parser` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 215 | Build the argparse parser for this command surface. |
| function | `main` | [`x86decomp.canonical`](../features/x86decomp-canonical.md) | 226 | Run the command-line entry point and return its process status. |
| function | `_print` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 81 | Support print processing for internal toolkit callers. |
| function | `_path` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 86 | Support path processing for internal toolkit callers. |
| function | `_int` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 91 | Support int processing for internal toolkit callers. |
| function | `_json_object` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 96 | Support json object processing for internal toolkit callers. |
| function | `_build_parser` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 104 | Support build parser processing for internal toolkit callers. |
| function | `_mcp_client` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 247 | Support mcp client processing for internal toolkit callers. |
| function | `_run` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 259 | Support run processing for internal toolkit callers. |
| function | `main` | [`x86decomp.cli`](../features/x86decomp-cli.md) | 435 | Run the command-line entry point and return its process status. |
| function | `parse_json_arg` | [`x86decomp.cli_utils`](../features/x86decomp-cli-utils.md) | 15 | Parse an optional JSON command argument and return a caller-supplied default. |
| function | `emit_json` | [`x86decomp.cli_utils`](../features/x86decomp-cli-utils.md) | 29 | Print a deterministic JSON representation of a command result. |
| function | `relocation_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 128 | Execute the relocation name operation for the current toolkit workflow. |
| function | `relocation_width` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 134 | Execute the relocation width operation for the current toolkit workflow. |
| function | `relocation_is_pc_relative` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 140 | Execute the relocation is pc relative operation for the current toolkit workflow. |
| class | `CoffRelocation` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 148 | Store validated coff relocation fields used by toolkit reports and adapters. |
| function | `width` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 156 | Execute the width operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 160 | Return a serializable dictionary representation. |
| class | `SectionDefinitionAux` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 176 | Store validated section definition aux fields used by toolkit reports and adapters. |
| function | `selection_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 186 | Select ion name for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 190 | Return a serializable dictionary representation. |
| class | `FunctionDefinitionAux` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 206 | Store validated function definition aux fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 213 | Return a serializable dictionary representation. |
| class | `WeakExternalAux` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 225 | Store validated weak external aux fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 230 | Return a serializable dictionary representation. |
| class | `FileAux` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 242 | Store validated file aux fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 246 | Return a serializable dictionary representation. |
| class | `RawAux` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 252 | Store validated raw aux fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 256 | Return a serializable dictionary representation. |
| class | `CoffSection` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 265 | Store validated coff section fields used by toolkit reports and adapters. |
| function | `is_comdat` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 282 | Execute the is comdat operation for the current toolkit workflow. |
| function | `comdat_selection_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 287 | Execute the comdat selection name operation for the current toolkit workflow. |
| function | `alignment_power` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 292 | Execute the alignment power operation for the current toolkit workflow. |
| function | `alignment` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 302 | Execute the alignment operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 307 | Return a serializable dictionary representation. |
| class | `CoffSymbol` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 333 | Store validated coff symbol fields used by toolkit reports and adapters. |
| function | `is_function` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 345 | Execute the is function operation for the current toolkit workflow. |
| function | `section_definition` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 352 | Execute the section definition operation for the current toolkit workflow. |
| function | `function_definition` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 360 | Execute the function definition operation for the current toolkit workflow. |
| function | `weak_external` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 368 | Execute the weak external operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 375 | Return a serializable dictionary representation. |
| class | `CoffObject` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 391 | Store validated coff object fields used by toolkit reports and adapters. |
| function | `architecture` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 404 | Execute the architecture operation for the current toolkit workflow. |
| function | `section` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 412 | Execute the section operation for the current toolkit workflow. |
| function | `find_symbols` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 418 | Execute the find symbols operation for the current toolkit workflow. |
| function | `symbol_by_index` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 425 | Execute the symbol by index operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 429 | Return a serializable dictionary representation. |
| class | `ExtractedSymbol` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 448 | Store validated extracted symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 457 | Return a serializable dictionary representation. |
| class | `ComdatCandidate` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 470 | Store validated comdat candidate fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 482 | Return a serializable dictionary representation. |
| class | `ComdatResolution` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 499 | Store validated comdat resolution fields used by toolkit reports and adapters. |
| function | `valid` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 506 | Execute the valid operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 510 | Return a serializable dictionary representation. |
| class | `SyntheticSymbolSpec` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 522 | Store validated synthetic symbol spec fields used by toolkit reports and adapters. |
| class | `SyntheticSectionSpec` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 533 | Store validated synthetic section spec fields used by toolkit reports and adapters. |
| function | `_read_string_table` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 547 | Support read string table processing for internal toolkit callers. |
| function | `_string_at` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 562 | Support string at processing for internal toolkit callers. |
| function | `_decode_symbol_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 572 | Support decode symbol name processing for internal toolkit callers. |
| function | `_decode_section_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 580 | Support decode section name processing for internal toolkit callers. |
| function | `_parse_header` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 588 | Return variant, machine, sections, timestamp, symptr, symcount, |
| function | `_parse_auxiliary_records` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 642 | Support parse auxiliary records processing for internal toolkit callers. |
| function | `_read_addend` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 701 | Support read addend processing for internal toolkit callers. |
| function | `parse_coff_bytes` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 708 | Parse coff bytes for the current toolkit workflow. |
| function | `parse_coff` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 907 | Parse coff for the current toolkit workflow. |
| function | `extract_symbol` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 915 | Extract symbol for the current toolkit workflow. |
| function | `collect_comdat_candidates` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 971 | Execute the collect comdat candidates operation for the current toolkit workflow. |
| function | `resolve_comdats` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 999 | Resolve COMDAT groups using PE/COFF selection semantics. |
| function | `_encode_name` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1100 | Support encode name processing for internal toolkit callers. |
| function | `_section_aux_bytes` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1110 | Support section aux bytes processing for internal toolkit callers. |
| function | `build_synthetic_coff_object` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1127 | Build a deterministic classic COFF object with multiple sections. |
| function | `synthetic_symbol_indices` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1244 | Execute the synthetic symbol indices operation for the current toolkit workflow. |
| function | `build_synthetic_coff` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1256 | Backward-compatible one-section synthetic COFF builder. |
| function | `build_comdat_coff` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1296 | Build comdat coff for the current toolkit workflow. |
| function | `write_synthetic_coff` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1362 | Write synthetic coff for the current toolkit workflow. |
| function | `write_synthetic_coff_object` | [`x86decomp.coff`](../features/x86decomp-coff.md) | 1380 | Write synthetic coff object for the current toolkit workflow. |
| class | `ArchiveMember` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 27 | Store validated archive member fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 43 | Return a serializable dictionary representation. |
| class | `CoffArchive` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 66 | Store validated coff archive fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 73 | Return a serializable dictionary representation. |
| function | `_decimal` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 86 | Support decimal processing for internal toolkit callers. |
| function | `_octal` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 97 | Support octal processing for internal toolkit callers. |
| function | `_long_name` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 108 | Support long name processing for internal toolkit callers. |
| function | `_parse_import_object` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 117 | Support parse import object processing for internal toolkit callers. |
| function | `_cstring_sequence` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 155 | Support cstring sequence processing for internal toolkit callers. |
| function | `_first_linker_symbols` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 170 | Support first linker symbols processing for internal toolkit callers. |
| function | `_second_linker_symbols` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 185 | Support second linker symbols processing for internal toolkit callers. |
| function | `parse_coff_archive_bytes` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 213 | Parse coff archive bytes for the current toolkit workflow. |
| function | `parse_coff_archive` | [`x86decomp.coff_archive`](../features/x86decomp-coff-archive.md) | 326 | Parse coff archive for the current toolkit workflow. |
| function | `load_profile` | [`x86decomp.compiler`](../features/x86decomp-compiler.md) | 19 | Load profile for the current toolkit workflow. |
| function | `_tool_version` | [`x86decomp.compiler`](../features/x86decomp-compiler.md) | 59 | Support tool version processing for internal toolkit callers. |
| function | `_resolve_executable` | [`x86decomp.compiler`](../features/x86decomp-compiler.md) | 75 | Support resolve executable processing for internal toolkit callers. |
| function | `compiler_cache_key` | [`x86decomp.compiler`](../features/x86decomp-compiler.md) | 88 | Execute the compiler cache key operation for the current toolkit workflow. |
| function | `run_compiler_profile` | [`x86decomp.compiler`](../features/x86decomp-compiler.md) | 105 | Run compiler profile for the current toolkit workflow. |
| function | `_variant_arguments` | [`x86decomp.compiler_lab`](../features/x86decomp-compiler-lab.md) | 16 | Support variant arguments processing for internal toolkit callers. |
| function | `run_compiler_lab` | [`x86decomp.compiler_lab`](../features/x86decomp-compiler-lab.md) | 29 | Run compiler lab for the current toolkit workflow. |
| function | `run_compiler_worker` | [`x86decomp.compiler_worker`](../features/x86decomp-compiler-worker.md) | 23 | Run compiler worker for the current toolkit workflow. |
| class | `StoredArtifact` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 22 | Store validated stored artifact fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 29 | Return a serializable dictionary representation. |
| function | `display` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 31 | Execute the display operation for the current toolkit workflow. |
| class | `ContentStore` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 47 | Immutable SHA-256 store rooted at ``root``. |
| function | `__init__` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 50 | Initialize the instance with validated constructor state. |
| function | `_paths` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 62 | Support paths processing for internal toolkit callers. |
| function | `_validate_digest` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 70 | Support validate digest processing for internal toolkit callers. |
| function | `_locked` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 76 | Cross-process advisory lock using an exclusive lock file. |
| function | `put_bytes` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 98 | Execute the put bytes operation for the current toolkit workflow. |
| function | `put_file` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 132 | Execute the put file operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 150 | Execute the get operation for the current toolkit workflow. |
| function | `read_bytes` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 158 | Read bytes for the current toolkit workflow. |
| function | `add_reference` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 166 | Execute the add reference operation for the current toolkit workflow. |
| function | `remove_reference` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 183 | Remove reference for the current toolkit workflow. |
| function | `referenced_digests` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 192 | Execute the referenced digests operation for the current toolkit workflow. |
| function | `verify` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 200 | Verify verify for the current toolkit workflow. |
| function | `garbage_collect` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 232 | Execute the garbage collect operation for the current toolkit workflow. |
| function | `export_index` | [`x86decomp.content_store`](../features/x86decomp-content-store.md) | 260 | Execute the export index operation for the current toolkit workflow. |
| class | `ContractError` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 17 | Raised when an input violates a stable project contract. |
| function | `utc_now` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 21 | Execute the utc now operation for the current toolkit workflow. |
| function | `canonical_json` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 26 | Execute the canonical json operation for the current toolkit workflow. |
| function | `sha256_bytes` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 31 | Execute the sha256 bytes operation for the current toolkit workflow. |
| function | `sha256_file` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 36 | Execute the sha256 file operation for the current toolkit workflow. |
| function | `stable_id` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 45 | Execute the stable id operation for the current toolkit workflow. |
| function | `random_id` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 51 | Execute the random id operation for the current toolkit workflow. |
| function | `validate_id` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 56 | Validate id for the current toolkit workflow. |
| function | `ensure_relative_path` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 63 | Execute the ensure relative path operation for the current toolkit workflow. |
| function | `atomic_write_bytes` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 72 | Execute the atomic write bytes operation for the current toolkit workflow. |
| function | `atomic_write_json` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 92 | Execute the atomic write json operation for the current toolkit workflow. |
| function | `read_json` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 97 | Read json for the current toolkit workflow. |
| function | `dedupe_preserve` | [`x86decomp.contracts`](../features/x86decomp-contracts.md) | 103 | Execute the dedupe preserve operation for the current toolkit workflow. |
| function | `_section_kind` | [`x86decomp.convergence`](../features/x86decomp-convergence.md) | 20 | Support section kind processing for internal toolkit callers. |
| function | `analyze_image_convergence` | [`x86decomp.convergence`](../features/x86decomp-convergence.md) | 36 | Execute the analyze image convergence operation for the current toolkit workflow. |
| function | `append_convergence_history` | [`x86decomp.convergence`](../features/x86decomp-convergence.md) | 167 | Append convergence history for the current toolkit workflow. |
| function | `_function_prefix` | [`x86decomp.cpp_recovery`](../features/x86decomp-cpp-recovery.md) | 18 | Support function prefix processing for internal toolkit callers. |
| function | `_adjustor_thunk_candidate` | [`x86decomp.cpp_recovery`](../features/x86decomp-cpp-recovery.md) | 28 | Support adjustor thunk candidate processing for internal toolkit callers. |
| function | `recover_cpp_model` | [`x86decomp.cpp_recovery`](../features/x86decomp-cpp-recovery.md) | 56 | Execute the recover cpp model operation for the current toolkit workflow. |
| function | `_copy_required` | [`x86decomp.decompme`](../features/x86decomp-decompme.md) | 14 | Support copy required processing for internal toolkit callers. |
| function | `create_decompme_packet` | [`x86decomp.decompme`](../features/x86decomp-decompme.md) | 24 | Build a local, reviewable function packet. |
| function | `compare_bytes` | [`x86decomp.diffing`](../features/x86decomp-diffing.md) | 13 | Compare bytes for the current toolkit workflow. |
| function | `compare_files` | [`x86decomp.diffing`](../features/x86decomp-diffing.md) | 61 | Compare files for the current toolkit workflow. |
| function | `_capstone` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 14 | Support capstone processing for internal toolkit callers. |
| class | `InstructionRecord` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 27 | Store validated instruction record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 39 | Return a serializable dictionary representation. |
| function | `_is_known_address` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 55 | Support is known address processing for internal toolkit callers. |
| function | `decode_instructions` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 60 | Decode instructions for the current toolkit workflow. |
| function | `control_flow_edges` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 149 | Execute the control flow edges operation for the current toolkit workflow. |
| function | `compare_instruction_streams` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 163 | Compare instruction streams for the current toolkit workflow. |
| function | `cross_check_ghidra_instructions` | [`x86decomp.disassembly`](../features/x86decomp-disassembly.md) | 226 | Execute the cross check ghidra instructions operation for the current toolkit workflow. |
| function | `_unicorn` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 21 | Support unicorn processing for internal toolkit callers. |
| function | `_align_down` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 33 | Support align down processing for internal toolkit callers. |
| function | `_align_up` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 38 | Support align up processing for internal toolkit callers. |
| class | `MemoryRegion` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 44 | Store validated memory region fields used by toolkit reports and adapters. |
| class | `ExecutionSpec` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 52 | Store validated execution spec fields used by toolkit reports and adapters. |
| function | `load_execution_spec` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 69 | Load execution spec for the current toolkit workflow. |
| function | `_register_map` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 157 | Support register map processing for internal toolkit callers. |
| function | `_map_region` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 175 | Support map region processing for internal toolkit callers. |
| function | `execute_code` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 188 | Execute the execute code operation for the current toolkit workflow. |
| function | `code_hook` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 232 | Execute the code hook operation for the current toolkit workflow. |
| function | `differential_validate` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 290 | Execute the differential validate operation for the current toolkit workflow. |
| function | `differential_validate_files` | [`x86decomp.dynamic`](../features/x86decomp-dynamic.md) | 339 | Execute the differential validate files operation for the current toolkit workflow. |
| function | `parse_drcov_text` | [`x86decomp.dynamorio`](../features/x86decomp-dynamorio.md) | 34 | Parse a drcov ``-dump_text`` log into stable module/block records. |
| function | `run_drcov_trace` | [`x86decomp.dynamorio`](../features/x86decomp-dynamorio.md) | 118 | Execute an authorized program under drcov and normalize produced logs. |
| class | `X86DecompError` | [`x86decomp.errors`](../features/x86decomp-errors.md) | 4 | Base class for user-facing toolkit errors. |
| class | `FormatError` | [`x86decomp.errors`](../features/x86decomp-errors.md) | 8 | Raised when an input binary or document violates its contract. |
| class | `ContractError` | [`x86decomp.errors`](../features/x86decomp-errors.md) | 12 | Raised when structured data violates a toolkit contract. |
| class | `VerificationError` | [`x86decomp.errors`](../features/x86decomp-errors.md) | 16 | Raised when integrity or evidence verification fails. |
| class | `ExternalToolError` | [`x86decomp.errors`](../features/x86decomp-errors.md) | 20 | Raised when a configured external tool cannot be executed successfully. |
| function | `_validate_id` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 17 | Support validate id processing for internal toolkit callers. |
| class | `EvidenceStore` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 25 | Filesystem-backed evidence and claims with deterministic validation rules. |
| function | `__init__` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 28 | Initialize the instance with validated constructor state. |
| function | `add_evidence` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 38 | Execute the add evidence operation for the current toolkit workflow. |
| function | `get_evidence` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 84 | Execute the get evidence operation for the current toolkit workflow. |
| function | `create_claim` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 106 | Create claim for the current toolkit workflow. |
| function | `get_claim` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 138 | Execute the get claim operation for the current toolkit workflow. |
| function | `save_claim` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 161 | Execute the save claim operation for the current toolkit workflow. |
| function | `attach_evidence` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 166 | Execute the attach evidence operation for the current toolkit workflow. |
| function | `add_contradiction` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 177 | Execute the add contradiction operation for the current toolkit workflow. |
| function | `audit_evidence_integrity` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 187 | Audit evidence integrity for the current toolkit workflow. |
| function | `verify_claim` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 210 | Apply the strict verification gate and persist the resulting state. |
| function | `require_verified` | [`x86decomp.evidence`](../features/x86decomp-evidence.md) | 256 | Execute the require verified operation for the current toolkit workflow. |
| function | `rva_to_file_offset` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 16 | Execute the rva to file offset operation for the current toolkit workflow. |
| function | `extract_pe_bytes` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 33 | Extract pe bytes for the current toolkit workflow. |
| function | `_masked_copy` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 51 | Support masked copy processing for internal toolkit callers. |
| function | `_candidate_relocation_masks` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 61 | Support candidate relocation masks processing for internal toolkit callers. |
| function | `_pe_base_relocation_masks` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 78 | Support pe base relocation masks processing for internal toolkit callers. |
| function | `compare_pe_function_to_coff_symbol` | [`x86decomp.exe_diff`](../features/x86decomp-exe-diff.md) | 89 | Compare pe function to coff symbol for the current toolkit workflow. |
| function | `build_export_command` | [`x86decomp.ghidra`](../features/x86decomp-ghidra.md) | 14 | Build export command for the current toolkit workflow. |
| function | `run_export` | [`x86decomp.ghidra`](../features/x86decomp-ghidra.md) | 65 | Run export for the current toolkit workflow. |
| class | `CampaignEngine` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 14 | Persistent, deterministic campaign control and next-action planning. |
| function | `__init__` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 17 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 22 | Create create for the current toolkit workflow. |
| function | `_validate_budget` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 44 | Support validate budget processing for internal toolkit callers. |
| function | `transition` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 56 | Execute the transition operation for the current toolkit workflow. |
| function | `start` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 75 | Execute the start operation for the current toolkit workflow. |
| function | `pause` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 79 | Execute the pause operation for the current toolkit workflow. |
| function | `resume` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 83 | Execute the resume operation for the current toolkit workflow. |
| function | `stop` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 87 | Execute the stop operation for the current toolkit workflow. |
| function | `consume_budget` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 91 | Execute the consume budget operation for the current toolkit workflow. |
| function | `branch` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 116 | Execute the branch operation for the current toolkit workflow. |
| function | `get_branch` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 134 | Execute the get branch operation for the current toolkit workflow. |
| function | `snapshot` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 142 | Execute the snapshot operation for the current toolkit workflow. |
| function | `_decision` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 152 | Support decision processing for internal toolkit callers. |
| function | `plan_next` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 158 | Execute the plan next operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 191 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.campaigns`](../features/x86decomp-governance-campaigns.md) | 202 | Execute the list operation for the current toolkit workflow. |
| class | `CandidateStore` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 15 | Coordinate candidate store behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 17 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 23 | Create create for the current toolkit workflow. |
| function | `_clone_files` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 41 | Support clone files processing for internal toolkit callers. |
| function | `add_file` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 51 | Execute the add file operation for the current toolkit workflow. |
| function | `record_evaluation` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 83 | Record evaluation for the current toolkit workflow. |
| function | `compare` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 99 | Compare compare for the current toolkit workflow. |
| function | `transition` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 122 | Execute the transition operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 147 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.candidates`](../features/x86decomp-governance-candidates.md) | 163 | Execute the list operation for the current toolkit workflow. |
| class | `ChangeSet` | [`x86decomp.governance.changesets`](../features/x86decomp-governance-changesets.md) | 14 | Portable, append-only governance audit changesets with base-tip conflict checks. |
| function | `export` | [`x86decomp.governance.changesets`](../features/x86decomp-governance-changesets.md) | 18 | Execute the export operation for the current toolkit workflow. |
| function | `inspect` | [`x86decomp.governance.changesets`](../features/x86decomp-governance-changesets.md) | 44 | Execute the inspect operation for the current toolkit workflow. |
| function | `apply` | [`x86decomp.governance.changesets`](../features/x86decomp-governance-changesets.md) | 71 | Execute the apply operation for the current toolkit workflow. |
| function | `_store` | [`x86decomp.governance.cli`](../features/x86decomp-governance-cli.md) | 31 | Open the project store requested by parsed command arguments. |
| function | `build_parser` | [`x86decomp.governance.cli`](../features/x86decomp-governance-cli.md) | 36 | Build the argparse parser for this command surface. |
| function | `dispatch` | [`x86decomp.governance.cli`](../features/x86decomp-governance-cli.md) | 131 | Dispatch parsed command arguments to the matching implementation. |
| function | `main` | [`x86decomp.governance.cli`](../features/x86decomp-governance-cli.md) | 225 | Run the command-line entry point and return its process status. |
| class | `ConsensusEngine` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 12 | Coordinate consensus engine behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 14 | Initialize the instance with validated constructor state. |
| function | `record` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 19 | Record record for the current toolkit workflow. |
| function | `scan` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 32 | Execute the scan operation for the current toolkit workflow. |
| function | `conflicts` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 75 | Execute the conflicts operation for the current toolkit workflow. |
| function | `resolve` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 79 | Resolve resolve for the current toolkit workflow. |
| function | `explain` | [`x86decomp.governance.consensus`](../features/x86decomp-governance-consensus.md) | 101 | Execute the explain operation for the current toolkit workflow. |
| class | `CounterexampleStore` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 15 | Coordinate counterexample store behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 17 | Initialize the instance with validated constructor state. |
| function | `add` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 23 | Execute the add operation for the current toolkit workflow. |
| function | `minimize` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 42 | Execute the minimize operation for the current toolkit workflow. |
| function | `promote_to_regression` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 68 | Execute the promote to regression operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 85 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 97 | Execute the list operation for the current toolkit workflow. |
| function | `ddmin_bytes` | [`x86decomp.governance.counterexamples`](../features/x86decomp-governance-counterexamples.md) | 104 | Delta-debug a byte string while preserving predicate(data) == True. |
| class | `BinaryFamilyStore` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 12 | Static, content-addressed related-binary correlation. |
| function | `__init__` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 15 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 21 | Create create for the current toolkit workflow. |
| function | `add` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 31 | Execute the add operation for the current toolkit workflow. |
| function | `_block_fingerprints` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 54 | Support block fingerprints processing for internal toolkit callers. |
| function | `correlate` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 60 | Execute the correlate operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 83 | Execute the get operation for the current toolkit workflow. |
| function | `member` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 91 | Execute the member operation for the current toolkit workflow. |
| function | `correlation` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 101 | Execute the correlation operation for the current toolkit workflow. |
| function | `report` | [`x86decomp.governance.family`](../features/x86decomp-governance-family.md) | 111 | Execute the report operation for the current toolkit workflow. |
| class | `Hypothesis` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 38 | Store validated hypothesis fields used by toolkit reports and adapters. |
| function | `_row_to_hypothesis` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 53 | Support row to hypothesis processing for internal toolkit callers. |
| class | `HypothesisLedger` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 70 | Coordinate hypothesis ledger behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 72 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 77 | Create create for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 100 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 108 | Execute the list operation for the current toolkit workflow. |
| function | `add_dependency` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 125 | Execute the add dependency operation for the current toolkit workflow. |
| function | `_has_dependency_cycle` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 137 | Support has dependency cycle processing for internal toolkit callers. |
| function | `attach_evidence` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 149 | Execute the attach evidence operation for the current toolkit workflow. |
| function | `_recalculate_confidence` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 180 | Support recalculate confidence processing for internal toolkit callers. |
| function | `transition` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 198 | Execute the transition operation for the current toolkit workflow. |
| function | `acceptance_gate` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 221 | Execute the acceptance gate operation for the current toolkit workflow. |
| function | `describe` | [`x86decomp.governance.hypotheses`](../features/x86decomp-governance-hypotheses.md) | 255 | Execute the describe operation for the current toolkit workflow. |
| class | `KnowledgeGraph` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 12 | Coordinate knowledge graph behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 14 | Initialize the instance with validated constructor state. |
| function | `upsert_node` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 19 | Execute the upsert node operation for the current toolkit workflow. |
| function | `add_edge` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 34 | Execute the add edge operation for the current toolkit workflow. |
| function | `get_node` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 55 | Execute the get node operation for the current toolkit workflow. |
| function | `impact` | [`x86decomp.governance.knowledge_graph`](../features/x86decomp-governance-knowledge-graph.md) | 65 | Execute the impact operation for the current toolkit workflow. |
| class | `PluginRegistry` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 17 | Coordinate plugin registry behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 19 | Initialize the instance with validated constructor state. |
| function | `validate_manifest` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 25 | Validate manifest for the current toolkit workflow. |
| function | `install` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 39 | Execute the install operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 57 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 68 | Execute the list operation for the current toolkit workflow. |
| function | `doctor` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 74 | Execute the doctor operation for the current toolkit workflow. |
| function | `invoke` | [`x86decomp.governance.plugins`](../features/x86decomp-governance-plugins.md) | 85 | Execute the invoke operation for the current toolkit workflow. |
| class | `ProofLedger` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 20 | Coordinate proof ledger behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 22 | Initialize the instance with validated constructor state. |
| function | `create_obligation` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 27 | Create obligation for the current toolkit workflow. |
| function | `add_result` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 40 | Execute the add result operation for the current toolkit workflow. |
| function | `obligation` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 56 | Execute the obligation operation for the current toolkit workflow. |
| function | `result` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 68 | Execute the result operation for the current toolkit workflow. |
| function | `evaluate` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 78 | Execute the evaluate operation for the current toolkit workflow. |
| class | `ProofBundle` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 86 | Deterministic, path-safe, independently verifiable proof package. |
| function | `_zip_info` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 90 | Support zip info processing for internal toolkit callers. |
| function | `export` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 98 | Execute the export operation for the current toolkit workflow. |
| function | `_validate_member` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 140 | Support validate member processing for internal toolkit callers. |
| function | `verify` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 147 | Verify verify for the current toolkit workflow. |
| function | `inspect` | [`x86decomp.governance.proofs`](../features/x86decomp-governance-proofs.md) | 193 | Execute the inspect operation for the current toolkit workflow. |
| class | `ReviewQueue` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 13 | Coordinate review queue behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 15 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 20 | Create create for the current toolkit workflow. |
| function | `assign` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 34 | Execute the assign operation for the current toolkit workflow. |
| function | `decide` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 49 | Execute the decide operation for the current toolkit workflow. |
| function | `lock` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 75 | Execute the lock operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 85 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.reviews`](../features/x86decomp-governance-reviews.md) | 98 | Execute the list operation for the current toolkit workflow. |
| class | `GovernanceStore` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 290 | Transactional governance extension store. |
| function | `__init__` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 297 | Initialize the instance with validated constructor state. |
| function | `initialize` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 302 | Initialize initialize for the current toolkit workflow. |
| function | `connect` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 321 | Execute the connect operation for the current toolkit workflow. |
| function | `transaction` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 332 | Execute the transaction operation for the current toolkit workflow. |
| function | `audit` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 345 | Audit audit for the current toolkit workflow. |
| function | `verify_audit_chain` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 381 | Verify audit chain for the current toolkit workflow. |
| function | `check` | [`x86decomp.governance.store`](../features/x86decomp-governance-store.md) | 402 | Check check for the current toolkit workflow. |
| class | `WorkerRegistry` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 13 | Coordinate worker registry behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 15 | Initialize the instance with validated constructor state. |
| function | `register` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 20 | Execute the register operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 35 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 45 | Execute the list operation for the current toolkit workflow. |
| function | `select` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 54 | Select select for the current toolkit workflow. |
| function | `set_status` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 65 | Execute the set status operation for the current toolkit workflow. |
| function | `doctor` | [`x86decomp.governance.workers`](../features/x86decomp-governance-workers.md) | 75 | Execute the doctor operation for the current toolkit workflow. |
| function | `_resolve_executable` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 24 | Support resolve executable processing for internal toolkit callers. |
| function | `_version` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 37 | Support version processing for internal toolkit callers. |
| function | `_expand_flag_matrix` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 48 | Support expand flag matrix processing for internal toolkit callers. |
| function | `build_ground_truth_corpus` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 75 | Build ground truth corpus for the current toolkit workflow. |
| function | `verify_ground_truth_corpus` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 195 | Verify ground truth corpus for the current toolkit workflow. |
| function | `compare_ground_truth_corpora` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 216 | Compare successful corpus builds across compiler/version reports. |
| function | `create_builtin_manifest` | [`x86decomp.ground_truth`](../features/x86decomp-ground-truth.md) | 298 | Create builtin manifest for the current toolkit workflow. |
| function | `_deterministic_word` | [`x86decomp.harness_generator`](../features/x86decomp-harness-generator.md) | 17 | Support deterministic word processing for internal toolkit callers. |
| function | `generate_execution_harness` | [`x86decomp.harness_generator`](../features/x86decomp-harness-generator.md) | 23 | Generate execution harness for the current toolkit workflow. |
| function | `generate_execution_harness_from_files` | [`x86decomp.harness_generator`](../features/x86decomp-harness-generator.md) | 141 | Generate execution harness from files for the current toolkit workflow. |
| function | `_assembly_bytes` | [`x86decomp.hybrid`](../features/x86decomp-hybrid.md) | 14 | Support assembly bytes processing for internal toolkit callers. |
| function | `generate_hybrid_project` | [`x86decomp.hybrid`](../features/x86decomp-hybrid.md) | 24 | Generate a continuously buildable hybrid tree. |
| class | `ByteRange` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 21 | Store validated byte range fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 27 | Return a serializable dictionary representation. |
| function | `_pe_offsets` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 32 | Support pe offsets processing for internal toolkit callers. |
| function | `derive_layout_profile` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 55 | Execute the derive layout profile operation for the current toolkit workflow. |
| function | `_mask_ranges` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 95 | Support mask ranges processing for internal toolkit callers. |
| function | `_rva_to_file_offset` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 105 | Support rva to file offset processing for internal toolkit callers. |
| function | `_profile_ranges` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 116 | Support profile ranges processing for internal toolkit callers. |
| function | `_apply_rebase` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 152 | Support apply rebase processing for internal toolkit callers. |
| function | `_mismatches` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 181 | Support mismatches processing for internal toolkit callers. |
| function | `compare_whole_images` | [`x86decomp.image_match`](../features/x86decomp-image-match.md) | 195 | Compare whole images for the current toolkit workflow. |
| function | `_require_string_list` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 24 | Support require string list processing for internal toolkit callers. |
| function | `_resolve_existing` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 33 | Support resolve existing processing for internal toolkit callers. |
| function | `_parse_stdin` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 43 | Support parse stdin processing for internal toolkit callers. |
| function | `_copy_fixtures` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 66 | Support copy fixtures processing for internal toolkit callers. |
| function | `_substitute_command` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 98 | Support substitute command processing for internal toolkit callers. |
| function | `_bounded_output` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 113 | Support bounded output processing for internal toolkit callers. |
| function | `_run_side` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 125 | Support run side processing for internal toolkit callers. |
| function | `_observe_file` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 204 | Support observe file processing for internal toolkit callers. |
| function | `_compare_stream` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 259 | Support compare stream processing for internal toolkit callers. |
| function | `run_integration_scenarios` | [`x86decomp.integration`](../features/x86decomp-integration.md) | 282 | Execute and compare all declared integration scenarios. |
| class | `MapSegment` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 35 | Store validated map segment fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 43 | Return a serializable dictionary representation. |
| class | `MapContribution` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 55 | Store validated map contribution fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 62 | Return a serializable dictionary representation. |
| class | `MapPublic` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 73 | Store validated map public fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 82 | Return a serializable dictionary representation. |
| class | `LinkerMap` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 95 | Store validated linker map fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 107 | Return a serializable dictionary representation. |
| function | `parse_msvc_map_text` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 126 | Parse msvc map text for the current toolkit workflow. |
| function | `parse_msvc_map` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 224 | Parse msvc map for the current toolkit workflow. |
| function | `_normalize_object_key` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 232 | Support normalize object key processing for internal toolkit callers. |
| function | `reconstruct_linker_layout` | [`x86decomp.linker_layout`](../features/x86decomp-linker-layout.md) | 240 | Reconstruct linker layout for the current toolkit workflow. |
| function | `build_linker_reconstruction_plan` | [`x86decomp.linker_reconstruction`](../features/x86decomp-linker-reconstruction.md) | 21 | Build linker reconstruction plan for the current toolkit workflow. |
| function | `write_relink_manifest_from_plan` | [`x86decomp.linker_reconstruction`](../features/x86decomp-linker-reconstruction.md) | 146 | Write relink manifest from plan for the current toolkit workflow. |
| function | `_parse_candidate` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 35 | Support parse candidate processing for internal toolkit callers. |
| function | `_prepare_output` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 91 | Support prepare output processing for internal toolkit callers. |
| function | `_feedback_from_compile` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 105 | Support feedback from compile processing for internal toolkit callers. |
| function | `_feedback_from_diff` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 116 | Support feedback from diff processing for internal toolkit callers. |
| function | `generate_candidate` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 130 | Generate and validate one uncompiled C proposal. |
| function | `run_match_loop` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 174 | Run bounded local generation, compilation, relocation, and exact comparison. |
| function | `verify_match_report` | [`x86decomp.local_llm.matching`](../features/x86decomp-local-llm-matching.md) | 366 | Verify report invariants and every referenced accepted artifact hash. |
| function | `provider_catalog` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 73 | Return the immutable built-in provider preset catalog. |
| function | `_normalized_base_url` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 89 | Support normalized base url processing for internal toolkit callers. |
| function | `is_loopback_host` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 106 | Return whether a hostname is an explicit local loopback identity. |
| function | `resolved_addresses_are_loopback` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 117 | Resolve a host and require every result to be loopback. |
| function | `create_profile` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 139 | Create and persist a validated provider profile. |
| function | `load_profile` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 179 | Load profile for the current toolkit workflow. |
| function | `validate_profile` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 187 | Validate and normalize a local-model profile. |
| function | `public_profile` | [`x86decomp.local_llm.profiles`](../features/x86decomp-local-llm-profiles.md) | 248 | Return report-safe profile metadata without secret values. |
| function | `_text` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 15 | Support text processing for internal toolkit callers. |
| function | `_integer` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 31 | Support integer processing for internal toolkit callers. |
| function | `_resolve_job_path` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 38 | Support resolve job path processing for internal toolkit callers. |
| function | `load_job` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 49 | Load and normalize a local-LLM generation/matching job. |
| function | `_evidence_block` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 131 | Support evidence block processing for internal toolkit callers. |
| function | `build_messages` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 146 | Build a deterministic two-message prompt with explicit trust boundaries. |
| function | `prompt_record` | [`x86decomp.local_llm.prompts`](../features/x86decomp-local-llm-prompts.md) | 193 | Execute the prompt record operation for the current toolkit workflow. |
| class | `ModelResponse` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 20 | Store validated model response fields used by toolkit reports and adapters. |
| class | `_SameOriginRedirectHandler` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 28 | Coordinate same origin redirect handler behavior for the current toolkit workflow. |
| function | `redirect_request` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 30 | Execute the redirect request operation for the current toolkit workflow. |
| function | `_endpoint` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 41 | Support endpoint processing for internal toolkit callers. |
| function | `_opener` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 46 | Support opener processing for internal toolkit callers. |
| function | `_headers` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 55 | Support headers processing for internal toolkit callers. |
| function | `_read_json_response` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 68 | Support read json response processing for internal toolkit callers. |
| function | `_request_json` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 92 | Support request json processing for internal toolkit callers. |
| function | `_model_ids` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 110 | Support model ids processing for internal toolkit callers. |
| function | `_ollama_model_matches` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 133 | Support ollama model matches processing for internal toolkit callers. |
| function | `probe_profile` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 142 | Probe a provider's model-list endpoint without generating text. |
| function | `_candidate_schema` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 160 | Support candidate schema processing for internal toolkit callers. |
| function | `_openai_body` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 175 | Support openai body processing for internal toolkit callers. |
| function | `_ollama_body` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 196 | Support ollama body processing for internal toolkit callers. |
| function | `_extract_content` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 212 | Support extract content processing for internal toolkit callers. |
| function | `chat` | [`x86decomp.local_llm.transport`](../features/x86decomp-local-llm-transport.md) | 229 | Generate one bounded response, retrying once without structured mode when unsupported. |
| class | `MCPTool` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 23 | Store validated m c p tool fields used by toolkit reports and adapters. |
| class | `StdioMCPClient` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 30 | Coordinate stdio m c p client behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 32 | Initialize the instance with validated constructor state. |
| function | `_send` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 49 | Support send processing for internal toolkit callers. |
| function | `_request` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 56 | Support request processing for internal toolkit callers. |
| function | `initialize` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 84 | Initialize initialize for the current toolkit workflow. |
| function | `_ensure_initialized` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 98 | Support ensure initialized processing for internal toolkit callers. |
| function | `list_tools` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 103 | Execute the list tools operation for the current toolkit workflow. |
| function | `call_tool` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 123 | Execute the call tool operation for the current toolkit workflow. |
| function | `close` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 128 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 142 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 146 | Exit the managed runtime context and release owned resources. |
| class | `StreamableHTTPMCPClient` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 151 | Coordinate streamable h t t p m c p client behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 153 | Initialize the instance with validated constructor state. |
| function | `_request` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 163 | Support request processing for internal toolkit callers. |
| function | `_notify` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 198 | Support notify processing for internal toolkit callers. |
| function | `initialize` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 208 | Initialize initialize for the current toolkit workflow. |
| function | `_ensure_initialized` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 215 | Support ensure initialized processing for internal toolkit callers. |
| function | `list_tools` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 220 | Execute the list tools operation for the current toolkit workflow. |
| function | `call_tool` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 226 | Execute the call tool operation for the current toolkit workflow. |
| function | `close` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 231 | Streamable HTTP has no persistent local process to close. |
| function | `is_probable_mutation` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 241 | Execute the is probable mutation operation for the current toolkit workflow. |
| class | `GhidraMCPGateway` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 247 | Separates read calls from hash-approved mutation transactions. |
| function | `__init__` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 250 | Initialize the instance with validated constructor state. |
| function | `read` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 258 | Read read for the current toolkit workflow. |
| function | `propose_mutation` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 266 | Execute the propose mutation operation for the current toolkit workflow. |
| function | `commit_mutation` | [`x86decomp.mcp`](../features/x86decomp-mcp.md) | 293 | Execute the commit mutation operation for the current toolkit workflow. |
| class | `ProjectMemory` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 14 | Coordinate project memory behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 16 | Initialize the instance with validated constructor state. |
| function | `read_events` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 26 | Read events for the current toolkit workflow. |
| function | `append` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 44 | Append append for the current toolkit workflow. |
| function | `verify` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 77 | Verify verify for the current toolkit workflow. |
| function | `require_valid` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 96 | Execute the require valid operation for the current toolkit workflow. |
| function | `render` | [`x86decomp.memory`](../features/x86decomp-memory.md) | 102 | Render render for the current toolkit workflow. |
| class | `EvidenceKind` | [`x86decomp.models`](../features/x86decomp-models.md) | 12 | Coordinate evidence kind behavior for the current toolkit workflow. |
| class | `ClaimState` | [`x86decomp.models`](../features/x86decomp-models.md) | 23 | Coordinate claim state behavior for the current toolkit workflow. |
| class | `VerificationStatus` | [`x86decomp.models`](../features/x86decomp-models.md) | 31 | Coordinate verification status behavior for the current toolkit workflow. |
| class | `EvidenceItem` | [`x86decomp.models`](../features/x86decomp-models.md) | 39 | Store validated evidence item fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.models`](../features/x86decomp-models.md) | 51 | Return a serializable dictionary representation. |
| class | `Claim` | [`x86decomp.models`](../features/x86decomp-models.md) | 59 | Store validated claim fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.models`](../features/x86decomp-models.md) | 72 | Return a serializable dictionary representation. |
| class | `TypeDescriptorRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 27 | Store validated type descriptor record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 36 | Return a serializable dictionary representation. |
| class | `BaseClassRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 49 | Store validated base class record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 61 | Return a serializable dictionary representation. |
| class | `CompleteObjectLocatorRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 79 | Store validated complete object locator record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 92 | Return a serializable dictionary representation. |
| class | `VTableRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 109 | Store validated v table record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 116 | Return a serializable dictionary representation. |
| class | `UnwindCodeRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 127 | Store validated unwind code record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 136 | Return a serializable dictionary representation. |
| class | `UnwindInfoRecord` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 149 | Store validated unwind info record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 165 | Return a serializable dictionary representation. |
| class | `PEView` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 184 | Coordinate p e view behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 186 | Initialize the instance with validated constructor state. |
| function | `rva_to_offset` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 194 | Execute the rva to offset operation for the current toolkit workflow. |
| function | `valid_rva` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 198 | Execute the valid rva operation for the current toolkit workflow. |
| function | `read` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 206 | Read read for the current toolkit workflow. |
| function | `u16` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 213 | Execute the u16 operation for the current toolkit workflow. |
| function | `u32` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 217 | Execute the u32 operation for the current toolkit workflow. |
| function | `i32` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 221 | Execute the i32 operation for the current toolkit workflow. |
| function | `u64` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 225 | Execute the u64 operation for the current toolkit workflow. |
| function | `pointer` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 229 | Execute the pointer operation for the current toolkit workflow. |
| function | `va_to_rva` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 233 | Execute the va to rva operation for the current toolkit workflow. |
| function | `encoded_pointer_to_rva` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 240 | Encode d pointer to rva for the current toolkit workflow. |
| function | `c_string` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 246 | Execute the c string operation for the current toolkit workflow. |
| function | `executable_rva` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 254 | Execute the executable rva operation for the current toolkit workflow. |
| function | `readonly_data_sections` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 262 | Read only data sections for the current toolkit workflow. |
| function | `_display_type_name` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 273 | Support display type name processing for internal toolkit callers. |
| function | `scan_type_descriptors` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 283 | Execute the scan type descriptors operation for the current toolkit workflow. |
| function | `_parse_base_class` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 317 | Support parse base class processing for internal toolkit callers. |
| function | `_parse_hierarchy` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 353 | Support parse hierarchy processing for internal toolkit callers. |
| function | `scan_complete_object_locators` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 383 | Execute the scan complete object locators operation for the current toolkit workflow. |
| function | `scan_vtables` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 429 | Execute the scan vtables operation for the current toolkit workflow. |
| function | `_decode_unwind_codes` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 483 | Support decode unwind codes processing for internal toolkit callers. |
| function | `parse_x64_unwind` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 542 | Parse x64 unwind for the current toolkit workflow. |
| function | `parse_safe_seh` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 599 | Parse safe seh for the current toolkit workflow. |
| function | `tls_report` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 613 | Execute the tls report operation for the current toolkit workflow. |
| function | `scan_exception_func_info` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 639 | Find structurally plausible MSVC EH3 FuncInfo records. |
| function | `scan_coff_tls` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 693 | Inventory COFF TLS template and callback subsections. |
| function | `scan_static_initializers` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 732 | Execute the scan static initializers operation for the current toolkit workflow. |
| function | `analyze_msvc_metadata` | [`x86decomp.msvc_metadata`](../features/x86decomp-msvc-metadata.md) | 786 | Execute the analyze msvc metadata operation for the current toolkit workflow. |
| function | `_json_file` | [`x86decomp.native.cli`](../features/x86decomp-native-cli.md) | 27 | Load and parse JSON content from a filesystem path. |
| function | `build_parser` | [`x86decomp.native.cli`](../features/x86decomp-native-cli.md) | 33 | Build the argparse parser for this command surface. |
| function | `dispatch` | [`x86decomp.native.cli`](../features/x86decomp-native-cli.md) | 91 | Dispatch parsed command arguments to the matching implementation. |
| function | `main` | [`x86decomp.native.cli`](../features/x86decomp-native-cli.md) | 146 | Run the command-line entry point and return its process status. |
| class | `ClosedLoop` | [`x86decomp.native.closed_loop`](../features/x86decomp-native-closed-loop.md) | 14 | Coordinate closed loop behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.closed_loop`](../features/x86decomp-native-closed-loop.md) | 16 | Initialize the instance with validated constructor state. |
| function | `run` | [`x86decomp.native.closed_loop`](../features/x86decomp-native-closed-loop.md) | 20 | Run run for the current toolkit workflow. |
| function | `show` | [`x86decomp.native.closed_loop`](../features/x86decomp-native-closed-loop.md) | 41 | Execute the show operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.native.closed_loop`](../features/x86decomp-native-closed-loop.md) | 48 | Execute the list operation for the current toolkit workflow. |
| class | `HybridComposer` | [`x86decomp.native.hybrid_composer`](../features/x86decomp-native-hybrid-composer.md) | 14 | Coordinate hybrid composer behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.hybrid_composer`](../features/x86decomp-native-hybrid-composer.md) | 16 | Initialize the instance with validated constructor state. |
| function | `compose` | [`x86decomp.native.hybrid_composer`](../features/x86decomp-native-hybrid-composer.md) | 20 | Execute the compose operation for the current toolkit workflow. |
| function | `verify` | [`x86decomp.native.hybrid_composer`](../features/x86decomp-native-hybrid-composer.md) | 59 | Verify verify for the current toolkit workflow. |
| function | `rva_to_file_offset` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 16 | Execute the rva to file offset operation for the current toolkit workflow. |
| function | `extract_candidate` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 27 | Extract candidate for the current toolkit workflow. |
| function | `compare_function_bytes` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 36 | Compare function bytes for the current toolkit workflow. |
| class | `FunctionMatching` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 81 | Coordinate function matching behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 83 | Initialize the instance with validated constructor state. |
| function | `batch` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 87 | Execute the batch operation for the current toolkit workflow. |
| function | `report` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 153 | Execute the report operation for the current toolkit workflow. |
| function | `mismatches` | [`x86decomp.native.matching`](../features/x86decomp-native-matching.md) | 164 | Execute the mismatches operation for the current toolkit workflow. |
| function | `_section_header_records` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 19 | Support section header records processing for internal toolkit callers. |
| function | `plan_patch` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 39 | Execute the plan patch operation for the current toolkit workflow. |
| function | `apply_operations` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 57 | Execute the apply operations operation for the current toolkit workflow. |
| class | `PEReconstruction` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 68 | Coordinate p e reconstruction behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 70 | Initialize the instance with validated constructor state. |
| function | `inventory` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 74 | Execute the inventory operation for the current toolkit workflow. |
| function | `export_sections` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 79 | Execute the export sections operation for the current toolkit workflow. |
| function | `export_coff` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 94 | Execute the export coff operation for the current toolkit workflow. |
| function | `create_plan` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 108 | Create plan for the current toolkit workflow. |
| function | `apply_plan` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 116 | Execute the apply plan operation for the current toolkit workflow. |
| function | `text_swap` | [`x86decomp.native.pe_reconstruction`](../features/x86decomp-native-pe-reconstruction.md) | 128 | Execute the text swap operation for the current toolkit workflow. |
| class | `RuntimeValidation` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 15 | Coordinate runtime validation behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 17 | Initialize the instance with validated constructor state. |
| function | `validate_image` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 21 | Validate image for the current toolkit workflow. |
| function | `launch` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 34 | Execute the launch operation for the current toolkit workflow. |
| function | `map_crash` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 50 | Execute the map crash operation for the current toolkit workflow. |
| function | `_record` | [`x86decomp.native.runtime`](../features/x86decomp-native-runtime.md) | 57 | Support record processing for internal toolkit callers. |
| function | `_int` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 13 | Support int processing for internal toolkit callers. |
| function | `inventory_from_project` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 25 | Execute the inventory from project operation for the current toolkit workflow. |
| class | `FunctionSlots` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 49 | Coordinate function slots behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 51 | Initialize the instance with validated constructor state. |
| function | `audit` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 56 | Audit audit for the current toolkit workflow. |
| function | `audit_project` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 129 | Audit project for the current toolkit workflow. |
| function | `list` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 141 | Execute the list operation for the current toolkit workflow. |
| function | `show` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 151 | Execute the show operation for the current toolkit workflow. |
| function | `export_fixes` | [`x86decomp.native.slots`](../features/x86decomp-native-slots.md) | 162 | Execute the export fixes operation for the current toolkit workflow. |
| class | `StagingBridge` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 26 | Coordinate staging bridge behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 28 | Initialize the instance with validated constructor state. |
| function | `scan` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 32 | Execute the scan operation for the current toolkit workflow. |
| function | `generate_context` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 45 | Generate context for the current toolkit workflow. |
| function | `resolve` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 65 | Resolve resolve for the current toolkit workflow. |
| function | `unresolved` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 77 | Execute the unresolved operation for the current toolkit workflow. |
| function | `compile_check` | [`x86decomp.native.staging`](../features/x86decomp-native-staging.md) | 81 | Execute the compile check operation for the current toolkit workflow. |
| class | `NativeStore` | [`x86decomp.native.store`](../features/x86decomp-native-store.md) | 74 | Native-PE reconstruction schema layered on current reconstruction data. |
| function | `initialize` | [`x86decomp.native.store`](../features/x86decomp-native-store.md) | 77 | Initialize initialize for the current toolkit workflow. |
| function | `check` | [`x86decomp.native.store`](../features/x86decomp-native-store.md) | 95 | Check check for the current toolkit workflow. |
| function | `decode` | [`x86decomp.native.store`](../features/x86decomp-native-store.md) | 123 | Decode configured JSON columns from a SQLite row. |
| function | `discover_ghidra_launcher` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 14 | Discover ghidra launcher for the current toolkit workflow. |
| function | `write_response_file` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 30 | Write response file for the current toolkit workflow. |
| function | `quote` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 33 | Execute the quote operation for the current toolkit workflow. |
| class | `WindowsTools` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 41 | Coordinate windows tools behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 43 | Initialize the instance with validated constructor state. |
| function | `doctor` | [`x86decomp.native.windows_tools`](../features/x86decomp-native-windows-tools.md) | 47 | Execute the doctor operation for the current toolkit workflow. |
| function | `_resolve_executable` | [`x86decomp.objdiff_adapter`](../features/x86decomp-objdiff-adapter.md) | 24 | Support resolve executable processing for internal toolkit callers. |
| function | `run_objdiff_manifest` | [`x86decomp.objdiff_adapter`](../features/x86decomp-objdiff-adapter.md) | 39 | Run objdiff manifest for the current toolkit workflow. |
| class | `JobState` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 32 | Coordinate job state behavior for the current toolkit workflow. |
| class | `PipelineStage` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 87 | Store validated pipeline stage fields used by toolkit reports and adapters. |
| function | `from_dict` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 102 | Execute the from dict operation for the current toolkit workflow. |
| function | `strings` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 112 | Execute the strings operation for the current toolkit workflow. |
| class | `PipelineManifest` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 157 | Store validated pipeline manifest fields used by toolkit reports and adapters. |
| function | `load` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 164 | Load load for the current toolkit workflow. |
| class | `Orchestrator` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 193 | Coordinate orchestrator behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 195 | Initialize the instance with validated constructor state. |
| function | `close` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 226 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 230 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 234 | Exit the managed runtime context and release owned resources. |
| function | `_transaction` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 238 | Support transaction processing for internal toolkit callers. |
| function | `register` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 242 | Execute the register operation for the current toolkit workflow. |
| function | `_idempotency_key` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 284 | Support idempotency key processing for internal toolkit callers. |
| function | `_event` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 309 | Support event processing for internal toolkit callers. |
| function | `_completed_result_is_intact` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 316 | Verify materialized outputs before reusing a succeeded job. |
| function | `_materialize_outputs` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 341 | Support materialize outputs processing for internal toolkit callers. |
| function | `_dependency_states` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 376 | Support dependency states processing for internal toolkit callers. |
| function | `run` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 387 | Run run for the current toolkit workflow. |
| function | `_set_state` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 420 | Support set state processing for internal toolkit callers. |
| function | `_run_stage` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 436 | Support run stage processing for internal toolkit callers. |
| function | `cancellation_requested` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 515 | Execute the cancellation requested operation for the current toolkit workflow. |
| function | `recover_stale_jobs` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 547 | Reset only RUNNING jobs whose durable heartbeat is older than the bound. |
| function | `cancel` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 592 | Execute the cancel operation for the current toolkit workflow. |
| function | `retry` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 612 | Execute the retry operation for the current toolkit workflow. |
| function | `_update_pipeline_status` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 638 | Support update pipeline status processing for internal toolkit callers. |
| function | `status` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 655 | Execute the status operation for the current toolkit workflow. |
| function | `create_default_pipeline` | [`x86decomp.orchestrator`](../features/x86decomp-orchestrator.md) | 687 | Generate a concrete pipeline for the current project. |
| function | `_checksum_offset` | [`x86decomp.patching`](../features/x86decomp-patching.md) | 15 | Support checksum offset processing for internal toolkit callers. |
| function | `calculate_pe_checksum` | [`x86decomp.patching`](../features/x86decomp-patching.md) | 25 | Execute the calculate pe checksum operation for the current toolkit workflow. |
| function | `patch_pe_function` | [`x86decomp.patching`](../features/x86decomp-patching.md) | 41 | Execute the patch pe function operation for the current toolkit workflow. |
| function | `_require` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 29 | Support require processing for internal toolkit callers. |
| function | `_u16` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 35 | Support u16 processing for internal toolkit callers. |
| function | `_u32` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 41 | Support u32 processing for internal toolkit callers. |
| function | `_cstring` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 47 | Support cstring processing for internal toolkit callers. |
| function | `_align4` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 57 | Support align4 processing for internal toolkit callers. |
| class | `PDBStream` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 63 | Store validated p d b stream fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 70 | Return a serializable dictionary representation. |
| class | `PDBFile` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 81 | Store validated p d b file fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 97 | Return a serializable dictionary representation. |
| class | `_MSF` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 129 | Coordinate m s f behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 131 | Initialize the instance with validated constructor state. |
| function | `_block` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 159 | Support block processing for internal toolkit callers. |
| function | `_parse_directory` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 166 | Support parse directory processing for internal toolkit callers. |
| function | `stream` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 199 | Execute the stream operation for the current toolkit workflow. |
| function | `_parse_info` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 209 | Support parse info processing for internal toolkit callers. |
| function | `_parse_tpi` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 228 | Support parse tpi processing for internal toolkit callers. |
| function | `_parse_modules` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 276 | Support parse modules processing for internal toolkit callers. |
| function | `_parse_source_info` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 341 | Support parse source info processing for internal toolkit callers. |
| function | `_parse_section_contributions` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 390 | Support parse section contributions processing for internal toolkit callers. |
| function | `_parse_section_map` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 421 | Support parse section map processing for internal toolkit callers. |
| function | `_parse_dbi` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 453 | Support parse dbi processing for internal toolkit callers. |
| function | `_correlate_pe` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 566 | Support correlate pe processing for internal toolkit callers. |
| function | `parse_pdb_bytes` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 598 | Parse pdb bytes for the current toolkit workflow. |
| function | `parse_pdb` | [`x86decomp.pdb`](../features/x86decomp-pdb.md) | 635 | Parse pdb for the current toolkit workflow. |
| class | `TLS64Info` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 43 | Store validated t l s64 info fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 53 | Return a serializable dictionary representation. |
| class | `RuntimeFunction` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 67 | Store validated runtime function fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 73 | Return a serializable dictionary representation. |
| class | `PE64Image` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 83 | Store validated p e64 image fields used by toolkit reports and adapters. |
| function | `entry_va` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 113 | Execute the entry va operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 117 | Return a serializable dictionary representation. |
| function | `_parse_imports64` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 158 | Support parse imports64 processing for internal toolkit callers. |
| function | `_parse_tls64` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 192 | Support parse tls64 processing for internal toolkit callers. |
| function | `_parse_delay_imports64` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 214 | Support parse delay imports64 processing for internal toolkit callers. |
| function | `to_rva` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 227 | Execute the to rva operation for the current toolkit workflow. |
| function | `_parse_load_config64` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 258 | Support parse load config64 processing for internal toolkit callers. |
| function | `_parse_runtime_functions` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 274 | Support parse runtime functions processing for internal toolkit callers. |
| function | `parse_pe64` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 285 | Parse pe64 for the current toolkit workflow. |
| function | `inspect_pe_kind` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 361 | Execute the inspect pe kind operation for the current toolkit workflow. |
| function | `parse_pe` | [`x86decomp.pe`](../features/x86decomp-pe.md) | 374 | Parse pe for the current toolkit workflow. |
| class | `DataDirectory` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 43 | Store validated data directory fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 49 | Return a serializable dictionary representation. |
| class | `Section` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 55 | Store validated section fields used by toolkit reports and adapters. |
| function | `mapped_size` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 66 | Execute the mapped size operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 70 | Return a serializable dictionary representation. |
| class | `ImportSymbol` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 86 | Store validated import symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 94 | Return a serializable dictionary representation. |
| class | `ImportLibrary` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 106 | Store validated import library fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 111 | Return a serializable dictionary representation. |
| class | `ExportSymbol` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 117 | Store validated export symbol fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 124 | Return a serializable dictionary representation. |
| class | `BaseRelocation` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 136 | Store validated base relocation fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 141 | Return a serializable dictionary representation. |
| class | `DebugRecord` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 147 | Store validated debug record fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 158 | Return a serializable dictionary representation. |
| class | `TLSInfo` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 173 | Store validated t l s info fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 183 | Return a serializable dictionary representation. |
| class | `ResourceLeaf` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 199 | Store validated resource leaf fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 207 | Return a serializable dictionary representation. |
| class | `DelayImportLibrary` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 220 | Store validated delay import library fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 227 | Return a serializable dictionary representation. |
| class | `LoadConfigInfo` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 238 | Store validated load config info fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 255 | Return a serializable dictionary representation. |
| class | `PE32Image` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 276 | Store validated p e32 image fields used by toolkit reports and adapters. |
| function | `entry_va` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 305 | Execute the entry va operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 309 | Return a serializable dictionary representation. |
| function | `_rva_to_offset` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 351 | Support rva to offset processing for internal toolkit callers. |
| function | `_directory` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 373 | Support directory processing for internal toolkit callers. |
| function | `_parse_imports` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 381 | Support parse imports processing for internal toolkit callers. |
| function | `_parse_exports` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 454 | Support parse exports processing for internal toolkit callers. |
| function | `_parse_relocations` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 521 | Support parse relocations processing for internal toolkit callers. |
| function | `_parse_debug_records` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 555 | Support parse debug records processing for internal toolkit callers. |
| function | `_parse_tls` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 617 | Support parse tls processing for internal toolkit callers. |
| function | `_parse_resources` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 664 | Support parse resources processing for internal toolkit callers. |
| function | `read_name` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 680 | Read name for the current toolkit workflow. |
| function | `walk` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 690 | Execute the walk operation for the current toolkit workflow. |
| function | `_parse_delay_imports` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 732 | Support parse delay imports processing for internal toolkit callers. |
| function | `to_rva` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 753 | Execute the to rva operation for the current toolkit workflow. |
| function | `_parse_load_config` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 793 | Support parse load config processing for internal toolkit callers. |
| function | `parse_pe32` | [`x86decomp.pe32`](../features/x86decomp-pe32.md) | 826 | Parse pe32 for the current toolkit workflow. |
| function | `initialize_project` | [`x86decomp.project`](../features/x86decomp-project.md) | 61 | Initialize project for the current toolkit workflow. |
| function | `_resolve_binary_path` | [`x86decomp.project`](../features/x86decomp-project.md) | 152 | Support resolve binary path processing for internal toolkit callers. |
| function | `verify_project` | [`x86decomp.project`](../features/x86decomp-project.md) | 166 | Verify project for the current toolkit workflow. |
| function | `require_valid_project` | [`x86decomp.project`](../features/x86decomp-project.md) | 226 | Execute the require valid project operation for the current toolkit workflow. |
| class | `ProjectCheck` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 70 | Store validated project check fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 78 | Return a serializable dictionary representation. |
| class | `ProjectStateDatabase` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 89 | Coordinate project state database behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 91 | Initialize the instance with validated constructor state. |
| function | `close` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 109 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 113 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 117 | Exit the managed runtime context and release owned resources. |
| function | `transaction` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 122 | Execute the transaction operation for the current toolkit workflow. |
| function | `integrity_check` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 133 | Execute the integrity check operation for the current toolkit workflow. |
| function | `record_migration` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 138 | Record migration for the current toolkit workflow. |
| function | `snapshot` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 159 | Execute the snapshot operation for the current toolkit workflow. |
| function | `upsert_artifact_reference` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 181 | Execute the upsert artifact reference operation for the current toolkit workflow. |
| function | `artifact_digests` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 190 | Execute the artifact digests operation for the current toolkit workflow. |
| function | `state_database_path` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 195 | Execute the state database path operation for the current toolkit workflow. |
| function | `create_project_backup` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 200 | Create a deterministic gzip tar backup without following symlinks. |
| function | `_migration_2_to_3` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 235 | Support migration 2 to 3 processing for internal toolkit callers. |
| function | `migrate_project` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 267 | Execute the migrate project operation for the current toolkit workflow. |
| function | `check_project_state` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 330 | Check project state for the current toolkit workflow. |
| function | `repair_project_state` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 370 | Repair only reconstructible indexes; never rewrite evidence or binaries. |
| function | `project_gc` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 400 | Execute the project gc operation for the current toolkit workflow. |
| function | `restore_project_backup` | [`x86decomp.project_state`](../features/x86decomp-project-state.md) | 407 | Safely restore a project backup into an empty destination. |
| function | `_artifact_roles` | [`x86decomp.project_template`](../features/x86decomp-project-template.md) | 20 | Support artifact roles processing for internal toolkit callers. |
| function | `derive_template_contract` | [`x86decomp.project_template`](../features/x86decomp-project-template.md) | 25 | Derive a target project shape only from recorded facts and decisions. |
| function | `_write_project_helper` | [`x86decomp.project_template`](../features/x86decomp-project-template.md) | 88 | Support write project helper processing for internal toolkit callers. |
| function | `materialize_project_template` | [`x86decomp.project_template`](../features/x86decomp-project-template.md) | 133 | Create a deterministic, non-fabricated project working layout. |
| class | `ABIContracts` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 11 | Coordinate a b i contracts behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 13 | Initialize the instance with validated constructor state. |
| function | `recover` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 16 | Execute the recover operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 32 | Execute the get operation for the current toolkit workflow. |
| function | `verify` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 37 | Verify verify for the current toolkit workflow. |
| function | `compare` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 44 | Compare compare for the current toolkit workflow. |
| function | `export` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 48 | Execute the export operation for the current toolkit workflow. |
| function | `shim` | [`x86decomp.reconstruction.abi_contracts`](../features/x86decomp-reconstruction-abi-contracts.md) | 51 | Execute the shim operation for the current toolkit workflow. |
| function | `_safe_rel` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 31 | Support safe rel processing for internal toolkit callers. |
| function | `_read_text_if_exists` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 42 | Support read text if exists processing for internal toolkit callers. |
| function | `_body_ranges` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 47 | Support body ranges processing for internal toolkit callers. |
| function | `_contiguous_single_range` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 62 | Support contiguous single range processing for internal toolkit callers. |
| function | `_read_range_bytes` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 73 | Support read range bytes processing for internal toolkit callers. |
| function | `_read_mnemonics` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 92 | Support read mnemonics processing for internal toolkit callers. |
| function | `_function_name` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 124 | Support function name processing for internal toolkit callers. |
| function | `llm_job_from_function_packet` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 133 | Create one local-LLM job from a verified function artifact directory. |
| function | `llm_job_from_range` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 219 | Create one local-LLM job from an explicitly supplied file offset/RVA range. |
| function | `llm_batch_create` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 293 | Execute the llm batch create operation for the current toolkit workflow. |
| function | `llm_batch_match` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 329 | Execute the llm batch match operation for the current toolkit workflow. |
| function | `candidate_promote` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 356 | Execute the candidate promote operation for the current toolkit workflow. |
| function | `source_map_annotate` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 386 | Execute the source map annotate operation for the current toolkit workflow. |
| function | `source_map_verify` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 405 | Execute the source map verify operation for the current toolkit workflow. |
| function | `module_assign` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 423 | Execute the module assign operation for the current toolkit workflow. |
| function | `module_suggest` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 435 | Execute the module suggest operation for the current toolkit workflow. |
| function | `type_propagate` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 454 | Emit a type-propagation plan without silently editing source files. |
| function | `header_synthesize_project` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 466 | Execute the header synthesize project operation for the current toolkit workflow. |
| function | `vtable_recover` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 486 | Execute the vtable recover operation for the current toolkit workflow. |
| function | `class_scaffold` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 492 | Execute the class scaffold operation for the current toolkit workflow. |
| function | `diff_explain` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 510 | Execute the diff explain operation for the current toolkit workflow. |
| function | `triage_next` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 525 | Execute the triage next operation for the current toolkit workflow. |
| function | `playability_smoke_plan` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 537 | Execute the playability smoke plan operation for the current toolkit workflow. |
| function | `asset_inventory` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 546 | Execute the asset inventory operation for the current toolkit workflow. |
| function | `mod_branch_init` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 558 | Execute the mod branch init operation for the current toolkit workflow. |
| function | `regression_compare` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 565 | Execute the regression compare operation for the current toolkit workflow. |
| function | `_json_out` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 599 | Support json out processing for internal toolkit callers. |
| function | `_read_any_text` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 606 | Support read any text processing for internal toolkit callers. |
| function | `_file_report` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 614 | Support file report processing for internal toolkit callers. |
| function | `function_discover` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 620 | Discover candidate function entry offsets using architecture profiles. |
| function | `function_boundary_reconcile` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 663 | Execute the function boundary reconcile operation for the current toolkit workflow. |
| function | `function_list_sort` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 686 | Execute the function list sort operation for the current toolkit workflow. |
| function | `sort_key` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 694 | Execute the sort key operation for the current toolkit workflow. |
| function | `function_list_classify` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 707 | Execute the function list classify operation for the current toolkit workflow. |
| function | `pattern_catalog` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 731 | Execute the pattern catalog operation for the current toolkit workflow. |
| function | `pattern_scan` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 737 | Execute the pattern scan operation for the current toolkit workflow. |
| function | `pattern_generate` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 763 | Execute the pattern generate operation for the current toolkit workflow. |
| function | `pattern_match` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 783 | Execute the pattern match operation for the current toolkit workflow. |
| function | `pattern_promote` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 794 | Execute the pattern promote operation for the current toolkit workflow. |
| function | `image_text_compose` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 802 | Execute the image text compose operation for the current toolkit workflow. |
| function | `_pe_section` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 850 | Support pe section processing for internal toolkit callers. |
| function | `text_swap_plan` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 872 | Execute the text swap plan operation for the current toolkit workflow. |
| function | `text_swap_inject` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 884 | Execute the text swap inject operation for the current toolkit workflow. |
| function | `text_swap_verify` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 908 | Execute the text swap verify operation for the current toolkit workflow. |
| function | `text_swap_build` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 920 | Execute the text swap build operation for the current toolkit workflow. |
| function | `progress_reconcile` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 929 | Execute the progress reconcile operation for the current toolkit workflow. |
| function | `project_health` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 949 | Execute the project health operation for the current toolkit workflow. |
| function | `source_stage_classify` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 962 | Execute the source stage classify operation for the current toolkit workflow. |
| function | `ghidra_mcp_probe` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 990 | Execute the ghidra mcp probe operation for the current toolkit workflow. |
| function | `_json_rpc` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1003 | Support json rpc processing for internal toolkit callers. |
| function | `ghidra_mcp_functions` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1011 | Execute the ghidra mcp functions operation for the current toolkit workflow. |
| function | `ghidra_mcp_decompile` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1018 | Execute the ghidra mcp decompile operation for the current toolkit workflow. |
| function | `ghidra_mcp_batch_decompile` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1025 | Execute the ghidra mcp batch decompile operation for the current toolkit workflow. |
| function | `ghidra_mcp_sync_names` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1040 | Execute the ghidra mcp sync names operation for the current toolkit workflow. |
| function | `compiler_rule_learn` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1052 | Execute the compiler rule learn operation for the current toolkit workflow. |
| function | `compiler_rule_report` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1062 | Execute the compiler rule report operation for the current toolkit workflow. |
| function | `compiler_compare_flags` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1069 | Execute the compiler compare flags operation for the current toolkit workflow. |
| function | `runtime_identify` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1079 | Run time identify for the current toolkit workflow. |
| function | `runtime_quarantine` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1093 | Run time quarantine for the current toolkit workflow. |
| function | `runtime_match_library` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1104 | Run time match library for the current toolkit workflow. |
| function | `subsystem_detect` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1111 | Execute the subsystem detect operation for the current toolkit workflow. |
| function | `state_machine_detect` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1126 | Execute the state machine detect operation for the current toolkit workflow. |
| function | `project_doctor_paths` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1140 | Execute the project doctor paths operation for the current toolkit workflow. |
| function | `script_port_audit` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1155 | Execute the script port audit operation for the current toolkit workflow. |
| function | `toolchain_hash_tree` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1171 | Execute the toolchain hash tree operation for the current toolkit workflow. |
| function | `toolchain_verify_local` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1179 | Execute the toolchain verify local operation for the current toolkit workflow. |
| function | `toolchain_redact_package` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1192 | Execute the toolchain redact package operation for the current toolkit workflow. |
| function | `decompiler_cleanup` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1207 | Execute the decompiler cleanup operation for the current toolkit workflow. |
| function | `candidate_search` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1229 | Execute the candidate search operation for the current toolkit workflow. |
| function | `release_goal_moddable_source` | [`x86decomp.reconstruction.acceleration`](../features/x86decomp-reconstruction-acceleration.md) | 1241 | Execute the release goal moddable source operation for the current toolkit workflow. |
| class | `BuildManager` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 11 | Coordinate build manager behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 13 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 16 | Create create for the current toolkit workflow. |
| function | `add_target` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 25 | Execute the add target operation for the current toolkit workflow. |
| function | `add_variant` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 34 | Execute the add variant operation for the current toolkit workflow. |
| function | `show` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 42 | Execute the show operation for the current toolkit workflow. |
| function | `show_target` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 49 | Execute the show target operation for the current toolkit workflow. |
| function | `show_variant` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 56 | Execute the show variant operation for the current toolkit workflow. |
| function | `generate` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 62 | Generate generate for the current toolkit workflow. |
| function | `validate` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 82 | Validate validate for the current toolkit workflow. |
| function | `compare_modes` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 93 | Compare modes for the current toolkit workflow. |
| function | `matrix` | [`x86decomp.reconstruction.builds`](../features/x86decomp-reconstruction-builds.md) | 98 | Execute the matrix operation for the current toolkit workflow. |
| class | `Capsules` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 12 | Coordinate capsules behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 14 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 17 | Create create for the current toolkit workflow. |
| function | `inspect` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 34 | Execute the inspect operation for the current toolkit workflow. |
| function | `verify` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 39 | Verify verify for the current toolkit workflow. |
| function | `reproduce` | [`x86decomp.reconstruction.capsules`](../features/x86decomp-reconstruction-capsules.md) | 54 | Execute the reproduce operation for the current toolkit workflow. |
| function | `_store` | [`x86decomp.reconstruction.cli`](../features/x86decomp-reconstruction-cli.md) | 56 | Open the project store requested by parsed command arguments. |
| function | `build_parser` | [`x86decomp.reconstruction.cli`](../features/x86decomp-reconstruction-cli.md) | 60 | Build the argparse parser for this command surface. |
| function | `dispatch` | [`x86decomp.reconstruction.cli`](../features/x86decomp-reconstruction-cli.md) | 273 | Dispatch parsed command arguments to the matching implementation. |
| function | `main` | [`x86decomp.reconstruction.cli`](../features/x86decomp-reconstruction-cli.md) | 451 | Run the command-line entry point and return its process status. |
| class | `GeneratedTests` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 9 | Coordinate generated tests behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 11 | Initialize the instance with validated constructor state. |
| function | `add` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 14 | Execute the add operation for the current toolkit workflow. |
| function | `synthesize` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 24 | Execute the synthesize operation for the current toolkit workflow. |
| function | `promote_counterexample` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 32 | Execute the promote counterexample operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 38 | Execute the get operation for the current toolkit workflow. |
| function | `list` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 43 | Execute the list operation for the current toolkit workflow. |
| function | `explain` | [`x86decomp.reconstruction.generated_tests`](../features/x86decomp-reconstruction-generated-tests.md) | 47 | Execute the explain operation for the current toolkit workflow. |
| class | `HeaderManager` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 10 | Coordinate header manager behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 12 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 15 | Create create for the current toolkit workflow. |
| function | `declare` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 25 | Execute the declare operation for the current toolkit workflow. |
| function | `include` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 36 | Execute the include operation for the current toolkit workflow. |
| function | `cycles` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 44 | Execute the cycles operation for the current toolkit workflow. |
| function | `visit` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 54 | Execute the visit operation for the current toolkit workflow. |
| function | `show` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 64 | Execute the show operation for the current toolkit workflow. |
| function | `synthesize` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 72 | Execute the synthesize operation for the current toolkit workflow. |
| function | `validate` | [`x86decomp.reconstruction.headers`](../features/x86decomp-reconstruction-headers.md) | 84 | Validate validate for the current toolkit workflow. |
| class | `LibraryRecognition` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 8 | Coordinate library recognition behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 10 | Initialize the instance with validated constructor state. |
| function | `identify` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 13 | Execute the identify operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 21 | Execute the get operation for the current toolkit workflow. |
| function | `candidates` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 26 | Execute the candidates operation for the current toolkit workflow. |
| function | `disposition` | [`x86decomp.reconstruction.libraries`](../features/x86decomp-reconstruction-libraries.md) | 30 | Execute the disposition operation for the current toolkit workflow. |
| class | `ProjectLayout` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 11 | Coordinate project layout behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 13 | Initialize the instance with validated constructor state. |
| function | `create_module` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 17 | Create module for the current toolkit workflow. |
| function | `add_member` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 28 | Execute the add member operation for the current toolkit workflow. |
| function | `create_translation_unit` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 38 | Create translation unit for the current toolkit workflow. |
| function | `add_translation_unit_member` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 51 | Execute the add translation unit member operation for the current toolkit workflow. |
| function | `synthesize` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 61 | Deterministically group inventory records by explicit object/library/source hints. |
| function | `show_module` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 80 | Execute the show module operation for the current toolkit workflow. |
| function | `show_translation_unit` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 89 | Execute the show translation unit operation for the current toolkit workflow. |
| function | `list_modules` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 98 | Execute the list modules operation for the current toolkit workflow. |
| function | `explain_boundaries` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 103 | Execute the explain boundaries operation for the current toolkit workflow. |
| function | `export` | [`x86decomp.reconstruction.project_layout`](../features/x86decomp-reconstruction-project-layout.md) | 108 | Execute the export operation for the current toolkit workflow. |
| class | `ProvenanceLedger` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 11 | Coordinate provenance ledger behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 13 | Initialize the instance with validated constructor state. |
| function | `record` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 16 | Record record for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 27 | Execute the get operation for the current toolkit workflow. |
| function | `source` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 32 | Execute the source operation for the current toolkit workflow. |
| function | `binary` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 39 | Execute the binary operation for the current toolkit workflow. |
| function | `lock` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 45 | Execute the lock operation for the current toolkit workflow. |
| function | `unlock` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 52 | Execute the unlock operation for the current toolkit workflow. |
| function | `reconcile` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 58 | Execute the reconcile operation for the current toolkit workflow. |
| function | `impact` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 74 | Execute the impact operation for the current toolkit workflow. |
| function | `export` | [`x86decomp.reconstruction.provenance`](../features/x86decomp-reconstruction-provenance.md) | 78 | Execute the export operation for the current toolkit workflow. |
| class | `SecurityReview` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 9 | Coordinate security review behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 11 | Initialize the instance with validated constructor state. |
| function | `finding` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 14 | Execute the finding operation for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 22 | Execute the get operation for the current toolkit workflow. |
| function | `scan` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 27 | Execute the scan operation for the current toolkit workflow. |
| function | `policy` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 35 | Execute the policy operation for the current toolkit workflow. |
| function | `report` | [`x86decomp.reconstruction.security`](../features/x86decomp-reconstruction-security.md) | 41 | Execute the report operation for the current toolkit workflow. |
| class | `SemanticChangeSets` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 9 | Coordinate semantic change sets behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 11 | Initialize the instance with validated constructor state. |
| function | `create` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 14 | Create create for the current toolkit workflow. |
| function | `get` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 20 | Execute the get operation for the current toolkit workflow. |
| function | `add_operation` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 27 | Execute the add operation operation for the current toolkit workflow. |
| function | `merge` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 37 | Execute the merge operation for the current toolkit workflow. |
| function | `conflicts` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 51 | Execute the conflicts operation for the current toolkit workflow. |
| function | `verify` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 54 | Verify verify for the current toolkit workflow. |
| function | `rebase` | [`x86decomp.reconstruction.semantic_changesets`](../features/x86decomp-reconstruction-semantic-changesets.md) | 58 | Execute the rebase operation for the current toolkit workflow. |
| class | `ReconstructionStore` | [`x86decomp.reconstruction.store`](../features/x86decomp-reconstruction-store.md) | 141 | Project-scale schema layered on the governance store. |
| function | `initialize` | [`x86decomp.reconstruction.store`](../features/x86decomp-reconstruction-store.md) | 144 | Initialize initialize for the current toolkit workflow. |
| function | `check` | [`x86decomp.reconstruction.store`](../features/x86decomp-reconstruction-store.md) | 155 | Check check for the current toolkit workflow. |
| function | `decode` | [`x86decomp.reconstruction.store`](../features/x86decomp-reconstruction-store.md) | 173 | Decode configured JSON columns from a SQLite row. |
| function | `_workflow_gate` | [`x86decomp.release_gate`](../features/x86decomp-release-gate.md) | 31 | Support workflow gate processing for internal toolkit callers. |
| function | `_claim_gate` | [`x86decomp.release_gate`](../features/x86decomp-release-gate.md) | 65 | Support claim gate processing for internal toolkit callers. |
| function | `_pipeline_gate` | [`x86decomp.release_gate`](../features/x86decomp-release-gate.md) | 79 | Support pipeline gate processing for internal toolkit callers. |
| function | `evaluate_release_gate` | [`x86decomp.release_gate`](../features/x86decomp-release-gate.md) | 94 | Execute the evaluate release gate operation for the current toolkit workflow. |
| function | `run_full_relink` | [`x86decomp.relink`](../features/x86decomp-relink.md) | 23 | Run full relink for the current toolkit workflow. |
| function | `_version` | [`x86decomp.reproducibility`](../features/x86decomp-reproducibility.md) | 24 | Support version processing for internal toolkit callers. |
| function | `build_reproduction_manifest` | [`x86decomp.reproducibility`](../features/x86decomp-reproducibility.md) | 51 | Build reproduction manifest for the current toolkit workflow. |
| function | `verify_reproduction_manifest` | [`x86decomp.reproducibility`](../features/x86decomp-reproducibility.md) | 120 | Verify reproduction manifest for the current toolkit workflow. |
| function | `_secret_findings` | [`x86decomp.security_audit`](../features/x86decomp-security-audit.md) | 30 | Support secret findings processing for internal toolkit callers. |
| function | `generate_sbom` | [`x86decomp.security_audit`](../features/x86decomp-security-audit.md) | 44 | Generate sbom for the current toolkit workflow. |
| function | `audit_source_tree` | [`x86decomp.security_audit`](../features/x86decomp-security-audit.md) | 80 | Audit source tree for the current toolkit workflow. |
| function | `verify_release_manifest` | [`x86decomp.security_audit`](../features/x86decomp-security-audit.md) | 136 | Verify release manifest for the current toolkit workflow. |
| function | `run_dependency_vulnerability_audit` | [`x86decomp.security_audit`](../features/x86decomp-security-audit.md) | 168 | Run an installed pip-audit executable and preserve its exact findings. |
| function | `_json_files` | [`x86decomp.service`](../features/x86decomp-service.md) | 24 | Support json files processing for internal toolkit callers. |
| function | `service_snapshot` | [`x86decomp.service`](../features/x86decomp-service.md) | 39 | Return a read-only, serializable project-control-plane snapshot. |
| function | `create_app` | [`x86decomp.service`](../features/x86decomp-service.md) | 78 | Create app for the current toolkit workflow. |
| function | `health` | [`x86decomp.service`](../features/x86decomp-service.md) | 89 | Execute the health operation for the current toolkit workflow. |
| function | `project` | [`x86decomp.service`](../features/x86decomp-service.md) | 100 | Execute the project operation for the current toolkit workflow. |
| function | `target_pack` | [`x86decomp.service`](../features/x86decomp-service.md) | 105 | Execute the target pack operation for the current toolkit workflow. |
| function | `pipelines` | [`x86decomp.service`](../features/x86decomp-service.md) | 117 | Execute the pipelines operation for the current toolkit workflow. |
| function | `convergence` | [`x86decomp.service`](../features/x86decomp-service.md) | 122 | Execute the convergence operation for the current toolkit workflow. |
| function | `reproducibility` | [`x86decomp.service`](../features/x86decomp-service.md) | 127 | Execute the reproducibility operation for the current toolkit workflow. |
| function | `security` | [`x86decomp.service`](../features/x86decomp-service.md) | 132 | Execute the security operation for the current toolkit workflow. |
| function | `functions` | [`x86decomp.service`](../features/x86decomp-service.md) | 137 | Execute the functions operation for the current toolkit workflow. |
| function | `workflow` | [`x86decomp.service`](../features/x86decomp-service.md) | 151 | Execute the workflow operation for the current toolkit workflow. |
| function | `next_task` | [`x86decomp.service`](../features/x86decomp-service.md) | 160 | Execute the next task operation for the current toolkit workflow. |
| function | `reports` | [`x86decomp.service`](../features/x86decomp-service.md) | 169 | Execute the reports operation for the current toolkit workflow. |
| function | `index` | [`x86decomp.service`](../features/x86decomp-service.md) | 174 | Return the read-only browser UI without injecting project data as HTML. |
| function | `run_service` | [`x86decomp.service`](../features/x86decomp-service.md) | 200 | Run service for the current toolkit workflow. |
| function | `decode_json_fields` | [`x86decomp.store_utils`](../features/x86decomp-store-utils.md) | 8 | Return a row dictionary with selected ``*_json`` columns decoded. |
| function | `_deps` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 18 | Support deps processing for internal toolkit callers. |
| class | `UnsupportedSymbolicInstruction` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 31 | Coordinate unsupported symbolic instruction behavior for the current toolkit workflow. |
| class | `SymState` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 37 | Store validated sym state fields used by toolkit reports and adapters. |
| function | `clone` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 46 | Execute the clone operation for the current toolkit workflow. |
| class | `Outcome` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 59 | Store validated outcome fields used by toolkit reports and adapters. |
| function | `_aliases` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 93 | Support aliases processing for internal toolkit callers. |
| function | `_read_reg` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 98 | Support read reg processing for internal toolkit callers. |
| function | `_write_reg` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 111 | Support write reg processing for internal toolkit callers. |
| function | `_concrete` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 133 | Support concrete processing for internal toolkit callers. |
| function | `_memory_address` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 139 | Support memory address processing for internal toolkit callers. |
| function | `_read_memory` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 159 | Support read memory processing for internal toolkit callers. |
| function | `_write_memory` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 171 | Support write memory processing for internal toolkit callers. |
| function | `_read_operand` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 183 | Support read operand processing for internal toolkit callers. |
| function | `_write_operand` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 196 | Support write operand processing for internal toolkit callers. |
| function | `_coerce_pair` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 209 | Support coerce pair processing for internal toolkit callers. |
| function | `_set_logic_flags` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 219 | Support set logic flags processing for internal toolkit callers. |
| function | `_set_add_flags` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 227 | Support set add flags processing for internal toolkit callers. |
| function | `_set_sub_flags` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 240 | Support set sub flags processing for internal toolkit callers. |
| function | `_condition` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 253 | Support condition processing for internal toolkit callers. |
| function | `_condition_for_family` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 273 | Resolve Jcc, SETcc, and CMOVcc names through the same flag model. |
| function | `_set_adc_flags` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 297 | Support set adc flags processing for internal toolkit callers. |
| function | `_set_sbb_flags` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 314 | Support set sbb flags processing for internal toolkit callers. |
| function | `_is_sat` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 330 | Support is sat processing for internal toolkit callers. |
| function | `symbolic_execute` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 337 | Execute the symbolic execute operation for the current toolkit workflow. |
| function | `_constraint_formula` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 624 | Support constraint formula processing for internal toolkit callers. |
| function | `bounded_symbolic_compare` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 629 | Execute the bounded symbolic compare operation for the current toolkit workflow. |
| function | `bounded_symbolic_compare_files` | [`x86decomp.symbolic`](../features/x86decomp-symbolic.md) | 709 | Execute the bounded symbolic compare files operation for the current toolkit workflow. |
| function | `_symbol` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 25 | Support symbol processing for internal toolkit callers. |
| function | `_c_arithmetic` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 35 | Support c arithmetic processing for internal toolkit callers. |
| function | `_c_branches` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 49 | Support c branches processing for internal toolkit callers. |
| function | `_c_loop` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 66 | Support c loop processing for internal toolkit callers. |
| function | `_c_switch` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 84 | Support c switch processing for internal toolkit callers. |
| function | `_c_struct_alias` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 100 | Support c struct alias processing for internal toolkit callers. |
| function | `_c_bitfield` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 124 | Support c bitfield processing for internal toolkit callers. |
| function | `_c_float` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 144 | Support c float processing for internal toolkit callers. |
| function | `_c_indirect` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 158 | Support c indirect processing for internal toolkit callers. |
| function | `_cpp_virtual` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 170 | Support cpp virtual processing for internal toolkit callers. |
| function | `_cpp_multiple_inheritance` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 194 | Support cpp multiple inheritance processing for internal toolkit callers. |
| function | `_cpp_exception` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 211 | Support cpp exception processing for internal toolkit callers. |
| function | `_cpp_template` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 228 | Support cpp template processing for internal toolkit callers. |
| function | `generate_synthetic_corpus` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 256 | Generate deterministic source cases and a compiler-corpus input manifest. |
| function | `verify_synthetic_corpus` | [`x86decomp.synthetic_corpus`](../features/x86decomp-synthetic-corpus.md) | 344 | Verify synthetic corpus for the current toolkit workflow. |
| class | `SupportingArtifact` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 30 | Store validated supporting artifact fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 37 | Return a serializable dictionary representation. |
| function | `_toml_string` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 42 | Support toml string processing for internal toolkit callers. |
| function | `_write_target_toml` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 47 | Support write target toml processing for internal toolkit callers. |
| function | `_safe_artifact` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 90 | Support safe artifact processing for internal toolkit callers. |
| function | `infer_target_pack` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 98 | Execute the infer target pack operation for the current toolkit workflow. |
| function | `load_target_pack` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 308 | Load target pack for the current toolkit workflow. |
| function | `verify_target_pack` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 320 | Verify target pack for the current toolkit workflow. |
| function | `generate_project_from_target_pack` | [`x86decomp.target_pack`](../features/x86decomp-target-pack.md) | 351 | Generate project from target pack for the current toolkit workflow. |
| class | `BundleLimits` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 49 | Store validated bundle limits fields used by toolkit reports and adapters. |
| function | `_safe_member_path` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 57 | Support safe member path processing for internal toolkit callers. |
| function | `_is_symlink` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 71 | Support is symlink processing for internal toolkit callers. |
| function | `_validate_archive_infos` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 77 | Support validate archive infos processing for internal toolkit callers. |
| function | `_extract_safely` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 107 | Support extract safely processing for internal toolkit callers. |
| function | `_manifest_artifacts` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 139 | Support manifest artifacts processing for internal toolkit callers. |
| function | `_single_role` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 193 | Support single role processing for internal toolkit callers. |
| function | `create_test_bundle` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 201 | Create a deterministic authorized static test bundle. |
| function | `inspect_test_bundle` | [`x86decomp.test_bundle`](../features/x86decomp-test-bundle.md) | 288 | Verify and statically inspect a test bundle without executing its contents. |
| function | `register_toolchain` | [`x86decomp.toolchains`](../features/x86decomp-toolchains.md) | 12 | Execute the register toolchain operation for the current toolkit workflow. |
| function | `verify_toolchain` | [`x86decomp.toolchains`](../features/x86decomp-toolchains.md) | 47 | Verify toolchain for the current toolkit workflow. |
| function | `_capture` | [`x86decomp.tools`](../features/x86decomp-tools.md) | 22 | Support capture processing for internal toolkit callers. |
| function | `discover_analyze_headless` | [`x86decomp.tools`](../features/x86decomp-tools.md) | 40 | Discover analyze headless for the current toolkit workflow. |
| function | `snapshot_tools` | [`x86decomp.tools`](../features/x86decomp-tools.md) | 61 | Execute the snapshot tools operation for the current toolkit workflow. |
| function | `utc_now` | [`x86decomp.util`](../features/x86decomp-util.md) | 17 | Return a stable RFC 3339 UTC timestamp. |
| function | `sha256_bytes` | [`x86decomp.util`](../features/x86decomp-util.md) | 22 | Execute the sha256 bytes operation for the current toolkit workflow. |
| function | `sha256_file` | [`x86decomp.util`](../features/x86decomp-util.md) | 27 | Execute the sha256 file operation for the current toolkit workflow. |
| function | `canonical_json_bytes` | [`x86decomp.util`](../features/x86decomp-util.md) | 36 | Execute the canonical json bytes operation for the current toolkit workflow. |
| function | `load_json` | [`x86decomp.util`](../features/x86decomp-util.md) | 43 | Load and parse JSON content from a filesystem path. |
| function | `atomic_write_bytes` | [`x86decomp.util`](../features/x86decomp-util.md) | 49 | Execute the atomic write bytes operation for the current toolkit workflow. |
| function | `atomic_write_text` | [`x86decomp.util`](../features/x86decomp-util.md) | 66 | Execute the atomic write text operation for the current toolkit workflow. |
| function | `write_json` | [`x86decomp.util`](../features/x86decomp-util.md) | 71 | Write json for the current toolkit workflow. |
| function | `copy_file_atomic` | [`x86decomp.util`](../features/x86decomp-util.md) | 77 | Execute the copy file atomic operation for the current toolkit workflow. |
| function | `ensure_relative_path` | [`x86decomp.util`](../features/x86decomp-util.md) | 92 | Resolve candidate and reject paths that escape root. |
| function | `require_mapping` | [`x86decomp.util`](../features/x86decomp-util.md) | 103 | Execute the require mapping operation for the current toolkit workflow. |
| function | `require_string` | [`x86decomp.util`](../features/x86decomp-util.md) | 110 | Execute the require string operation for the current toolkit workflow. |
| function | `require_int` | [`x86decomp.util`](../features/x86decomp-util.md) | 118 | Execute the require int operation for the current toolkit workflow. |
| class | `WorkQueue` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 35 | Coordinate work queue behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 37 | Initialize the instance with validated constructor state. |
| function | `close` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 45 | Execute the close operation for the current toolkit workflow. |
| function | `create` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 49 | Create create for the current toolkit workflow. |
| function | `get` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 73 | Execute the get operation for the current toolkit workflow. |
| function | `claim` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 84 | Execute the claim operation for the current toolkit workflow. |
| function | `propose` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 94 | Execute the propose operation for the current toolkit workflow. |
| function | `record_validator` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 107 | Record validator for the current toolkit workflow. |
| function | `next` | [`x86decomp.work_queue`](../features/x86decomp-work-queue.md) | 122 | Execute the next operation for the current toolkit workflow. |
| class | `WorkerLimits` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 27 | Store validated worker limits fields used by toolkit reports and adapters. |
| function | `validate` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 35 | Validate validate for the current toolkit workflow. |
| class | `WorkerRequest` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 43 | Store validated worker request fields used by toolkit reports and adapters. |
| class | `WorkerResult` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 56 | Store validated worker result fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 73 | Return a serializable dictionary representation. |
| function | `discover_worker_capabilities` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 94 | Discover worker capabilities for the current toolkit workflow. |
| function | `_bounded_environment` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 109 | Support bounded environment processing for internal toolkit callers. |
| function | `_preexec` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 145 | Return the legacy resource-limit callback for API compatibility. |
| function | `apply` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 156 | Execute the apply operation for the current toolkit workflow. |
| function | `_confined_paths` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 172 | Support confined paths processing for internal toolkit callers. |
| function | `_container_command` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 189 | Support container command processing for internal toolkit callers. |
| function | `execute_worker_request` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 215 | Execute the execute worker request operation for the current toolkit workflow. |
| function | `resource_wrapped_command` | [`x86decomp.worker`](../features/x86decomp-worker.md) | 253 | Execute the resource wrapped command operation for the current toolkit workflow. |
| class | `DecompilationMode` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 21 | Coordinate decompilation mode behavior for the current toolkit workflow. |
| class | `SourceStage` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 27 | Coordinate source stage behavior for the current toolkit workflow. |
| class | `MatchingStatus` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 36 | Coordinate matching status behavior for the current toolkit workflow. |
| class | `FunctionalStatus` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 49 | Coordinate functional status behavior for the current toolkit workflow. |
| class | `FunctionWorkflow` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 69 | Store validated function workflow fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 84 | Return a serializable dictionary representation. |
| function | `from_dict` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 101 | Execute the from dict operation for the current toolkit workflow. |
| function | `_state_path` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 133 | Support state path processing for internal toolkit callers. |
| function | `initialize_function_workflow` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 139 | Initialize function workflow for the current toolkit workflow. |
| function | `load_function_workflow` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 170 | Load function workflow for the current toolkit workflow. |
| function | `save_function_workflow` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 178 | Execute the save function workflow operation for the current toolkit workflow. |
| function | `update_function_workflow` | [`x86decomp.workflow`](../features/x86decomp-workflow.md) | 184 | Update function workflow for the current toolkit workflow. |
| class | `CapabilityResult` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 22 | Store validated capability result fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 29 | Return a serializable dictionary representation. |
| function | `host_is_loopback` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 34 | Execute the host is loopback operation for the current toolkit workflow. |
| function | `endpoint_is_allowed` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 50 | Execute the endpoint is allowed operation for the current toolkit workflow. |
| function | `normalize_endpoint` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 58 | Normalize endpoint for the current toolkit workflow. |
| function | `probe_openai_compatible_endpoint` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 69 | Execute the probe openai compatible endpoint operation for the current toolkit workflow. |
| function | `capabilities_from_adapters` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 97 | Execute the capabilities from adapters operation for the current toolkit workflow. |
| function | `capability_map` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 129 | Execute the capability map operation for the current toolkit workflow. |
| function | `write_capability_report` | [`x86decomp_testkit.adapters.capabilities`](../features/x86decomp-testkit-adapters-capabilities.md) | 134 | Write capability report for the current toolkit workflow. |
| function | `adapter_catalog` | [`x86decomp_testkit.adapters.catalog`](../features/x86decomp-testkit-adapters-catalog.md) | 7 | Execute the adapter catalog operation for the current toolkit workflow. |
| function | `_module_version` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 18 | Support module version processing for internal toolkit callers. |
| function | `_run_version` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 38 | Support run version processing for internal toolkit callers. |
| function | `_windows_executable_suffixes` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 56 | Support windows executable suffixes processing for internal toolkit callers. |
| function | `_prefer_windows_executable` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 61 | Support prefer windows executable processing for internal toolkit callers. |
| function | `_candidate_from_root` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 73 | Support candidate from root processing for internal toolkit callers. |
| function | `_known_windows_msvc_roots` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 97 | Support known windows msvc roots processing for internal toolkit callers. |
| function | `_find_recursive` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 125 | Support find recursive processing for internal toolkit callers. |
| function | `_with_capabilities` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 140 | Support with capabilities processing for internal toolkit callers. |
| function | `_detect_http_endpoint` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 153 | Support detect http endpoint processing for internal toolkit callers. |
| function | `detect_adapter` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 174 | Execute the detect adapter operation for the current toolkit workflow. |
| function | `detect_all` | [`x86decomp_testkit.adapters.detection`](../features/x86decomp-testkit-adapters-detection.md) | 295 | Execute the detect all operation for the current toolkit workflow. |
| function | `platform_key` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 20 | Execute the platform key operation for the current toolkit workflow. |
| function | `github_latest_release` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 31 | Execute the github latest release operation for the current toolkit workflow. |
| function | `select_release_asset` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 44 | Select release asset for the current toolkit workflow. |
| function | `download_file` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 60 | Execute the download file operation for the current toolkit workflow. |
| function | `_safe_destination` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 86 | Support safe destination processing for internal toolkit callers. |
| function | `safe_extract_archive` | [`x86decomp_testkit.adapters.download`](../features/x86decomp-testkit-adapters-download.md) | 98 | Execute the safe extract archive operation for the current toolkit workflow. |
| function | `_yes` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 80 | Support yes processing for internal toolkit callers. |
| function | `_find_package_manager` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 85 | Support find package manager processing for internal toolkit callers. |
| function | `_run_checked` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 93 | Support run checked processing for internal toolkit callers. |
| function | `install_python_adapter` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 102 | Execute the install python adapter operation for the current toolkit workflow. |
| function | `install_github_release` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 110 | Execute the install github release operation for the current toolkit workflow. |
| function | `install_package_manager_adapter` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 165 | Execute the install package manager adapter operation for the current toolkit workflow. |
| function | `_validate_custom_path` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 191 | Support validate custom path processing for internal toolkit callers. |
| function | `_automatic_install_available` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 225 | Support automatic install available processing for internal toolkit callers. |
| function | `install_adapter` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 235 | Execute the install adapter operation for the current toolkit workflow. |
| function | `resolve_missing_adapters` | [`x86decomp_testkit.adapters.installation`](../features/x86decomp-testkit-adapters-installation.md) | 247 | Detect first, then prompt only for missing adapters. |
| function | `_path` | [`x86decomp_testkit.cli`](../features/x86decomp-testkit-cli.md) | 17 | Support path processing for internal toolkit callers. |
| function | `_base_parser` | [`x86decomp_testkit.cli`](../features/x86decomp-testkit-cli.md) | 22 | Build the argparse parser for this command surface. |
| function | `_load` | [`x86decomp_testkit.cli`](../features/x86decomp-testkit-cli.md) | 61 | Support load processing for internal toolkit callers. |
| function | `main` | [`x86decomp_testkit.cli`](../features/x86decomp-testkit-cli.md) | 68 | Run the command-line entry point and return its process status. |
| class | `TestConfig` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 15 | Store validated test config fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 33 | Return a serializable dictionary representation. |
| function | `from_dict` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 55 | Execute the from dict operation for the current toolkit workflow. |
| function | `resolve` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 59 | Resolve resolve for the current toolkit workflow. |
| function | `load_config` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 89 | Load config for the current toolkit workflow. |
| function | `save_config` | [`x86decomp_testkit.config`](../features/x86decomp-testkit-config.md) | 97 | Execute the save config operation for the current toolkit workflow. |
| function | `_coverage_file` | [`x86decomp_testkit.coverage_audit`](../features/x86decomp-testkit-coverage-audit.md) | 11 | Support coverage file processing for internal toolkit callers. |
| function | `audit_public_symbol_execution` | [`x86decomp_testkit.coverage_audit`](../features/x86decomp-testkit-coverage-audit.md) | 25 | Audit public symbol execution for the current toolkit workflow. |
| function | `write_json` | [`x86decomp_testkit.fixtures`](../features/x86decomp-testkit-fixtures.md) | 10 | Write json for the current toolkit workflow. |
| function | `build_minimal_pe32` | [`x86decomp_testkit.fixtures`](../features/x86decomp-testkit-fixtures.md) | 17 | Build minimal pe32 for the current toolkit workflow. |
| function | `build_minimal_pe64` | [`x86decomp_testkit.fixtures`](../features/x86decomp-testkit-fixtures.md) | 51 | Build minimal pe64 for the current toolkit workflow. |
| function | `create_common_fixtures` | [`x86decomp_testkit.fixtures`](../features/x86decomp-testkit-fixtures.md) | 86 | Create common fixtures for the current toolkit workflow. |
| class | `PublicSymbol` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 16 | Store validated public symbol fields used by toolkit reports and adapters. |
| function | `symbol_id` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 25 | Execute the symbol id operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 29 | Return a serializable dictionary representation. |
| function | `_direct_body_lines` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 41 | Support direct body lines processing for internal toolkit callers. |
| function | `_python_files` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 55 | Support python files processing for internal toolkit callers. |
| function | `_module_name` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 63 | Support module name processing for internal toolkit callers. |
| function | `_discover_symbols` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 73 | Support discover symbols processing for internal toolkit callers. |
| function | `discover_public_symbols` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 106 | Discover public symbols for the current toolkit workflow. |
| function | `discover_all_function_symbols` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 111 | Discover all function symbols for the current toolkit workflow. |
| function | `discover_modules` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 116 | Discover modules for the current toolkit workflow. |
| function | `discover_schemas` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 121 | Discover schemas for the current toolkit workflow. |
| function | `discover_ghidra_scripts` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 127 | Discover ghidra scripts for the current toolkit workflow. |
| function | `discover_cli_commands` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 133 | Discover cli commands for the current toolkit workflow. |
| function | `build_inventory` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 154 | Build inventory for the current toolkit workflow. |
| function | `load_feature_catalog` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 169 | Load feature catalog for the current toolkit workflow. |
| function | `audit_catalog` | [`x86decomp_testkit.inventory`](../features/x86decomp-testkit-inventory.md) | 177 | Audit catalog for the current toolkit workflow. |
| function | `parse_junit` | [`x86decomp_testkit.junit`](../features/x86decomp-testkit-junit.md) | 9 | Parse junit for the current toolkit workflow. |
| function | `_path_for` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 20 | Support path for processing for internal toolkit callers. |
| function | `_python_adapter_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 48 | Support python adapter test processing for internal toolkit callers. |
| function | `_generic_executable_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 75 | Support generic executable test processing for internal toolkit callers. |
| function | `_compiler_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 100 | Support compiler test processing for internal toolkit callers. |
| function | `_lld_link_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 133 | Support lld link test processing for internal toolkit callers. |
| function | `_ghidra_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 171 | Support ghidra test processing for internal toolkit callers. |
| function | `_dynamorio_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 206 | Support dynamorio test processing for internal toolkit callers. |
| function | `_objdiff_test` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 235 | Support objdiff test processing for internal toolkit callers. |
| function | `run_live_adapter_tests` | [`x86decomp_testkit.live_adapters`](../features/x86decomp-testkit-live-adapters.md) | 259 | Run live adapter tests for the current toolkit workflow. |
| class | `JsonlEventLogger` | [`x86decomp_testkit.logging_utils`](../features/x86decomp-testkit-logging-utils.md) | 15 | Coordinate jsonl event logger behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp_testkit.logging_utils`](../features/x86decomp-testkit-logging-utils.md) | 17 | Initialize the instance with validated constructor state. |
| function | `emit` | [`x86decomp_testkit.logging_utils`](../features/x86decomp-testkit-logging-utils.md) | 22 | Execute the emit operation for the current toolkit workflow. |
| function | `configure_logging` | [`x86decomp_testkit.logging_utils`](../features/x86decomp-testkit-logging-utils.md) | 36 | Execute the configure logging operation for the current toolkit workflow. |
| class | `Status` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 10 | Enumerate supported status values. |
| class | `AdapterKind` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 18 | Enumerate supported adapter kind values. |
| class | `ProbeResult` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 28 | Store validated probe result fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 38 | Return a serializable dictionary representation. |
| class | `AdapterSpec` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 44 | Store validated adapter spec fields used by toolkit reports and adapters. |
| class | `TestResult` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 66 | Store validated test result fields used by toolkit reports and adapters. |
| function | `to_dict` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 82 | Return a serializable dictionary representation. |
| class | `RunSummary` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 90 | Store validated run summary fields used by toolkit reports and adapters. |
| function | `counts` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 104 | Execute the counts operation for the current toolkit workflow. |
| function | `exit_code` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 111 | Execute the exit code operation for the current toolkit workflow. |
| function | `to_dict` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 120 | Return a serializable dictionary representation. |
| function | `normalized_path` | [`x86decomp_testkit.models`](../features/x86decomp-testkit-models.md) | 140 | Normalize d path for the current toolkit workflow. |
| function | `package_root` | [`x86decomp_testkit.orchestrator`](../features/x86decomp-testkit-orchestrator.md) | 26 | Execute the package root operation for the current toolkit workflow. |
| function | `suite_root` | [`x86decomp_testkit.orchestrator`](../features/x86decomp-testkit-orchestrator.md) | 31 | Execute the suite root operation for the current toolkit workflow. |
| function | `feature_catalog_path` | [`x86decomp_testkit.orchestrator`](../features/x86decomp-testkit-orchestrator.md) | 38 | Execute the feature catalog path operation for the current toolkit workflow. |
| function | `run_all` | [`x86decomp_testkit.orchestrator`](../features/x86decomp-testkit-orchestrator.md) | 43 | Run all for the current toolkit workflow. |
| function | `run_process_test` | [`x86decomp_testkit.process`](../features/x86decomp-testkit-process.md) | 15 | Run process test for the current toolkit workflow. |
| function | `blocked_result` | [`x86decomp_testkit.process`](../features/x86decomp-testkit-process.md) | 91 | Execute the blocked result operation for the current toolkit workflow. |
| function | `write_json_report` | [`x86decomp_testkit.reports`](../features/x86decomp-testkit-reports.md) | 12 | Write json report for the current toolkit workflow. |
| function | `write_adapter_report` | [`x86decomp_testkit.reports`](../features/x86decomp-testkit-reports.md) | 18 | Write adapter report for the current toolkit workflow. |
| function | `_status_icon` | [`x86decomp_testkit.reports`](../features/x86decomp-testkit-reports.md) | 28 | Support status icon processing for internal toolkit callers. |
| function | `write_markdown_report` | [`x86decomp_testkit.reports`](../features/x86decomp-testkit-reports.md) | 38 | Write markdown report for the current toolkit workflow. |
| function | `write_html_report` | [`x86decomp_testkit.reports`](../features/x86decomp-testkit-reports.md) | 108 | Write html report for the current toolkit workflow. |
| class | `_ModelsHandler` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 16 | Coordinate models handler behavior for the current toolkit workflow. |
| function | `do_GET` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 18 | Execute the do  g e t operation for the current toolkit workflow. |
| function | `log_message` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 31 | Execute the log message operation for the current toolkit workflow. |
| function | `_config` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 36 | Support config processing for internal toolkit callers. |
| function | `test_lm_studio_http_satisfies_openai_capability_without_product_aliasing` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 41 | Verify lm studio http satisfies openai capability without product aliasing behavior. |
| function | `test_non_loopback_http_endpoint_requires_network_opt_in` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 72 | Verify non loopback http endpoint requires network opt in behavior. |
| function | `test_loopback_host_classifier_is_strict` | [`x86decomp_testkit.self_tests.test_adapter_capabilities`](../features/x86decomp-testkit-self-tests-test-adapter-capabilities.md) | 80 | Verify loopback host classifier is strict behavior. |
| function | `_config` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 15 | Support config processing for internal toolkit callers. |
| function | `test_installed_adapter_never_prompts` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 22 | Verify installed adapter never prompts behavior. |
| function | `prompt` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 28 | Execute the prompt operation for the current toolkit workflow. |
| function | `test_missing_adapter_prompts_custom_path_then_accepts` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 38 | Verify missing adapter prompts custom path then accepts behavior. |
| function | `prompt` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 48 | Execute the prompt operation for the current toolkit workflow. |
| function | `test_missing_noninteractive_is_explicit_unresolved` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 60 | Verify missing noninteractive is explicit unresolved behavior. |
| function | `test_environment_and_configured_root_detection` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 69 | Verify environment and configured root detection behavior. |
| function | `test_path_detection_preserves_symlink_argv0` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 87 | Verify that adapter detection keeps a symlinked argv0 path when supported. |
| function | `test_missing_python_adapter_accepts_custom_interpreter` | [`x86decomp_testkit.self_tests.test_adapter_detection_resolution`](../features/x86decomp-testkit-self-tests-test-adapter-detection-resolution.md) | 105 | Verify missing python adapter accepts custom interpreter behavior. |
| function | `test_safe_zip_and_tar_extraction` | [`x86decomp_testkit.self_tests.test_archive_security`](../features/x86decomp-testkit-self-tests-test-archive-security.md) | 14 | Verify safe zip and tar extraction behavior. |
| function | `test_rejects_traversal_and_links` | [`x86decomp_testkit.self_tests.test_archive_security`](../features/x86decomp-testkit-self-tests-test-archive-security.md) | 34 | Verify rejects traversal and links behavior. |
| function | `test_release_asset_selection_is_deterministic` | [`x86decomp_testkit.self_tests.test_archive_security`](../features/x86decomp-testkit-self-tests-test-archive-security.md) | 52 | Verify release asset selection is deterministic behavior. |
| function | `test_download_file_hash_and_size_limit` | [`x86decomp_testkit.self_tests.test_archive_security`](../features/x86decomp-testkit-self-tests-test-archive-security.md) | 62 | Verify download file hash and size limit behavior. |
| function | `test_cli_init_config_catalog_and_missing_config` | [`x86decomp_testkit.self_tests.test_cli_and_installation`](../features/x86decomp-testkit-self-tests-test-cli-and-installation.md) | 15 | Verify cli init config catalog and missing config behavior. |
| function | `test_install_python_command_and_failure` | [`x86decomp_testkit.self_tests.test_cli_and_installation`](../features/x86decomp-testkit-self-tests-test-cli-and-installation.md) | 25 | Verify install python command and failure behavior. |
| function | `run_ok` | [`x86decomp_testkit.self_tests.test_cli_and_installation`](../features/x86decomp-testkit-self-tests-test-cli-and-installation.md) | 31 | Run ok for the current toolkit workflow. |
| function | `run_bad` | [`x86decomp_testkit.self_tests.test_cli_and_installation`](../features/x86decomp-testkit-self-tests-test-cli-and-installation.md) | 40 | Run bad for the current toolkit workflow. |
| function | `test_config_roundtrip_and_relative_resolution` | [`x86decomp_testkit.self_tests.test_config_models`](../features/x86decomp-testkit-self-tests-test-config-models.md) | 11 | Verify config roundtrip and relative resolution behavior. |
| function | `test_status_counts_and_strict_exit_code` | [`x86decomp_testkit.self_tests.test_config_models`](../features/x86decomp-testkit-self-tests-test-config-models.md) | 38 | Verify status counts and strict exit code behavior. |
| function | `result` | [`x86decomp_testkit.self_tests.test_config_models`](../features/x86decomp-testkit-self-tests-test-config-models.md) | 40 | Execute the result operation for the current toolkit workflow. |
| function | `_mini_toolkit` | [`x86decomp_testkit.self_tests.test_inventory_reports_process`](../features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 16 | Support mini toolkit processing for internal toolkit callers. |
| function | `test_inventory_catalog_and_public_coverage` | [`x86decomp_testkit.self_tests.test_inventory_reports_process`](../features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 32 | Verify inventory catalog and public coverage behavior. |
| function | `test_junit_process_logging_and_reports` | [`x86decomp_testkit.self_tests.test_inventory_reports_process`](../features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 54 | Verify junit process logging and reports behavior. |
| function | `test_suite_schemas_and_catalog_are_valid` | [`x86decomp_testkit.self_tests.test_inventory_reports_process`](../features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 84 | Verify suite schemas and catalog are valid behavior. |
| function | `test_recursive_inventory_includes_capability_packages_and_nested_schemas` | [`x86decomp_testkit.self_tests.test_inventory_reports_process`](../features/x86decomp-testkit-self-tests-test-inventory-reports-process.md) | 103 | Verify recursive inventory includes capability packages and nested schemas behavior. |
| function | `_missing` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 21 | Support missing processing for internal toolkit callers. |
| function | `_result` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 32 | Support result processing for internal toolkit callers. |
| function | `run_inventory_tests` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 47 | Run inventory tests for the current toolkit workflow. |
| function | `run_cli_surface_tests` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 92 | Run cli surface tests for the current toolkit workflow. |
| function | `_verify_manifest` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 117 | Support verify manifest processing for internal toolkit callers. |
| function | `_validate_schemas` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 146 | Support validate schemas processing for internal toolkit callers. |
| function | `_validate_java` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 164 | Support validate java processing for internal toolkit callers. |
| function | `_validate_skill` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 181 | Support validate skill processing for internal toolkit callers. |
| function | `run_structural_tests` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 202 | Run structural tests for the current toolkit workflow. |
| function | `run_harness_self_tests` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 271 | Run harness self tests for the current toolkit workflow. |
| function | `run_pytest_and_coverage` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 314 | Run pytest and coverage for the current toolkit workflow. |
| function | `run_packaging_tests` | [`x86decomp_testkit.suites`](../features/x86decomp-testkit-suites.md) | 399 | Run packaging tests for the current toolkit workflow. |
| function | `utc_now` | [`x86decomp_testkit.timeutil`](../features/x86decomp-testkit-timeutil.md) | 7 | Execute the utc now operation for the current toolkit workflow. |
| function | `test_unified_canonical_entry_point` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 75 | Verify unified canonical entry point behavior. |
| function | `test_abi_contract_loading` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 89 | Verify abi contract loading behavior. |
| function | `test_analysis_database_complete_public_surface` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 109 | Verify analysis database complete public surface behavior. |
| function | `test_angr_public_file_wrappers` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 138 | Verify angr wrappers or their explicit optional-dependency error path. |
| function | `test_benchmark_metrics_and_runner` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 165 | Verify benchmark metrics and runner behavior. |
| function | `test_coff_remaining_value_objects_and_writer` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 181 | Verify coff remaining value objects and writer behavior. |
| function | `test_compiler_lab_with_deterministic_fake_compiler` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 200 | Verify compiler lab with deterministic fake compiler behavior. |
| function | `test_diff_disassembly_and_crosscheck` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 236 | Verify diff disassembly and crosscheck behavior. |
| function | `test_dynamic_file_wrapper_and_spec_loader` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 257 | Verify dynamic file wrapper and spec loader behavior. |
| function | `test_dynamorio_runner_with_fake_subprocess` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 281 | Verify dynamorio runner with fake subprocess behavior. |
| function | `fake_run` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 289 | Execute the fake run operation for the current toolkit workflow. |
| function | `_verified_store` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 306 | Support verified store processing for internal toolkit callers. |
| function | `test_evidence_contradiction_require_verified_and_project_memory` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 320 | Verify evidence contradiction require verified and project memory behavior. |
| function | `test_exe_diff_extract_and_compare` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 332 | Verify exe diff extract and compare behavior. |
| function | `test_ghidra_run_export_success` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 344 | Verify ghidra run export success behavior. |
| function | `test_remaining_value_objects_and_peview` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 353 | Verify remaining value objects and peview behavior. |
| function | `test_service_create_and_run` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 371 | Verify service create and run behavior. |
| function | `test_symbolic_clone_and_file_wrapper` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 383 | Verify symbolic clone behavior and the optional symbolic backend error path. |
| function | `test_toolchain_snapshot_util_contract_and_workqueue` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 407 | Verify toolchain snapshot util contract and workqueue behavior. |
| function | `test_cli_main_executes_public_entrypoint` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 430 | Verify cli main executes public entrypoint behavior. |
| function | `test_streamable_http_mcp_public_methods` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 440 | Verify streamable http mcp public methods behavior. |
| class | `Headers` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 444 | Coordinate headers behavior for the current toolkit workflow. |
| function | `get` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 446 | Execute the get operation for the current toolkit workflow. |
| function | `get_content_type` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 450 | Execute the get content type operation for the current toolkit workflow. |
| class | `Response` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 454 | Coordinate response behavior for the current toolkit workflow. |
| function | `__init__` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 458 | Initialize the instance with validated constructor state. |
| function | `__enter__` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 462 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 466 | Exit the managed runtime context and release owned resources. |
| function | `read` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 470 | Read read for the current toolkit workflow. |
| function | `fake_urlopen` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 474 | Execute the fake urlopen operation for the current toolkit workflow. |
| function | `test_private_function_surface_regression` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 496 | Exercise the remaining internal function bodies so no defined function is omitted. |
| function | `test_remaining_current_function_surface` | [`x86decomp_testkit.toolkit_tests.test_public_api_contract`](../features/x86decomp-testkit-toolkit-tests-test-public-api-contract.md) | 540 | Verify remaining current function surface behavior. |
