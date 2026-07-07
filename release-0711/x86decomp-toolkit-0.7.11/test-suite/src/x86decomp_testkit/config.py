"""Provide the installed test-suite implementation for the `x86decomp_testkit.config` module."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_NAME = "x86decomp-test.json"


@dataclass
class TestConfig:
    """Store validated test config fields used by toolkit reports and adapters."""
    __test__ = False
    toolkit_root: Path
    output_root: Path
    adapter_paths: dict[str, str] = field(default_factory=dict)
    install_root: Path | None = None
    python_executable: str = os.sys.executable
    strict: bool = True
    interactive: bool = True
    allow_network: bool = False
    allow_install: bool = False
    allow_host_execution: bool = False
    timeout_seconds: int = 900
    line_coverage_floor: float = 70.0
    branch_coverage_floor: float = 50.0
    require_public_api_execution: bool = True
    custom_environment: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "toolkit_root": str(self.toolkit_root),
            "output_root": str(self.output_root),
            "adapter_paths": dict(sorted(self.adapter_paths.items())),
            "install_root": str(self.install_root) if self.install_root else None,
            "python_executable": self.python_executable,
            "strict": self.strict,
            "interactive": self.interactive,
            "allow_network": self.allow_network,
            "allow_install": self.allow_install,
            "allow_host_execution": self.allow_host_execution,
            "timeout_seconds": self.timeout_seconds,
            "line_coverage_floor": self.line_coverage_floor,
            "branch_coverage_floor": self.branch_coverage_floor,
            "require_public_api_execution": self.require_public_api_execution,
            "custom_environment": dict(sorted(self.custom_environment.items())),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any], base: Path | None = None) -> "TestConfig":
        """Execute the from dict operation for the current toolkit workflow."""
        base = base or Path.cwd()

        def resolve(value: str | None, default: Path) -> Path:
            """Resolve resolve for the current toolkit workflow."""
            path = Path(value) if value else default
            if not path.is_absolute():
                path = base / path
            return path.expanduser().resolve()

        toolkit_root = resolve(data.get("toolkit_root"), base / "x86decomp-toolkit")
        output_root = resolve(data.get("output_root"), base / "test-results")
        install_value = data.get("install_root")
        install_root = resolve(install_value, base / ".x86decomp-test-tools") if install_value else None
        return cls(
            toolkit_root=toolkit_root,
            output_root=output_root,
            adapter_paths={str(k): str(v) for k, v in data.get("adapter_paths", {}).items()},
            install_root=install_root,
            python_executable=str(data.get("python_executable", os.sys.executable)),
            strict=bool(data.get("strict", True)),
            interactive=bool(data.get("interactive", True)),
            allow_network=bool(data.get("allow_network", False)),
            allow_install=bool(data.get("allow_install", False)),
            allow_host_execution=bool(data.get("allow_host_execution", False)),
            timeout_seconds=int(data.get("timeout_seconds", 900)),
            line_coverage_floor=float(data.get("line_coverage_floor", 70.0)),
            branch_coverage_floor=float(data.get("branch_coverage_floor", 50.0)),
            require_public_api_execution=bool(data.get("require_public_api_execution", True)),
            custom_environment={str(k): str(v) for k, v in data.get("custom_environment", {}).items()},
        )


def load_config(path: Path) -> TestConfig:
    """Load config for the current toolkit workflow."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("configuration root must be a JSON object")
    return TestConfig.from_dict(data, path.parent)


def save_config(config: TestConfig, path: Path) -> None:
    """Execute the save config operation for the current toolkit workflow."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
