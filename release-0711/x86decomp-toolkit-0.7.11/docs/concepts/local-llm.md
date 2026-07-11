# Local LLM Integration

The local LLM subsystem generates C source proposals from disassembly context. Every proposal
is an **untrusted candidate** — acceptance requires passing deterministic gates: compilation,
COFF extraction, relocation resolution, and exact byte comparison.

## Provider Presets

Six built-in providers cover common local inference servers:

| Provider | Protocol | Default URL | Structured Output |
|---|---|---|---|
| `lm-studio` | `openai-chat` | `http://127.0.0.1:1234/v1` | `openai-json-schema` |
| `ollama` | `ollama-chat` | `http://127.0.0.1:11434` | `ollama-json-schema` |
| `llama.cpp` | `openai-chat` | `http://127.0.0.1:8080/v1` | `openai-json-schema` |
| `vllm` | `openai-chat` | `http://127.0.0.1:8000/v1` | `openai-json-schema` |
| `localai` | `openai-chat` | `http://127.0.0.1:8080/v1` | `openai-json-schema` |
| `openai-compatible` | `openai-chat` | `http://127.0.0.1:8000/v1` | `openai-json-schema` |

## Security Model

### Loopback-Only by Default

All presets default to `127.0.0.1`. Profiles with non-loopback hostnames are rejected
unless `allow_remote: true` is explicitly set:

```json
{
  "provider": "ollama",
  "base_url": "http://192.168.1.50:11434",
  "allow_remote": true
}
```

!!! danger "Remote endpoints"
    Non-loopback endpoints expose proposal generation to network-resident models.
    The toolkit cannot verify the model's identity, training data provenance, or
    output integrity over a remote connection. Use loopback endpoints whenever possible.

### Secrets via Environment Variables

API keys are referenced by environment variable name, never embedded in profiles:

```json
{
  "api_key_env": "OPENAI_API_KEY"
}
```

Headers like `Authorization`, `Proxy-Authorization`, and `Cookie` are forbidden in profile
configuration — use `api_key_env` instead.

## Creating a Profile

```bash
x86decomp llm-profile-create \
  --provider ollama \
  --model "codellama:13b" \
  --output config/llm/codellama.json
```

With custom base URL and API key:

```bash
x86decomp llm-profile-create \
  --provider openai-compatible \
  --model "deepseek-coder-v2" \
  --base-url "http://127.0.0.1:8000/v1" \
  --api-key-env "LLM_API_KEY" \
  --output config/llm/deepseek.json
```

### Profile Settings

| Field | Default | Range | Description |
|---|---|---|---|
| `temperature` | `0.0` | 0.0–2.0 | Sampling temperature (0 = deterministic) |
| `max_tokens` | `4096` | 1–1,000,000 | Maximum response tokens |
| `timeout_seconds` | `180` | 1–3600 | Request timeout |
| `max_response_bytes` | `2,097,152` | 1024–67,108,864 | Maximum response body size |
| `verify_tls` | `true` | bool | Verify TLS certificates |
| `structured_output` | preset default | `openai-json-schema`, `ollama-json-schema`, `none` | Structured output mode |

## Generating a Single Candidate

```bash
x86decomp llm-generate \
  --profile config/llm/codellama.json \
  --job config/llm/jobs/func-401000.json \
  --output build/candidates/func-401000.c
```

The job file specifies the function context:

```json
{
  "id": "job-00401000",
  "function_name": "ProcessInput",
  "symbol": "_ProcessInput@4",
  "architecture": "x86",
  "target_sha256": "abc123...",
  "base_rva": 4198400,
  "image_base": 4194304,
  "target_bytes": "558BEC83EC10...",
  "symbol_map": {},
  "section_placements": [],
  "max_attempts": 8
}
```

### Candidate Validation

Before the C source is written, the candidate passes strict contract validation:

1. **JSON structure**: Response must be exactly `{"status", "c_source", "assumptions", "rationale"}`.
2. **Status check**: Must be `proposed` or `blocked`.
3. **Content checks** (for `proposed`):
   - `c_source` is non-empty.
   - No forbidden patterns: `TODO`, `FIXME`, `...`, inline assembly (`__asm`), machine-byte
     emission (`__emit`), linker pragmas, naked functions.
   - Exactly one function definition with the requested name.
4. **Size limit**: Source must be under 1 MiB.

A `blocked` status with empty source is valid — it means the model declined to propose.

!!! tip "Blocked is information"
    A `blocked` response is still recorded. It tells you the model couldn't produce a
    candidate for this function, which is useful information for prioritization.

## The Match Loop

`llm-match-loop` runs the full generate → compile → compare cycle up to `max_attempts` times:

```bash
x86decomp llm-match-loop \
  --profile config/llm/codellama.json \
  --compiler-profile config/compiler-profiles/msvc-2019-x86.json \
  --job config/llm/jobs/func-401000.json \
  --output-directory build/match-loops/func-401000 \
  --max-attempts 8
```

### Loop Phases

```
Attempt N:
  ┌─────────────┐
  │ 1. GENERATE │── LLM response → candidate.c
  └──────┬──────┘
         ▼
  ┌─────────────┐
  │ 2. COMPILE  │── compiler profile → candidate.obj
  └──────┬──────┘    Fail? → feedback to next attempt
         ▼
  ┌─────────────┐
  │ 3. EXTRACT  │── COFF symbol extraction
  └──────┬──────┘
         ▼
  ┌─────────────┐
  │ 4. RELOCATE │── relocation resolution
  └──────┬──────┘
         ▼
  ┌──────────────┐
  │ 5. COMPARE   │── exact byte comparison
  └──────┬───────┘
         │
    ┌────┴────┐
    │ MATCH?  │── YES → accepted, loop exits
    └────┬────┘
         │ NO → feedback to next attempt
```

### The 8 Conditions for byte_matched

The loop accepts a candidate when ALL of:

1. Compilation succeeded (no compiler errors).
2. COFF machine matches expected (`0x014C` for x86, `0x8664` for x86-64).
3. Symbol extraction from COFF succeeded.
4. Relocation resolution completed (no unresolved relocations).
5. Resolved bytes length equals target bytes length.
6. Exact byte comparison returns `equal: true`.
7. Hash of resolved bytes matches target SHA-256.
8. All artifact files (source, object, resolved bytes) are present and hash-verified.

### Feedback Loop

Failed attempts provide bounded feedback to the next generation:

**Compilation failure:**
```json
{
  "gate": "compile",
  "passed": false,
  "error": "error C2065: 'unregistered_var': undeclared identifier",
  "compiler_stderr": "<...last 12000 chars of stderr...>"
}
```

**Byte mismatch:**
```json
{
  "gate": "byte_match",
  "passed": false,
  "candidate_size": 248,
  "target_size": 256,
  "matching_prefix_bytes": 64,
  "matching_suffix_bytes": 32,
  "reported_mismatches": [
    {"offset": 64, "expected": "8B", "actual": "89"},
    {"offset": 65, "expected": "45", "actual": "C1"}
  ],
  "unresolved_relocations": 0
}
```

### Output Structure

```
build/match-loops/func-401000/
├── report.json
├── attempts/
│   ├── 01/
│   │   ├── prompt.json
│   │   ├── response.json.txt
│   │   ├── candidate.c
│   │   ├── candidate.obj
│   │   ├── compile.json
│   │   ├── relocation.json
│   │   ├── byte-comparison.json
│   │   └── attempt.json
│   ├── 02/
│   │   ...
│   └── 03/
│       ├── candidate.c
│       ├── candidate.obj
│       ├── candidate-resolved.bin
│       └── attempt.json (status: accepted)
├── accepted.c
├── accepted.obj
└── accepted-resolved.bin
```

### Report Status

| Status | Meaning |
|---|---|
| `byte_matched` | An attempt produced byte-identical output; `accepted.c` is the winner |
| `blocked` | The model returned `status: blocked` on the last attempt |
| `exhausted` | All `max_attempts` consumed without a byte match or block |

## Verifying Match Reports

```bash
x86decomp llm-match-verify --report build/match-loops/func-401000/report.json
```

This re-validates:
- Report schema and status consistency.
- All accepted artifact hashes.
- Resolved bytes hash equals target hash.
- No unresolved relocations in accepted output.

## Catalog of Provider Presets

```bash
x86decomp llm-provider-catalog
```

```json
{
  "schema_version": 1,
  "providers": [
    {
      "id": "llama.cpp",
      "protocol": "openai-chat",
      "base_url": "http://127.0.0.1:8080/v1",
      "structured_output": "openai-json-schema"
    },
    {
      "id": "lm-studio",
      "protocol": "openai-chat",
      "base_url": "http://127.0.0.1:1234/v1",
      "structured_output": "openai-json-schema"
    }
  ],
  "security_default": "loopback_only",
  "secrets": "environment variables only"
}
```

## Practical Usage

### Step 1: Start a local model server

```bash
# Ollama
ollama serve
ollama pull codellama:13b

# Or LM Studio — launch the GUI and start the local server on port 1234.
```

### Step 2: Create a profile

```bash
x86decomp llm-profile-create \
  --provider ollama \
  --model "codellama:13b" \
  --output config/llm/codellama.json
```

### Step 3: Prepare a job from a known function

Extract target bytes from the PE, create a job JSON with the function context (assembly
listing, symbol map, section placements).

### Step 4: Run the match loop

```bash
x86decomp llm-match-loop \
  --profile config/llm/codellama.json \
  --compiler-profile config/compiler-profiles/msvc-2019-x86.json \
  --job config/llm/jobs/func-401000.json \
  --output-directory build/match-loops/func-401000
```

### Step 5: Verify and integrate

```bash
x86decomp llm-match-verify --report build/match-loops/func-401000/report.json

# If verified, use accepted.c as the matching source:
cp build/match-loops/func-401000/accepted.c src/matched/00401000.c
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=byte_matched \
  --active-candidate src/matched/00401000.c \
  --report-kind byte_match --report-path build/match-loops/func-401000/report.json
```

!!! warning "Model output is always a proposal"
    The `byte_matched` status is granted by the deterministic gates (compiler + relocation +
    byte comparison), NOT by the model. The model's `rationale` and `assumptions` are
    documented but do not influence acceptance. This is the core safety property of the
    LLM integration.
