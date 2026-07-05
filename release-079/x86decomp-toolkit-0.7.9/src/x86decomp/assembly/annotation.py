"""Provide x86decomp.assembly.annotation functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from x86decomp.disassembly import decode_instructions
from x86decomp.contracts import ContractError, atomic_write_bytes

_BYTE_RE = re.compile(r"^\s*\.byte\s+(.+?)(?:\s+#.*)?$")
_SYMBOL_RE = re.compile(r"^[A-Za-z_.$?@][A-Za-z0-9_.$?@-]*$")


def validate_symbol(symbol: str) -> str:
    """Validate symbol.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not _SYMBOL_RE.fullmatch(symbol):
        raise ContractError(f"unsafe assembly symbol: {symbol!r}")
    return symbol


def render_byte_assembly(symbol: str, code: bytes, architecture: str) -> str:
    """Render the original compatibility form. This output intentionally preserves byte-form assembly semantics."""
    validate_symbol(symbol)
    if architecture not in {"x86", "x86_64"}:
        raise ContractError("architecture must be x86 or x86_64")
    directives = [
        ".text",
        ".code32" if architecture == "x86" else ".code64",
        f".globl {symbol}",
        f"{symbol}:",
    ]
    for offset in range(0, len(code), 16):
        chunk = code[offset : offset + 16]
        directives.append("  .byte " + ", ".join(f"0x{value:02x}" for value in chunk))
    directives.append("")
    return "\n".join(directives)


def parse_byte_directives(text: str) -> bytes:
    """Parse byte directives.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    output = bytearray()
    found = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = _BYTE_RE.match(line)
        if not match:
            continue
        found = True
        for token in match.group(1).split(","):
            raw = token.strip()
            try:
                value = int(raw, 0)
            except ValueError as exc:
                raise ContractError(f"invalid .byte value on line {line_number}: {raw}") from exc
            if not 0 <= value <= 0xFF:
                raise ContractError(f".byte value outside byte range on line {line_number}: {raw}")
            output.append(value)
    if not found:
        raise ContractError("assembly source contains no .byte directives")
    return bytes(output)


def _chunk_comments(code: bytes, *, base_address: int, architecture: str) -> dict[int, list[str]]:
    """Implement chunk comments.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    records = decode_instructions(code, base_address=base_address, architecture=architecture)
    comments: dict[int, list[str]] = {}
    for record in records:
        chunk = record.offset // 16
        rendered = record.mnemonic + (f" {record.op_str}" if record.op_str else "")
        comments.setdefault(chunk, []).append(rendered)
    return comments


def render_annotated_assembly(
    symbol: str,
    code: bytes,
    architecture: str,
    *,
    base_address: int,
) -> str:
    """Render byte-identical directives with idempotent Capstone comments."""
    comments = _chunk_comments(code, base_address=base_address, architecture=architecture)
    lines = render_byte_assembly(symbol, code, architecture).splitlines()
    byte_index = 0
    output: list[str] = []
    for line in lines:
        if line.lstrip().startswith(".byte"):
            comment = "; ".join(comments.get(byte_index, []))
            output.append(line + (f"  # x86decomp: {comment}" if comment else ""))
            byte_index += 1
        else:
            output.append(line)
    return "\n".join(output) + "\n"


def annotate_source(
    source: Path,
    output: Path,
    *,
    symbol: str,
    architecture: str,
    base_address: int,
) -> dict[str, object]:
    """Implement annotate source.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    code = parse_byte_directives(source.read_text(encoding="utf-8"))
    rendered = render_annotated_assembly(
        symbol, code, architecture, base_address=base_address
    )
    atomic_write_bytes(output, rendered.encode("utf-8"))
    return {
        "source": str(source.resolve()),
        "output": str(output.resolve()),
        "format": "annotated",
        "architecture": architecture,
        "base_address": base_address,
        "byte_count": len(code),
        "byte_identical_by_construction": True,
    }


def byte_directive_lines(code: bytes, *, indent: str = "  ") -> Iterable[str]:
    """Implement byte directive lines.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    for offset in range(0, len(code), 16):
        chunk = code[offset : offset + 16]
        yield indent + ".byte " + ", ".join(f"0x{value:02x}" for value in chunk)
