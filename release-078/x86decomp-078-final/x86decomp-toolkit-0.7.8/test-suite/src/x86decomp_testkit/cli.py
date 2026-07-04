from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .adapters import adapter_catalog, detect_all, resolve_missing_adapters
from .adapters.capabilities import capabilities_from_adapters
from .config import DEFAULT_CONFIG_NAME, TestConfig, load_config, save_config
from .inventory import build_inventory
from .logging_utils import configure_logging
from .orchestrator import feature_catalog_path, run_all


def _path(value: str) -> Path:
    return Path(value).expanduser()


def _base_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x86decomp-test",
        description="No-silent-skip comprehensive verification harness for x86decomp-toolkit",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init-config", help="create a test configuration")
    p.add_argument("--toolkit-root", type=_path, required=True)
    p.add_argument("--output-root", type=_path, default=Path("test-results"))
    p.add_argument("--config", type=_path, default=Path(DEFAULT_CONFIG_NAME))
    p.add_argument("--install-root", type=_path)
    p.add_argument("--non-interactive", action="store_true")
    p.add_argument("--allow-network", action="store_true")
    p.add_argument("--allow-install", action="store_true")
    p.add_argument("--non-strict", action="store_true")

    p = sub.add_parser("adapters", help="detect adapters and optionally resolve missing ones")
    p.add_argument("--config", type=_path, default=Path(DEFAULT_CONFIG_NAME))
    p.add_argument("--resolve", action="store_true")
    p.add_argument("--verbose", action="store_true")

    p = sub.add_parser("capabilities", help="show adapter capabilities resolved from installed adapters and local endpoints")
    p.add_argument("--config", type=_path, default=Path(DEFAULT_CONFIG_NAME))

    p = sub.add_parser("inventory", help="print the discovered toolkit surface")
    p.add_argument("--config", type=_path, default=Path(DEFAULT_CONFIG_NAME))
    p.add_argument("--output", type=_path)

    p = sub.add_parser("run", help="run the complete suite")
    p.add_argument("--config", type=_path, default=Path(DEFAULT_CONFIG_NAME))
    p.add_argument("--verbose", action="store_true")

    p = sub.add_parser("catalog", help="show the pinned feature catalog path")
    p.add_argument("--print", action="store_true", dest="print_catalog")
    return parser


def _load(path: Path) -> TestConfig:
    if not path.is_file():
        raise FileNotFoundError(f"configuration does not exist: {path}; run init-config first")
    return load_config(path.resolve())


def main(argv: list[str] | None = None) -> int:
    parser = _base_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "init-config":
            config = TestConfig(
                toolkit_root=args.toolkit_root.resolve(),
                output_root=args.output_root.resolve(),
                install_root=args.install_root.resolve() if args.install_root else None,
                interactive=not args.non_interactive,
                allow_network=args.allow_network,
                allow_install=args.allow_install,
                strict=not args.non_strict,
            )
            save_config(config, args.config.resolve())
            print(json.dumps(config.to_dict(), indent=2, sort_keys=True))
            return 0
        if args.command == "adapters":
            config_path = args.config.resolve()
            config = _load(config_path)
            catalog = adapter_catalog()
            if args.resolve:
                output = config.output_root / "adapter-resolution"
                _logger, event_logger = configure_logging(output, verbose=args.verbose)
                results = resolve_missing_adapters(catalog, config, config_path=config_path, event_logger=event_logger)
            else:
                results = detect_all(catalog, config)
            print(json.dumps({"adapters": [item.to_dict() for item in results]}, indent=2, sort_keys=True))
            return 0 if all(item.installed or catalog[item.adapter_id].optional for item in results) else 2
        if args.command == "capabilities":
            config = _load(args.config.resolve())
            catalog = adapter_catalog()
            adapter_results = detect_all(catalog, config)
            capabilities = capabilities_from_adapters(catalog, adapter_results)
            print(json.dumps({"capabilities": [item.to_dict() for item in capabilities]}, indent=2, sort_keys=True))
            return 0
        if args.command == "inventory":
            config = _load(args.config.resolve())
            inventory = build_inventory(config.toolkit_root, config.python_executable)
            payload = json.dumps(inventory, indent=2, sort_keys=True) + "\n"
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(payload, encoding="utf-8")
            print(payload, end="")
            return 0
        if args.command == "run":
            config_path = args.config.resolve()
            config = _load(config_path)
            summary = run_all(config, config_path=config_path, verbose=args.verbose)
            print(json.dumps({"run_id": summary.run_id, "output_directory": summary.output_directory, "counts": summary.counts(), "exit_code": summary.exit_code()}, indent=2, sort_keys=True))
            return summary.exit_code()
        if args.command == "catalog":
            path = feature_catalog_path()
            if args.print_catalog:
                print(path.read_text(encoding="utf-8"))
            else:
                print(path)
            return 0
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    raise AssertionError("unhandled command")
