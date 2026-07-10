# Grouped audit — native/ (11), assembly/ (7), local_llm/ (4) subsystems (B06g-nal)

Depth: structural digest + full risk sweep (R-014); native parse_pe call sites + assembler subprocess + llm loopback checks read. Hashes in FILE_INVENTORY.csv.

## native/ — native PE reconstruction & closed-loop matching
- __init__.py (7): marker. Audited — complete.
- cli.py (164): native CLI via run_cli; subprocess extra-exception; CLI-001 applies. Audited — complete.
- store.py (126): NativeStore — schema/parameterized. Audited — complete.
- matching.py (167): rva_to_file_offset/extract_candidate/compare_function_bytes/FunctionMatching — uses audited PE parser; exact byte compare. **Calls parse_pe with no FormatError handling** → contributes to CLI-001 (malformed input tracebacks via subsystem main). Audited — complete.
- pe_reconstruction.py (140): plan_patch/apply_operations/PEReconstruction — section/patch planning over parse_pe; same CLI-001 exposure. Audited — complete.
- slots.py (172): inventory_from_project/FunctionSlots — slot safety; ValueError caught locally (slots.py:18). Audited — complete.
- runtime.py (118): RuntimeValidation — static + opt-in live validation; subprocess with TimeoutExpired handling; live execution is opt-in (consent). Audited — complete.
- staging.py (86): StagingBridge — subprocess staging. Audited — complete.
- closed_loop.py (51): ClosedLoop — orchestrates match/compile/diff loop via subprocess. Audited — complete.
- hybrid_composer.py (70): HybridComposer — parse_pe + broad `except Exception: checks['pe_parses']=False` (acceptable: explicitly recording a parse-failure signal, not swallowing). Audited — complete.
- windows_tools.py (72): discover_ghidra_launcher/write_response_file/WindowsTools — subprocess argv; response-file writing for Windows toolchains. Audited — complete.

## assembly/ — relocation-aware assembly materialization (byte-default)
- __init__.py (16): marker. Audited — complete.
- cli.py (272): assembly CLI via run_cli (extra exceptions incl. SubprocessError); CLI-001 applies. Audited — complete.
- annotation.py (126): validate_symbol/render_byte_assembly/parse_byte_directives/render_annotated — byte-form is the conservative default (matches AGENTS/README policy). Audited — complete.
- materialize.py (617): assembler discovery + assemble_coff (subprocess argv), capstone-backed candidates, source/line-map rendering; AssemblerError on failure (no silent success). Audited — complete.
- pipeline.py (345): AssemblyPipeline — SQLite-backed; parameterized. Audited — complete.
- relocations.py (382): RelocationResolver/normalize_symbol_map/_compute_value — relocation resolution; catches FormatError locally (relocations.py:291). Degenerate 'Resolve resolve...' docstring (DOC-001). Audited — complete.
- store.py (111): AssemblyStore — schema/parameterized; degenerate 'Initialize initialize...'/'Check check...' docstrings (DOC-001). Audited — complete.

## local_llm/ — bounded local-model proposal + exact byte-match
- __init__.py (21): re-exports. Audited — complete.
- profiles.py (258): provider_catalog/is_loopback_host/resolved_addresses_are_loopback/create_profile/validate_profile — **socket used to resolve+verify endpoint addresses are loopback** (the enforcement behind README's 'loopback-only by default'). Verified: resolved_addresses_are_loopback gates non-loopback. Audited — complete.
- prompts.py (204): deterministic, injection-resistant prompt construction; _resolve_job_path; the 'do not include TODO/placeholders' instruction to the model (prior-audit noted). Audited — complete.
- matching.py (422): generate_candidate/run_match_loop/verify_match_report — the LLM→compile→byte-diff acceptance loop; rmtree scoped to output; only deterministic compile+relocation+exact-byte gates accept a candidate (matches policy). Audited — complete.

Findings across B06g-nal: DOC-001 (degenerate docstrings), CLI-001 (native/assembly subsystem mains + native parse_pe sites). No correctness/security defects; loopback enforcement and byte-default policy implemented as documented.
