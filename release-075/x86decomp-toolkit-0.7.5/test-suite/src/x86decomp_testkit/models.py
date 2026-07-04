from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


class Status(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    BLOCKED = "blocked"
    ERROR = "error"


class AdapterKind(str, Enum):
    PYTHON = "python"
    EXECUTABLE = "executable"
    DIRECTORY = "directory"
    TOOLCHAIN = "toolchain"


@dataclass(frozen=True)
class ProbeResult:
    adapter_id: str
    installed: bool
    path: str | None = None
    version: str | None = None
    source: str | None = None
    diagnostics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AdapterSpec:
    adapter_id: str
    display_name: str
    kind: AdapterKind
    required_for: tuple[str, ...]
    commands: tuple[str, ...] = ()
    python_modules: tuple[str, ...] = ()
    environment_variables: tuple[str, ...] = ()
    root_markers: tuple[str, ...] = ()
    version_args: tuple[str, ...] = ("--version",)
    pip_requirement: str | None = None
    github_repository: str | None = None
    release_asset_patterns: dict[str, tuple[str, ...]] = field(default_factory=dict)
    manual_install_note: str = ""
    custom_path_kind: str = "file_or_directory"
    optional: bool = True


@dataclass
class TestResult:
    test_id: str
    suite: str
    status: Status
    started_at: str
    finished_at: str
    duration_seconds: float
    summary: str
    command: list[str] = field(default_factory=list)
    return_code: int | None = None
    stdout_path: str | None = None
    stderr_path: str | None = None
    details: dict[str, Any] = field(default_factory=dict)
    required_adapters: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data


@dataclass
class RunSummary:
    run_id: str
    toolkit_root: str
    output_directory: str
    strict: bool
    started_at: str
    finished_at: str
    adapter_results: list[ProbeResult]
    test_results: list[TestResult]
    inventory: dict[str, Any]
    configuration: dict[str, Any]

    def counts(self) -> dict[str, int]:
        counts = {status.value: 0 for status in Status}
        for result in self.test_results:
            counts[result.status.value] += 1
        return counts

    def exit_code(self) -> int:
        counts = self.counts()
        if counts[Status.FAIL.value] or counts[Status.ERROR.value]:
            return 1
        if self.strict and counts[Status.BLOCKED.value]:
            return 2
        return 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "run_id": self.run_id,
            "toolkit_root": self.toolkit_root,
            "output_directory": self.output_directory,
            "strict": self.strict,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "adapter_results": [item.to_dict() for item in self.adapter_results],
            "test_results": [item.to_dict() for item in self.test_results],
            "inventory": self.inventory,
            "configuration": self.configuration,
            "counts": self.counts(),
            "exit_code": self.exit_code(),
        }


def normalized_path(value: str | Path) -> str:
    return str(Path(value).expanduser().resolve())
