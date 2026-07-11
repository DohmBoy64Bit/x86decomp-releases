"""Build fact-checked project example workflows with actual SHA-256 hashes."""
import hashlib
import os
import json
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parent.parent / "x86decomp-toolkit-0.7.11"
SRC = TOOLKIT / "src" / "x86decomp"
TESTS = TOOLKIT / "tests"
OUTPUT = Path(__file__).resolve().parent / "js" / "examples.js"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def h(rel):
    """Get actual SHA-256 for a file relative to toolkit root."""
    fp = TOOLKIT / rel
    if fp.exists():
        return sha256(fp)
    return "FILE_NOT_FOUND"


WORKFLOWS = [
    {
        "id": "matching-project",
        "title": "End-to-End Matching Project",
        "summary": "Compile, ABI-check, function-diff, image-match, and converge toward relink validation.",
        "classification": "End-to-end project workflow using the matching mode.",
        "sections": [
            {
                "heading": "Matching Model",
                "body": '<p>The matching pipeline targets byte-identical reconstruction. Each function progresses through a state machine:</p>'
                       '<pre><code>not_started → decompiled → compiles → abi_compatible → instruction_similar → byte_matched → image_integrated → full_relink_validated</code></pre>'
                       '<p>Flow: <strong>Target pack → Function artifact → COFF candidate → ABI check → Function diff → Image match → Relink gate</strong></p>'
                       '<p>At any stage, a function can be marked <code>blocked</code> for obstructions.</p>'
            },
            {
                "heading": "1. Ground the Target",
                "body": '<p>Create a target pack from the PE binary, PDB debug data, and MAP file. Verify the pack, then derive the project:</p>'
                       '<pre><code>x86decomp target-pack-infer build/mytarget.pack.json --pe target.exe --pdb target.pdb --map target.map</code></pre>'
                       '<pre><code>x86decomp target-pack-verify build/mytarget.pack.json</code></pre>'
                       '<pre><code>x86decomp project-from-target build/mytarget.pack.json --output project/</code></pre>'
            },
            {
                "heading": "2. Export, Import, and Verify Analysis Artifacts",
                "body": '<p>Export function data from Ghidra, then import and verify artifacts into the project:</p>'
                       '<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre>'
                       '<pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre>'
                       '<pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre>'
                       '<pre><code>x86decomp workflow-init project/ --mode matching</code></pre>'
            },
            {
                "heading": "3. Compile a Target-Specific Candidate",
                "body": '<p>Compile your C source into a COFF object file using a registered compiler profile:</p>'
                       '<pre><code>x86decomp compile build/compile.json --profile compiler-profiles/msvc-coff.json --source src/myfunc.c --output build/myfunc.obj</code></pre>'
            },
            {
                "heading": "4. Check the Candidate ABI",
                "body": '<p>Extract the COFF section and check ABI compatibility against the contract:</p>'
                       '<pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre>'
                       '<pre><code>x86decomp abi-check build/myfunc.bin contracts/myfunc-abi.json --base 0 --report reports/abi/myfunc-check.json</code></pre>'
            },
            {
                "heading": "5. Compare Functions",
                "body": '<p>Run function-level diff between the linked target and your COFF symbol. The diff command produces a '
                       'classification: <code>byte_matched</code>, <code>relocation_normalized_match</code>, '
                       '<code>instruction_similar</code>, or <code>mismatch</code>.</p>'
                       '<pre><code>x86decomp diff-function target/sub_00401230.bin build/myfunc.bin --base 0x401230 --report reports/diff/myfunc.json</code></pre>'
            },
            {
                "heading": "6. Integrate, Relink, and Compare Whole Images",
                "body": '<p>Build a linker plan from layout evidence, relink the executable, profile both images, and compare them:</p>'
                       '<pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre>'
                       '<pre><code>x86decomp relink build/relink-manifest.json</code></pre>'
                       '<pre><code>x86decomp image-profile target.exe --output build/target-profile.json</code></pre>'
                       '<pre><code>x86decomp image-match target.exe build/relinked.exe --profile build/target-profile.json --report reports/image-match.json</code></pre>'
                       '<pre><code>x86decomp convergence-analyze reports/convergence.json --previous reports/prev-convergence.json --history reports/convergence-history.json</code></pre>'
            },
            {
                "heading": "7. Record Matching Progress",
                "body": '<p>Update workflow status after reviewing validator outputs. Validators do <strong>not</strong> auto-promote:</p>'
                       '<pre><code>x86decomp workflow-update project/ --matching-status instruction_similar</code></pre>'
                       '<pre><code>x86decomp workflow-show project/</code></pre>'
            },
            {
                "heading": "What This Project Does Not Prove",
                "body": '<ul>'
                       '<li>Does not prove the original compiler family or version.</li>'
                       '<li>Does not recover original source code — only byte-identical reconstruction.</li>'
                       '<li>Validators are bounded by timeout, instruction count, and path limits.</li>'
                       '<li>A single function match does not prove the whole binary is reconstructable.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/compiler.py</code></td><td><code>{h("src/x86decomp/compiler.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/exe_diff.py</code></td><td><code>{h("src/x86decomp/exe_diff.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/image_match.py</code></td><td><code>{h("src/x86decomp/image_match.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/workflow.py</code></td><td><code>{h("src/x86decomp/workflow.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_modes_and_db.py</code></td><td><code>{h("tests/test_modes_and_db.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "functional-project",
        "title": "End-to-End Functional Project",
        "summary": "Use bounded concrete, symbolic, and integration validation without requiring byte identity.",
        "classification": "End-to-end project workflow using the functional mode.",
        "sections": [
            {
                "heading": "Functional Model",
                "body": '<p>Functional reconstruction validates semantic equivalence without byte matching. State machine:</p>'
                       '<pre><code>not_started → decompiled → compiles → abi_compatible → differentially_validated → symbolically_bounded → integration_validated</code></pre>'
                       '<p>Flow: <strong>Target evidence → Source candidate → Compile + ABI → Concrete harness → Symbolic model → Integration → Functional status</strong></p>'
            },
            {
                "heading": "1. Create the Project",
                "body": '<p>Create a target pack with functional-mode decisions, verify, derive, init workflow, import Ghidra artifacts, '
                       'extract function body range, and generate a deterministic harness:</p>'
                       '<pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --pdb target.pdb'
                       '\n    --decisions-json config/target-decisions.json</code></pre>'
                       '<pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre>'
                       '<pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre>'
                       '<pre><code>x86decomp workflow-init project/ --mode functional</code></pre>'
                       '<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre>'
                       '<pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre>'
                       '<pre><code>x86decomp harness-generate contracts/myfunc-abi.json harnesses/myfunc.json'
                       '\n    --pointer-parameters contracts/myfunc-ptr.json --max-instructions 500 --timeout-ms 5000</code></pre>'
            },
            {
                "heading": "2. Prepare the Candidate",
                "body": '<p>Compile and ABI-check the candidate function:</p>'
                       '<pre><code>x86decomp compile build/compile.json --profile profiles/msvc-coff.json --source src/myfunc.c --output build/myfunc.obj</code></pre>'
                       '<pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre>'
                       '<pre><code>x86decomp abi-check build/myfunc.bin contracts/myfunc-abi.json --base 0 --report reports/abi/myfunc.json</code></pre>'
            },
            {
                "heading": "3. Differential Execution",
                "body": '<p>Run concrete dynamic validation with Unicorn. Bounded by instruction count and timeout:</p>'
                       '<pre><code>x86decomp dynamic-validate target/sub_00401230.bin build/myfunc.bin \n    --harness harnesses/myfunc.json --architecture x86 --report reports/dynamic/myfunc.json</code></pre>'
            },
            {
                "heading": "4. Bounded Symbolic Validation",
                "body": '<p>Run Z3-based symbolic validation to explore all reachable paths within bounds:</p>'
                       '<pre><code>x86decomp symbolic-validate target/sub_00401230.bin build/myfunc.bin \n    --architecture x86 --stack-argument-words 2 --output-registers eax'
                       '\n    --max-steps 100 --max-paths 8 --report reports/symbolic/myfunc.json</code></pre>'
                       '<pre><code>x86decomp symbolic-memory-validate target/sub_00401230.bin build/myfunc.bin \n    --harness harnesses/myfunc-memory.json --report reports/symbolic-memory/myfunc.json</code></pre>'
            },
            {
                "heading": "5. Integration Scenarios",
                "body": '<p>Define process-level integration scenarios in a manifest and run them. Use <code>--allow-host-execution</code> '
                       'with caution — host execution is off by default for untrusted code:</p>'
                       '<pre><code>x86decomp integration-run examples/integration/bounded-demo.json \n    --allow-host-execution --report reports/integration/demo.json</code></pre>'
            },
            {
                "heading": "6. Record Status",
                "body": '<p>Validators do <strong>not</strong> auto-promote. Update status after reviewing reports:</p>'
                       '<pre><code>x86decomp workflow-update project/ --functional-status integration_validated</code></pre>'
                       '<pre><code>x86decomp workflow-show project/</code></pre>'
            },
            {
                "heading": "Truth Boundary",
                "body": '<ul>'
                       '<li>Concrete dynamic validation covers only the harnessed inputs — not all possible inputs.</li>'
                       '<li>Symbolic validation is bounded by max_steps and max_paths.</li>'
                       '<li>Integration scenarios cover only the declared scenarios.</li>'
                       '<li>Functional validation does not imply byte-identical reconstruction.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>{h("src/x86decomp/dynamic.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>{h("src/x86decomp/symbolic.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/integration.py</code></td><td><code>{h("src/x86decomp/integration.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/workflow.py</code></td><td><code>{h("src/x86decomp/workflow.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_dynamic_symbolic.py</code></td><td><code>{h("tests/test_dynamic_symbolic.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "hybrid-project",
        "title": "End-to-End Hybrid Composition",
        "summary": "Keep assembly fallbacks while matching and functional lanes progress independently.",
        "classification": "v0.7.11 has only matching and functional modes. 'Hybrid' is the composition when preferred_mode is both.",
        "sections": [
            {
                "heading": "Hybrid Composition Model",
                "body": '<p>v0.7.11 uses two modes: <code>matching</code> and <code>functional</code>. When <code>preferred_mode</code> '
                       'is <code>both</code>, the project maintains two independent lanes. Source stages:</p>'
                       '<pre><code>original_bytes → generated_assembly → decompiler_candidate → human_candidate → accepted_source</code></pre>'
                       '<p>Flow: <strong>Target pack mode:both → Function packets → Byte-form assembly → Staging C → Matching lane → Functional lane → Selected source</strong></p>'
            },
            {
                "heading": "1. Create a Both-Mode Project",
                "body": '<p>Use target decisions with <code>preferred_mode: both</code>:</p>'
                       '<pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --decisions-json config/both-decisions.json</code></pre>'
                       '<pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre>'
                       '<pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre>'
            },
            {
                "heading": "2. Import Functions",
                "body": '<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre>'
                       '<pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre>'
                       '<pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre>'
            },
            {
                "heading": "3. Generate Fallbacks",
                "body": '<p>Generate byte-form assembly fallbacks for every function and staging C sources. Output structure:</p>'
                       '<pre><code>x86decomp hybrid-generate project/ --asm-format bytes --image-base 0x400000</code></pre>'
                       '<pre><code>project/\n  src/asm/          # Byte-form assembly fallback for every function\n  src/staging/      # Staging C source derived from decompiler output\n  src/matched/      # Populated later with accepted matching sources\n  src/functional/   # Populated later with accepted functional sources\n  config/original/  # Original binary reference\n  Makefile          # Build system with per-lane targets\n  hybrid-project.json</code></pre>'
            },
            {
                "heading": "4. Develop Candidates",
                "body": '<p>Compile from staging C, update to human_candidate:</p>'
                       '<pre><code>x86decomp compile build/myfunc-compile.json --profile profiles/gcc-coff.json --source project/src/staging/myfunc.c --output build/myfunc.obj</code></pre>'
                       '<pre><code>x86decomp workflow-update project/ --matching-status human_candidate --functional-status human_candidate</code></pre>'
            },
            {
                "heading": "5. Validate Independent Lanes",
                "body": '<p>Run matching validators (diff-function) and functional validators (dynamic, symbolic) independently:</p>'
                       '<pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre>'
                       '<pre><code>x86decomp diff-function target/sub_00401230.bin build/myfunc.bin --report reports/diff/myfunc.json</code></pre>'
                       '<pre><code>x86decomp dynamic-validate target/sub_00401230.bin build/myfunc.bin --harness harnesses/myfunc.json --report reports/dynamic/myfunc.json</code></pre>'
                       '<pre><code>x86decomp symbolic-validate target/sub_00401230.bin build/myfunc.bin --stack-argument-words 2 --max-steps 100 --max-paths 8 --report reports/symbolic/myfunc.json</code></pre>'
            },
            {
                "heading": "6. Promote Source Deliberately",
                "body": '<p>Manually copy accepted source into <code>src/matched</code> and/or <code>src/functional</code>. '
                       'Update both statuses. Matching and functional are separate fields — they coexist without contradiction.</p>'
                       '<pre><code>x86decomp workflow-update project/ --matching-status instruction_similar --functional-status integration_validated</code></pre>'
                       '<pre><code>x86decomp workflow-show project/</code></pre>'
            },
            {
                "heading": "Truth Boundary",
                "body": '<ul>'
                       '<li>Byte-form assembly fallbacks are not in the Makefile build graph by default.</li>'
                       '<li>Staging C sources are decompiler-derived, not original.</li>'
                       '<li><code>both</code> is not a third mode — it is the composition of matching + functional.</li>'
                       '<li>Matching and functional status can differ; this is expected and not contradictory.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/hybrid.py</code></td><td><code>{h("src/x86decomp/hybrid.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/workflow.py</code></td><td><code>{h("src/x86decomp/workflow.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>{h("src/x86decomp/dynamic.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>{h("src/x86decomp/symbolic.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_pe64_patch_hybrid.py</code></td><td><code>{h("tests/test_pe64_patch_hybrid.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "static-analysis-evidence",
        "title": "Static Analysis and Evidence",
        "summary": "Inventory formats, import analysis artifacts, cross-check instructions, and govern claims.",
        "classification": "Supporting analysis workflow, not a project mode.",
        "sections": [
            {
                "heading": "Evidence Flow",
                "body": '<p><strong>Authorized files → Target pack → PE/PDB/MAP/COFF → Ghidra export → Disassembly check → Evidence claims → Analysis report</strong></p>'
            },
            {
                "heading": "1. Seal Inputs",
                "body": '<pre><code>x86decomp target-pack-infer build/evidence.pack.json --pe target.exe --pdb target.pdb --map target.map</code></pre>'
                       '<pre><code>x86decomp target-pack-verify build/evidence.pack.json</code></pre>'
            },
            {
                "heading": "2. Inspect Formats",
                "body": '<p>Inventory every format present in the target:</p>'
                       '<pre><code>x86decomp inspect-pe target.exe --report reports/pe-inventory.json</code></pre>'
                       '<pre><code>x86decomp pdb-inspect target.pdb --report reports/pdb-inventory.json</code></pre>'
                       '<pre><code>x86decomp map-inspect target.map --report reports/map-inventory.json</code></pre>'
                       '<pre><code>x86decomp coff-inspect build/myfunc.obj --report reports/coff-inventory.json</code></pre>'
                       '<pre><code>x86decomp lib-inspect target.lib --report reports/lib-inventory.json</code></pre>'
                       '<pre><code>x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json</code></pre>'
            },
            {
                "heading": "3. Export Ghidra Artifacts",
                "body": '<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre>'
                       '<pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre>'
                       '<pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre>'
            },
            {
                "heading": "4. Cross-Check Instructions",
                "body": '<p>Independently disassemble and cross-check against Ghidra output:</p>'
                       '<pre><code>x86decomp disassemble target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json</code></pre>'
                       '<pre><code>x86decomp crosscheck-ghidra project/functions/sub_00401230/instructions.jsonl target/sub_00401230.bin --base 0x401230 --report reports/crosscheck/sub_00401230.json</code></pre>'
            },
            {
                "heading": "5. Record Evidence and Claims",
                "body": '<p>Record at least 3 evidence items from 3 independent groups, then create and verify a claim. '
                       'The strict gate requires: min 3 evidence records, 3 independent groups, 2 kinds, no contradictions, intact hashes.</p>'
                       '<pre><code>x86decomp evidence-add project/ pe-rva:00401230 disassembly-crosscheck --evidence-json reports/crosscheck/sub_00401230.json</code></pre>'
                       '<pre><code>x86decomp evidence-add project/ pe-rva:00401230 metadata-scan --evidence-json reports/metadata.json</code></pre>'
                       '<pre><code>x86decomp evidence-add project/ pe-rva:00401230 ghidra-export --evidence-json project/ghidra_export/sub_00401230.json</code></pre>'
                       '<pre><code>x86decomp claim-create project/ sub_00401230-is-stdcall --evidence-ids ev-001,ev-002,ev-003</code></pre>'
                       '<pre><code>x86decomp claim-verify project/ sub_00401230-is-stdcall</code></pre>'
            },
            {
                "heading": "6. Ingest into Analysis Database",
                "body": '<pre><code>x86decomp db-ingest project/analysis.sqlite --evidence-json reports/evidence-bundle.json</code></pre>'
                       '<pre><code>x86decomp db-query project/analysis.sqlite "SELECT id, subject_entity, relation, object_value, provenance, status FROM type_constraints WHERE subject_entity LIKE \'%00401230%\'"</code></pre>'
                       '<pre><code>x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall --evidence-id ev-001</code></pre>'
                       '<pre><code>x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention</code></pre>'
            },
            {
                "heading": "Truth Boundary",
                "body": '<ul>'
                       '<li>Static analysis does not run the target — all claims are derived from observation.</li>'
                       '<li>Ghidra output is treated as one evidence source, not ground truth.</li>'
                       '<li>Claims are only as strong as their supporting evidence.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/pe.py</code></td><td><code>{h("src/x86decomp/pe.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/ghidra.py</code></td><td><code>{h("src/x86decomp/ghidra.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/disassembly.py</code></td><td><code>{h("src/x86decomp/disassembly.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/evidence.py</code></td><td><code>{h("src/x86decomp/evidence.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/analysis_db.py</code></td><td><code>{h("src/x86decomp/analysis_db.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_ghidra.py</code></td><td><code>{h("tests/test_ghidra.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "compiler-laboratory",
        "title": "Compiler Identification and Laboratory",
        "summary": "Register toolchains, run bounded matrices, preserve provenance, and rank evidence.",
        "classification": "Supporting experiment workflow; ranking is evidence, not historical attribution.",
        "sections": [
            {
                "heading": "Laboratory Model",
                "body": '<p><strong>Known source → Toolchain registry → Profile matrix → Bounded compile → Object comparison → Ranked evidence → Independent corroboration</strong></p>'
            },
            {
                "heading": "1. Register Toolchains",
                "body": '<p>Register and verify real compiler toolchains. The toolkit hashes executables and records roles:</p>'
                       '<pre><code>x86decomp toolchain-register project/ gcc --executable /usr/bin/gcc --version-info "$(gcc --version)"</code></pre>'
                       '<pre><code>x86decomp toolchain-verify project/ gcc</code></pre>'
            },
            {
                "heading": "2. Use a Compiler Profile",
                "body": '<p>Use the bundled <code>examples/compiler-profiles/gcc-i686-object.json</code> profile. It produces '
                       'ELF relocatable objects — <strong>not COFF</strong>. Change the output kind and linker for COFF matching profiles.</p>'
                       '<pre><code>{\n  "schema_version": 2,\n  "id": "gcc-i686-c-object-o2",\n  "executable": "gcc",\n  "language": "c",\n  "output_kind": "relocatable_object",\n  "arguments": ["-m32", "-std=c11", "-O2", "-fno-pic", "-fno-pie", "-c", "{source}", "-o", "{output}"]\n}</code></pre>'
            },
            {
                "heading": "3. Run a Bounded Optimization Matrix",
                "body": '<p>Define a matrix manifest with optimization axes and cap experiments. The bundled '
                       '<code>examples/labs/gcc-optimization-matrix.json</code> varies <code>-O0</code> vs <code>-O2</code>:</p>'
                       '<pre><code>x86decomp compiler-lab examples/labs/gcc-optimization-matrix.json --report reports/lab/gcc-matrix.json</code></pre>'
                       '<p>For matching, add a target PE function to the manifest:</p>'
                       '<pre><code>"target": {\n  "kind": "pe_function",\n  "pe_path": "../target.exe",\n  "rva": "0x401230",\n  "size": "0x40",\n  "symbol": "_myfunc"\n}</code></pre>'
            },
            {
                "heading": "4. Interpret the Ranking",
                "body": '<p>Each experiment gets an ID like <code>p000-v0000</code>. The highest-scoring candidate is the best '
                       '<em>under that scoring policy</em> — it is <strong>not proof of the original compiler</strong>. '
                       'Ranking is evidence that must be corroborated independently.</p>'
            },
            {
                "heading": "5. Build and Compare Ground Truth",
                "body": '<p>Create controlled corpora for reproducible comparisons:</p>'
                       '<pre><code>x86decomp corpus-create-manifest project/corpus/manifest.json --source examples/sample_source/add.c --profiles-json profiles.json</code></pre>'
                       '<pre><code>x86decomp corpus-build project/corpus/manifest.json</code></pre>'
                       '<pre><code>x86decomp corpus-verify project/corpus/manifest.json</code></pre>'
                       '<pre><code>x86decomp corpus-compare project/corpus/manifest.json --other build/other-corpus/manifest.json --report reports/corpus-compare.json</code></pre>'
            },
            {
                "heading": "6. Bounded Compiler Worker",
                "body": '<p>Use the compile worker when isolation policy requires bounded execution:</p>'
                       '<pre><code>x86decomp compile-worker project/ --isolation local_bounded</code></pre>'
            },
            {
                "heading": "Required Interpretation",
                "body": '<ul>'
                       '<li>Successful compilation proves: the toolchain can compile this source to this object.</li>'
                       '<li>It does <strong>not</strong> prove the original binary was compiled with that toolchain.</li>'
                       '<li>Scoring ranks candidates — it does not attribute the historical compiler.</li>'
                       '<li>Unknown compiler flags remain unknown until corroborated by independent evidence.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/compiler.py</code></td><td><code>{h("src/x86decomp/compiler.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/compiler_lab.py</code></td><td><code>{h("src/x86decomp/compiler_lab.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/toolchains.py</code></td><td><code>{h("src/x86decomp/toolchains.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_compiler.py</code></td><td><code>{h("tests/test_compiler.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "patch-image-integration",
        "title": "Patch-Image Integration",
        "summary": "Create a fixed-length derived patch image after independently establishing the allowed target range.",
        "classification": "Incremental integration workflow, not a project mode.",
        "sections": [
            {
                "heading": "Patch Model",
                "body": '<p><strong>Pristine PE → Expected hashes → Evidence-sized bytes → Patch copied image → Refresh checksum → Static check → Isolated test</strong></p>'
            },
            {
                "heading": "1. Seal the Baseline",
                "body": '<p>Hash the original PE and function bytes:</p>'
                       '<pre><code>x86decomp inspect-pe target.exe --report reports/pe-baseline.json</code></pre>'
                       '<pre><code>x86decomp diff-bytes target/sub_00401230.bin build/candidate.bin --report reports/byte-diff.json</code></pre>'
            },
            {
                "heading": "2. Prepare Bytes",
                "body": '<p>Compile and extract exact-size bytes. The candidate length defines the overwrite size:</p>'
                       '<pre><code>x86decomp compile build/patch-compile.json --profile profiles/msvc-coff.json --source src/myfunc.c --output build/patch.obj</code></pre>'
                       '<pre><code>x86decomp coff-extract build/patch.obj --symbol _myfunc --size 0x20 --output build/patch.bin</code></pre>'
            },
            {
                "heading": "3. Create the Patch Image",
                "body": '<p>Copy the original PE, overwrite at the given RVA range, refresh the PE checksum. '
                       'Gated on expected hashes — blocks if hashes differ:</p>'
                       '<pre><code>x86decomp patch-image target.exe --rva 0x401230 --candidate build/patch.bin \n    --expected-original-sha256 abc123... --expected-function-sha256 def456... \n    --output build/patched.exe</code></pre>'
            },
            {
                "heading": "4. Verify Structure",
                "body": '<p>Verify the patched PE is structurally intact. Image match is expected to report "different" by design:</p>'
                       '<pre><code>x86decomp inspect-pe build/patched.exe --report reports/pe-patched.json</code></pre>'
                       '<pre><code>x86decomp image-profile build/patched.exe --output build/patched-profile.json</code></pre>'
                       '<pre><code>x86decomp image-match target.exe build/patched.exe --profile build/patched-profile.json --report reports/image-match.json</code></pre>'
            },
            {
                "heading": "5. Run Bounded Validation",
                "body": '<pre><code>x86decomp integration-run examples/integration/bounded-demo.json --report reports/integration/patched.json</code></pre>'
            },
            {
                "heading": "6. Record Provenance",
                "body": '<pre><code>x86decomp evidence-add project/ patch-rva-0x401230 patch-created --evidence-json reports/patch.json</code></pre>'
                       '<pre><code>x86decomp memory-add project/ "Patched function at RVA 0x401230 with 32 bytes from COFF compilation"</code></pre>'
            },
            {
                "heading": "Hard Constraints",
                "body": '<ul>'
                       '<li>No code caves or trampolines supported.</li>'
                       '<li>No relocation repair, unwind info regeneration, or import reconstruction.</li>'
                       '<li>Operator must enforce correct same-size replacement — the tool does not verify function boundaries.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/patching.py</code></td><td><code>{h("src/x86decomp/patching.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/pe32.py</code></td><td><code>{h("src/x86decomp/pe32.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_pe64_patch_hybrid.py</code></td><td><code>{h("tests/test_pe64_patch_hybrid.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
    {
        "id": "full-relink-convergence",
        "title": "Full Relink and Convergence",
        "summary": "Build evidence-limited linker plans, relink, compare images, and track convergence.",
        "classification": "Supporting linker-reconstruction workflow.",
        "sections": [
            {
                "heading": "Convergence Model",
                "body": '<p><strong>PE + MAP → COFF + libraries → Layout report → Linker plan → Relink manifest → Image match → Convergence history</strong></p>'
            },
            {
                "heading": "1. Inventory Inputs",
                "body": '<pre><code>x86decomp inspect-pe target.exe --report reports/pe-inventory.json</code></pre>'
                       '<pre><code>x86decomp map-inspect target.map --report reports/map-inventory.json</code></pre>'
                       '<pre><code>x86decomp coff-inspect build/myfunc.obj --report reports/coff-inventory.json</code></pre>'
                       '<pre><code>x86decomp lib-inspect target.lib --report reports/lib-inventory.json</code></pre>'
                       '<pre><code>x86decomp coff-comdat-resolve build/myfunc.obj --report reports/comdat.json</code></pre>'
            },
            {
                "heading": "2. Reconstruct Layout",
                "body": '<p>Correlate layout evidence, expose gaps:</p>'
                       '<pre><code>x86decomp layout-reconstruct project/ --pe target.exe --map target.map --objects-dir build/objects/ --report reports/layout.json</code></pre>'
            },
            {
                "heading": "3. Build a Linker Plan",
                "body": '<p>Use the bundled <code>examples/relink/lld-link-x64.json</code> manifest as a starting point:</p>'
                       '<pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre>'
            },
            {
                "heading": "4. Execute Relink",
                "body": '<pre><code>x86decomp relink build/relink-manifest.json</code></pre>'
            },
            {
                "heading": "5. Compare Images",
                "body": '<p>Profile and compare the original vs relinked image:</p>'
                       '<pre><code>x86decomp image-profile target.exe --output build/target-profile.json</code></pre>'
                       '<pre><code>x86decomp image-match target.exe build/relinked.exe --profile build/target-profile.json --report reports/image-match.json</code></pre>'
            },
            {
                "heading": "6. Iterate Through Convergence",
                "body": '<p>Track convergence across iterations. <code>complete</code> = raw exact match:</p>'
                       '<pre><code>x86decomp convergence-analyze reports/convergence.json \n    --previous reports/prev-convergence.json --history reports/convergence-history.json</code></pre>'
            },
            {
                "heading": "7. Advance Workflow",
                "body": '<pre><code>x86decomp workflow-update project/ --matching-status full_relink_validated</code></pre>'
            },
            {
                "heading": "Truth Boundary",
                "body": '<ul>'
                       '<li>Successful relink is not a byte-identical image — it is a normalized match.</li>'
                       '<li>Normalized match is not raw identity.</li>'
                       '<li>The tool does not guess erased linker state.</li>'
                       '</ul>'
            },
            {
                "heading": "v0.7.11 Source Basis",
                "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                       f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/linker_reconstruction.py</code></td><td><code>{h("src/x86decomp/linker_reconstruction.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/relink.py</code></td><td><code>{h("src/x86decomp/relink.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/image_match.py</code></td><td><code>{h("src/x86decomp/image_match.py")}</code></td></tr>'
                       f'<tr><td><code>src/x86decomp/convergence.py</code></td><td><code>{h("src/x86decomp/convergence.py")}</code></td></tr>'
                       f'<tr><td><code>tests/test_relink.py</code></td><td><code>{h("tests/test_relink.py")}</code></td></tr>'
                       '</tbody></table>'
            },
        ]
    },
]

# Write remaining 6 workflows
WORKFLOWS += [
    {
        "id": "abi-type-recovery",
        "title": "ABI and Type Recovery",
        "summary": "Recover calling-convention and C++ relationship candidates, store provenance-bearing constraints, reject conflicts, and generate bounded harnesses.",
        "classification": "Supporting recovery workflow, not original-header recovery.",
        "sections": [
            {"heading": "Constraint Model", "body": '<p><strong>Call sites → Instruction evidence → ABI contract → C++ metadata → Type constraints → Conflict gate → Harness</strong></p>'},
            {"heading": "1. Collect Observations", "body": '<pre><code>x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json</code></pre><pre><code>x86decomp disassemble target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json</code></pre><pre><code>x86decomp crosscheck-ghidra project/functions/sub_00401230/instructions.jsonl target/sub_00401230.bin --base 0x401230 --report reports/crosscheck/sub_00401230.json</code></pre>'},
            {"heading": "2. Write and Check an ABI Contract", "body": '<p>Use the bundled <code>examples/abi/stdcall-two-ints.json</code> contract: 8 bytes stack args, callee cleanup, eax return. Then check both target and candidate:</p><pre><code>x86decomp abi-check target/sub_00401230.bin examples/abi/stdcall-two-ints.json --base 0x401230 --report reports/abi/target.json</code></pre><pre><code>x86decomp abi-check build/candidate.bin examples/abi/stdcall-two-ints.json --base 0 --report reports/abi/candidate.json</code></pre>'},
            {"heading": "3. Recover C++ Relationships", "body": '<p>Reports bounded RTTI, vtables, base relationships, adjustor thunks, static initializers. NOT original class declarations:</p><pre><code>x86decomp cpp-recover target.exe --metadata-report reports/metadata.json --object original/foo.obj --map target.map --report reports/cpp-recovery.json</code></pre>'},
            {"heading": "4. Store Provenance-Bearing Constraints", "body": '<pre><code>x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall --evidence-id ev-abi-001 --confidence high</code></pre><pre><code>x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention</code></pre>'},
            {"heading": "5. Resolve Contradictions Before Acceptance", "body": '<p>DB refuses acceptance while contradictory constraints exist:</p><pre><code>x86decomp db-query project/analysis.sqlite "SELECT id, subject_entity, relation, object_value, provenance, status FROM type_constraints WHERE subject_entity LIKE \'%00401230%\'"</code></pre><pre><code>x86decomp db-constraint-accept project/analysis.sqlite 42</code></pre>'},
            {"heading": "6. Generate a Bounded Harness", "body": '<pre><code>x86decomp harness-generate contracts/sub_00401230-abi.json harnesses/sub_00401230.json --pointer-parameters contracts/sub_00401230-ptr.json --max-instructions 500 --timeout-ms 5000</code></pre>'},
            {"heading": "Truth Boundary", "body": '<ul><li>ABI checks are bounded by the contract definition.</li><li>C++ recovery candidates are not original class declarations.</li><li>Confidence scores rank constraints — they do not prove correctness.</li></ul>'},
            {"heading": "v0.7.11 Source Basis", "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/abi.py</code></td><td><code>{h("src/x86decomp/abi.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/cpp_recovery.py</code></td><td><code>{h("src/x86decomp/cpp_recovery.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/harness_generator.py</code></td><td><code>{h("src/x86decomp/harness_generator.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/analysis_db.py</code></td><td><code>{h("src/x86decomp/analysis_db.py")}</code></td></tr>'
                f'<tr><td><code>tests/test_abi_disassembly.py</code></td><td><code>{h("tests/test_abi_disassembly.py")}</code></td></tr>'
                '</tbody></table>'},
        ]
    },
    {
        "id": "target-release-reproducibility",
        "title": "Target Release and Reproducibility",
        "summary": "Verify manifests, audits, workflows, claims, pipelines, and release contracts.",
        "classification": "Release-acceptance workflow.",
        "sections": [
            {"heading": "Release Model", "body": '<p><strong>Project check → Workflow records → Verified claims → Pipeline results → Reproduction → Security → Release gate</strong></p>'},
            {"heading": "1. Check Project State", "body": '<pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp memory-verify project/</code></pre><pre><code>x86decomp content-verify project/</code></pre><pre><code>x86decomp workflow-show project/</code></pre>'},
            {"heading": "2. Create Reproducibility Manifest", "body": '<pre><code>x86decomp reproduce-create project/ --required-tool gcc --required-tool lld-link --output build/repro-manifest.json</code></pre><pre><code>x86decomp reproduce-verify build/repro-manifest.json</code></pre>'},
            {"heading": "3. Run Audits", "body": '<pre><code>x86decomp security-audit project/ --report reports/security.json</code></pre><pre><code>x86decomp dependency-audit project/ --report reports/dependency.json</code></pre><pre><code>x86decomp sbom-generate project/ --output build/sbom.json</code></pre><pre><code>x86decomp release-manifest-verify build/release-manifest.json</code></pre>'},
            {"heading": "4. Verify Claims and Pipelines", "body": '<pre><code>x86decomp claim-verify project/ my-claim-id</code></pre><pre><code>x86decomp pipeline-status project/ --pipeline-id my-pipeline</code></pre>'},
            {"heading": "5. Evaluate Release Gate", "body": '<p><strong>Known limitation:</strong> v0.7.11 release-gate reads legacy <code>modes</code> object, not schema-v2 fields. <code>--require-workflows</code> only checks file existence, not status minima. Inspect separately with <code>workflow-show</code>.</p><pre><code>x86decomp release-gate project/ --require-workflows --require-verified-claims --require-succeeded-pipelines --require-reproduction-manifest --require-security-report</code></pre>'},
            {"heading": "6. Archive Evidence", "body": '<pre><code>x86decomp project-backup project/ --output build/project-backup.tar.gz</code></pre>'},
            {"heading": "Truth Boundary", "body": '<ul><li>Passing the gate proves only the declared bounded release contracts.</li><li>It does not prove original-source recovery or universal semantic equivalence.</li><li>Backups protect project state, not external toolchains.</li></ul>'},
            {"heading": "v0.7.11 Source Basis", "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/reproducibility.py</code></td><td><code>{h("src/x86decomp/reproducibility.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/security_audit.py</code></td><td><code>{h("src/x86decomp/security_audit.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/release_gate.py</code></td><td><code>{h("src/x86decomp/release_gate.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/project_state.py</code></td><td><code>{h("src/x86decomp/project_state.py")}</code></td></tr>'
                f'<tr><td><code>tests/test_production.py</code></td><td><code>{h("tests/test_production.py")}</code></td></tr>'
                '</tbody></table>'},
        ]
    },
    {
        "id": "benchmark-validation-corpus",
        "title": "Benchmark and Validation Corpus",
        "summary": "Run controlled byte, dynamic, symbolic, integration, and corpus experiments.",
        "classification": "Evaluation workflow, not a decompilation mode.",
        "sections": [
            {"heading": "Benchmark Model", "body": '<p><strong>Known cases → Hash identities → Byte cases → Dynamic cases → Symbolic cases → Integration cases → Aggregate report</strong></p>'},
            {"heading": "1. Generate Deterministic Source Corpus", "body": '<pre><code>x86decomp corpus-generate corpus/sources/ --cases-per-family 8 --seed 0x86DEC0DE</code></pre><pre><code>x86decomp corpus-generated-verify corpus/sources/</code></pre>'},
            {"heading": "2. Build Ground Truth", "body": '<pre><code>x86decomp corpus-create-manifest corpus/ground-truth-manifest.json --sources corpus/sources/ --profiles-json profiles.json</code></pre><pre><code>x86decomp corpus-build corpus/ground-truth-manifest.json</code></pre><pre><code>x86decomp corpus-verify corpus/ground-truth-manifest.json</code></pre>'},
            {"heading": "3. Define Benchmark Cases", "body": '<p>The bundled <code>examples/benchmarks/bounded-demo.json</code> defines 4 cases: byte_pair, dynamic (Unicorn), symbolic (Z3), integration. Each case tracks <code>human_interventions</code>.</p><pre><code>x86decomp benchmark-run examples/benchmarks/bounded-demo.json --report reports/benchmark/demo.json</code></pre>'},
            {"heading": "4. Compare Cross-Corpus Outputs", "body": '<pre><code>x86decomp corpus-compare corpus/ground-truth-manifest.json --other corpus/alternate-manifest.json --report reports/corpus-compare.json</code></pre>'},
            {"heading": "5. Create Authorized Static Test Bundle", "body": '<pre><code>x86decomp test-bundle-create project/ --authorization --expected-architecture x86 --output build/test-bundle.json</code></pre><pre><code>x86decomp test-bundle-inspect build/test-bundle.json</code></pre>'},
            {"heading": "Truth Boundary", "body": '<ul><li>Do not merge passes into universal claims — report counts and human interventions.</li><li>Benchmarks are bounded by max_steps, max_paths, and timeout limits.</li><li>Byte-identical results under one compiler do not generalize.</li></ul>'},
            {"heading": "v0.7.11 Source Basis", "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/benchmarks.py</code></td><td><code>{h("src/x86decomp/benchmarks.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/ground_truth.py</code></td><td><code>{h("src/x86decomp/ground_truth.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>{h("src/x86decomp/dynamic.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>{h("src/x86decomp/symbolic.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/integration.py</code></td><td><code>{h("src/x86decomp/integration.py")}</code></td></tr>'
                f'<tr><td><code>tests/test_linker_metadata_corpus.py</code></td><td><code>{h("tests/test_linker_metadata_corpus.py")}</code></td></tr>'
                '</tbody></table>'},
        ]
    },
    {
        "id": "project-operations-recovery",
        "title": "Project Operations and Recovery",
        "summary": "Back up, migrate, repair, collect, orchestrate, recover, and restore safely.",
        "classification": "Shared lifecycle workflow for all project modes.",
        "sections": [
            {"heading": "Operations Model", "body": '<p><strong>Project check → Deterministic backup → Dry-run change → Apply repair → Durable pipeline → Recovery → Verified restore</strong></p>'},
            {"heading": "1. Check and Back Up", "body": '<p>Always backup before destructive operations:</p><pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp project-backup project/ --output backups/project-20250711.tar.gz</code></pre>'},
            {"heading": "2. Migrate and Repair", "body": '<p>Always dry-run first. Repair only fixes derivable infrastructure:</p><pre><code>x86decomp project-migrate project/ --dry-run</code></pre><pre><code>x86decomp project-repair project/ --dry-run</code></pre>'},
            {"heading": "3. Verify and Collect Content", "body": '<p>GC removes only unreferenced content-store objects. Always dry-run first:</p><pre><code>x86decomp content-verify project/</code></pre><pre><code>x86decomp project-gc project/ --dry-run</code></pre>'},
            {"heading": "4. Create and Run Pipelines", "body": '<p>Pipelines are SQLite-backed, idempotent, and durable:</p><pre><code>x86decomp pipeline-create project/ --pipeline-id my-pipeline --contracts-json contracts.json</code></pre><pre><code>x86decomp pipeline-run project/ --pipeline-id my-pipeline</code></pre>'},
            {"heading": "5. Inspect, Retry, Cancel", "body": '<pre><code>x86decomp pipeline-status project/ --pipeline-id my-pipeline</code></pre><pre><code>x86decomp pipeline-retry project/ --pipeline-id my-pipeline --cascade</code></pre><pre><code>x86decomp pipeline-cancel project/ --pipeline-id my-pipeline --stage-id build-3</code></pre>'},
            {"heading": "6. Recover Stale Jobs", "body": '<pre><code>x86decomp pipeline-recover project/ --stale-seconds 600</code></pre>'},
            {"heading": "7. Restore Safely", "body": '<p>Restore into a new directory, then verify:</p><pre><code>x86decomp project-restore backups/project-20250711.tar.gz --output project-restored/</code></pre><pre><code>x86decomp project-check project-restored/</code></pre><pre><code>x86decomp content-verify project-restored/</code></pre>'},
            {"heading": "Truth Boundary", "body": '<ul><li>Backups protect project state, not external toolchains.</li><li>Repair is infrastructure-only — it does not fix source code.</li><li>Restore always goes into a new directory.</li></ul>'},
            {"heading": "v0.7.11 Source Basis", "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/project_state.py</code></td><td><code>{h("src/x86decomp/project_state.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/orchestrator.py</code></td><td><code>{h("src/x86decomp/orchestrator.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/content_store.py</code></td><td><code>{h("src/x86decomp/content_store.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/security_audit.py</code></td><td><code>{h("src/x86decomp/security_audit.py")}</code></td></tr>'
                f'<tr><td><code>tests/test_project.py</code></td><td><code>{h("tests/test_project.py")}</code></td></tr>'
                '</tbody></table>'},
        ]
    },
    {
        "id": "text-swap-project",
        "title": "End-to-End Text-Swap Project",
        "summary": "Compose replacement text bytes, inject them into the original PE container, verify the bounded section replacement, and keep full-relink claims separate.",
        "classification": "Intermediate workflow — not full relink or source recovery.",
        "sections": [
            {"heading": "Overview", "body": '<p><strong>Original PE container + replacement .text bytes → text-swap plan → text-swap inject → text-swap verify → derived executable</strong></p><p>Intermediate milestone for playable testing without full source reconstruction.</p>'},
            {"heading": "1. Establish Target and Function Evidence", "body": '<pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --decisions-json config/decisions.json</code></pre><pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre><pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre><pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp function discover project/ --profile prologue</code></pre><pre><code>x86decomp function reconcile project/</code></pre><pre><code>x86decomp function sort project/</code></pre><pre><code>x86decomp function classify project/</code></pre>'},
            {"heading": "2. Compose Replacement .text Bytes", "body": '<p>Filled from artifact ranges, fallback byte for gaps. Companion report at <code>build/replacement-text.bin.compose.json</code>:</p><pre><code>x86decomp image-text compose --project project/ --function-list config/function-list.json --output build/replacement-text.bin</code></pre>'},
            {"heading": "3. Create a Text-Swap Plan", "body": '<p>Records original image path/hash, replacement stream path/hash, section raw offset/size/VA. Rejects if replacement exceeds section raw allocation:</p><pre><code>x86decomp text-swap plan target.exe --replacement build/replacement-text.bin --section-name .text --output build/text-swap-plan.json</code></pre>'},
            {"heading": "4. Inject Replacement Bytes", "body": '<p>Re-hashes before writing; blocks if hashes differ from plan:</p><pre><code>x86decomp text-swap inject build/text-swap-plan.json --output build/patched.exe</code></pre>'},
            {"heading": "5. Verify the Derived Executable", "body": '<pre><code>x86decomp text-swap verify build/text-swap-plan.json --image build/patched.exe</code></pre>'},
            {"heading": "6. Run Isolated Functional Tests", "body": '<pre><code>x86decomp integration-run examples/integration/bounded-demo.json --report reports/integration/text-swap.json</code></pre>'},
            {"heading": "7. Reconcile Progress and Source Stages", "body": '<pre><code>x86decomp progress reconcile project/</code></pre><pre><code>x86decomp source-stage classify project/</code></pre><pre><code>x86decomp project health project/</code></pre>'},
            {"heading": "8. Move Toward Full Relink Later", "body": '<pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre><pre><code>x86decomp relink build/relink-manifest.json</code></pre><pre><code>x86decomp image-profile build/relinked.exe --output build/relinked-profile.json</code></pre><pre><code>x86decomp image-match target.exe build/relinked.exe --report reports/image-match.json</code></pre>'},
            {"heading": "Bounded Claims", "body": '<ul><li><strong>Can claim:</strong> Planned bytes injected at planned offset in the PE section.</li><li><strong>Cannot claim:</strong> Source recovered, full relink achieved, all functions matched, whole game proven, mod-ready source.</li></ul>'},
            {"heading": "v0.7.11 Source Basis", "body": '<table class="arg-table"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody>'
                f'<tr><td><code>src/x86decomp/cli.py</code></td><td><code>{h("src/x86decomp/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/reconstruction/cli.py</code></td><td><code>{h("src/x86decomp/reconstruction/cli.py")}</code></td></tr>'
                f'<tr><td><code>src/x86decomp/reconstruction/acceleration.py</code></td><td><code>{h("src/x86decomp/reconstruction/acceleration.py")}</code></td></tr>'
                f'<tr><td><code>tests/reconstruction/test_real_project_acceleration.py</code></td><td><code>{h("tests/reconstruction/test_real_project_acceleration.py")}</code></td></tr>'
                '</tbody></table>'},
        ]
    },
    {
        "id": "source-audit",
        "title": "Source Audit — SHA-256 Hash Ledger",
        "summary": "Authoritative SHA-256 checksums for all bundled example and corpus files in the 0.7.11 release.",
        "classification": "Hash ledger — not a workflow.",
        "sections": [
            {"heading": "Purpose",
             "body": '<p>Provides the exact SHA-256 checksums for every file shipped in the <code>examples/</code> and '
                     '<code>corpus/ground_truth_sources/</code> directories. Use to verify that your copy of the toolkit '
                     'has unmodified reference files.</p>'},
            {"heading": "Example Files",
             "body": '<table class="arg-table"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody>'
                     ''.join(f'<tr><td><code>examples/{f}</code></td><td><code>{h(f"examples/{f}")}</code></td></tr>'
                            for f in sorted([p.relative_to(TOOLKIT / "examples").as_posix()
                                           for p in (TOOLKIT / "examples").rglob("*") if p.is_file()]))
                     + '</tbody></table>'},
            {"heading": "Corpus Ground Truth Sources",
             "body": '<table class="arg-table"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody>'
                     ''.join(f'<tr><td><code>corpus/ground_truth_sources/{f}</code></td><td><code>{h(f"corpus/ground_truth_sources/{f}")}</code></td></tr>'
                            for f in sorted([p.name for p in (TOOLKIT / "corpus" / "ground_truth_sources").glob("*") if p.is_file()]))
                     + '</tbody></table>'},
        ]
    },
]


def main():
    output_js = f"// x86decomp 0.7.11 — Project Example Workflows (fact-checked, actual SHA-256)\n// {len(WORKFLOWS)} workflow pages\nvar WORKFLOW_DATA = {json.dumps(WORKFLOWS, indent=2, ensure_ascii=False)};\n"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(output_js, encoding="utf-8")
    print(f"Written {len(WORKFLOWS)} workflows to {OUTPUT} ({len(output_js):,} bytes)")


if __name__ == "__main__":
    main()
