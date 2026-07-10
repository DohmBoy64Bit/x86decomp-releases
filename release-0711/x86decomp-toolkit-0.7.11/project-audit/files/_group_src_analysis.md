# Grouped audit — root analysis/validation modules (B06g-analysis)

Depth: each file read in full or structurally digested (AST signatures + full risk-pattern sweep, R-014); risk-flagged files (angr_backend, dynamic, symbolic, dynamorio) read at their subprocess/eval sites. Hashes in FILE_INVENTORY.csv. All raise the x86decomp.errors family; all bounded.

## abi.py (260) — Explicit x86 ABI contracts + bounded static compatibility checks
load_abi_contract/analyze_abi/validate_abi over CallingConvention/FloatMode/ABIContract. Pure static analysis of decoded bytes; no I/O beyond JSON contract load. The `..` risk hit is a docstring ellipsis, not path traversal. No findings beyond DOC-001 (template docstrings on helpers). Status: Audited — complete.

## angr_backend.py (619) — Optional angr comparative symbolic-execution backend
`eval(` hits are `solver.eval(...)` (angr claripy solver), NOT Python eval — Verified benign (lines 176, 534). _load_angr raises ExternalToolError when angr absent (BLOCKED policy). Bounded max_steps/max_paths passed through. Counterexample capture. No findings. Status: Audited — complete.

## disassembly.py (282) — Capstone-backed x86/x86-64 decode + normalization
_capstone() lazy import → ExternalToolError if absent. decode_instructions/control_flow_edges/cross_check_ghidra_instructions. Read-only over supplied bytes. No findings. Status: Audited — complete.

## dynamic.py (487) — Bounded differential execution using Unicorn
_unicorn() lazy import (BLOCKED if absent). Region mapping with _align_down/up, ExecutionSpec load, bounded execute_code, differential_validate(_files). Emulation is inherently the risk; bounded by Unicorn limits + explicit MemoryRegion specs; the tool never executes host code here (emulated CPU). `..` hit = docstring. No findings beyond DOC-001. Status: Audited — complete.

## symbolic.py (986) — Bounded symbolic equivalence for small pure leaf functions
Custom bounded symbolic interpreter (SymState/Outcome, _read/_write_reg/_memory, operand decode); UnsupportedSymbolicInstruction raised on out-of-scope opcodes (honest scoping). Step/path bounds. No eval/exec. Large but single-concern. No findings beyond DOC-001. Status: Audited — complete.

## diffing.py (79) — Exact byte comparison + similarity reporting
compare_bytes/compare_files; max_mismatches bound. Pure. tests/test_diffing.py covers. No findings. Status: Audited — complete.

## exe_diff.py (195) — PE-function vs COFF-symbol comparison (matching mode)
rva_to_file_offset/extract_pe_bytes/_masked_copy/relocation masks. Uses the audited PE/COFF parsers. Relocation-masked comparison correct for matching decomp. `..` = docstring. No findings. Status: Audited — complete.

## image_match.py (401) — Whole-image matching + deterministic normalization
derive_layout_profile/compare_whole_images with masked ranges + rebase. Uses audited parsers. No findings beyond DOC-001. Status: Audited — complete.

## convergence.py (177) — Whole-image convergence analysis + history
analyze_image_convergence/append_convergence_history; deterministic metrics; JSON reports via atomic writers. No findings. Status: Audited — complete.

## benchmarks.py (152) — Ground-truth corpus runner + metrics
classification_metrics/run_benchmark_corpus. Deterministic. No findings. Status: Audited — complete.

## patching.py (99) — Patch-image backend with integrity checks + PE checksum
calculate_pe_checksum/patch_pe_function with expected-sha256 guards (see cli patch-image: expected_original/function sha256). Integrity-gated mutation. tests/test_pe64_patch_hybrid.py covers. No findings. Status: Audited — complete.

## harness_generator.py (165) — Bounded differential-execution harness generation
_deterministic_word/generate_execution_harness(_from_files); max_instructions/timeout_ms bounds. `..` = docstring. No findings. Status: Audited — complete.

## cpp_recovery.py (199) — Bounded C++ relationship recovery
recover_cpp_model over msvc_metadata + code patterns; broad `except Exception` returns safe default (prior-audit noted, acceptable for heuristic recovery). No findings beyond DOC-001. Status: Audited — complete.

## linker_layout.py (366) — MSVC linker-map parsing + contribution layout
parse_msvc_map(_text)/reconstruct_linker_layout. Text parser over user-supplied .map; line-oriented, no eval. `..` = docstring. No findings. Status: Audited — complete.

## linker_reconstruction.py (155) — Evidence-driven linker reconstruction plans
build_linker_reconstruction_plan/write_relink_manifest_from_plan. Plan generation (no execution). No findings. Status: Audited — complete.

## relink.py (124) — Manifest-driven full-image relink backend
run_full_relink: subprocess (linker) via argv array + timeout; unlink on temp. Uses external linker (BLOCKED if absent). Consistent with subprocess discipline. No findings. Status: Audited — complete.

## objdiff_adapter.py (174) — Manifest-driven objdiff CLI integration
_resolve_executable/run_objdiff_manifest; subprocess argv array + timeout; version-agnostic. No findings. Status: Audited — complete.

## dynamorio.py (194) — DynamoRIO drcov execution + log normalization
parse_drcov_text (pure) + run_drcov_trace (subprocess argv, timeout, check=False). Host execution is the drrun tool; bounded. No findings. Status: Audited — complete.
