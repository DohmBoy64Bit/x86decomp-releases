# Local LLM Exact Match

**Technical objective:** End-to-end local-LLM pipeline — provider configuration, endpoint probing, profile creation, job creation for small target functions, batch matching with the deterministic byte-identity gate, verification, and candidate promotion into the project workflow.

**Game:** Darkwater Cove (fictional point-and-click adventure game, x86 PE32, MSVC 2005 /O1 /Ob1, many small utility functions 24–128 bytes).

---

## Overview

Darkwater Cove has 800+ utility functions under 128 bytes — string formatters, coordinate wrappers, inventory slot math, dialogue state machines. These small, self-contained functions are ideal candidates for local-LLM proposal generation. The goal is to use a locally running LLM (LM Studio with Qwen 2.5 Coder 7B) to propose C implementations, then gate acceptance exclusively through the deterministic compiler → COFF → relocation → byte-compare pipeline. LLM output is never trusted directly; only exact-byte matches are accepted.

You will learn:

1. How to install and probe an LLM provider (LM Studio).
2. How to create and validate an LLM profile.
3. How to create jobs for individual functions and batch-create for the whole project.
4. How to run the `llm match` loop (propose → compile → COFF → relocate → byte compare).
5. How to verify match reports and promote accepted candidates to project workflow.

---

## Prerequisites

| Requirement | Detail |
|---|---|
| **Binary** | `games/darkwater-cove/darkwater_cove.exe` — PE32 x86, 1.4 MB |
| **LLM provider** | LM Studio running locally at `http://127.0.0.1:1234` with Qwen 2.5 Coder 7B loaded |
| **Compiler** | MSVC 2005 toolchain registered; compiler profile at `config/compiler-profiles/msvc2005-o1.json` |
| **Ghidra** | Ghidra 11.2+ for function artifact export |
| **Project** | `games/darkwater-cove/project/` |

---

## Starting directory structure

```
games/darkwater-cove/
├── darkwater_cove.exe
├── exports/
│   └── (Ghidra export of all functions under 256 bytes)
├── jobs/
│   ├── sub_401000.json
│   ├── sub_401050.json
│   └── ...
├── match-output/
│   ├── sub_401000/
│   ├── sub_401050/
│   └── ...
├── candidates/
│   └── (promoted C sources)
└── project/
    ├── project.json
    ├── config/
    │   ├── compiler-profiles/
    │   │   └── msvc2005-o1.json
    │   └── llm/
    │       └── lm-studio-qwen.json
    ├── functions/
    ├── src/
    │   └── matched/
    └── reports/
        └── llm/
```

---

## Step 1: Install and probe the LLM provider

List available provider presets:
```console
$ x86decomp llm providers
```

Output (abbreviated):
```json
{
  "providers": [
    {"id": "lm-studio", "protocol": "openai-chat", "default_base_url": "http://127.0.0.1:1234/v1", "structured_output": "openai-json-schema"},
    {"id": "ollama", "protocol": "ollama-chat", "default_base_url": "http://127.0.0.1:11434", "structured_output": "ollama-json-schema"},
    {"id": "llama.cpp", "protocol": "openai-chat", "default_base_url": "http://127.0.0.1:8080/v1", "structured_output": "openai-json-schema"}
  ]
}
```

Create an LM Studio profile:
```console
$ x86decomp llm profile-create lm-studio games/darkwater-cove/project/config/llm/lm-studio-qwen.json \
    --model qwen2.5-coder-7b-instruct
```

**What happens:** `llm profile-create` creates a validated JSON profile for the LM Studio provider, recording the model name, protocol (`openai-chat`), base URL (`http://127.0.0.1:1234/v1`), and structured-output capability.

Validate the profile:
```console
$ x86decomp llm profile-validate games/darkwater-cove/project/config/llm/lm-studio-qwen.json
```

Probe the endpoint:
```console
$ x86decomp llm probe games/darkwater-cove/project/config/llm/lm-studio-qwen.json
```

**What happens:** `llm probe` contacts the LM Studio model-list endpoint and returns the list of currently loaded models. Confirm `qwen2.5-coder-7b-instruct` appears in the response.

!!! tip "Loopback-only by default"
    All LLM presets default to `127.0.0.1`. The profile is rejected if the base URL contains a non-loopback hostname, unless `--allow-remote` is explicitly passed. This prevents accidental data disclosure.

---

## Step 2: Initialize project and export function artifacts

```console
$ x86decomp init games/darkwater-cove/darkwater_cove.exe games/darkwater-cove/project/
$ x86decomp snapshot-tools --output games/darkwater-cove/project/config/tools.json
$ x86decomp ghidra-export games/darkwater-cove/darkwater_cove.exe \
    games/darkwater-cove/ghidra-project/ darkwater_cove \
    games/darkwater-cove/exports/ \
    --ghidra-home "C:\ghidra_11.2_PUBLIC" --overwrite
$ x86decomp artifact-import games/darkwater-cove/project/ games/darkwater-cove/exports/
```

---

## Step 3: Create jobs for individual functions

Create a job from a function packet (Ghidra-exported artifact):
```console
$ x86decomp llm job-create games/darkwater-cove/project/functions/sub_401000/function.json \
    games/darkwater-cove/jobs/sub_401000.json \
    --architecture x86 \
    --function-name format_dialogue_string \
    --symbol _format_dialogue_string@8 \
    --image-base 0x400000 \
    --max-attempts 8 \
    --inline
```

**What happens:** `llm job-create` reads the function packet (`function.json` with RVA, size, disassembly), inlines the target bytes and mnemonics (`--inline`), assigns a C function name and COFF symbol, and writes a job file. `--max-attempts 8` allows the match loop up to 8 retries.

Create a job from an explicit byte range (bypassing Ghidra export):
```console
$ x86decomp llm job-from-range games/darkwater-cove/darkwater_cove.exe \
    games/darkwater-cove/jobs/sub_401050.json \
    --rva 0x1050 --size 64 \
    --architecture x86 \
    --function-name clamp_inventory_index \
    --symbol _clamp_inventory_index@4 \
    --image-base 0x400000 \
    --max-attempts 8
```

**What happens:** `llm job-from-range` extracts 64 bytes at RVA `0x1050` from the PE image, creates a job with the raw bytes and function metadata. No Ghidra export needed — useful for quick ad-hoc functions.

---

## Step 4: Batch-create jobs for all small functions

```console
$ x86decomp llm batch-create games/darkwater-cove/project/ \
    games/darkwater-cove/jobs/ \
    --architecture x86 \
    --image-base 0x400000 \
    --max-bytes 256 \
    --max-attempts 8 \
    --overwrite
```

**What happens:** `llm batch-create` scans the project's `functions/` directory, identifies all function packets with byte size ≤ 256, and generates a job file for each. The output directory receives `batch-create-report.json` with created and blocked counts:

```json
{
  "jobs_created": 487,
  "jobs_blocked": 12,
  "blocked_reasons": {
    "size_exceeds_max": 0,
    "missing_packet": 5,
    "unsupported_instructions": 7
  }
}
```

---

## Step 5: Materialize a prompt (inspection only)

Before running the full match loop, inspect the deterministic prompt:

```console
$ x86decomp llm prompt games/darkwater-cove/jobs/sub_401000.json \
    games/darkwater-cove/project/reports/llm/prompt-sub_401000.json
```

**What happens:** `llm prompt` materializes the exact prompt JSON that will be sent to the LLM — without contacting the model. Useful for reviewing the prompt template, verifying inline bytes, and auditing for reproducibility. The prompt includes function metadata, raw bytes, mnemonics, calling-convention hints, and the required JSON output schema.

---

## Step 6: Run the match loop for a single function

```console
$ x86decomp llm match games/darkwater-cove/project/config/llm/lm-studio-qwen.json \
    games/darkwater-cove/project/config/compiler-profiles/msvc2005-o1.json \
    games/darkwater-cove/jobs/sub_401000.json \
    games/darkwater-cove/match-output/sub_401000/ \
    --max-attempts 8
```

**What happens:** The `llm match` loop runs the full pipeline:

1. **Generate:** Sends the prompt to the LLM, receives a JSON response with a `c_source` field.
2. **Validate:** Checks the response passes the C-source contract (no inline asm, no byte emission, no `__declspec(naked)`).
3. **Compile:** Compiles the proposed C under the MSVC 2005 profile → produces a COFF object.
4. **Extract:** Locates the requested symbol (`_format_dialogue_string@8`) in the COFF.
5. **Relocate:** Resolves all COFF relocations from the job's declared inputs.
6. **Compare:** Byte-compares the resolved candidate against the target bytes.
7. **Loop:** If mismatched and attempts remain, feeds the diff back to the LLM for a revised proposal.

The loop stops on `byte_matched`, a valid `blocked` response, or exhausting `--max-attempts`.

Output directory structure:
```
match-output/sub_401000/
├── attempt_001/
│   ├── prompt.json          # prompt sent to LLM
│   ├── response.json        # raw LLM response
│   ├── candidate.c          # proposed C source
│   ├── compile_report.json  # compiler exit code and output
│   ├── coff_metadata.json   # COFF symbol and section info
│   ├── relocation_report.json # relocation resolution results
│   └── byte_diff.json       # byte comparison report
├── attempt_002/
│   └── ...
├── accepted/
│   ├── source.c             # accepted C source
│   ├── object.obj           # accepted COFF object
│   └── resolved.bin         # resolved bytes (exact match)
└── report.json              # overall match report with status
```

!!! info "Acceptance gate"
    A candidate reaches `byte_matched` only when **all eight** conditions pass: valid JSON response, passes C-source contract, compiler succeeds, output is correct-architecture COFF, symbol exists, all relocations resolve, lengths match, and every byte equals the target. Partial matches — relocation-normalized similarity, instruction similarity, dynamic equivalence — do not satisfy this gate.

---

## Step 7: Verify the match report

```console
$ x86decomp llm verify games/darkwater-cove/match-output/sub_401000/report.json
```

**What happens:** `llm verify` independently re-validates the match report:
- Verifies the report's `status` and attempt invariants
- Checks path containment (no path traversal in the report)
- Re-hashes accepted source, object, and resolved-byte files
- Confirms zero unresolved relocations
- Verifies `accepted.resolved_sha256 == target.sha256`

---

## Step 8: Batch-match the entire job queue

```console
$ x86decomp llm batch-match games/darkwater-cove/project/config/llm/lm-studio-qwen.json \
    games/darkwater-cove/project/config/compiler-profiles/msvc2005-o1.json \
    games/darkwater-cove/jobs/ \
    games/darkwater-cove/match-output/ \
    --max-attempts 8 \
    --max-workers 1
```

**What happens:** `llm batch-match` iterates over every job file in the `jobs/` directory and runs the match loop for each. With `--max-workers 1`, processing is deterministic and single-threaded (v0.7.11 constraint). The output directory receives one subdirectory per function, each with the same structure as step 6.

!!! note "Batch processing time"
    With 487 small functions and `--max-attempts 8`, expect ~2–10 seconds per function depending on LLM inference speed. At ~4 seconds average, the full batch completes in ~32 minutes. Use a machine with GPU acceleration for the LLM backend to minimize inference latency.

---

## Step 9: Promote accepted candidates to the project

For each function with a `byte_matched` report, promote the candidate:

```console
$ x86decomp candidate promote sub_401000 \
    --candidate games/darkwater-cove/match-output/sub_401000/accepted/source.c \
    --report games/darkwater-cove/match-output/sub_401000/report.json \
    --stage matched \
    --update-workflow \
    --project games/darkwater-cove/project/
```

**What happens:** `candidate promote` copies the accepted source into `src/matched/`, creates a provenance record linking the source to the match report, and (with `--update-workflow`) advances the function's workflow state:

```console
$ x86decomp workflow-update games/darkwater-cove/project/ sub_401000 \
    --source-stage matched \
    --matching-status exact_match \
    --candidate format_dialogue_string \
    --compiler-profile config/compiler-profiles/msvc2005-o1.json \
    --report-kind llm_match \
    --report-path match-output/sub_401000/report.json
```

Record evidence for each match:
```console
$ x86decomp evidence-add games/darkwater-cove/project/ \
    --kind verified \
    --source llm-match \
    --locator "sub_401000:llm-exact-match" \
    --assertion "Function sub_401000 byte-matched on attempt 3; 64 bytes identical under MSVC 2005 /O1 /Ob1" \
    --independent-group group-llm-validation \
    --file games/darkwater-cove/match-output/sub_401000/report.json
```

---

## Expected state after each stage

| Stage | Key deliverable |
|---|---|
| **llm providers** | Provider catalog — lm-studio, ollama, llama.cpp, vllm, localai, openai-compatible |
| **llm profile-create** | `config/llm/lm-studio-qwen.json` — validated provider profile |
| **llm probe** | Model list from LM Studio, confirming qwen2.5-coder loaded |
| **llm batch-create** | `jobs/` with 487 job files; `batch-create-report.json` |
| **llm match** | `match-output/sub_401000/` with attempt directories, `accepted/`, and `report.json` |
| **llm verify** | Independent report verification — `valid: true` |
| **llm batch-match** | 487 match-output directories, one per function |
| **candidate promote** | Accepted source in `src/matched/`; workflow state updated |

---

## Verification checklist

- [ ] `llm profile-validate` returns `valid: true`
- [ ] `llm probe` confirms the expected model is loaded
- [ ] `llm batch-create` generates a job for every eligible function packet
- [ ] `llm prompt` materializes a reviewable prompt without contacting the model
- [ ] `llm match` report shows `status: byte_matched` and `attempts_used ≤ max_attempts`
- [ ] `accepted/resolved.bin` byte-identical to target bytes (verify with `diff-bytes`)
- [ ] `llm verify` independently confirms the report's hash chain
- [ ] Promoted candidates appear in `src/matched/` with valid workflow state
- [ ] `verify-project` passes after all promotions

---

## Common failure cases and recovery

| Failure | Cause | Recovery |
|---|---|---|
| `llm probe` fails | LM Studio not running or wrong port | Start LM Studio, load the model, verify port at `http://127.0.0.1:1234` |
| `llm generate` returns invalid JSON | LLM produced malformed output | Increase `--max-attempts`; the match loop feeds parse errors back to the LLM |
| `llm match` exhausts attempts | Function too complex for the model's capability | Lower `--max-bytes` filter, or manually write the C source for this function |
| `llm match` reports `blocked` | LLM declares unsupported instructions | Accept as explicit blocked evidence; hand-write this function |
| Compile step fails in match loop | Proposed C uses invalid syntax | The loop catches compiler errors and feeds them back; increase `--max-attempts` |
| Relocation resolution fails | Symbol references not declared in job inputs | Verify the job file includes all required symbols; re-create with `llm job-create` |
| `llm batch-match` stalls | LLM backend crashed or unresponsive | Check LM Studio logs; restart the backend and re-run batch-match (completed jobs are skipped) |
| `candidate promote` fails | Report path invalid or hash mismatch | Verify the match report with `llm verify` first; only promote verified reports |

---

## Related reference pages

- [Local LLM Commands](../commands/local-llm.md)
- [Local LLM Concepts](../concepts/local-llm.md)
- [LLM Profile Configuration](../config/llm-profile.md)
- [compile](../commands/compilation/compile.md)
- [Compiler Profile](../config/compiler-profile.md)
- [Evidence and Claims](../commands/workflow/evidence-claims.md)
- [Workflow Commands](../commands/workflow/workflow.md)

---

## Optional extensions

1. **Multiple LLM provider round-robin:** Create profiles for LM Studio, Ollama, and llama.cpp. Run `llm match` with different profiles on different function subsets to compare match rates across models. Record results with `corpus-compare`.

2. **Progressive batch refinement:** After a first `llm batch-match` run, identify functions that exhausted attempts. Re-create their jobs with more detailed Ghidra disassembly context (`--mnemonics`), then re-run `llm match` individually.

3. **LLM + symbolic validation hybrid:** For functions that approach but don't reach exact match, run `symbolic-validate` on the closest candidate:
   ```console
   $ x86decomp symbolic-validate target_bytes.bin candidate_bytes.bin \
       --architecture x86 --max-steps 2000 --report symbolic.json
   ```
   If symbolic validation proves equivalence, reclassify the function as `functional` rather than `matching`.

4. **Evidence chain for LLM-accepted functions:** After promoting, create a `claim-create` with evidence from both the `llm verify` report and an independent `diff-function` run against the original PE. This provides multi-source corroboration.

5. **Pipeline automation:** Create a `pipeline-create` manifest with stages: `llm batch-create` → `llm batch-match` → `llm verify` (all matches) → `candidate promote` (byte-matched only) → `evidence-add` (batch). Run with `pipeline-run` for fully automated processing.
