"""Provide logging utils support for the standalone verification harness."""
from __future__ import annotations

import json
import logging
import os
import sys
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from .timeutil import utc_now


class JsonlEventLogger:
    """Append structured events as JSON Lines to a file, one JSON object per line."""
    def __init__(self, path: Path):
        """Initialize JsonlEventLogger with `path`."""
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(self, event: str, **fields: Any) -> None:
        """Append one event record to the log file.

        Dataclass field values are serialized via :func:`dataclasses.asdict` and ``Path`` values
        as strings; every record carries a UTC ``timestamp`` and the ``event`` name.

        Args:
            event: Name of the event being recorded.
            **fields: Arbitrary event fields serialized into the JSON record.
        """
        payload: dict[str, Any] = {"timestamp": utc_now(), "event": event}
        for key, value in fields.items():
            if is_dataclass(value):
                payload[key] = asdict(value)
            elif isinstance(value, Path):
                payload[key] = str(value)
            else:
                payload[key] = value
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, sort_keys=True, ensure_ascii=False) + "\n")


def configure_logging(output_directory: Path, verbose: bool = False) -> tuple[logging.Logger, JsonlEventLogger]:
    """Configure the ``x86decomp_testkit`` logger and a companion JSONL event logger.

    Resets any existing handlers and installs a file handler (``run.log``, DEBUG) plus a stderr
    console handler, all using UTC timestamps. An initial ``logging.configured`` event is emitted.

    Args:
        output_directory: Directory to create and write ``run.log`` and ``events.jsonl`` into.
        verbose: When true, the console handler logs at DEBUG rather than INFO.

    Returns:
        A tuple of the configured standard logger and the JSONL event logger.
    """
    output_directory.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("x86decomp_testkit")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03dZ %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    formatter.converter = __import__("time").gmtime

    file_handler = logging.FileHandler(output_directory / "run.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    event_logger = JsonlEventLogger(output_directory / "events.jsonl")
    event_logger.emit(
        "logging.configured",
        output_directory=str(output_directory),
        pid=os.getpid(),
        verbose=verbose,
    )
    return logger, event_logger
