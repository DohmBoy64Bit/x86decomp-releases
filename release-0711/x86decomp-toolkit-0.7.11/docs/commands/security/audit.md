# Security Audit Commands

Deterministic, offline security auditing of source trees and dependency vulnerability scanning.

---

## `x86decomp security-audit`

Audit a source tree for declared security checks.

### Purpose

Performs a deterministic offline audit of a source tree. Scans for hardcoded secrets (PEM private-key blocks, credential-like assignments), world-writable files, and other declared security patterns. The audit is deterministic and does not require network access. Vulnerability databases require an external scanner and are reported as unavailable rather than fabricated.

### Syntax

```
x86decomp security-audit ROOT [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ROOT` | yes | path | Root directory of the source tree to audit |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON audit report to this path |

### Checks performed

| Check | Description |
|---|---|
| Secret patterns | PEM private-key blocks (RSA, OpenSSH), credential-like assignments (`aws_secret_access_key`, `client_secret`) |
| File permissions | World-writable and setuid/setgid files |
| Source inventory | Full file listing with sizes and SHA-256 hashes |

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp security-audit ./src --report reports/security-audit.json
```

---

## `x86decomp dependency-audit`

Run an installed pip-audit adapter and preserve exact findings.

### Purpose

Invokes the `pip-audit` tool (or a declared alternative executable) against the current environment and captures its exact output. Findings are preserved in a structured report. The adapter reports unavailability rather than fabricating results when the tool is not installed.

### Syntax

```
x86decomp dependency-audit [--executable EXE] [--timeout SECONDS] [--report REPORT]
```

### Arguments

None required.

### Options

| Option | Default | Description |
|---|---|---|
| `--executable EXE` | `pip-audit` | Path or name of the pip-audit executable |
| `--timeout SECONDS` | `300` | Maximum time in seconds before the audit is terminated |
| `--report REPORT` | none | Write structured JSON audit report to this path |

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error or tool execution failure
- Reports tool unavailability as structured data, not as a fabricated pass

### Example

```console
$ x86decomp dependency-audit --timeout 600 --report reports/dependency-audit.json

$ x86decomp dependency-audit --executable pip-audit --report reports/dep-audit.json
```

### Related commands

- [security-audit](#x86decomp-security-audit) — Source tree security audit
- [sbom-generate](release.md#x86decomp-sbom-generate) — Generate software bill of materials
- [release-manifest-verify](release.md#x86decomp-release-manifest-verify) — Verify release hash manifest
