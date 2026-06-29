# Security policy — 0.4.0

Treat every target binary, PDB, MAP, object, archive, project backup, compiler, linker, container image, objdiff build, MCP server, Ghidra installation, trace, script, and generated source file as untrusted until verified for its intended use.

## Static-by-default execution policy

The following operations parse, hash, copy, compare, or generate files and do not intentionally execute the target:

- PE/PDB/COFF/archive/MAP inspection;
- target-pack inference and verification;
- project initialization, migration, backup, restore, repair, and GC;
- Ghidra command construction and static artifact import;
- image/byte comparison, metadata recovery, and corpus source generation;
- test-bundle creation/inspection;
- evidence, memory, workflow, release-gate, and reproducibility operations.

External analyzers and compilers still execute their own code. Pin and verify those tools.

## Native and emulated execution

- `dynamic-validate` executes function bytes inside Unicorn. Hostile input can still exercise emulator bugs; isolate the process for untrusted targets.
- `drcov-run` launches a real program through DynamoRIO. Use a disposable VM/sandbox with controlled network, filesystem, credentials, devices, and snapshots.
- `integration-run` requires explicit host consent or an external wrapper. The toolkit records the wrapper contract but cannot certify it as a complete security boundary.
- Unknown native programs must not run on an ordinary developer host.

## Worker isolation

### `local_bounded`

Applies timeout, process-group termination, output bounds, and platform-supported CPU/memory/process limits. It is not a security sandbox.

### `container`

Docker/Podman command generation enforces:

- no network;
- read-only root;
- all capabilities dropped;
- `no-new-privileges`;
- explicit work-directory bind mount;
- bounded memory and PID count;
- ephemeral no-exec `/tmp`.

Use image digests rather than mutable tags for production. Container runtime and kernel vulnerabilities remain outside the toolkit’s assurance boundary.

## Toolchain execution

Compiler, linker, objdiff, Ghidra, DynamoRIO, and registered toolchain commands use argument arrays rather than shell interpolation. Review and record executable paths, hashes, versions, arguments, environment, and inputs. Proprietary/historical compilers are user-owned and must not be bundled or redistributed.

## File, archive, and artifact controls

- Original and supporting artifacts are SHA-256 bound.
- The content store writes objects atomically and addresses them by digest.
- Imported function artifacts reject symlinks and path traversal.
- Test bundles and project restore reject absolute/parent/drive-qualified paths, duplicate names, links, devices, oversized members, excessive expansion, and hash mismatches.
- Project backups reject symlinks and normalize metadata for deterministic output.
- Restore extracts through a staging directory and does not merge into a non-empty destination.
- GC defaults to dry-run and deletes only unreferenced content objects.
- PE patch operations create a new file and can require original-image/function hashes.
- Local decomp.me packets do not upload data.

## Target packs and authorization

A target-pack authorization requirement records operator intent; it is not legal advice or proof of permission. Do not upload or distribute malware, credentials, private keys, packed DRM targets, or proprietary artifacts you lack authority to share.

`allow_host_execution` is an explicit target decision. It is never inferred from the presence of a binary, PDB, test bundle, or generated project.

## MCP and service controls

- Ghidra MCP is read-only by default.
- Mutations require an allowlist, evidence IDs, rationale, persisted proposal, and exact approval hash.
- Re-export and validate after every mutation.
- The FastAPI service is read-only but has no built-in authentication or multi-tenant authorization. Bind to loopback or place behind a trusted authenticated gateway.
- Never expose target artifacts, source, traces, or evidence through a public service without authorization.

## Dependency and release security

- `sbom-generate` inventories the current Python environment; an SBOM is not a vulnerability scan.
- `dependency-audit` uses a real installed `pip-audit` adapter and preserves exact findings/return code.
- If the scanner is absent, the test suite reports it as `BLOCKED`; absence is not a clean scan.
- `security-audit` performs deterministic source-tree checks for unsafe files, symlinks, credential-like material, and release residue.
- `release-manifest-verify` checks every listed source hash.
- The comprehensive test suite isolates pytest from unrelated auto-loaded host plugins and logs every external process separately.

## Sensitive reports

Logs can contain local paths, compiler diagnostics, symbol names, or target-derived values. Review and redact reports before sharing. Do not include proprietary evidence in public bug reports.

## Reporting vulnerabilities

Report the affected version, operating system, exact command, minimal authorized reproducer, expected/actual behavior, and security impact. Do not include third-party proprietary artifacts. For suspected command injection, archive traversal, unsafe execution, evidence tampering, or authorization bypass, stop using the affected path until reviewed.
