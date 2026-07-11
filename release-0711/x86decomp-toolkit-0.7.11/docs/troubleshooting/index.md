# Troubleshooting

This page covers common error scenarios, their causes, confirmation steps, and fixes.
Each entry follows a consistent structure: symptom → cause → confirmation → fix.

## Project Verification Failures

### Hash Mismatch

**Symptom:** `verify-project` reports `critical file changed` or `hash mismatch`.

```
VerificationError: project integrity check failed
failures: ["binary sha256 does not match project.json: expected abc123... got def456..."]
```

**Cause:** The binary file was modified, replaced, or corrupted after project initialization.

**Confirmation:**

```bash
x86decomp verify-project --project .
# Look for the specific file path in failures
```

**Fix:** Restore the original binary from backup, or if the change is intentional (e.g.,
you're working with a patched version), update the project:

```bash
# Check what the current binary hash is
x86decomp inspect-pe --binary original/game.exe | grep sha256

# If intentional: re-initialize or update project.json hash manually
# If unintentional: restore from backup
x86decomp project-restore --project . --backup state/backups/latest.tar.gz
```

**Related commands:** `verify-project`, `project-restore`, `project-backup`

---

### Missing Binary

**Symptom:** `verify-project` reports `binary file is missing`.

```
ContractError: binary file does not exist: C:\projects\myproject\original\game.exe
```

**Cause:** The binary was moved, deleted, or the project directory was relocated.

**Confirmation:**

```bash
Test-Path -LiteralPath "original/game.exe"
# Check project.json for expected path
```

**Fix:** Copy the original binary back to the expected location:

```bash
Copy-Item "C:\backups\game.exe" "original/game.exe"
x86decomp verify-project --project .
```

---

### Schema Version Mismatch

**Symptom:** `verify-project` reports `unsupported project schema version`.

```
ContractError: project schema_version 2 is not supported; current is 3
```

**Cause:** The project was created with an older toolkit version.

**Confirmation:**

```bash
# Check current schema version
Get-Content project.json | ConvertFrom-Json | Select-Object schema_version
```

**Fix:** Migrate the project:

```bash
x86decomp project-migrate --project .
```

!!! warning "Backup before migration"
    Always create a backup before migrating. Schema migrations are one-way.
    ```bash
    x86decomp project-backup --project . --output state/backups/pre-migrate.tar.gz
    x86decomp project-migrate --project .
    ```

**Related commands:** `project-migrate`, `project-backup`

---

### Missing Required Directory

**Symptom:** `verify-project` reports a missing required directory.

```
VerificationError: required project directory does not exist: functions
```

**Cause:** A project directory was deleted manually.

**Confirmation:**

```bash
x86decomp verify-project --project .
# Lists all missing directories
```

**Fix:** Run project repair:

```bash
x86decomp project-repair --project .
```

This recreates missing directories and rebuilds index files.

**Related commands:** `project-repair`, `verify-project`

---

## Compilation Failures

### Missing Executable

**Symptom:** `compile` fails with `ExternalToolError` about a missing compiler.

```
ExternalToolError: [WinError 2] The system cannot find the file specified
```

**Cause:** The compiler specified in the profile is not installed or not on PATH.

**Confirmation:**

```bash
# Check toolchain registration
x86decomp toolchain-verify --toolchain config/toolchains/msvc-2019.json

# Manually check PATH
Get-Command cl.exe -ErrorAction SilentlyContinue
```

**Fix:** Install the compiler or update the profile to point to an available toolchain:

```bash
# Register an available toolchain
x86decomp toolchain-register \
  --name msvc-2019 \
  --compiler "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x86\cl.exe" \
  --output config/toolchains/msvc-2019.json

# Verify it works
x86decomp toolchain-verify --toolchain config/toolchains/msvc-2019.json
```

**Related commands:** `toolchain-register`, `toolchain-verify`, `snapshot-tools`

---

### Compilation Timeout

**Symptom:** `compile` times out with no output.

```
ExternalToolError: compilation timed out after N seconds
```

**Cause:** The compiler is hanging (possibly waiting for input, or an infinite optimization pass).

**Confirmation:**

```bash
# Check the compiler process
Get-Process cl -ErrorAction SilentlyContinue
```

**Fix:** Increase timeout or reduce optimization level. Check the compiler profile:

```json
{
  "timeout_seconds": 300,
  "arguments": ["/O1", "/c", "{source}", "/Fo{output}"]
}
```

For complex files, increase to 600 seconds. For suspected hangs, try `/Od` (no optimization)
to verify the source is valid.

---

### Architecture Mismatch

**Symptom:** LLM match loop reports `architecture` gate failure.

```
gate: architecture
error: compiler produced machine 0x8664; expected 0x014C
```

**Cause:** The compiler produced x86-64 code but the target is x86 (or vice versa).

**Confirmation:**

```bash
x86decomp coff-inspect --input candidate.obj | grep machine
```

**Fix:** Verify the compiler profile targets the correct architecture. For MSVC, check
the `bin` path (`x86` vs `x64`) and ensure no conflicting `/arch` flags.

**Related commands:** `coff-inspect`, `compile`

---

## Dynamic Validation Errors

### Unicorn Not Installed

**Symptom:** `dynamic-validate` fails with `ImportError`.

```
ExternalToolError: Unicorn is required for dynamic validation; install x86decomp-toolkit[dynamic]
```

**Cause:** The Unicorn emulation engine Python package is not installed.

**Confirmation:**

```bash
pip show unicorn
```

**Fix:**

```bash
pip install "x86decomp-toolkit[dynamic]"
```

Or directly:

```bash
pip install unicorn
```

**Related commands:** `dynamic-validate`

---

### Harness Issues

**Symptom:** `dynamic-validate` reports harness generation failure.

```
ExternalToolError: harness generation failed: function at 0x401000 imports unresolved symbol 'GetModuleHandleA'
```

**Cause:** The function references external symbols that the harness cannot resolve.

**Confirmation:**

```bash
x86decomp coff-inspect --input original/game.exe
# Check import table for unresolved symbols
```

**Fix:** Provide stub implementations for imported functions in a harness configuration:

```json
{
  "stubs": {
    "GetModuleHandleA": {
      "convention": "stdcall",
      "return": "module_handle",
      "arguments": ["lpModuleName"]
    }
  }
}
```

Then regenerate:

```bash
x86decomp harness-generate \
  --pe original/game.exe \
  --function-rva 0x401000 \
  --config config/harnesses/function-401000.json \
  --output tests/harnesses/func-401000
```

**Related commands:** `harness-generate`, `dynamic-validate`

---

### Differential Validation Timeout

**Symptom:** `dynamic-validate` times out after the configured limit.

```
ExternalToolError: dynamic validation timeout
```

**Cause:** One or both functions entered an infinite loop or the input space is too large.

**Confirmation:**

```bash
# Check the validation report
Get-Content reports/functional/00401000-dynamic.json | ConvertFrom-Json | Select-Object *
```

**Fix:**
- Reduce `max_instructions` in the validation config.
- Implement loop detection in the harness (bounded loop iteration cap).
- Add an iteration limit to the test input generation.

---

## Ghidra Export Failures

### analyzeHeadless Not Found

**Symptom:** `ghidra-export` fails with `ExternalToolError`.

```
ExternalToolError: analyzeHeadless not found at C:\ghidra\support\analyzeHeadless.bat
```

**Cause:** The `--ghidra-home` path is incorrect or Ghidra is not installed.

**Confirmation:**

```bash
Test-Path -LiteralPath "C:\ghidra_11.0_PUBLIC\support\analyzeHeadless.bat"
```

**Fix:** Provide the correct Ghidra installation path:

```bash
x86decomp ghidra-export \
  --ghidra-home "C:\ghidra_11.0_PUBLIC" \
  --project "C:\ghidra-projects\MyProject" \
  --program game.exe \
  --output-dir ./analysis/ghidra
```

---

### Java Not Found

**Symptom:** `ghidra-export` fails with Java-related error.

```
ExternalToolError: JAVA_HOME not set or java not on PATH
```

**Cause:** Java is not installed or `JAVA_HOME` is not configured.

**Confirmation:**

```bash
java -version
# or
$env:JAVA_HOME
```

**Fix:** Install Java 17+ (required by Ghidra 11+) and set `JAVA_HOME`:

```bash
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
```

Or pass Java arguments directly:

```bash
x86decomp ghidra-export \
  --ghidra-home "C:\ghidra_11.0_PUBLIC" \
  --project "C:\ghidra-projects\MyProject" \
  --program game.exe \
  --output-dir ./analysis/ghidra \
  --java-args "-Xmx4G"
```

---

### Ghidra Export Timeout

**Symptom:** `ghidra-export` times out.

```
ExternalToolError: Ghidra export process timed out
```

**Cause:** The program is large or Ghidra hasn't completed analysis.

**Confirmation:** Check if Ghidra is still analyzing the program (open it in Ghidra GUI).

**Fix:** Increase timeout or run analysis before export:

```bash
x86decomp ghidra-export \
  --ghidra-home "C:\ghidra_11.0_PUBLIC" \
  --project "C:\ghidra-projects\MyProject" \
  --program game.exe \
  --output-dir ./analysis/ghidra \
  --timeout 3600
```

!!! tip "Pre-analyze in Ghidra GUI"
    Open the program in Ghidra GUI, auto-analyze it, save, and close before running
    headless exports. This skips analysis during export and avoids timeouts.

---

### Project Not Found

**Symptom:** `ghidra-export` reports project doesn't exist.

```
ExternalToolError: Ghidra project not found: C:\ghidra-projects\MyProject
```

**Cause:** The project path is incorrect or the project was moved.

**Confirmation:**

```bash
Test-Path -LiteralPath "C:\ghidra-projects\MyProject\MyProject.gpr"
```

**Fix:** Provide the correct path. The `--project` argument must point to the directory
containing the `.gpr` file, not the `.gpr` file itself.

---

## MCP Connection Issues

### Server Not Running

**Symptom:** `mcp-tools` or `mcp-read` fails to connect.

```
ExternalToolError: MCP server exited with 1: ModuleNotFoundError: No module named 'ghidra_mcp'
```

**Cause (stdio):** The MCP server command is wrong or the Python package is not installed.

**Cause (HTTP):** The MCP server is not running at the specified URL.

**Confirmation (stdio):**

```bash
python -m ghidra_mcp.server --help
```

**Confirmation (HTTP):**

```bash
curl http://127.0.0.1:8080/mcp
```

**Fix (stdio):** Install the Ghidra MCP server package and verify the command:

```bash
pip install ghidra-mcp
python -m ghidra_mcp.server --help
```

**Fix (HTTP):** Start the server before using MCP commands. The toolkit does not manage
the server lifecycle.

---

### Pipe/Socket Closed

**Symptom:** MCP command fails mid-operation.

```
ExternalToolError: MCP server closed stdout
```

**Cause:** The MCP server process crashed or was terminated.

**Confirmation:**

```bash
# Check for zombie processes
Get-Process python -ErrorAction SilentlyContinue
```

**Fix:** Restart the MCP server. For stdio transport, each command starts a fresh
subprocess, so the issue is transient. For HTTP transport, restart the server daemon.

---

### Protocol Version Mismatch

**Symptom:** `mcp-read` reports protocol error during initialize.

```
ExternalToolError: MCP initialize error: unsupported protocol version
```

**Cause:** The MCP server uses a protocol version incompatible with `2025-06-18`.

**Confirmation:** Check the MCP server's supported protocol versions.

**Fix:** Update the MCP server to one that supports the 2025-06-18 protocol, or use a
compatible version.

---

## Pipeline Recovery

### Pipeline Stage Failed

**Symptom:** `pipeline-run` stops with a stage failure.

```
Pipeline stage "compile-candidates" failed: ExternalToolError: compilation failed
```

**Cause:** A stage's command failed (compilation error, missing tool, timeout).

**Confirmation:**

```bash
x86decomp pipeline-status --pipeline orchestration/pipelines/default.json
```

**Fix:**

1. Inspect the failed stage's output in `orchestration/logs/`.
2. Fix the underlying issue (missing tool, invalid source, etc.).
3. Retry the stage:

```bash
x86decomp pipeline-retry --pipeline orchestration/pipelines/default.json --stage compile-candidates
```

### Pipeline Hanging

**Symptom:** `pipeline-run` never completes.

**Cause:** A stage is waiting on an external resource or has no timeout configured.

**Confirmation:**

```bash
x86decomp pipeline-status --pipeline orchestration/pipelines/default.json
```

**Fix:** Cancel and retry with a timeout:

```bash
x86decomp pipeline-cancel --pipeline orchestration/pipelines/default.json
# Edit the pipeline manifest to add timeout_seconds to the hanging stage
x86decomp pipeline-retry --pipeline orchestration/pipelines/default.json --stage waiting-stage
```

**Related commands:** `pipeline-run`, `pipeline-status`, `pipeline-cancel`, `pipeline-retry`

---

## Project Migration Failures

### Migration Pre-Check Failed

**Symptom:** `project-migrate` refuses to run.

```
ContractError: cannot migrate: project has uncommitted changes in state database
```

**Cause:** The project state database has pending changes that must be resolved.

**Confirmation:**

```bash
x86decomp project-repair --project .
```

**Fix:** Run repair first, then retry migration:

```bash
x86decomp project-repair --project .
x86decomp project-migrate --project .
```

### Migration Rollback Needed

**Symptom:** Migration completed but project is in an inconsistent state.

```
VerificationError: post-migration verification failed
```

**Cause:** Schema migration produced an invalid project state.

**Confirmation:**

```bash
x86decomp verify-project --project .
```

**Fix:** Restore from the pre-migration backup:

```bash
x86decomp project-restore --project . --backup state/backups/pre-migrate-20260711.tar.gz
```

The migration process automatically creates a backup before applying changes. The backup
path is recorded in the `migrations` table of the state database.

**Related commands:** `project-migrate`, `project-restore`, `project-backup`

---

## Backup Restore Issues

### Backup Verification Failed

**Symptom:** `project-restore` reports the backup is invalid.

```
ContractError: backup integrity check failed: manifest hash mismatch
```

**Cause:** The backup archive was modified or corrupted after creation.

**Confirmation:**

```bash
# Check backup file
Get-Item -LiteralPath "state/backups/latest.tar.gz" | Select-Object Length, LastWriteTime
```

**Fix:** Use a different backup. If no backups are available, reconstruct from project
files and re-verify:

```bash
x86decomp project-repair --project .
x86decomp verify-project --project .
```

---

### Restore Over Active Project

**Symptom:** `project-restore` warns about overwriting current state.

**Cause:** The project directory contains files that would be overwritten.

**Confirmation:**

```bash
x86decomp project-repair --project .
```

**Fix:** Back up the current state first, then restore:

```bash
x86decomp project-backup --project . --output state/backups/pre-restore-current.tar.gz
x86decomp project-restore --project . --backup state/backups/desired.tar.gz
```

---

### Content Store Mismatch

**Symptom:** `content-verify` reports missing or corrupted content.

```
ContractError: content verification failed for sha256:abc123... (missing)
```

**Cause:** Content-addressed files in the artifacts store were deleted or corrupted.

**Confirmation:**

```bash
x86decomp content-verify --store artifacts
```

**Fix:** Restore missing content from backup or regenerate:

```bash
x86decomp project-restore --project . --backup state/backups/latest.tar.gz
# Or regenerate from source:
x86decomp compile --profile config/compiler-profiles/msvc-2019-x86.json \
  --source src/matched/00401000.c --output build/candidates/00401000.obj
x86decomp content-put --store artifacts --file build/candidates/00401000.obj
```

**Related commands:** `content-put`, `content-verify`

---

## Work Queue Issues

### No Eligible Tasks

**Symptom:** `work-next` returns null.

```
null
```

**Cause:** All tasks are either claimed, completed, or blocked by dependencies.

**Confirmation:**

```bash
# Check work queue status via direct query
x86decomp db-query --project . --sql "SELECT * FROM work_queue WHERE status = 'pending'"
```

**Fix:** Create new tasks or unblock existing ones:

```bash
x86decomp work-create --project . --kind matching --subject pe-rva:00401000 \
  --description "Match function 0x401000 to MSVC 2019 /O2"
```

**Related commands:** `work-create`, `work-next`, `work-claim`

---

## Memory Ledger Issues

### Ledger Integrity Failure

**Symptom:** `memory-verify` reports hash chain break.

```
VerificationError: memory ledger hash chain broken at line 42
```

**Cause:** A memory entry was manually edited or the events file was truncated.

**Confirmation:**

```bash
x86decomp memory-verify --project .
```

**Fix:** Entries cannot be repaired individually. Restore from backup:

```bash
x86decomp project-restore --project . --backup state/backups/latest.tar.gz
```

Or if the loss is acceptable, render the valid prefix:

```bash
x86decomp memory-render --project . --output memory-valid-prefix.md
```

!!! danger "Never edit memory/events.jsonl manually"
    The memory ledger is a hash-chained append-only log. Manual edits break the chain
    irreversibly. Always use `memory-add` for new entries.

**Related commands:** `memory-add`, `memory-verify`, `memory-render`
