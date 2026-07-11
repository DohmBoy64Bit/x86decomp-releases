# Local LLM Commands

Bounded local-model C proposal generation with deterministic byte matching via compilation, relocation resolution, and exact byte comparison. All LLM output is an untrusted proposal; acceptance requires deterministic gates.

## Command group

The `llm` command group uses canonical routing:

```bash
x86decomp llm [--project .] [--actor analyst] ACTION [ARGS...]
```

## `llm providers`

List built-in local-model provider presets.

```bash
x86decomp llm providers
```

No subcommand arguments. Returns the provider catalog with protocol, default base URL, and structured output capability for each preset.

| Provider | Protocol | Default URL | Structured Output |
|---|---|---|---|
| `lm-studio` | openai-chat | `http://127.0.0.1:1234/v1` | `openai-json-schema` |
| `ollama` | ollama-chat | `http://127.0.0.1:11434` | `ollama-json-schema` |
| `llama.cpp` | openai-chat | `http://127.0.0.1:8080/v1` | `openai-json-schema` |
| `vllm` | openai-chat | `http://127.0.0.1:8000/v1` | `openai-json-schema` |
| `localai` | openai-chat | `http://127.0.0.1:8080/v1` | `openai-json-schema` |
| `openai-compatible` | openai-chat | `http://127.0.0.1:8000/v1` | `openai-json-schema` |

---

## `llm profile-create`

Create a validated local-model provider profile.

```bash
x86decomp llm profile-create PROVIDER OUTPUT \
  --model MODEL [--base-url URL] [--id ID] \
  [--api-key-env ENV] [--allow-remote]
```

| Argument | Required | Description |
|---|---|---|
| `PROVIDER` | yes | Provider preset ID (one from `llm providers`) |
| `OUTPUT` | yes | Path for the generated profile JSON |
| `--model` | yes | Model identifier (e.g. `codellama:13b`, `qwen2.5-coder`) |
| `--base-url` | no | Override the default base URL |
| `--id` | no | Explicit profile identifier |
| `--api-key-env` | no | Environment variable name for the API key |
| `--allow-remote` | no | Permit non-loopback endpoints |

!!! danger "Remote endpoints"
    All presets default to `127.0.0.1`. Non-loopback hostnames are rejected unless `--allow-remote` is explicitly supplied. Remote inference changes the data-disclosure boundary.

### Examples

```bash
# Ollama local profile
x86decomp llm profile-create ollama ./config/llm/codellama.json --model codellama:13b

# LM Studio profile
x86decomp llm profile-create lm-studio ./config/llm/lm-studio.json --model loaded-model-id

# OpenAI-compatible with API key
x86decomp llm profile-create openai-compatible ./config/llm/deepseek.json \
  --model deepseek-coder-v2 \
  --base-url http://127.0.0.1:8000/v1 \
  --api-key-env LLM_API_KEY
```

---

## `llm profile-validate`

Validate a local-model provider profile.

```bash
x86decomp llm profile-validate PROFILE
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the profile JSON file |

Validates the profile schema, loopback enforcement, and credential hygiene.

### Example

```bash
x86decomp llm profile-validate ./config/llm/codellama.json
```

---

## `llm probe`

Probe the provider model-list endpoint without generating text.

```bash
x86decomp llm probe PROFILE
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the profile JSON file |

Returns the list of available models from the server.

### Example

```bash
x86decomp llm probe ./config/llm/codellama.json
```

---

## `llm job-create`

Create a local-LLM job from a function packet.

```bash
x86decomp llm job-create FUNCTION_PACKET OUTPUT \
  --architecture {x86,x86_64} \
  [--image-base 0] [--function-name NAME] [--symbol SYM] \
  [--max-attempts 4] [--inline] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `FUNCTION_PACKET` | yes | Path to the function packet JSON |
| `OUTPUT` | yes | Path for the generated job file |
| `--architecture` | yes | Target architecture: `x86` or `x86_64` |
| `--image-base` | no | Image base address (default: `0`) |
| `--function-name` | no | Requested C function name |
| `--symbol` | no | COFF symbol name |
| `--max-attempts` | no | Maximum match-loop attempts (default: `4`) |
| `--inline` | no | Inline target bytes and mnemonics into the job file |
| `--overwrite` | no | Overwrite existing output file |

### Example

```bash
x86decomp llm job-create ./artifacts/packets/00401000.json ./jobs/func-401000.json \
  --architecture x86 --function-name ProcessInput --symbol _ProcessInput@4 \
  --image-base 0x400000 --max-attempts 8 --inline
```

---

## `llm job-from-range`

Create a local-LLM job from an explicit byte range.

```bash
x86decomp llm job-from-range IMAGE OUTPUT \
  --rva RVA --size SIZE \
  --architecture {x86,x86_64} \
  --function-name NAME \
  [--symbol SYM] [--image-base 0] [--mnemonics PATH] \
  [--max-attempts 4] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `IMAGE` | yes | Path to the PE image file |
| `OUTPUT` | yes | Path for the generated job file |
| `--rva` | yes | Relative virtual address of the function |
| `--size` | yes | Size in bytes of the function |
| `--architecture` | yes | Target architecture: `x86` or `x86_64` |
| `--function-name` | yes | Requested C function name |
| `--symbol` | no | COFF symbol name |
| `--image-base` | no | Image base address (default: `0`) |
| `--mnemonics` | no | Path to a mnemonic listing file |
| `--max-attempts` | no | Maximum match-loop attempts (default: `4`) |
| `--overwrite` | no | Overwrite existing output file |

!!! note
    This command does not infer PE section mappings. It extracts the raw byte range at the given RVA.

### Example

```bash
x86decomp llm job-from-range ./original.exe ./jobs/func-401000.json \
  --rva 0x1000 --size 80 --architecture x86 \
  --function-name ProcessInput --image-base 0x400000
```

---

## `llm batch-create`

Create local-LLM jobs for eligible project function packets.

```bash
x86decomp llm batch-create PROJECT_ROOT OUTPUT_DIRECTORY \
  --architecture {x86,x86_64} \
  [--image-base 0] [--max-bytes 256] [--max-attempts 4] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT_ROOT` | yes | Path to the project root |
| `OUTPUT_DIRECTORY` | yes | Output directory for generated job files |
| `--architecture` | yes | Target architecture: `x86` or `x86_64` |
| `--image-base` | no | Image base address (default: `0`) |
| `--max-bytes` | no | Maximum function byte size to include (default: `256`) |
| `--max-attempts` | no | Maximum match-loop attempts per job (default: `4`) |
| `--overwrite` | no | Overwrite existing output files |

Generates a `batch-create-report.json` in the output directory with created and blocked counts.

### Example

```bash
x86decomp llm batch-create ./myproject ./batch-jobs \
  --architecture x86 --image-base 0x400000 --max-bytes 512
```

---

## `llm prompt`

Materialize the deterministic prompt without contacting a model.

```bash
x86decomp llm prompt JOB OUTPUT
```

| Argument | Required | Description |
|---|---|---|
| `JOB` | yes | Path to the job JSON file |
| `OUTPUT` | yes | Path for the generated prompt file |

Useful for review, reproducibility, and prompt-hash comparison. No model is contacted.

### Example

```bash
x86decomp llm prompt ./jobs/func-401000.json ./prompts/func-401000.json
```

---

## `llm generate`

Generate one uncompiled C proposal.

```bash
x86decomp llm generate PROFILE JOB OUTPUT \
  [--report PATH] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the LLM profile JSON |
| `JOB` | yes | Path to the job JSON file |
| `OUTPUT` | yes | Path for the generated C source file |
| `--report` | no | Path for the generation report |
| `--overwrite` | no | Overwrite existing output file |

The output is an untrusted proposal. The report claim is `proposal_only`.

### Example

```bash
x86decomp llm generate ./config/llm/codellama.json ./jobs/func-401000.json \
  ./candidates/func-401000.c --report ./reports/gen-401000.json
```

---

## `llm cpp-generate`

Generate one bounded C++ proposal using a local-model profile.

```bash
x86decomp llm cpp-generate PROFILE JOB OUTPUT \
  [--class-context PATH] [--report PATH] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the LLM profile JSON |
| `JOB` | yes | Path to the job JSON file |
| `OUTPUT` | yes | Path for the generated C++ source file |
| `--class-context` | no | Path to a class-context JSON file |
| `--report` | no | Path for the generation report |
| `--overwrite` | no | Overwrite existing output file |

!!! warning "Proposal-only"
    `cpp-generate` is proposal-only. It does not change the v0.7.5 exact-byte acceptance boundary. C++ proposals do not participate in the closed exact-match loop.

### Example

```bash
x86decomp llm cpp-generate ./config/llm/codellama.json ./jobs/func-401000.json \
  ./candidates/func-401000.cpp \
  --class-context ./context/classes.json \
  --report ./reports/cpp-gen-401000.json
```

---

## `llm match`

Run bounded generation, compilation, relocation resolution, and exact byte matching.

```bash
x86decomp llm match PROFILE COMPILER_PROFILE JOB OUTPUT_DIRECTORY \
  [--max-attempts N] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the LLM profile JSON |
| `COMPILER_PROFILE` | yes | Path to the compiler profile JSON |
| `JOB` | yes | Path to the job JSON file |
| `OUTPUT_DIRECTORY` | yes | Output directory for all loop artifacts |
| `--max-attempts` | no | Override the job's max attempts |
| `--overwrite` | no | Overwrite existing output directory |

The loop stops when exact byte identity is established, the model returns a valid `blocked` response, or the attempt limit is exhausted. Each attempt preserves the prompt, model response, candidate C, compiler report, COFF symbol metadata, relocation resolution report, and exact byte-comparison report.

### Acceptance gate

A candidate reaches `byte_matched` only when **all** of:

1. Response is exactly one valid JSON object with required keys
2. Proposed source passes the C-source contract
3. Compiler profile completes successfully
4. Output is a COFF object for the declared architecture
5. Requested symbol exists with one extractable function body
6. Every COFF relocation resolves from explicit job inputs
7. Resolved candidate length equals target length
8. Every resolved candidate byte equals the target byte

### Example

```bash
x86decomp llm match ./config/llm/codellama.json \
  ./config/compiler-profiles/msvc-2019-x86.json \
  ./jobs/func-401000.json \
  ./match-output/func-401000 \
  --max-attempts 8
```

---

## `llm batch-match`

Run bounded match loops for a deterministic job queue.

```bash
x86decomp llm batch-match PROFILE COMPILER_PROFILE JOBS OUTPUT_DIRECTORY \
  [--max-workers 1] [--max-attempts N] [--overwrite]
```

| Argument | Required | Description |
|---|---|---|
| `PROFILE` | yes | Path to the LLM profile JSON |
| `COMPILER_PROFILE` | yes | Path to the compiler profile JSON |
| `JOBS` | yes | Path to the job queue directory |
| `OUTPUT_DIRECTORY` | yes | Output directory for match results |
| `--max-workers` | no | Maximum concurrent workers (default: `1`) |
| `--max-attempts` | no | Override per-job max attempts |
| `--overwrite` | no | Overwrite existing output |

!!! note "Single-worker deterministic"
    v0.7.11 batch-match is deterministic and single-worker. Pass `--max-workers 1`.

### Example

```bash
x86decomp llm batch-match ./config/llm/codellama.json \
  ./config/compiler-profiles/msvc-2019-x86.json \
  ./batch-jobs \
  ./batch-output \
  --max-attempts 8
```

---

## `llm verify`

Verify a local-model byte-match report and accepted artifact hashes.

```bash
x86decomp llm verify REPORT
```

| Argument | Required | Description |
|---|---|---|
| `REPORT` | yes | Path to the `report.json` from a match-loop output directory |

Verifies status and attempt invariants, path containment, accepted source/object/resolved-byte hashes, zero unresolved relocations, and equality between the accepted resolved-byte hash and target hash.

### Example

```bash
x86decomp llm verify ./match-output/func-401000/report.json
```

---

## Security boundary

- Profiles are loopback-only by default; use `--allow-remote` to override
- API keys via environment variable name only; never embedded in profiles
- Same-origin-only redirects; bounded request timeouts and response sizes
- TLS verification enabled by default
- No native target execution; no direct workflow-state mutation
- Strict source rejection for inline assembly, byte emission, naked functions

!!! warning "Untrusted proposals"
    LLM output is an untrusted proposal at every stage. The `byte_matched` status is granted exclusively by deterministic gates (compiler, relocation resolution, byte comparison). Relocation-normalized similarity, instruction similarity, finite dynamic equivalence, and model confidence do not satisfy this gate.
