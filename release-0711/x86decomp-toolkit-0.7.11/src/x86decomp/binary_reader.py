"""Shared bounded binary-reading primitives for PE and COFF parsers."""
from __future__ import annotations

import struct
from typing import Any

from .errors import FormatError


class BinaryReader:
    """Read little-endian binary structures while enforcing file bounds."""

    def __init__(self, data: bytes):
        """Store immutable input bytes for bounded reads."""
        self.data = data

    def require(self, offset: int, size: int, context: str) -> None:
        """Raise ``FormatError`` when a requested byte range is outside the file."""
        if offset < 0 or size < 0 or offset + size > len(self.data):
            raise FormatError(
                f"{context} exceeds file bounds: offset={offset} size={size} file={len(self.data)}"
            )

    def unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]:
        """Unpack a structure after validating that the entire range exists."""
        size = struct.calcsize(fmt)
        self.require(offset, size, context)
        return struct.unpack_from(fmt, self.data, offset)

    def u16(self, offset: int, context: str) -> int:
        """Read an unsigned little-endian 16-bit integer."""
        return int(self.unpack("<H", offset, context)[0])

    def u32(self, offset: int, context: str) -> int:
        """Read an unsigned little-endian 32-bit integer."""
        return int(self.unpack("<I", offset, context)[0])

    def u64(self, offset: int, context: str) -> int:
        """Read an unsigned little-endian 64-bit integer."""
        return int(self.unpack("<Q", offset, context)[0])

    def c_string(self, offset: int, context: str, max_length: int = 4096) -> str:
        """Read a bounded NUL-terminated UTF-8 string."""
        self.require(offset, 1, context)
        end_limit = min(len(self.data), offset + max_length)
        end = self.data.find(b"\x00", offset, end_limit)
        if end < 0:
            raise FormatError(f"unterminated string while reading {context}")
        return self.data[offset:end].decode("utf-8", errors="replace")

    def optional_u16(self, base: int, relative: int, available: int, context: str) -> int | None:
        """Read a relative 16-bit field when it is present in a bounded record."""
        return self.u16(base + relative, context) if available >= relative + 2 else None

    def optional_u32(self, base: int, relative: int, available: int, context: str) -> int | None:
        """Read a relative 32-bit field when it is present in a bounded record."""
        return self.u32(base + relative, context) if available >= relative + 4 else None

    def optional_u64(self, base: int, relative: int, available: int, context: str) -> int | None:
        """Read a relative 64-bit field when it is present in a bounded record."""
        return self.u64(base + relative, context) if available >= relative + 8 else None
