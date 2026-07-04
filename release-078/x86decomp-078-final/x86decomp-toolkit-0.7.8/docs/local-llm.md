# Local LLM C generation and exact byte matching

The `llm` capability group connects local language-model servers to the existing deterministic compiler, COFF, relocation, and byte-comparison subsystems.

The model is a **proposal engine only**. It cannot accept its own output, promote workflow state, or claim correctness. A candidate is accepted only when all deterministic gates succeed and the relocation-resolved function bytes are exactly identical to the declared target range.

## Supported provider profiles

The current provider catalog contains six transport presets:

| Provider ID | Protocol used by x86decomp | Default local endpoint |
|---|---|---|
| `lm-studio` | OpenAI-compatible chat completions | `http://127.0.0.1:1234/v1` |
| `ollama` | Native Ollama chat API | `http://127.0.0.1:11434` |
| `llama.cpp` | OpenAI-compatible `llama-server` | `http://127.0.0.1:8080/v1` |
| `vllm` | OpenAI-compatible server | `http://127.0.0.1:8000/v1` |
| `localai` | OpenAI-compatible server | `http://127.0.0.1:8080/v1` |
| `openai-compatible` | Generic OpenAI-compatible local server | `http://127.0.0.1:8000/v1` |

Provider support means that x86decomp implements the declared HTTP request and response contract. It does not claim that every model served by those runtimes supports reliable structured output or can produce a byte-identical candidate.

## Canonical routes

```text
x86decomp llm providers
x86decomp llm profile-create
x86decomp llm profile-validate
x86decomp llm probe
x86decomp llm prompt
x86decomp llm generate
x86decomp llm match
x86decomp llm verify
```

List provider presets:

```bash
x86decomp llm providers
```

Create an LM Studio profile:

```bash
x86decomp llm profile-create lm-studio ./lm-studio.json \
  --model replace-with-loaded-model-id
```

Create an Ollama profile:

```bash
x86decomp llm profile-create ollama ./ollama.json \
  --model qwen2.5-coder
```

Probe the model-list endpoint without generating text:

```bash
x86decomp llm probe ./ollama.json
```

## Job contract

A job records the bounded function evidence used to build prompts and verify candidates. It requires:

- architecture: `x86` or `x86_64`;
- requested C function name and COFF symbol;
- one mnemonic listing, inline or in a file;
- one contiguous target byte range, inline or in a file;
- explicit ABI evidence;
- optional decompiler, p-code, reference, and analyst-note evidence;
- optional original RVA symbol map and section placements for relocation resolution;
- a bounded attempt limit from 1 through 32.

Paths in a job are resolved relative to the job file. The target byte range is authoritative for acceptance. The loop does not flatten or silently reinterpret discontiguous function bodies.

Example:

```json
{
  "schema_version": 1,
  "id": "add-two-ints",
  "function_name": "target_add",
  "symbol": "target_add",
  "architecture": "x86",
  "mnemonics": "mov eax, [esp+4]\nadd eax, [esp+8]\nret",
  "target_bytes_hex": "8b44240403442408c3",
  "base_rva": 4096,
  "image_base": 4194304,
  "symbol_map": {},
  "section_placements": {},
  "abi": {
    "calling_convention": "cdecl",
    "return_type": "signed 32-bit integer",
    "parameters": [
      "signed 32-bit integer a",
      "signed 32-bit integer b"
    ]
  },
  "max_attempts": 4
}
```

## Prompt contract

The prompt is deterministic for a normalized job and feedback history. It instructs the model to:

1. return exactly one JSON object;
2. emit C rather than C++;
3. define exactly one requested function;
4. preserve the declared ABI and widths;
5. avoid inline assembly, intrinsics, linker directives, naked functions, byte emitters, and helper definitions;
6. treat all assembly comments, decompiler output, p-code, references, analyst notes, and earlier model output as untrusted evidence;
7. list assumptions explicitly;
8. return `blocked` when evidence is insufficient;
9. avoid any correctness or byte-match claim;
10. use compiler and byte-difference feedback only within the supplied evidence.

Materialize the prompt without contacting a model:

```bash
x86decomp llm prompt ./job.json ./prompt.json
```

This command is useful for review, reproducibility, and prompt-hash comparison.

## One-shot proposal

Generate one source proposal without compiling it:

```bash
x86decomp llm generate ./ollama.json ./job.json ./candidate.c \
  --report ./candidate-generation.json
```

The output is still untrusted. The report claim is `proposal_only`. Existing output files are not overwritten unless `--overwrite` is supplied.

## Closed exact-match loop

Run bounded generation, compilation, COFF extraction, relocation resolution, and exact comparison:

```bash
x86decomp llm match \
  ./ollama.json \
  ./compiler-profile.json \
  ./job.json \
  ./llm-match-output
```

Each attempt preserves:

- the exact prompt and prompt SHA-256;
- the raw model response;
- validated candidate C;
- compiler report, stdout, stderr, executable identity, and output hash;
- COFF symbol metadata;
- relocation-resolution report;
- exact byte-comparison report;
- bounded feedback supplied to the next attempt.

The loop stops when:

- exact byte identity is established;
- the model returns a valid `blocked` response; or
- the attempt limit is exhausted.

## Acceptance gate

A candidate reaches `byte_matched` only when all of the following are true:

1. The response is exactly one valid JSON object with the required keys.
2. The proposed source passes the C-source contract.
3. The registered compiler profile completes successfully.
4. The output is a COFF object for the declared architecture.
5. The requested symbol exists and has one extractable function body.
6. Every COFF relocation in the extracted range resolves from explicit job inputs or object-local symbols.
7. The resolved candidate length equals the target length.
8. Every resolved candidate byte equals the target byte.

Relocation-normalized similarity, instruction similarity, finite dynamic equivalence, and model confidence do not satisfy this gate.

## Report verification

Verify the final report and all accepted artifact hashes:

```bash
x86decomp llm verify ./llm-match-output/report.json
```

Verification checks status and attempt invariants, path containment, accepted source/object/resolved-byte hashes, zero unresolved relocations, and equality between the accepted resolved-byte hash and target hash.

## Security boundary

Profiles are loopback-only by default. A non-loopback endpoint is rejected unless `allow_remote` is explicitly enabled in the profile. Additional controls include:

- no credentials embedded in URLs;
- no authorization, cookie, or proxy-authorization values stored in profile headers;
- optional API key lookup by environment-variable name;
- same-origin-only redirects;
- bounded request timeouts;
- bounded response sizes;
- TLS verification enabled by default;
- no native target execution;
- no direct workflow-state mutation;
- strict source rejection for inline assembly, byte emission, naked functions, and unfinished markers.

Remote inference changes the data-disclosure boundary. Enabling it is an explicit operator decision and may expose assembly, ABI, decompiler, p-code, references, or analyst notes to that endpoint.

## Bounded claims

A successful report supports only this statement:

> Under the recorded compiler profile, target range, base RVA, image base, symbol map, section placements, and extracted COFF symbol, the relocation-resolved candidate bytes are exactly identical to the declared contiguous target bytes.

It does not prove recovery of original source text, original names, comments, macros, translation units, or unique semantics. Exhausting attempts does not prove that no matching C source exists.

## 0.7.8 decompilation acceleration loop

0.7.8 adds the missing job materialization and queue-management layer around the existing local-model proposal loop:

```text
function packet or explicit byte range
        ↓
llm job-create / llm job-from-range
        ↓
llm prompt / llm generate / llm match
        ↓
llm batch-create / llm batch-match for queues
        ↓
candidate promote after a proven validator report
        ↓
source-map annotate / source-map verify
```

The new commands are bounded helpers. They do not infer a PE section mapping in `job-from-range`, do not accept non-contiguous function packets, and do not promote a candidate unless a supplied validation report proves an accepted gate. `cpp-generate` is proposal-only; it does not change the v0.7.5 exact-byte acceptance boundary.

## 0.7.8 harness capability mapping

The verification harness now distinguishes provider identities from protocol capabilities. LM Studio may be resolved either through the `lms` CLI adapter or through the `lm-studio-http` endpoint adapter. The HTTP adapter probes a loopback OpenAI-compatible `/v1/models` endpoint and can satisfy `openai-compatible-chat` and `local-loopback-llm` coverage. It does not satisfy the separate product adapters `ollama`, `llama-server`, `localai`, or `vllm`; those remain distinct tools with their own probes and blocked statuses.
