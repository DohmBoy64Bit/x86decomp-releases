// x86decomp 0.7.11 — Project Example Workflows (fact-checked, actual SHA-256)
// 13 workflow pages
var WORKFLOW_DATA = [
  {
    "id": "matching-project",
    "title": "End-to-End Matching Project",
    "summary": "Compile, ABI-check, function-diff, image-match, and converge toward relink validation.",
    "classification": "End-to-end project workflow using the matching mode.",
    "sections": [
      {
        "heading": "Matching Model",
        "body": "<p>The matching pipeline targets byte-identical reconstruction. Each function progresses through a state machine:</p><pre><code>not_started → decompiled → compiles → abi_compatible → instruction_similar → byte_matched → image_integrated → full_relink_validated</code></pre><p>Flow: <strong>Target pack → Function artifact → COFF candidate → ABI check → Function diff → Image match → Relink gate</strong></p><p>At any stage, a function can be marked <code>blocked</code> for obstructions.</p>"
      },
      {
        "heading": "1. Ground the Target",
        "body": "<p>Create a target pack from the PE binary, PDB debug data, and MAP file. Verify the pack, then derive the project:</p><pre><code>x86decomp target-pack-infer build/mytarget.pack.json --pe target.exe --pdb target.pdb --map target.map</code></pre><pre><code>x86decomp target-pack-verify build/mytarget.pack.json</code></pre><pre><code>x86decomp project-from-target build/mytarget.pack.json --output project/</code></pre>"
      },
      {
        "heading": "2. Export, Import, and Verify Analysis Artifacts",
        "body": "<p>Export function data from Ghidra, then import and verify artifacts into the project:</p><pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre><pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre><pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre><pre><code>x86decomp workflow-init project/ --mode matching</code></pre>"
      },
      {
        "heading": "3. Compile a Target-Specific Candidate",
        "body": "<p>Compile your C source into a COFF object file using a registered compiler profile:</p><pre><code>x86decomp compile build/compile.json --profile compiler-profiles/msvc-coff.json --source src/myfunc.c --output build/myfunc.obj</code></pre>"
      },
      {
        "heading": "4. Check the Candidate ABI",
        "body": "<p>Extract the COFF section and check ABI compatibility against the contract:</p><pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre><pre><code>x86decomp abi-check build/myfunc.bin contracts/myfunc-abi.json --base 0 --report reports/abi/myfunc-check.json</code></pre>"
      },
      {
        "heading": "5. Compare Functions",
        "body": "<p>Run function-level diff between the linked target and your COFF symbol. The diff command produces a classification: <code>byte_matched</code>, <code>relocation_normalized_match</code>, <code>instruction_similar</code>, or <code>mismatch</code>.</p><pre><code>x86decomp diff-function target/sub_00401230.bin build/myfunc.bin --base 0x401230 --report reports/diff/myfunc.json</code></pre>"
      },
      {
        "heading": "6. Integrate, Relink, and Compare Whole Images",
        "body": "<p>Build a linker plan from layout evidence, relink the executable, profile both images, and compare them:</p><pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre><pre><code>x86decomp relink build/relink-manifest.json</code></pre><pre><code>x86decomp image-profile target.exe --output build/target-profile.json</code></pre><pre><code>x86decomp image-match target.exe build/relinked.exe --profile build/target-profile.json --report reports/image-match.json</code></pre><pre><code>x86decomp convergence-analyze reports/convergence.json --previous reports/prev-convergence.json --history reports/convergence-history.json</code></pre>"
      },
      {
        "heading": "7. Record Matching Progress",
        "body": "<p>Update workflow status after reviewing validator outputs. Validators do <strong>not</strong> auto-promote:</p><pre><code>x86decomp workflow-update project/ --matching-status instruction_similar</code></pre><pre><code>x86decomp workflow-show project/</code></pre>"
      },
      {
        "heading": "What This Project Does Not Prove",
        "body": "<ul><li>Does not prove the original compiler family or version.</li><li>Does not recover original source code — only byte-identical reconstruction.</li><li>Validators are bounded by timeout, instruction count, and path limits.</li><li>A single function match does not prove the whole binary is reconstructable.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/compiler.py</code></td><td><code>20515d33e6c5e53cdeecacd27ce6556b7f8704a78dafc924888a84e989d5bd38</code></td></tr><tr><td><code>src/x86decomp/exe_diff.py</code></td><td><code>7235903592a6f42e085f9f8a3b60596a3353d1288810ac2c440f5ac1fce51bde</code></td></tr><tr><td><code>src/x86decomp/image_match.py</code></td><td><code>31550da63849a38c19b606e0fd2c05836bb1924b8d24401504d5793ecab2ffaa</code></td></tr><tr><td><code>src/x86decomp/workflow.py</code></td><td><code>b10d1efdc9f7e7f77e0a7ce59d6959533cb8a864d28b1a72e0679ee997854191</code></td></tr><tr><td><code>tests/test_modes_and_db.py</code></td><td><code>84554d4fd263de392d7d3e43471ad0b538672e354b28b1ad639ccbd8f5a60f94</code></td></tr></tbody></table>"
      }
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
        "body": "<p>Functional reconstruction validates semantic equivalence without byte matching. State machine:</p><pre><code>not_started → decompiled → compiles → abi_compatible → differentially_validated → symbolically_bounded → integration_validated</code></pre><p>Flow: <strong>Target evidence → Source candidate → Compile + ABI → Concrete harness → Symbolic model → Integration → Functional status</strong></p>"
      },
      {
        "heading": "1. Create the Project",
        "body": "<p>Create a target pack with functional-mode decisions, verify, derive, init workflow, import Ghidra artifacts, extract function body range, and generate a deterministic harness:</p><pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --pdb target.pdb\n    --decisions-json config/target-decisions.json</code></pre><pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre><pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre><pre><code>x86decomp workflow-init project/ --mode functional</code></pre><pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre><pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre><pre><code>x86decomp harness-generate contracts/myfunc-abi.json harnesses/myfunc.json\n    --pointer-parameters contracts/myfunc-ptr.json --max-instructions 500 --timeout-ms 5000</code></pre>"
      },
      {
        "heading": "2. Prepare the Candidate",
        "body": "<p>Compile and ABI-check the candidate function:</p><pre><code>x86decomp compile build/compile.json --profile profiles/msvc-coff.json --source src/myfunc.c --output build/myfunc.obj</code></pre><pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre><pre><code>x86decomp abi-check build/myfunc.bin contracts/myfunc-abi.json --base 0 --report reports/abi/myfunc.json</code></pre>"
      },
      {
        "heading": "3. Differential Execution",
        "body": "<p>Run concrete dynamic validation with Unicorn. Bounded by instruction count and timeout:</p><pre><code>x86decomp dynamic-validate target/sub_00401230.bin build/myfunc.bin \n    --harness harnesses/myfunc.json --architecture x86 --report reports/dynamic/myfunc.json</code></pre>"
      },
      {
        "heading": "4. Bounded Symbolic Validation",
        "body": "<p>Run Z3-based symbolic validation to explore all reachable paths within bounds:</p><pre><code>x86decomp symbolic-validate target/sub_00401230.bin build/myfunc.bin \n    --architecture x86 --stack-argument-words 2 --output-registers eax\n    --max-steps 100 --max-paths 8 --report reports/symbolic/myfunc.json</code></pre><pre><code>x86decomp symbolic-memory-validate target/sub_00401230.bin build/myfunc.bin \n    --harness harnesses/myfunc-memory.json --report reports/symbolic-memory/myfunc.json</code></pre>"
      },
      {
        "heading": "5. Integration Scenarios",
        "body": "<p>Define process-level integration scenarios in a manifest and run them. Use <code>--allow-host-execution</code> with caution — host execution is off by default for untrusted code:</p><pre><code>x86decomp integration-run examples/integration/bounded-demo.json \n    --allow-host-execution --report reports/integration/demo.json</code></pre>"
      },
      {
        "heading": "6. Record Status",
        "body": "<p>Validators do <strong>not</strong> auto-promote. Update status after reviewing reports:</p><pre><code>x86decomp workflow-update project/ --functional-status integration_validated</code></pre><pre><code>x86decomp workflow-show project/</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Concrete dynamic validation covers only the harnessed inputs — not all possible inputs.</li><li>Symbolic validation is bounded by max_steps and max_paths.</li><li>Integration scenarios cover only the declared scenarios.</li><li>Functional validation does not imply byte-identical reconstruction.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>9a271b38f2231b4a7a1f37e5663ac186fbad3be2d7d03f6983ffe70185bef8ed</code></td></tr><tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>3d52cc7c0718b6d6f86485c95c3396d5f6d74663f3399dbb1ab3aa053f22ece5</code></td></tr><tr><td><code>src/x86decomp/integration.py</code></td><td><code>341737bc244f29b4b9cefee52e3673f4acbb2449ffcf63eaeacfb91c440ad064</code></td></tr><tr><td><code>src/x86decomp/workflow.py</code></td><td><code>b10d1efdc9f7e7f77e0a7ce59d6959533cb8a864d28b1a72e0679ee997854191</code></td></tr><tr><td><code>tests/test_dynamic_symbolic.py</code></td><td><code>7b601226798d54a0e509cc81282a1372384b26a75fae690d62399d3c01e89f12</code></td></tr></tbody></table>"
      }
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
        "body": "<p>v0.7.11 uses two modes: <code>matching</code> and <code>functional</code>. When <code>preferred_mode</code> is <code>both</code>, the project maintains two independent lanes. Source stages:</p><pre><code>original_bytes → generated_assembly → decompiler_candidate → human_candidate → accepted_source</code></pre><p>Flow: <strong>Target pack mode:both → Function packets → Byte-form assembly → Staging C → Matching lane → Functional lane → Selected source</strong></p>"
      },
      {
        "heading": "1. Create a Both-Mode Project",
        "body": "<p>Use target decisions with <code>preferred_mode: both</code>:</p><pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --decisions-json config/both-decisions.json</code></pre><pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre><pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre>"
      },
      {
        "heading": "2. Import Functions",
        "body": "<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre><pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre><pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre>"
      },
      {
        "heading": "3. Generate Fallbacks",
        "body": "<p>Generate byte-form assembly fallbacks for every function and staging C sources. Output structure:</p><pre><code>x86decomp hybrid-generate project/ --asm-format bytes --image-base 0x400000</code></pre><pre><code>project/\n  src/asm/          # Byte-form assembly fallback for every function\n  src/staging/      # Staging C source derived from decompiler output\n  src/matched/      # Populated later with accepted matching sources\n  src/functional/   # Populated later with accepted functional sources\n  config/original/  # Original binary reference\n  Makefile          # Build system with per-lane targets\n  hybrid-project.json</code></pre>"
      },
      {
        "heading": "4. Develop Candidates",
        "body": "<p>Compile from staging C, update to human_candidate:</p><pre><code>x86decomp compile build/myfunc-compile.json --profile profiles/gcc-coff.json --source project/src/staging/myfunc.c --output build/myfunc.obj</code></pre><pre><code>x86decomp workflow-update project/ --matching-status human_candidate --functional-status human_candidate</code></pre>"
      },
      {
        "heading": "5. Validate Independent Lanes",
        "body": "<p>Run matching validators (diff-function) and functional validators (dynamic, symbolic) independently:</p><pre><code>x86decomp coff-extract build/myfunc.obj --symbol _myfunc --output build/myfunc.bin</code></pre><pre><code>x86decomp diff-function target/sub_00401230.bin build/myfunc.bin --report reports/diff/myfunc.json</code></pre><pre><code>x86decomp dynamic-validate target/sub_00401230.bin build/myfunc.bin --harness harnesses/myfunc.json --report reports/dynamic/myfunc.json</code></pre><pre><code>x86decomp symbolic-validate target/sub_00401230.bin build/myfunc.bin --stack-argument-words 2 --max-steps 100 --max-paths 8 --report reports/symbolic/myfunc.json</code></pre>"
      },
      {
        "heading": "6. Promote Source Deliberately",
        "body": "<p>Manually copy accepted source into <code>src/matched</code> and/or <code>src/functional</code>. Update both statuses. Matching and functional are separate fields — they coexist without contradiction.</p><pre><code>x86decomp workflow-update project/ --matching-status instruction_similar --functional-status integration_validated</code></pre><pre><code>x86decomp workflow-show project/</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Byte-form assembly fallbacks are not in the Makefile build graph by default.</li><li>Staging C sources are decompiler-derived, not original.</li><li><code>both</code> is not a third mode — it is the composition of matching + functional.</li><li>Matching and functional status can differ; this is expected and not contradictory.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/hybrid.py</code></td><td><code>82f09030766be3ec3f33b28d73147eb9ae7d520892f54db970bfa49fbc08333f</code></td></tr><tr><td><code>src/x86decomp/workflow.py</code></td><td><code>b10d1efdc9f7e7f77e0a7ce59d6959533cb8a864d28b1a72e0679ee997854191</code></td></tr><tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>9a271b38f2231b4a7a1f37e5663ac186fbad3be2d7d03f6983ffe70185bef8ed</code></td></tr><tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>3d52cc7c0718b6d6f86485c95c3396d5f6d74663f3399dbb1ab3aa053f22ece5</code></td></tr><tr><td><code>tests/test_pe64_patch_hybrid.py</code></td><td><code>1c4c7817684d2149bfa82bb3c91f820ae79e81f0f5ea8b82835cb876e8985fba</code></td></tr></tbody></table>"
      }
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
        "body": "<p><strong>Authorized files → Target pack → PE/PDB/MAP/COFF → Ghidra export → Disassembly check → Evidence claims → Analysis report</strong></p>"
      },
      {
        "heading": "1. Seal Inputs",
        "body": "<pre><code>x86decomp target-pack-infer build/evidence.pack.json --pe target.exe --pdb target.pdb --map target.map</code></pre><pre><code>x86decomp target-pack-verify build/evidence.pack.json</code></pre>"
      },
      {
        "heading": "2. Inspect Formats",
        "body": "<p>Inventory every format present in the target:</p><pre><code>x86decomp inspect-pe target.exe --report reports/pe-inventory.json</code></pre><pre><code>x86decomp pdb-inspect target.pdb --report reports/pdb-inventory.json</code></pre><pre><code>x86decomp map-inspect target.map --report reports/map-inventory.json</code></pre><pre><code>x86decomp coff-inspect build/myfunc.obj --report reports/coff-inventory.json</code></pre><pre><code>x86decomp lib-inspect target.lib --report reports/lib-inventory.json</code></pre><pre><code>x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json</code></pre>"
      },
      {
        "heading": "3. Export Ghidra Artifacts",
        "body": "<pre><code>x86decomp ghidra-export project/ghidra_export/ --project project/</code></pre><pre><code>x86decomp artifact-import project/ project/ghidra_export/</code></pre><pre><code>x86decomp artifact-verify project/ghidra_export/</code></pre>"
      },
      {
        "heading": "4. Cross-Check Instructions",
        "body": "<p>Independently disassemble and cross-check against Ghidra output:</p><pre><code>x86decomp disassemble target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json</code></pre><pre><code>x86decomp crosscheck-ghidra project/functions/sub_00401230/instructions.jsonl target/sub_00401230.bin --base 0x401230 --report reports/crosscheck/sub_00401230.json</code></pre>"
      },
      {
        "heading": "5. Record Evidence and Claims",
        "body": "<p>Record at least 3 evidence items from 3 independent groups, then create and verify a claim. The strict gate requires: min 3 evidence records, 3 independent groups, 2 kinds, no contradictions, intact hashes.</p><pre><code>x86decomp evidence-add project/ pe-rva:00401230 disassembly-crosscheck --evidence-json reports/crosscheck/sub_00401230.json</code></pre><pre><code>x86decomp evidence-add project/ pe-rva:00401230 metadata-scan --evidence-json reports/metadata.json</code></pre><pre><code>x86decomp evidence-add project/ pe-rva:00401230 ghidra-export --evidence-json project/ghidra_export/sub_00401230.json</code></pre><pre><code>x86decomp claim-create project/ sub_00401230-is-stdcall --evidence-ids ev-001,ev-002,ev-003</code></pre><pre><code>x86decomp claim-verify project/ sub_00401230-is-stdcall</code></pre>"
      },
      {
        "heading": "6. Ingest into Analysis Database",
        "body": "<pre><code>x86decomp db-ingest project/analysis.sqlite --evidence-json reports/evidence-bundle.json</code></pre><pre><code>x86decomp db-query project/analysis.sqlite \"SELECT id, subject_entity, relation, object_value, provenance, status FROM type_constraints WHERE subject_entity LIKE '%00401230%'\"</code></pre><pre><code>x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall --evidence-id ev-001</code></pre><pre><code>x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Static analysis does not run the target — all claims are derived from observation.</li><li>Ghidra output is treated as one evidence source, not ground truth.</li><li>Claims are only as strong as their supporting evidence.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/pe.py</code></td><td><code>ef9ab01d711a61c9dede6021b860ca005fe371f0c56caea8bc6da00782ba24a6</code></td></tr><tr><td><code>src/x86decomp/ghidra.py</code></td><td><code>ea266fe809d4d14f1e3171b1c8884c87acc22aa98c4655c2f70907a742a1b60d</code></td></tr><tr><td><code>src/x86decomp/disassembly.py</code></td><td><code>347044ce894e23eef72abe893005aa48904e968ea40d6354ad52c5a57d26cd8c</code></td></tr><tr><td><code>src/x86decomp/evidence.py</code></td><td><code>c09f870993b42d07b8ec9aed95214455efdc8d22261b68c88d4a3b4275397dc7</code></td></tr><tr><td><code>src/x86decomp/analysis_db.py</code></td><td><code>7f4f961f4ccab04e13c81007aa5810388e255bd3efa95de8cd5d5d2682cd4a27</code></td></tr><tr><td><code>tests/test_ghidra.py</code></td><td><code>cbba0e5399843226fd2eeb42a80befda46c517b07c07cd23761bb3526968ab6d</code></td></tr></tbody></table>"
      }
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
        "body": "<p><strong>Known source → Toolchain registry → Profile matrix → Bounded compile → Object comparison → Ranked evidence → Independent corroboration</strong></p>"
      },
      {
        "heading": "1. Register Toolchains",
        "body": "<p>Register and verify real compiler toolchains. The toolkit hashes executables and records roles:</p><pre><code>x86decomp toolchain-register project/ gcc --executable /usr/bin/gcc --version-info \"$(gcc --version)\"</code></pre><pre><code>x86decomp toolchain-verify project/ gcc</code></pre>"
      },
      {
        "heading": "2. Use a Compiler Profile",
        "body": "<p>Use the bundled <code>examples/compiler-profiles/gcc-i686-object.json</code> profile. It produces ELF relocatable objects — <strong>not COFF</strong>. Change the output kind and linker for COFF matching profiles.</p><pre><code>{\n  \"schema_version\": 2,\n  \"id\": \"gcc-i686-c-object-o2\",\n  \"executable\": \"gcc\",\n  \"language\": \"c\",\n  \"output_kind\": \"relocatable_object\",\n  \"arguments\": [\"-m32\", \"-std=c11\", \"-O2\", \"-fno-pic\", \"-fno-pie\", \"-c\", \"{source}\", \"-o\", \"{output}\"]\n}</code></pre>"
      },
      {
        "heading": "3. Run a Bounded Optimization Matrix",
        "body": "<p>Define a matrix manifest with optimization axes and cap experiments. The bundled <code>examples/labs/gcc-optimization-matrix.json</code> varies <code>-O0</code> vs <code>-O2</code>:</p><pre><code>x86decomp compiler-lab examples/labs/gcc-optimization-matrix.json --report reports/lab/gcc-matrix.json</code></pre><p>For matching, add a target PE function to the manifest:</p><pre><code>\"target\": {\n  \"kind\": \"pe_function\",\n  \"pe_path\": \"../target.exe\",\n  \"rva\": \"0x401230\",\n  \"size\": \"0x40\",\n  \"symbol\": \"_myfunc\"\n}</code></pre>"
      },
      {
        "heading": "4. Interpret the Ranking",
        "body": "<p>Each experiment gets an ID like <code>p000-v0000</code>. The highest-scoring candidate is the best <em>under that scoring policy</em> — it is <strong>not proof of the original compiler</strong>. Ranking is evidence that must be corroborated independently.</p>"
      },
      {
        "heading": "5. Build and Compare Ground Truth",
        "body": "<p>Create controlled corpora for reproducible comparisons:</p><pre><code>x86decomp corpus-create-manifest project/corpus/manifest.json --source examples/sample_source/add.c --profiles-json profiles.json</code></pre><pre><code>x86decomp corpus-build project/corpus/manifest.json</code></pre><pre><code>x86decomp corpus-verify project/corpus/manifest.json</code></pre><pre><code>x86decomp corpus-compare project/corpus/manifest.json --other build/other-corpus/manifest.json --report reports/corpus-compare.json</code></pre>"
      },
      {
        "heading": "6. Bounded Compiler Worker",
        "body": "<p>Use the compile worker when isolation policy requires bounded execution:</p><pre><code>x86decomp compile-worker project/ --isolation local_bounded</code></pre>"
      },
      {
        "heading": "Required Interpretation",
        "body": "<ul><li>Successful compilation proves: the toolchain can compile this source to this object.</li><li>It does <strong>not</strong> prove the original binary was compiled with that toolchain.</li><li>Scoring ranks candidates — it does not attribute the historical compiler.</li><li>Unknown compiler flags remain unknown until corroborated by independent evidence.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/compiler.py</code></td><td><code>20515d33e6c5e53cdeecacd27ce6556b7f8704a78dafc924888a84e989d5bd38</code></td></tr><tr><td><code>src/x86decomp/compiler_lab.py</code></td><td><code>d7af86c22450d845090b49c53c7e415d30ac388684ad6b46a3a9900fd1878029</code></td></tr><tr><td><code>src/x86decomp/toolchains.py</code></td><td><code>3edc57ee8c42dee979f77ba99cc475059c5a144d2c62593085017d122c59d840</code></td></tr><tr><td><code>tests/test_compiler.py</code></td><td><code>aaf8399cc2f4a86d6d96545cbcde509cb58ad883f8c59c4b11dfd755d222ef19</code></td></tr></tbody></table>"
      }
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
        "body": "<p><strong>Pristine PE → Expected hashes → Evidence-sized bytes → Patch copied image → Refresh checksum → Static check → Isolated test</strong></p>"
      },
      {
        "heading": "1. Seal the Baseline",
        "body": "<p>Hash the original PE and function bytes:</p><pre><code>x86decomp inspect-pe target.exe --report reports/pe-baseline.json</code></pre><pre><code>x86decomp diff-bytes target/sub_00401230.bin build/candidate.bin --report reports/byte-diff.json</code></pre>"
      },
      {
        "heading": "2. Prepare Bytes",
        "body": "<p>Compile and extract exact-size bytes. The candidate length defines the overwrite size:</p><pre><code>x86decomp compile build/patch-compile.json --profile profiles/msvc-coff.json --source src/myfunc.c --output build/patch.obj</code></pre><pre><code>x86decomp coff-extract build/patch.obj --symbol _myfunc --size 0x20 --output build/patch.bin</code></pre>"
      },
      {
        "heading": "3. Create the Patch Image",
        "body": "<p>Copy the original PE, overwrite at the given RVA range, refresh the PE checksum. Gated on expected hashes — blocks if hashes differ:</p><pre><code>x86decomp patch-image target.exe --rva 0x401230 --candidate build/patch.bin \n    --expected-original-sha256 abc123... --expected-function-sha256 def456... \n    --output build/patched.exe</code></pre>"
      },
      {
        "heading": "4. Verify Structure",
        "body": "<p>Verify the patched PE is structurally intact. Image match is expected to report \"different\" by design:</p><pre><code>x86decomp inspect-pe build/patched.exe --report reports/pe-patched.json</code></pre><pre><code>x86decomp image-profile build/patched.exe --output build/patched-profile.json</code></pre><pre><code>x86decomp image-match target.exe build/patched.exe --profile build/patched-profile.json --report reports/image-match.json</code></pre>"
      },
      {
        "heading": "5. Run Bounded Validation",
        "body": "<pre><code>x86decomp integration-run examples/integration/bounded-demo.json --report reports/integration/patched.json</code></pre>"
      },
      {
        "heading": "6. Record Provenance",
        "body": "<pre><code>x86decomp evidence-add project/ patch-rva-0x401230 patch-created --evidence-json reports/patch.json</code></pre><pre><code>x86decomp memory-add project/ \"Patched function at RVA 0x401230 with 32 bytes from COFF compilation\"</code></pre>"
      },
      {
        "heading": "Hard Constraints",
        "body": "<ul><li>No code caves or trampolines supported.</li><li>No relocation repair, unwind info regeneration, or import reconstruction.</li><li>Operator must enforce correct same-size replacement — the tool does not verify function boundaries.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/patching.py</code></td><td><code>b36c51a681676a288269e14d526764777a5bf7ae0882b252eeaf51f008dcea3f</code></td></tr><tr><td><code>src/x86decomp/pe32.py</code></td><td><code>9b9e3b948c92f68bfa352544f7117329d4d3baaaecc0f25d0cc87ffda35b3fbb</code></td></tr><tr><td><code>tests/test_pe64_patch_hybrid.py</code></td><td><code>1c4c7817684d2149bfa82bb3c91f820ae79e81f0f5ea8b82835cb876e8985fba</code></td></tr></tbody></table>"
      }
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
        "body": "<p><strong>PE + MAP → COFF + libraries → Layout report → Linker plan → Relink manifest → Image match → Convergence history</strong></p>"
      },
      {
        "heading": "1. Inventory Inputs",
        "body": "<pre><code>x86decomp inspect-pe target.exe --report reports/pe-inventory.json</code></pre><pre><code>x86decomp map-inspect target.map --report reports/map-inventory.json</code></pre><pre><code>x86decomp coff-inspect build/myfunc.obj --report reports/coff-inventory.json</code></pre><pre><code>x86decomp lib-inspect target.lib --report reports/lib-inventory.json</code></pre><pre><code>x86decomp coff-comdat-resolve build/myfunc.obj --report reports/comdat.json</code></pre>"
      },
      {
        "heading": "2. Reconstruct Layout",
        "body": "<p>Correlate layout evidence, expose gaps:</p><pre><code>x86decomp layout-reconstruct project/ --pe target.exe --map target.map --objects-dir build/objects/ --report reports/layout.json</code></pre>"
      },
      {
        "heading": "3. Build a Linker Plan",
        "body": "<p>Use the bundled <code>examples/relink/lld-link-x64.json</code> manifest as a starting point:</p><pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre>"
      },
      {
        "heading": "4. Execute Relink",
        "body": "<pre><code>x86decomp relink build/relink-manifest.json</code></pre>"
      },
      {
        "heading": "5. Compare Images",
        "body": "<p>Profile and compare the original vs relinked image:</p><pre><code>x86decomp image-profile target.exe --output build/target-profile.json</code></pre><pre><code>x86decomp image-match target.exe build/relinked.exe --profile build/target-profile.json --report reports/image-match.json</code></pre>"
      },
      {
        "heading": "6. Iterate Through Convergence",
        "body": "<p>Track convergence across iterations. <code>complete</code> = raw exact match:</p><pre><code>x86decomp convergence-analyze reports/convergence.json \n    --previous reports/prev-convergence.json --history reports/convergence-history.json</code></pre>"
      },
      {
        "heading": "7. Advance Workflow",
        "body": "<pre><code>x86decomp workflow-update project/ --matching-status full_relink_validated</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Successful relink is not a byte-identical image — it is a normalized match.</li><li>Normalized match is not raw identity.</li><li>The tool does not guess erased linker state.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/linker_reconstruction.py</code></td><td><code>5af77b480cf94aa7f825f507ad4b0ff3a0c5ed3988d3f4a9515fef1910419eae</code></td></tr><tr><td><code>src/x86decomp/relink.py</code></td><td><code>e1a67dd9a3581d2d0beeefc27c04e4841ede6b50b9247ced3da031475ebd4e53</code></td></tr><tr><td><code>src/x86decomp/image_match.py</code></td><td><code>31550da63849a38c19b606e0fd2c05836bb1924b8d24401504d5793ecab2ffaa</code></td></tr><tr><td><code>src/x86decomp/convergence.py</code></td><td><code>cf8193925c1325c3e3158ea8f4883d40ce3df113a4d755f797b65d72ee5a9e37</code></td></tr><tr><td><code>tests/test_relink.py</code></td><td><code>1d4a4b9959fa574e52245cfb9c18921d48fbd3334c414b1d248143f014eb6ef6</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "abi-type-recovery",
    "title": "ABI and Type Recovery",
    "summary": "Recover calling-convention and C++ relationship candidates, store provenance-bearing constraints, reject conflicts, and generate bounded harnesses.",
    "classification": "Supporting recovery workflow, not original-header recovery.",
    "sections": [
      {
        "heading": "Constraint Model",
        "body": "<p><strong>Call sites → Instruction evidence → ABI contract → C++ metadata → Type constraints → Conflict gate → Harness</strong></p>"
      },
      {
        "heading": "1. Collect Observations",
        "body": "<pre><code>x86decomp metadata-scan target.exe --object original/foo.obj --map target.map --report reports/metadata.json</code></pre><pre><code>x86decomp disassemble target/sub_00401230.bin --base 0x401230 --architecture x86 --report reports/disassembly/sub_00401230.json</code></pre><pre><code>x86decomp crosscheck-ghidra project/functions/sub_00401230/instructions.jsonl target/sub_00401230.bin --base 0x401230 --report reports/crosscheck/sub_00401230.json</code></pre>"
      },
      {
        "heading": "2. Write and Check an ABI Contract",
        "body": "<p>Use the bundled <code>examples/abi/stdcall-two-ints.json</code> contract: 8 bytes stack args, callee cleanup, eax return. Then check both target and candidate:</p><pre><code>x86decomp abi-check target/sub_00401230.bin examples/abi/stdcall-two-ints.json --base 0x401230 --report reports/abi/target.json</code></pre><pre><code>x86decomp abi-check build/candidate.bin examples/abi/stdcall-two-ints.json --base 0 --report reports/abi/candidate.json</code></pre>"
      },
      {
        "heading": "3. Recover C++ Relationships",
        "body": "<p>Reports bounded RTTI, vtables, base relationships, adjustor thunks, static initializers. NOT original class declarations:</p><pre><code>x86decomp cpp-recover target.exe --metadata-report reports/metadata.json --object original/foo.obj --map target.map --report reports/cpp-recovery.json</code></pre>"
      },
      {
        "heading": "4. Store Provenance-Bearing Constraints",
        "body": "<pre><code>x86decomp db-constraint-add project/analysis.sqlite pe-rva:00401230 calling_convention stdcall --evidence-id ev-abi-001 --confidence high</code></pre><pre><code>x86decomp db-constraint-conflicts project/analysis.sqlite pe-rva:00401230 calling_convention</code></pre>"
      },
      {
        "heading": "5. Resolve Contradictions Before Acceptance",
        "body": "<p>DB refuses acceptance while contradictory constraints exist:</p><pre><code>x86decomp db-query project/analysis.sqlite \"SELECT id, subject_entity, relation, object_value, provenance, status FROM type_constraints WHERE subject_entity LIKE '%00401230%'\"</code></pre><pre><code>x86decomp db-constraint-accept project/analysis.sqlite 42</code></pre>"
      },
      {
        "heading": "6. Generate a Bounded Harness",
        "body": "<pre><code>x86decomp harness-generate contracts/sub_00401230-abi.json harnesses/sub_00401230.json --pointer-parameters contracts/sub_00401230-ptr.json --max-instructions 500 --timeout-ms 5000</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>ABI checks are bounded by the contract definition.</li><li>C++ recovery candidates are not original class declarations.</li><li>Confidence scores rank constraints — they do not prove correctness.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/abi.py</code></td><td><code>216c5f2f6a843c6f74533d643605cab93fec52880b56ca9730e2ab4660d54fd6</code></td></tr><tr><td><code>src/x86decomp/cpp_recovery.py</code></td><td><code>95b7b494434d17e9d165eefa89399e4feb3c5740fe68808b61001d014fe969db</code></td></tr><tr><td><code>src/x86decomp/harness_generator.py</code></td><td><code>af602f9120a38a8dd33ced7b7243a6140b01813eb0402b4abd35ee3aa789b3c4</code></td></tr><tr><td><code>src/x86decomp/analysis_db.py</code></td><td><code>7f4f961f4ccab04e13c81007aa5810388e255bd3efa95de8cd5d5d2682cd4a27</code></td></tr><tr><td><code>tests/test_abi_disassembly.py</code></td><td><code>91ebeb183e6f9728fff8d8d828615c79506b7b1d2752a0caaf016379aec1c590</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "target-release-reproducibility",
    "title": "Target Release and Reproducibility",
    "summary": "Verify manifests, audits, workflows, claims, pipelines, and release contracts.",
    "classification": "Release-acceptance workflow.",
    "sections": [
      {
        "heading": "Release Model",
        "body": "<p><strong>Project check → Workflow records → Verified claims → Pipeline results → Reproduction → Security → Release gate</strong></p>"
      },
      {
        "heading": "1. Check Project State",
        "body": "<pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp memory-verify project/</code></pre><pre><code>x86decomp content-verify project/</code></pre><pre><code>x86decomp workflow-show project/</code></pre>"
      },
      {
        "heading": "2. Create Reproducibility Manifest",
        "body": "<pre><code>x86decomp reproduce-create project/ --required-tool gcc --required-tool lld-link --output build/repro-manifest.json</code></pre><pre><code>x86decomp reproduce-verify build/repro-manifest.json</code></pre>"
      },
      {
        "heading": "3. Run Audits",
        "body": "<pre><code>x86decomp security-audit project/ --report reports/security.json</code></pre><pre><code>x86decomp dependency-audit project/ --report reports/dependency.json</code></pre><pre><code>x86decomp sbom-generate project/ --output build/sbom.json</code></pre><pre><code>x86decomp release-manifest-verify build/release-manifest.json</code></pre>"
      },
      {
        "heading": "4. Verify Claims and Pipelines",
        "body": "<pre><code>x86decomp claim-verify project/ my-claim-id</code></pre><pre><code>x86decomp pipeline-status project/ --pipeline-id my-pipeline</code></pre>"
      },
      {
        "heading": "5. Evaluate Release Gate",
        "body": "<p><strong>Known limitation:</strong> v0.7.11 release-gate reads legacy <code>modes</code> object, not schema-v2 fields. <code>--require-workflows</code> only checks file existence, not status minima. Inspect separately with <code>workflow-show</code>.</p><pre><code>x86decomp release-gate project/ --require-workflows --require-verified-claims --require-succeeded-pipelines --require-reproduction-manifest --require-security-report</code></pre>"
      },
      {
        "heading": "6. Archive Evidence",
        "body": "<pre><code>x86decomp project-backup project/ --output build/project-backup.tar.gz</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Passing the gate proves only the declared bounded release contracts.</li><li>It does not prove original-source recovery or universal semantic equivalence.</li><li>Backups protect project state, not external toolchains.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/reproducibility.py</code></td><td><code>e7e8309e3f517a1027975a0562e1a8e453a35f7aae72de3a1a1a3db59ccc64c9</code></td></tr><tr><td><code>src/x86decomp/security_audit.py</code></td><td><code>4d352a6a4a7d03a3442f695c220298341a1e6754f72a820271c73d78c293c79b</code></td></tr><tr><td><code>src/x86decomp/release_gate.py</code></td><td><code>85c874f601c2271608e664eb80e7b604c76a5313eb1b8a0df8ab6ff9f7f98803</code></td></tr><tr><td><code>src/x86decomp/project_state.py</code></td><td><code>53e3610b62be1afd58e1a1113d052349b4bb5a66874f0d20121a6e24313db1f9</code></td></tr><tr><td><code>tests/test_production.py</code></td><td><code>f3575e49c46f49d61705e658d4ba3ae1803607a2f5fcb96f02113c3995a0f58d</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "benchmark-validation-corpus",
    "title": "Benchmark and Validation Corpus",
    "summary": "Run controlled byte, dynamic, symbolic, integration, and corpus experiments.",
    "classification": "Evaluation workflow, not a decompilation mode.",
    "sections": [
      {
        "heading": "Benchmark Model",
        "body": "<p><strong>Known cases → Hash identities → Byte cases → Dynamic cases → Symbolic cases → Integration cases → Aggregate report</strong></p>"
      },
      {
        "heading": "1. Generate Deterministic Source Corpus",
        "body": "<pre><code>x86decomp corpus-generate corpus/sources/ --cases-per-family 8 --seed 0x86DEC0DE</code></pre><pre><code>x86decomp corpus-generated-verify corpus/sources/</code></pre>"
      },
      {
        "heading": "2. Build Ground Truth",
        "body": "<pre><code>x86decomp corpus-create-manifest corpus/ground-truth-manifest.json --sources corpus/sources/ --profiles-json profiles.json</code></pre><pre><code>x86decomp corpus-build corpus/ground-truth-manifest.json</code></pre><pre><code>x86decomp corpus-verify corpus/ground-truth-manifest.json</code></pre>"
      },
      {
        "heading": "3. Define Benchmark Cases",
        "body": "<p>The bundled <code>examples/benchmarks/bounded-demo.json</code> defines 4 cases: byte_pair, dynamic (Unicorn), symbolic (Z3), integration. Each case tracks <code>human_interventions</code>.</p><pre><code>x86decomp benchmark-run examples/benchmarks/bounded-demo.json --report reports/benchmark/demo.json</code></pre>"
      },
      {
        "heading": "4. Compare Cross-Corpus Outputs",
        "body": "<pre><code>x86decomp corpus-compare corpus/ground-truth-manifest.json --other corpus/alternate-manifest.json --report reports/corpus-compare.json</code></pre>"
      },
      {
        "heading": "5. Create Authorized Static Test Bundle",
        "body": "<pre><code>x86decomp test-bundle-create project/ --authorization --expected-architecture x86 --output build/test-bundle.json</code></pre><pre><code>x86decomp test-bundle-inspect build/test-bundle.json</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Do not merge passes into universal claims — report counts and human interventions.</li><li>Benchmarks are bounded by max_steps, max_paths, and timeout limits.</li><li>Byte-identical results under one compiler do not generalize.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/benchmarks.py</code></td><td><code>396fc44141a8c3e230d5d0140f7de568179446e1ff2b0d1f1f08cccfda155a9b</code></td></tr><tr><td><code>src/x86decomp/ground_truth.py</code></td><td><code>a75d53655de3da08956d73647b2d2cd9e9c360c7c7a4f59429e4aa0e83b4b873</code></td></tr><tr><td><code>src/x86decomp/dynamic.py</code></td><td><code>9a271b38f2231b4a7a1f37e5663ac186fbad3be2d7d03f6983ffe70185bef8ed</code></td></tr><tr><td><code>src/x86decomp/symbolic.py</code></td><td><code>3d52cc7c0718b6d6f86485c95c3396d5f6d74663f3399dbb1ab3aa053f22ece5</code></td></tr><tr><td><code>src/x86decomp/integration.py</code></td><td><code>341737bc244f29b4b9cefee52e3673f4acbb2449ffcf63eaeacfb91c440ad064</code></td></tr><tr><td><code>tests/test_linker_metadata_corpus.py</code></td><td><code>1be3d4a4d56607adb3e7fec6a671d22f07af426579765d11b4929c606c3ddf8c</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "project-operations-recovery",
    "title": "Project Operations and Recovery",
    "summary": "Back up, migrate, repair, collect, orchestrate, recover, and restore safely.",
    "classification": "Shared lifecycle workflow for all project modes.",
    "sections": [
      {
        "heading": "Operations Model",
        "body": "<p><strong>Project check → Deterministic backup → Dry-run change → Apply repair → Durable pipeline → Recovery → Verified restore</strong></p>"
      },
      {
        "heading": "1. Check and Back Up",
        "body": "<p>Always backup before destructive operations:</p><pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp project-backup project/ --output backups/project-20250711.tar.gz</code></pre>"
      },
      {
        "heading": "2. Migrate and Repair",
        "body": "<p>Always dry-run first. Repair only fixes derivable infrastructure:</p><pre><code>x86decomp project-migrate project/ --dry-run</code></pre><pre><code>x86decomp project-repair project/ --dry-run</code></pre>"
      },
      {
        "heading": "3. Verify and Collect Content",
        "body": "<p>GC removes only unreferenced content-store objects. Always dry-run first:</p><pre><code>x86decomp content-verify project/</code></pre><pre><code>x86decomp project-gc project/ --dry-run</code></pre>"
      },
      {
        "heading": "4. Create and Run Pipelines",
        "body": "<p>Pipelines are SQLite-backed, idempotent, and durable:</p><pre><code>x86decomp pipeline-create project/ --pipeline-id my-pipeline --contracts-json contracts.json</code></pre><pre><code>x86decomp pipeline-run project/ --pipeline-id my-pipeline</code></pre>"
      },
      {
        "heading": "5. Inspect, Retry, Cancel",
        "body": "<pre><code>x86decomp pipeline-status project/ --pipeline-id my-pipeline</code></pre><pre><code>x86decomp pipeline-retry project/ --pipeline-id my-pipeline --cascade</code></pre><pre><code>x86decomp pipeline-cancel project/ --pipeline-id my-pipeline --stage-id build-3</code></pre>"
      },
      {
        "heading": "6. Recover Stale Jobs",
        "body": "<pre><code>x86decomp pipeline-recover project/ --stale-seconds 600</code></pre>"
      },
      {
        "heading": "7. Restore Safely",
        "body": "<p>Restore into a new directory, then verify:</p><pre><code>x86decomp project-restore backups/project-20250711.tar.gz --output project-restored/</code></pre><pre><code>x86decomp project-check project-restored/</code></pre><pre><code>x86decomp content-verify project-restored/</code></pre>"
      },
      {
        "heading": "Truth Boundary",
        "body": "<ul><li>Backups protect project state, not external toolchains.</li><li>Repair is infrastructure-only — it does not fix source code.</li><li>Restore always goes into a new directory.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/project_state.py</code></td><td><code>53e3610b62be1afd58e1a1113d052349b4bb5a66874f0d20121a6e24313db1f9</code></td></tr><tr><td><code>src/x86decomp/orchestrator.py</code></td><td><code>98aa89769e42ad4195fee2db26418b31cfe45202f6883cd8ab9b2227dab39a09</code></td></tr><tr><td><code>src/x86decomp/content_store.py</code></td><td><code>aead9e16737c23da18e4c379f5ecbea7afa420aeb7d47940130331b0970321df</code></td></tr><tr><td><code>src/x86decomp/security_audit.py</code></td><td><code>4d352a6a4a7d03a3442f695c220298341a1e6754f72a820271c73d78c293c79b</code></td></tr><tr><td><code>tests/test_project.py</code></td><td><code>7a595f937faa13d9cc1de37a6330a3c628844aaca3d36226cbc7053d01b1e535</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "text-swap-project",
    "title": "End-to-End Text-Swap Project",
    "summary": "Compose replacement text bytes, inject them into the original PE container, verify the bounded section replacement, and keep full-relink claims separate.",
    "classification": "Intermediate workflow — not full relink or source recovery.",
    "sections": [
      {
        "heading": "Overview",
        "body": "<p><strong>Original PE container + replacement .text bytes → text-swap plan → text-swap inject → text-swap verify → derived executable</strong></p><p>Intermediate milestone for playable testing without full source reconstruction.</p>"
      },
      {
        "heading": "1. Establish Target and Function Evidence",
        "body": "<pre><code>x86decomp target-pack-infer build/target.pack.json --pe target.exe --decisions-json config/decisions.json</code></pre><pre><code>x86decomp target-pack-verify build/target.pack.json</code></pre><pre><code>x86decomp project-from-target build/target.pack.json --output project/</code></pre><pre><code>x86decomp project-check project/</code></pre><pre><code>x86decomp function discover project/ --profile prologue</code></pre><pre><code>x86decomp function reconcile project/</code></pre><pre><code>x86decomp function sort project/</code></pre><pre><code>x86decomp function classify project/</code></pre>"
      },
      {
        "heading": "2. Compose Replacement .text Bytes",
        "body": "<p>Filled from artifact ranges, fallback byte for gaps. Companion report at <code>build/replacement-text.bin.compose.json</code>:</p><pre><code>x86decomp image-text compose --project project/ --function-list config/function-list.json --output build/replacement-text.bin</code></pre>"
      },
      {
        "heading": "3. Create a Text-Swap Plan",
        "body": "<p>Records original image path/hash, replacement stream path/hash, section raw offset/size/VA. Rejects if replacement exceeds section raw allocation:</p><pre><code>x86decomp text-swap plan target.exe --replacement build/replacement-text.bin --section-name .text --output build/text-swap-plan.json</code></pre>"
      },
      {
        "heading": "4. Inject Replacement Bytes",
        "body": "<p>Re-hashes before writing; blocks if hashes differ from plan:</p><pre><code>x86decomp text-swap inject build/text-swap-plan.json --output build/patched.exe</code></pre>"
      },
      {
        "heading": "5. Verify the Derived Executable",
        "body": "<pre><code>x86decomp text-swap verify build/text-swap-plan.json --image build/patched.exe</code></pre>"
      },
      {
        "heading": "6. Run Isolated Functional Tests",
        "body": "<pre><code>x86decomp integration-run examples/integration/bounded-demo.json --report reports/integration/text-swap.json</code></pre>"
      },
      {
        "heading": "7. Reconcile Progress and Source Stages",
        "body": "<pre><code>x86decomp progress reconcile project/</code></pre><pre><code>x86decomp source-stage classify project/</code></pre><pre><code>x86decomp project health project/</code></pre>"
      },
      {
        "heading": "8. Move Toward Full Relink Later",
        "body": "<pre><code>x86decomp linker-plan project/ --linker lld-link --write-relink-manifest build/relink-manifest.json</code></pre><pre><code>x86decomp relink build/relink-manifest.json</code></pre><pre><code>x86decomp image-profile build/relinked.exe --output build/relinked-profile.json</code></pre><pre><code>x86decomp image-match target.exe build/relinked.exe --report reports/image-match.json</code></pre>"
      },
      {
        "heading": "Bounded Claims",
        "body": "<ul><li><strong>Can claim:</strong> Planned bytes injected at planned offset in the PE section.</li><li><strong>Cannot claim:</strong> Source recovered, full relink achieved, all functions matched, whole game proven, mod-ready source.</li></ul>"
      },
      {
        "heading": "v0.7.11 Source Basis",
        "body": "<table class=\"arg-table\"><thead><tr><th>Source File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>src/x86decomp/cli.py</code></td><td><code>19e6ded80c08032e900ea420274bd610cb2bca256f3229d48a2a8f623b3b7004</code></td></tr><tr><td><code>src/x86decomp/reconstruction/cli.py</code></td><td><code>9bf306fcd8139edb0c137c41f431ed696578870c1691c57198f546a41b81352d</code></td></tr><tr><td><code>src/x86decomp/reconstruction/acceleration.py</code></td><td><code>6754b04bf0b1cd6308637226f9861350ae1d9c92f29e21b2be6f4caab4cc18c9</code></td></tr><tr><td><code>tests/reconstruction/test_real_project_acceleration.py</code></td><td><code>bac9286b994d72730b89bd3e72e922aaf8b995bec89d837e2311b89d1e9f1d6f</code></td></tr></tbody></table>"
      }
    ]
  },
  {
    "id": "source-audit",
    "title": "Source Audit — SHA-256 Hash Ledger",
    "summary": "Authoritative SHA-256 checksums for all bundled example and corpus files in the 0.7.11 release.",
    "classification": "Hash ledger — not a workflow.",
    "sections": [
      {
        "heading": "Purpose",
        "body": "<p>Provides the exact SHA-256 checksums for every file shipped in the <code>examples/</code> and <code>corpus/ground_truth_sources/</code> directories. Use to verify that your copy of the toolkit has unmodified reference files.</p>"
      },
      {
        "heading": "Example Files",
        "body": "<tr><td><code>examples/abi/stdcall-two-ints.json</code></td><td><code>f2c7a723de83de7169612e1cdc305a4bd8779e9ad82c7ff3a2ce90d400ac3ace</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/benchmarks/bounded-demo.json</code></td><td><code>980ad9dc8352019f4dca1f06e25a8654ec87248befc178c35490ecc3d129a51a</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/compiler-profiles/gcc-i686-object.json</code></td><td><code>dc5dee89f0aff786350b51e24e7b77067de8d2a0a332fc6e880041a330729572</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/contracts/command-surface.json</code></td><td><code>85a67b1da249fa898cfa7b65c7cbd1c1896297993cc547e8823ddd440a50d5e2</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/contracts/public-surface.json</code></td><td><code>d04d7f8622da4eb0c103fd7515720a32265ae6336e410bfa5358398f9d975fda</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/integration/bounded-demo.json</code></td><td><code>e1b589e23a5fa0a7c1310c69760ef7729fa912c2a5584985a7cbb487f57eab26</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/integration/candidate.py</code></td><td><code>2b348feb64cd2832d57b07c74cd35c58a2b9c36916263a04b3d80bc0c377b8b3</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/integration/candidate_mismatch.py</code></td><td><code>108e2316477fc03c410ec8ca790b035729fcdc2199f8ec5cd0ca749e09e21347</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/integration/target.py</code></td><td><code>2b348feb64cd2832d57b07c74cd35c58a2b9c36916263a04b3d80bc0c377b8b3</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/labs/gcc-optimization-matrix.json</code></td><td><code>f4f19ea47da16374312c4eff46d2914e3d0c425a229f92a95b2fe99221acbd78</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/local-llm/add-two-ints-job.json</code></td><td><code>aac7785ac0e8ccc9e408fe583c7a96ca8a4bb01abd51eb17c1553f127a8a86b5</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/local-llm/lm-studio-profile.json</code></td><td><code>f8135459f4354bf16ab4797924efb4a02f44b494ac36ee4873464609307c202e</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/local-llm/ollama-profile.json</code></td><td><code>f10e53e8646689be08c75c7e06fa238ddf78159aa672da8e35aa3c3df415e5bb</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/release/release-gate-policy.json</code></td><td><code>7ad41612264a71c3bd1d1ea44b5ad0f9145710ef926492975796dd9264948026</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/release/target-decisions.json</code></td><td><code>91b5bfcd613ac3d76fc020e5bb415d0ae11594886c6cac4317cc06e7ea5df1cb</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/relink/lld-link-x64.json</code></td><td><code>6addc382de2d64d223f4e24e47207b5741d2583d1717f4aec04107123a6013ef</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/sample_source/add.c</code></td><td><code>860aaedc4520b18df5ce99de71a36487eb333dcdb09f65fce222677c8fe8cd97</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/symbolic/symbolic-alias-harness.json</code></td><td><code>e5bbc6d9470e269f41051e95a444a9218f9919140bc74070dd223caf4eb7c130</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/test-bundle/x86decomp-test-bundle.json</code></td><td><code>6d88af2c016e6e88a5ba66fab7c88c9d7b56f70c1f5e71d2cb494aab69da6a68</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/validators/add_stack_candidate.bin</code></td><td><code>6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/validators/add_stack_harness.json</code></td><td><code>beeaeeecbe1136402ef0b3c1c3f799256a2613f87bb9457f97b71fe605ec0d0f</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/validators/add_stack_target.bin</code></td><td><code>6d1e1d30f2068501de61e0022c4352fda2a7650f29eb96f01ad04fa160305e21</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>examples/validators/sub_stack_candidate.bin</code></td><td><code>fe10777e0899cf9cabd2bc8dc3367d711f6af675bdda9c5e28144539792f922f</code></td></tr></tbody></table>"
      },
      {
        "heading": "Corpus Ground Truth Sources",
        "body": "<tr><td><code>corpus/ground_truth_sources/aliasing.c</code></td><td><code>09a93c1038059384920be8ed617f196950b3b935fa4e7ecdcccd4b38215f222c</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/arithmetic.c</code></td><td><code>1a39b20e36efc0d23c5570152a1db30922527835bfc82ddf4b629980c916326e</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/bitfields.c</code></td><td><code>44c9a66d27e87a270af05fdb87d82d87512b70fe72600df0bc89f4e091b5a7dd</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/branches.c</code></td><td><code>0dcc84cf6d38aa0a3e90a66bd349f349d504cd2dc0160db16933466c56aa99bb</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/calling_conventions.c</code></td><td><code>cfb331698f9ccdb113849a7c535a500ee6631a46a716be1d3791e49f9c1e69b3</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/classes.cpp</code></td><td><code>d04c86180d9424ea91914dc7b73d93b4b3da432d7a26d8d801ff9d5718701521</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/eh_multiple.cpp</code></td><td><code>7b3cc0e687132f70957e55dbbaa5c479d6a4864fde0e11cb49df0c600d6f2665</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/exceptions.cpp</code></td><td><code>fd15c6bd23f39262a9aa02f94f02210dacab53a2a5d358aae415bba2c329394e</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/floating_point.c</code></td><td><code>ff00c63ae76817932bdd0b4a5b0a0c8bc661e03314889d1eef404e580279bb89</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/globals.c</code></td><td><code>e4fbe6bc2a51161e651a23264f5de4e90d052b2e9efcbcea1c1ff76a748528c4</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/indirect_calls.c</code></td><td><code>b9b6dc58d6912bf8a54c46868a5a61b321447c9826660dfb29f76f741b21b92e</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/loops.c</code></td><td><code>d929c2eb356d9e45d27aa9a9e9929d1ce3fad324d8843d7e53e4dbe7dabe9262</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/member_pointers.cpp</code></td><td><code>8e84a7254ebeda7ec4db40335350606cf26227868e20be7db4f4382cdd3e9f69</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/multiple_inheritance.cpp</code></td><td><code>2fc99918de8375a035774b6cff12866defb77d2095bf1a6005b6419c4afc4410</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/static_initializers.cpp</code></td><td><code>5566d58941846d63fafa6e6047f5f0a70dd19ff484aea58f1eac88cfa1c3156c</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/structs.c</code></td><td><code>0b29f69d01886989d3d34fb430acb259ca55c604b8b59c968e5d341972102280</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/switch_dense.c</code></td><td><code>2a696a875c034a89e16a9b28359f6603942c536954321bc7403a9b780d24546f</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/tail_calls.c</code></td><td><code>874edb70e2470cafdd6bed6a7a05519da95c926d1b0777622d1fba726194ddb3</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/templates.cpp</code></td><td><code>cd18fc097a4bbbacacff6685edb8c5e6a0dfe7d8e27a68eb0b0febad6508194b</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/tls.c</code></td><td><code>9f917229ae42021f4045f2f56af5ac3116987dc442e304c1b9b6b441200ba54b</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/unions.c</code></td><td><code>2906ac1f944da7f6020756df9f20451048f8e2ed81ed5ac6ea06554afe1c7f60</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/varargs.c</code></td><td><code>3326edfa00e59cd41f5409c8ef01d1d5b96c0e1a13471972a2a107725032cdbb</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/vectorizable.c</code></td><td><code>4e71d283a0479bd5264da8f235bdb4f434a1b841289d9eac335c8b997be10f43</code></td></tr><table class=\"arg-table\"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody><tr><td><code>corpus/ground_truth_sources/virtual_inheritance.cpp</code></td><td><code>c8e83579cd4d6159e716c23270110d997349e3b1a609bf1d50c0b93a2e64d1d2</code></td></tr></tbody></table>"
      }
    ]
  }
];
