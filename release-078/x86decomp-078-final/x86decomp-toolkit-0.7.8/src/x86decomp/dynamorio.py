"""DynamoRIO drcov execution and text-log normalization.

This backend executes a user-authorized program under ``drrun -t drcov`` and
parses the text basic-block table. It never executes target programs implicitly;
the caller must invoke the command and supply the executable and arguments.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError, FormatError
from .util import sha256_file, utc_now, write_json

_MODULE_HEADER = re.compile(r"^Module Table:\s*version\s+(?P<version>\d+),\s*count\s+(?P<count>\d+)", re.I)
_BB_HEADER = re.compile(r"^BB Table:\s*(?P<count>\d+)\s+bbs", re.I)
_MODULE_LINE = re.compile(
    r"^\s*(?P<id>\d+)\s*,\s*(?P<base>0x[0-9a-f]+)\s*,\s*(?P<end>0x[0-9a-f]+)\s*,\s*"
    r"(?P<entry>0x[0-9a-f]+)\s*,\s*(?P<checksum>0x[0-9a-f]+)\s*,\s*"
    r"(?P<timestamp>0x[0-9a-f]+)\s*,\s*(?P<path>.*)$",
    re.I,
)
_BB_LINE = re.compile(
    r"^\s*module\[\s*(?P<module>\d+)\s*\]\s*:\s*(?P<start>0x[0-9a-f]+)\s*,\s*(?P<size>\d+)\s*$",
    re.I,
)


def parse_drcov_text(path: Path) -> dict[str, Any]:
    """Parse a drcov ``-dump_text`` log into stable module/block records."""
    source = path.resolve()
    if not source.is_file():
        raise ContractError(f"drcov log does not exist: {source}")
    lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
    version = None
    flavor = None
    module_version = None
    declared_modules = None
    declared_blocks = None
    modules: list[dict[str, Any]] = []
    blocks: list[dict[str, Any]] = []
    in_modules = False
    in_blocks = False
    for line in lines:
        if line.startswith("DRCOV VERSION:"):
            version = line.partition(":")[2].strip()
            continue
        if line.startswith("DRCOV FLAVOR:"):
            flavor = line.partition(":")[2].strip()
            continue
        module_header = _MODULE_HEADER.match(line)
        if module_header:
            module_version = int(module_header.group("version"))
            declared_modules = int(module_header.group("count"))
            in_modules = True
            in_blocks = False
            continue
        block_header = _BB_HEADER.match(line)
        if block_header:
            declared_blocks = int(block_header.group("count"))
            in_modules = False
            in_blocks = True
            continue
        if in_modules:
            match = _MODULE_LINE.match(line)
            if match:
                modules.append(
                    {
                        "id": int(match.group("id")),
                        "base": int(match.group("base"), 16),
                        "end": int(match.group("end"), 16),
                        "entry": int(match.group("entry"), 16),
                        "checksum": int(match.group("checksum"), 16),
                        "timestamp": int(match.group("timestamp"), 16),
                        "path": match.group("path").strip(),
                    }
                )
            continue
        if in_blocks:
            match = _BB_LINE.match(line)
            if match:
                blocks.append(
                    {
                        "module_id": int(match.group("module")),
                        "start": int(match.group("start"), 16),
                        "size": int(match.group("size")),
                    }
                )
    if version is None or declared_modules is None or declared_blocks is None:
        raise FormatError("log is not a recognizable text drcov file")
    if len(modules) != declared_modules:
        raise FormatError(f"drcov module count mismatch: declared {declared_modules}, parsed {len(modules)}")
    if len(blocks) != declared_blocks:
        raise FormatError(f"drcov basic-block count mismatch: declared {declared_blocks}, parsed {len(blocks)}")
    module_ids = {item["id"] for item in modules}
    unknown = sorted({item["module_id"] for item in blocks} - module_ids)
    if unknown:
        raise FormatError(f"drcov blocks reference unknown module IDs: {unknown}")
    return {
        "schema_version": 1,
        "kind": "dynamorio_drcov_text",
        "source": str(source),
        "source_sha256": sha256_file(source),
        "drcov_version": version,
        "drcov_flavor": flavor,
        "module_table_version": module_version,
        "modules": modules,
        "basic_blocks": blocks,
        "unique_basic_blocks": len({(b["module_id"], b["start"], b["size"]) for b in blocks}),
    }


def run_drcov_trace(
    executable: Path,
    *,
    program_arguments: list[str] | None = None,
    drrun: Path | None = None,
    output_directory: Path,
    timeout_seconds: int = 300,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Execute an authorized program under drcov and normalize produced logs."""
    target = executable.resolve()
    if not target.is_file():
        raise ContractError(f"trace target does not exist: {target}")
    if timeout_seconds <= 0:
        raise ContractError("timeout_seconds must be positive")
    resolved_drrun = None
    if drrun is not None:
        candidate = drrun.expanduser().resolve()
        if candidate.is_file():
            resolved_drrun = str(candidate)
    else:
        resolved_drrun = shutil.which("drrun")
    if resolved_drrun is None:
        raise ExternalToolError("DynamoRIO drrun executable is unavailable")
    destination = output_directory.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="x86decomp-drcov-", dir=destination) as temporary:
        logdir = Path(temporary)
        command = [resolved_drrun, "-t", "drcov", "-dump_text", "-logdir", str(logdir), "--", str(target), *(program_arguments or [])]
        started = utc_now()
        try:
            completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout_seconds, check=False)
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            completed = None
            timed_out = True
            stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        if completed is not None:
            stdout, stderr = completed.stdout, completed.stderr
            return_code = completed.returncode
        else:
            return_code = None
        logs = sorted(logdir.glob("*.log"))
        parsed: list[dict[str, Any]] = []
        copied_logs: list[str] = []
        for index, log in enumerate(logs):
            copied = destination / f"drcov-{index:04d}-{log.name}"
            copied.write_bytes(log.read_bytes())
            copied_logs.append(str(copied))
            parsed.append(parse_drcov_text(copied))
        report = {
            "schema_version": 1,
            "kind": "dynamorio_drcov_run",
            "started_at": started,
            "finished_at": utc_now(),
            "command": command,
            "drrun": resolved_drrun,
            "drrun_sha256": sha256_file(Path(resolved_drrun)),
            "target": str(target),
            "target_sha256": sha256_file(target),
            "return_code": return_code,
            "timed_out": timed_out,
            "stdout": stdout,
            "stderr": stderr,
            "logs": copied_logs,
            "traces": parsed,
            "success": return_code == 0 and bool(parsed),
            "scope_statement": "Coverage contains only blocks observed during this explicitly requested execution and is not proof that unobserved code is unreachable.",
        }
        if report_path is not None:
            write_json(report_path, report)
        if not report["success"]:
            reason = "timeout" if timed_out else f"exit code {return_code}"
            raise ExternalToolError(f"DynamoRIO trace failed ({reason}); parsed logs: {len(parsed)}")
        return report
