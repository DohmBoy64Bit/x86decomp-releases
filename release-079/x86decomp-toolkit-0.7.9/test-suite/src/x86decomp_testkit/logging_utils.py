"""Provide test-suite.x86decomp_testkit.logging_utils functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
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
    """Represent jsonl event logger state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, path: Path):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(self, event: str, **fields: Any) -> None:
        """Emit the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
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
    """Implement configure logging.
    
    Parameters and return values follow the signature and runtime validation in the body.
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
