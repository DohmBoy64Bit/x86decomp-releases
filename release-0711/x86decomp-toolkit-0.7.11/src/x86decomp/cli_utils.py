"""Shared command-line JSON parsing and output helpers.

The toolkit has several capability-specific command parsers.  This module keeps
JSON argument diagnostics, deterministic JSON emission, and end-to-end command
execution consistent across those CLIs without changing their public command
surface.
"""
from __future__ import annotations

import json
import sys
from typing import Any, Callable

from x86decomp.errors import ContractError, X86DecompError

#: Exception types every JSON-emitting CLI treats as an expected, user-facing
#: error. Catching this uniform set (rather than per-module subsets) guarantees
#: that all sibling commands report failures with the same structured payload
#: and process exit code instead of leaking an interpreter traceback.
CLI_ERROR_TYPES: tuple[type[BaseException], ...] = (
    X86DecompError,
    KeyError,
    OSError,
    TypeError,
    ValueError,
)


def parse_json_arg(raw: str | None, default: Any) -> Any:
    """Parse an optional JSON command argument, falling back to a default.

    Args:
        raw: The raw JSON string supplied on the command line, or ``None`` when
            the argument was omitted.
        default: Value returned when ``raw`` is ``None``.

    Returns:
        The decoded JSON value, or ``default`` when ``raw`` is ``None``.

    Raises:
        ContractError: If ``raw`` is provided but is not valid JSON.
    """
    if raw is None:
        return default
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON argument: {exc}") from exc


def emit_json(value: Any) -> None:
    """Print a deterministic JSON representation of a command result.

    Dataclass-like objects are converted through their instance dictionaries;
    otherwise values are serialized directly with sorted keys and a stable
    string fallback for non-JSON-native values.

    Args:
        value: The command result to serialize and print to standard output.
    """
    if hasattr(value, "__dict__"):
        value = value.__dict__
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def run_cli(
    build_parser: Callable[[], Any],
    dispatch: Callable[[Any], Any],
    argv: list[str] | None,
    *,
    emit: Callable[[Any], None] = emit_json,
    extra_exceptions: tuple[type[BaseException], ...] = (),
) -> int:
    """Run a capability CLI end to end and return a process exit status.

    This is the shared implementation behind each capability module's ``main``
    function. It builds the argument parser, parses ``argv``, dispatches the
    parsed command, and emits the result, converting the expected family of
    user-facing errors into a deterministic JSON diagnostic on standard error
    instead of an interpreter traceback.

    Args:
        build_parser: Zero-argument factory returning the module's
            ``argparse.ArgumentParser``.
        dispatch: Callable that executes a parsed ``argparse.Namespace`` and
            returns the JSON-serializable command result.
        argv: Argument vector to parse, or ``None`` to use ``sys.argv[1:]``.
        emit: Callable used to render a successful result to standard output.
            Defaults to :func:`emit_json`; callers pass a custom emitter when
            they need to post-process the result before printing.
        extra_exceptions: Additional exception types (beyond
            :data:`CLI_ERROR_TYPES`) that should be reported as structured
            user-facing errors rather than propagating.

    Returns:
        ``0`` when the command completes successfully, or ``2`` when an expected
        error is caught and reported.
    """
    parser = build_parser()
    try:
        emit(dispatch(parser.parse_args(argv)))
        return 0
    except (*CLI_ERROR_TYPES, *extra_exceptions) as exc:
        print(
            json.dumps({"error": type(exc).__name__, "message": str(exc)}, sort_keys=True),
            file=sys.stderr,
        )
        return 2
