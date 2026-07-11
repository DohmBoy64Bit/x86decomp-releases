# serve

## `x86decomp serve`

Serve a read-only project API.

### Purpose

Starts a FastAPI HTTP server that exposes durable project, pipeline, and validation records for inspection. The service is read-only and never mutates project state. Loopback-only by default; binding to a non-loopback address requires the explicit `--allow-remote` flag.

### Syntax

```
x86decomp serve PROJECT [--host HOST] [--port PORT] [--allow-remote]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root directory to serve |

### Options

| Option | Default | Description |
|---|---|---|
| `--host HOST` | `127.0.0.1` | Bind address; loopback by default |
| `--port PORT` | `8765` | TCP port to listen on |
| `--allow-remote` | false | Explicitly authorize binding to a non-loopback address |

!!! warning "Remote access requires explicit authorization"
    Without `--allow-remote`, the server binds only to `127.0.0.1`. Any non-loopback
    `--host` value requires this flag or the command fails.

### API endpoints

The service exposes read-only JSON endpoints for:

- Project structure verification
- Project state health check
- Workflow records per function
- Analysis database queries
- Work queue status
- Worker capability reports
- Pipeline and stage status
- Compilation reports
- Evidence and claim records
- Project memory entries

### Exit behavior

- Runs until interrupted (Ctrl+C), then returns `{"stopped": true}` on stdout
- Exit 2 on argument error or project verification failure

### Example

```console
$ x86decomp serve ./my-project --port 8080

# With remote access authorized:
$ x86decomp serve ./my-project --host 0.0.0.0 --port 8765 --allow-remote
```

### Related commands

- [verify-project](../project/init-verify.md) — Verify project structure and hashes
- [pipeline-status](../pipeline/pipeline.md) — Show pipeline status
