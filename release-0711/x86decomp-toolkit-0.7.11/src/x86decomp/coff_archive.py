"""Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.

The archive container format is shared with ``ar``. Microsoft libraries additionally
use linker members and import-object records. This module inventories members, resolves
long names, parses linker symbol indexes when structurally valid, recognizes import
objects, and invokes the normal COFF parser for embedded object members.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .coff import parse_coff_bytes
from .errors import ContractError, FormatError
from .util import sha256_bytes, sha256_file

_ARCHIVE_MAGIC = b"!<arch>\n"
_HEADER_SIZE = 60
_MAX_MEMBERS = 1_000_000
_MAX_SYMBOLS = 10_000_000


@dataclass(frozen=True)
class ArchiveMember:
    """Store validated archive member fields used by toolkit reports and adapters."""
    index: int
    header_offset: int
    data_offset: int
    name: str
    size: int
    timestamp: int | None
    user_id: int | None
    group_id: int | None
    mode: int | None
    kind: str
    sha256: str
    import_object: dict[str, Any] | None = None
    coff: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        result = {
            "index": self.index,
            "header_offset": self.header_offset,
            "data_offset": self.data_offset,
            "name": self.name,
            "size": self.size,
            "timestamp": self.timestamp,
            "user_id": self.user_id,
            "group_id": self.group_id,
            "mode": self.mode,
            "kind": self.kind,
            "sha256": self.sha256,
        }
        if self.import_object is not None:
            result["import_object"] = self.import_object
        if self.coff is not None:
            result["coff"] = self.coff
        return result


@dataclass(frozen=True)
class CoffArchive:
    """Store validated coff archive fields used by toolkit reports and adapters."""
    path: Path | None
    raw_sha256: str
    members: tuple[ArchiveMember, ...]
    linker_symbols: tuple[dict[str, Any], ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "schema_version": 1,
            "format": "coff_archive",
            "source_path": None if self.path is None else str(self.path),
            "source_sha256": self.raw_sha256,
            "member_count": len(self.members),
            "members": [member.to_dict() for member in self.members],
            "linker_symbols": list(self.linker_symbols),
        }


def _decimal(field: bytes, context: str, *, optional: bool = True) -> int | None:
    """Parse an ASCII decimal archive header field.

    Args:
        field: Raw header field bytes.
        context: Field description used in error messages.
        optional: If True, a blank field returns None instead of erroring.

    Returns:
        The parsed integer, or None when the field is blank and ``optional``.

    Raises:
        FormatError: If the field is non-blank and not a valid decimal integer.
    """
    text = field.decode("ascii", errors="strict").strip()
    if not text and optional:
        return None
    try:
        return int(text, 10)
    except ValueError as exc:
        raise FormatError(f"invalid decimal {context}: {text!r}") from exc


def _octal(field: bytes, context: str) -> int | None:
    """Parse an ASCII octal archive header field (used for the file mode).

    Args:
        field: Raw header field bytes.
        context: Field description used in error messages.

    Returns:
        The parsed integer, or None when the field is blank.

    Raises:
        FormatError: If the field is non-blank and not a valid octal integer.
    """
    text = field.decode("ascii", errors="strict").strip()
    if not text:
        return None
    try:
        return int(text, 8)
    except ValueError as exc:
        raise FormatError(f"invalid octal {context}: {text!r}") from exc


def _long_name(table: bytes, offset: int) -> str:
    """Resolve a long member name from the ``//`` long-name string table.

    Args:
        table: Bytes of the long-name string table member.
        offset: Byte offset of the name within the table.

    Returns:
        The decoded member name, terminated at ``/\n`` or NUL.

    Raises:
        FormatError: If ``offset`` lies outside the table.
    """
    if offset < 0 or offset >= len(table):
        raise FormatError(f"archive long-name offset outside table: {offset}")
    endings = [value for value in (table.find(b"/\n", offset), table.find(b"\x00", offset)) if value >= 0]
    end = min(endings) if endings else len(table)
    return table[offset:end].decode("utf-8", errors="replace")


def _parse_import_object(data: bytes) -> dict[str, Any] | None:
    """Parse a Microsoft short-import-object member if the data is one.

    Args:
        data: Raw member payload bytes.

    Returns:
        A dict describing the import (machine, type, name type, symbol, DLL, etc.),
        or None if the payload is too short or lacks the import-object signature.

    Raises:
        FormatError: If the declared data size overruns the member, or the symbol or
            DLL name is unterminated.
    """
    if len(data) < 20:
        return None
    sig1, sig2, version, machine, timestamp, data_size, ordinal_hint, type_info = struct.unpack_from(
        "<HHHHIIHH", data, 0
    )
    if sig1 != 0 or sig2 != 0xFFFF:
        return None
    if data_size > len(data) - 20:
        raise FormatError("import object data size exceeds archive member")
    payload = data[20 : 20 + data_size]
    first_end = payload.find(b"\x00")
    if first_end < 0:
        raise FormatError("import object symbol name is unterminated")
    second_end = payload.find(b"\x00", first_end + 1)
    if second_end < 0:
        raise FormatError("import object DLL name is unterminated")
    type_names = {0: "code", 1: "data", 2: "const"}
    name_type_names = {0: "ordinal", 1: "name", 2: "name_no_prefix", 3: "name_undecorate", 4: "name_exportas"}
    import_type = type_info & 0x3
    name_type = (type_info >> 2) & 0x7
    return {
        "version": version,
        "machine": machine,
        "machine_hex": f"0x{machine:04x}",
        "timestamp": timestamp,
        "size_of_data": data_size,
        "ordinal_or_hint": ordinal_hint,
        "import_type": import_type,
        "import_type_name": type_names.get(import_type, f"unknown_{import_type}"),
        "name_type": name_type,
        "name_type_name": name_type_names.get(name_type, f"unknown_{name_type}"),
        "symbol": payload[:first_end].decode("utf-8", errors="replace"),
        "dll": payload[first_end + 1 : second_end].decode("utf-8", errors="replace"),
    }


def _cstring_sequence(data: bytes, offset: int, count: int) -> tuple[list[str], int]:
    """Read ``count`` consecutive NUL-terminated strings starting at an offset.

    Args:
        data: Buffer to read from.
        offset: Starting byte offset.
        count: Number of strings to read.

    Returns:
        A tuple of the decoded string list and the cursor position past the last string.

    Raises:
        FormatError: If the buffer is truncated or a string is unterminated.
    """
    names: list[str] = []
    cursor = offset
    for _ in range(count):
        if cursor >= len(data):
            raise FormatError("archive linker symbol string table is truncated")
        end = data.find(b"\x00", cursor)
        if end < 0:
            raise FormatError("archive linker symbol is unterminated")
        names.append(data[cursor:end].decode("utf-8", errors="replace"))
        cursor = end + 1
    return names, cursor


def _first_linker_symbols(data: bytes) -> list[tuple[str, int]] | None:
    """Parse the first (big-endian) linker symbol-index member.

    Args:
        data: Raw first-linker-member payload.

    Returns:
        A list of (symbol name, member header offset) pairs, or None if the data is
        too small, exceeds safety limits, or is not structurally valid.
    """
    if len(data) < 4:
        return None
    count = struct.unpack_from(">I", data, 0)[0]
    if count > _MAX_SYMBOLS or 4 + count * 4 > len(data):
        return None
    offsets = list(struct.unpack_from(f">{count}I", data, 4)) if count else []
    try:
        names, _ = _cstring_sequence(data, 4 + count * 4, count)
    except FormatError:
        return None
    return list(zip(names, offsets))


def _second_linker_symbols(data: bytes) -> list[tuple[str, int]] | None:
    """Parse the second (little-endian) linker symbol-index member.

    Resolves each symbol's one-based member index into a member header offset.

    Args:
        data: Raw second-linker-member payload.

    Returns:
        A list of (symbol name, member header offset) pairs, or None if the data is
        too small, exceeds safety limits, or contains an out-of-range member index.
    """
    if len(data) < 8:
        return None
    member_count = struct.unpack_from("<I", data, 0)[0]
    if member_count > _MAX_MEMBERS or 4 + member_count * 4 + 4 > len(data):
        return None
    cursor = 4
    member_offsets = list(struct.unpack_from(f"<{member_count}I", data, cursor)) if member_count else []
    cursor += member_count * 4
    symbol_count = struct.unpack_from("<I", data, cursor)[0]
    cursor += 4
    if symbol_count > _MAX_SYMBOLS or cursor + symbol_count * 2 > len(data):
        return None
    indices = list(struct.unpack_from(f"<{symbol_count}H", data, cursor)) if symbol_count else []
    cursor += symbol_count * 2
    try:
        names, _ = _cstring_sequence(data, cursor, symbol_count)
    except FormatError:
        return None
    result: list[tuple[str, int]] = []
    for name, index in zip(names, indices):
        if index == 0 or index > len(member_offsets):
            return None
        result.append((name, member_offsets[index - 1]))
    return result


def parse_coff_archive_bytes(data: bytes, *, path: Path | None = None) -> CoffArchive:
    """Parse a COFF/ar archive from raw bytes into a structured model.

    Walks the archive member table, resolving BSD (#1/) and SysV (/N) long names,
    parses linker symbol indexes when present, and classifies each member as a
    linker member, long-name table, import object, embedded COFF object, or unknown.

    Args:
        data: Raw archive bytes.
        path: Optional source path recorded on the result.

    Returns:
        A :class:`CoffArchive` with parsed members and linker symbols.

    Raises:
        FormatError: If the signature is missing, a header is truncated or malformed,
            a member exceeds file bounds, member alignment overruns the file, or the
            member/symbol counts exceed safety limits.
    """
    if not data.startswith(_ARCHIVE_MAGIC):
        raise FormatError("missing COFF archive signature")
    raw_members: list[dict[str, Any]] = []
    cursor = len(_ARCHIVE_MAGIC)
    long_names = b""
    while cursor < len(data):
        if len(raw_members) >= _MAX_MEMBERS:
            raise FormatError("archive member count exceeds safety limit")
        if cursor + _HEADER_SIZE > len(data):
            raise FormatError("truncated archive member header")
        header = data[cursor : cursor + _HEADER_SIZE]
        if header[58:60] != b"`\n":
            raise FormatError(f"invalid archive member header terminator at offset {cursor}")
        declared_size = _decimal(header[48:58], "member size", optional=False)
        assert declared_size is not None
        data_offset = cursor + _HEADER_SIZE
        end = data_offset + declared_size
        if end > len(data):
            raise FormatError("archive member exceeds file bounds")
        raw_name = header[0:16].decode("ascii", errors="replace").rstrip()
        payload = data[data_offset:end]
        name_prefix = 0
        if raw_name.startswith("#1/"):
            try:
                name_prefix = int(raw_name[3:], 10)
            except ValueError as exc:
                raise FormatError(f"invalid BSD archive extended name: {raw_name!r}") from exc
            if name_prefix > len(payload):
                raise FormatError("BSD archive name exceeds member size")
            name = payload[:name_prefix].decode("utf-8", errors="replace").rstrip("\x00")
            payload = payload[name_prefix:]
            data_offset += name_prefix
        elif raw_name == "//":
            name = "//"
            long_names = payload
        elif raw_name.startswith("/") and raw_name[1:].isdigit():
            name = _long_name(long_names, int(raw_name[1:], 10))
        elif raw_name in ("/", "/SYM64/"):
            name = raw_name
        else:
            name = raw_name[:-1] if raw_name.endswith("/") else raw_name
        raw_members.append(
            {
                "header_offset": cursor,
                "data_offset": data_offset,
                "name": name,
                "payload": payload,
                "timestamp": _decimal(header[16:28], "member timestamp"),
                "user_id": _decimal(header[28:34], "member user id"),
                "group_id": _decimal(header[34:40], "member group id"),
                "mode": _octal(header[40:48], "member mode"),
            }
        )
        cursor = end + (end & 1)
    if cursor != len(data):
        raise FormatError("archive alignment extends outside file")

    linker_symbols: list[dict[str, Any]] = []
    slash_members = [item for item in raw_members if item["name"] == "/"]
    for position, item in enumerate(slash_members):
        parsed = _first_linker_symbols(item["payload"]) if position == 0 else _second_linker_symbols(item["payload"])
        if parsed is None:
            # Some producers emit only one of the two forms or reverse their order.
            parsed = _second_linker_symbols(item["payload"]) or _first_linker_symbols(item["payload"])
        if parsed is not None:
            linker_symbols.extend(
                {"name": name, "member_header_offset": offset, "linker_member_index": position}
                for name, offset in parsed
            )

    members: list[ArchiveMember] = []
    for index, item in enumerate(raw_members):
        payload: bytes = item["payload"]
        name = item["name"]
        kind = "unknown"
        import_object: dict[str, Any] | None = None
        coff: dict[str, Any] | None = None
        if name in ("/", "/SYM64/"):
            kind = "linker_member"
        elif name == "//":
            kind = "longnames"
        else:
            import_object = _parse_import_object(payload)
            if import_object is not None:
                kind = "import_object"
            else:
                try:
                    coff = parse_coff_bytes(payload).to_dict()
                    kind = "coff_object"
                except FormatError:
                    kind = "unknown"
        members.append(
            ArchiveMember(
                index=index,
                header_offset=item["header_offset"],
                data_offset=item["data_offset"],
                name=name,
                size=len(payload),
                timestamp=item["timestamp"],
                user_id=item["user_id"],
                group_id=item["group_id"],
                mode=item["mode"],
                kind=kind,
                sha256=sha256_bytes(payload),
                import_object=import_object,
                coff=coff,
            )
        )
    return CoffArchive(path=path, raw_sha256=sha256_bytes(data), members=tuple(members), linker_symbols=tuple(linker_symbols))


def parse_coff_archive(path: Path) -> CoffArchive:
    """Parse a COFF/ar archive from a file path.

    Args:
        path: Path to the ``.lib``/``.a`` archive file.

    Returns:
        A :class:`CoffArchive` parsed from the file's bytes.

    Raises:
        ContractError: If the file does not exist.
        AssertionError: If the internally computed hash disagrees with the file hash.
        FormatError: Propagated from :func:`parse_coff_archive_bytes` on malformed data.
    """
    resolved = path.resolve()
    if not resolved.is_file():
        raise ContractError(f"COFF archive does not exist: {resolved}")
    result = parse_coff_archive_bytes(resolved.read_bytes(), path=resolved)
    if result.raw_sha256 != sha256_file(resolved):
        raise AssertionError("archive hash calculation mismatch")
    return result
