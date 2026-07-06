"""Microsoft C++ metadata, unwind, TLS, and initializer recovery.

The scanner is intentionally conservative.  A record is returned only after its
internal pointers, counts, and section relationships pass structural checks.
RTTI layouts are derived from the Microsoft C++ ABI as emitted by Clang/MSVC;
these structures are not a promise that original source-level class names or
layouts have been fully recovered.
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .coff import CoffObject, parse_coff
from .errors import FormatError
from .linker_layout import LinkerMap, parse_msvc_map
from .pe import parse_pe
from .pe32 import Section, _rva_to_offset
from .util import sha256_bytes, utc_now, write_json


@dataclass(frozen=True)
class TypeDescriptorRecord:
    """Store validated type descriptor record fields used by toolkit reports and adapters."""
    rva: int
    name_rva: int
    mangled_name: str
    display_name: str
    vfptr: int
    spare: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "rva": self.rva,
            "name_rva": self.name_rva,
            "mangled_name": self.mangled_name,
            "display_name": self.display_name,
            "vfptr": self.vfptr,
            "spare": self.spare,
        }


@dataclass(frozen=True)
class BaseClassRecord:
    """Store validated base class record fields used by toolkit reports and adapters."""
    descriptor_rva: int
    type_descriptor_rva: int
    type_name: str | None
    contained_bases: int
    member_displacement: int
    vbtable_displacement: int
    vbase_displacement: int
    attributes: int
    hierarchy_rva: int | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "descriptor_rva": self.descriptor_rva,
            "type_descriptor_rva": self.type_descriptor_rva,
            "type_name": self.type_name,
            "contained_bases": self.contained_bases,
            "pmd": {
                "member_displacement": self.member_displacement,
                "vbtable_displacement": self.vbtable_displacement,
                "vbase_displacement": self.vbase_displacement,
            },
            "attributes": self.attributes,
            "hierarchy_rva": self.hierarchy_rva,
        }


@dataclass(frozen=True)
class CompleteObjectLocatorRecord:
    """Store validated complete object locator record fields used by toolkit reports and adapters."""
    rva: int
    signature: int
    offset: int
    constructor_displacement_offset: int
    type_descriptor_rva: int
    class_hierarchy_rva: int
    self_rva: int | None
    type_name: str
    hierarchy_attributes: int
    bases: tuple[BaseClassRecord, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "rva": self.rva,
            "signature": self.signature,
            "offset": self.offset,
            "constructor_displacement_offset": self.constructor_displacement_offset,
            "type_descriptor_rva": self.type_descriptor_rva,
            "class_hierarchy_rva": self.class_hierarchy_rva,
            "self_rva": self.self_rva,
            "type_name": self.type_name,
            "hierarchy_attributes": self.hierarchy_attributes,
            "bases": [base.to_dict() for base in self.bases],
        }


@dataclass(frozen=True)
class VTableRecord:
    """Store validated v table record fields used by toolkit reports and adapters."""
    address_point_rva: int
    locator_rva: int
    type_name: str
    function_rvas: tuple[int, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "address_point_rva": self.address_point_rva,
            "locator_rva": self.locator_rva,
            "type_name": self.type_name,
            "function_rvas": list(self.function_rvas),
        }


@dataclass(frozen=True)
class UnwindCodeRecord:
    """Store validated unwind code record fields used by toolkit reports and adapters."""
    code_offset: int
    operation: int
    operation_name: str
    operation_info: int
    slots: int
    decoded: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "code_offset": self.code_offset,
            "operation": self.operation,
            "operation_name": self.operation_name,
            "operation_info": self.operation_info,
            "slots": self.slots,
            "decoded": self.decoded,
        }


@dataclass(frozen=True)
class UnwindInfoRecord:
    """Store validated unwind info record fields used by toolkit reports and adapters."""
    function_begin_rva: int
    function_end_rva: int
    unwind_info_rva: int
    version: int
    flags: int
    prolog_size: int
    frame_register: int
    frame_offset: int
    codes: tuple[UnwindCodeRecord, ...]
    handler_rva: int | None
    language_data_rva: int | None
    chained_function: dict[str, int] | None
    raw_language_data_hex: str | None

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {
            "function_begin_rva": self.function_begin_rva,
            "function_end_rva": self.function_end_rva,
            "unwind_info_rva": self.unwind_info_rva,
            "version": self.version,
            "flags": self.flags,
            "prolog_size": self.prolog_size,
            "frame_register": self.frame_register,
            "frame_offset": self.frame_offset,
            "codes": [code.to_dict() for code in self.codes],
            "handler_rva": self.handler_rva,
            "language_data_rva": self.language_data_rva,
            "chained_function": self.chained_function,
            "raw_language_data_hex": self.raw_language_data_hex,
        }


class PEView:
    """Coordinate p e view behavior for the current toolkit workflow."""
    def __init__(self, path: Path):
        """Initialize the instance with validated constructor state."""
        self.path = path.resolve()
        self.data = self.path.read_bytes()
        self.image = parse_pe(self.path)
        self.architecture = self.image.to_dict()["architecture"]
        self.pointer_size = 4 if self.architecture == "x86" else 8

    def rva_to_offset(self, rva: int) -> int:
        """Execute the rva to offset operation for the current toolkit workflow."""
        return _rva_to_offset(rva, self.image.sections, self.image.size_of_headers, len(self.data))

    def valid_rva(self, rva: int, size: int = 1) -> bool:
        """Execute the valid rva operation for the current toolkit workflow."""
        try:
            offset = self.rva_to_offset(rva)
        except FormatError:
            return False
        return 0 <= offset <= len(self.data) and 0 <= size <= len(self.data) - offset

    def read(self, rva: int, size: int) -> bytes:
        """Read read for the current toolkit workflow."""
        offset = self.rva_to_offset(rva)
        if size < 0 or offset + size > len(self.data):
            raise FormatError(f"read outside PE image at RVA 0x{rva:x}")
        return self.data[offset : offset + size]

    def u16(self, rva: int) -> int:
        """Execute the u16 operation for the current toolkit workflow."""
        return struct.unpack("<H", self.read(rva, 2))[0]

    def u32(self, rva: int) -> int:
        """Execute the u32 operation for the current toolkit workflow."""
        return struct.unpack("<I", self.read(rva, 4))[0]

    def i32(self, rva: int) -> int:
        """Execute the i32 operation for the current toolkit workflow."""
        return struct.unpack("<i", self.read(rva, 4))[0]

    def u64(self, rva: int) -> int:
        """Execute the u64 operation for the current toolkit workflow."""
        return struct.unpack("<Q", self.read(rva, 8))[0]

    def pointer(self, rva: int) -> int:
        """Execute the pointer operation for the current toolkit workflow."""
        return self.u32(rva) if self.pointer_size == 4 else self.u64(rva)

    def va_to_rva(self, value: int) -> int | None:
        """Execute the va to rva operation for the current toolkit workflow."""
        if value < self.image.image_base:
            return None
        rva = value - self.image.image_base
        return rva if self.valid_rva(rva) else None

    def encoded_pointer_to_rva(self, value: int) -> int | None:
        """Encode d pointer to rva for the current toolkit workflow."""
        if self.architecture == "x86_64":
            return value if self.valid_rva(value) else None
        return self.va_to_rva(value)

    def c_string(self, rva: int, limit: int = 4096) -> str:
        """Execute the c string operation for the current toolkit workflow."""
        offset = self.rva_to_offset(rva)
        end = self.data.find(b"\x00", offset, min(len(self.data), offset + limit))
        if end < 0:
            raise FormatError(f"unterminated string at RVA 0x{rva:x}")
        return self.data[offset:end].decode("utf-8", errors="replace")

    def executable_rva(self, rva: int) -> bool:
        """Execute the executable rva operation for the current toolkit workflow."""
        return any(
            section.virtual_address <= rva < section.virtual_address + section.mapped_size
            and bool(section.characteristics & 0x20000000)
            for section in self.image.sections
        )

    def readonly_data_sections(self) -> tuple[Section, ...]:
        """Read only data sections for the current toolkit workflow."""
        return tuple(
            section
            for section in self.image.sections
            if section.raw_size
            and bool(section.characteristics & 0x40000000)
            and not bool(section.characteristics & 0x20000000)
        )


def _display_type_name(name: str) -> str:
    """Support display type name processing for internal toolkit callers."""
    match = re.fullmatch(r"\.\?A([VUT])(.+)@@", name)
    if not match:
        return name
    kind = {"V": "class", "U": "struct", "T": "union"}[match.group(1)]
    pieces = [piece for piece in match.group(2).split("@") if piece]
    return f"{kind} " + "::".join(reversed(pieces))


def scan_type_descriptors(view: PEView) -> tuple[TypeDescriptorRecord, ...]:
    """Execute the scan type descriptors operation for the current toolkit workflow."""
    results: dict[int, TypeDescriptorRecord] = {}
    markers = (b".?AV", b".?AU", b".?AT")
    for section in view.readonly_data_sections():
        blob = view.read(section.virtual_address, section.raw_size)
        for marker in markers:
            cursor = 0
            while True:
                index = blob.find(marker, cursor)
                if index < 0:
                    break
                cursor = index + 1
                name_rva = section.virtual_address + index
                descriptor_rva = name_rva - view.pointer_size * 2
                if descriptor_rva < 0 or not view.valid_rva(descriptor_rva, view.pointer_size * 2):
                    continue
                try:
                    name = view.c_string(name_rva, 1024)
                except FormatError:
                    continue
                if not name.endswith("@@"):
                    continue
                results[descriptor_rva] = TypeDescriptorRecord(
                    rva=descriptor_rva,
                    name_rva=name_rva,
                    mangled_name=name,
                    display_name=_display_type_name(name),
                    vfptr=view.pointer(descriptor_rva),
                    spare=view.pointer(descriptor_rva + view.pointer_size),
                )
    return tuple(results[key] for key in sorted(results))


def _parse_base_class(
    view: PEView,
    descriptor_rva: int,
    types: dict[int, TypeDescriptorRecord],
) -> BaseClassRecord | None:
    """Support parse base class processing for internal toolkit callers."""
    if not view.valid_rva(descriptor_rva, 24):
        return None
    type_value = view.u32(descriptor_rva)
    type_rva = view.encoded_pointer_to_rva(type_value)
    if type_rva is None or type_rva not in types:
        return None
    contained = view.u32(descriptor_rva + 4)
    mdisp = view.i32(descriptor_rva + 8)
    pdisp = view.i32(descriptor_rva + 12)
    vdisp = view.i32(descriptor_rva + 16)
    attrs = view.u32(descriptor_rva + 20)
    hierarchy: int | None = None
    if view.valid_rva(descriptor_rva + 24, 4):
        value = view.u32(descriptor_rva + 24)
        candidate = view.encoded_pointer_to_rva(value)
        if candidate is not None and view.valid_rva(candidate, 16):
            hierarchy = candidate
    return BaseClassRecord(
        descriptor_rva=descriptor_rva,
        type_descriptor_rva=type_rva,
        type_name=types[type_rva].display_name,
        contained_bases=contained,
        member_displacement=mdisp,
        vbtable_displacement=pdisp,
        vbase_displacement=vdisp,
        attributes=attrs,
        hierarchy_rva=hierarchy,
    )


def _parse_hierarchy(
    view: PEView,
    hierarchy_rva: int,
    types: dict[int, TypeDescriptorRecord],
) -> tuple[int, tuple[BaseClassRecord, ...]] | None:
    """Support parse hierarchy processing for internal toolkit callers."""
    if not view.valid_rva(hierarchy_rva, 16):
        return None
    signature = view.u32(hierarchy_rva)
    attributes = view.u32(hierarchy_rva + 4)
    count = view.u32(hierarchy_rva + 8)
    array_value = view.u32(hierarchy_rva + 12)
    array_rva = view.encoded_pointer_to_rva(array_value)
    if signature not in (0, 1) or count == 0 or count > 4096 or array_rva is None:
        return None
    if not view.valid_rva(array_rva, count * 4):
        return None
    bases: list[BaseClassRecord] = []
    for index in range(count):
        value = view.u32(array_rva + index * 4)
        descriptor_rva = view.encoded_pointer_to_rva(value)
        if descriptor_rva is None:
            return None
        base = _parse_base_class(view, descriptor_rva, types)
        if base is None:
            return None
        bases.append(base)
    return attributes, tuple(bases)


def scan_complete_object_locators(
    view: PEView, type_descriptors: Iterable[TypeDescriptorRecord]
) -> tuple[CompleteObjectLocatorRecord, ...]:
    """Execute the scan complete object locators operation for the current toolkit workflow."""
    types = {record.rva: record for record in type_descriptors}
    results: dict[int, CompleteObjectLocatorRecord] = {}
    size = 20 if view.architecture == "x86" else 24
    for section in view.readonly_data_sections():
        for relative in range(0, max(0, section.raw_size - size + 1), 4):
            rva = section.virtual_address + relative
            signature = view.u32(rva)
            if view.architecture == "x86":
                if signature != 0:
                    continue
                type_rva = view.va_to_rva(view.u32(rva + 12))
                hierarchy_rva = view.va_to_rva(view.u32(rva + 16))
                self_rva = None
            else:
                if signature != 1:
                    continue
                type_rva = view.u32(rva + 12)
                hierarchy_rva = view.u32(rva + 16)
                self_rva = view.u32(rva + 20)
                if self_rva != rva:
                    continue
            if type_rva not in types or hierarchy_rva is None:
                continue
            hierarchy = _parse_hierarchy(view, hierarchy_rva, types)
            if hierarchy is None:
                continue
            attributes, bases = hierarchy
            results[rva] = CompleteObjectLocatorRecord(
                rva=rva,
                signature=signature,
                offset=view.u32(rva + 4),
                constructor_displacement_offset=view.u32(rva + 8),
                type_descriptor_rva=type_rva,
                class_hierarchy_rva=hierarchy_rva,
                self_rva=self_rva,
                type_name=types[type_rva].display_name,
                hierarchy_attributes=attributes,
                bases=bases,
            )
    return tuple(results[key] for key in sorted(results))


def scan_vtables(
    view: PEView, locators: Iterable[CompleteObjectLocatorRecord]
) -> tuple[VTableRecord, ...]:
    """Execute the scan vtables operation for the current toolkit workflow."""
    locator_by_pointer = {
        view.image.image_base + locator.rva: locator for locator in locators
    }
    results: dict[int, VTableRecord] = {}
    for section in view.readonly_data_sections():
        blob = view.read(section.virtual_address, section.raw_size)
        for relative in range(0, len(blob) - view.pointer_size + 1, view.pointer_size):
            value = int.from_bytes(blob[relative : relative + view.pointer_size], "little")
            locator = locator_by_pointer.get(value)
            if locator is None:
                continue
            address_point_rva = section.virtual_address + relative + view.pointer_size
            functions: list[int] = []
            for slot in range(512):
                pointer_rva = address_point_rva + slot * view.pointer_size
                if not view.valid_rva(pointer_rva, view.pointer_size):
                    break
                function_va = view.pointer(pointer_rva)
                function_rva = view.va_to_rva(function_va)
                if function_rva is None or not view.executable_rva(function_rva):
                    break
                functions.append(function_rva)
            if functions:
                results[address_point_rva] = VTableRecord(
                    address_point_rva=address_point_rva,
                    locator_rva=locator.rva,
                    type_name=locator.type_name,
                    function_rvas=tuple(functions),
                )
    return tuple(results[key] for key in sorted(results))


_UNWIND_OP_NAMES = {
    0: "PUSH_NONVOL",
    1: "ALLOC_LARGE",
    2: "ALLOC_SMALL",
    3: "SET_FPREG",
    4: "SAVE_NONVOL",
    5: "SAVE_NONVOL_FAR",
    6: "EPILOG",
    7: "SPARE_CODE",
    8: "SAVE_XMM128",
    9: "SAVE_XMM128_FAR",
    10: "PUSH_MACHFRAME",
}
_REG_NAMES = ["rax", "rcx", "rdx", "rbx", "rsp", "rbp", "rsi", "rdi"] + [
    f"r{index}" for index in range(8, 16)
]


def _decode_unwind_codes(view: PEView, rva: int, count: int) -> tuple[UnwindCodeRecord, ...]:
    """Support decode unwind codes processing for internal toolkit callers."""
    records: list[UnwindCodeRecord] = []
    slot = 0
    while slot < count:
        code_offset = view.read(rva + slot * 2, 1)[0]
        op_byte = view.read(rva + slot * 2 + 1, 1)[0]
        operation = op_byte & 0x0F
        info = op_byte >> 4
        slots = 1
        decoded: dict[str, Any] = {}
        if operation == 0:
            decoded["register"] = _REG_NAMES[info] if info < len(_REG_NAMES) else info
        elif operation == 1:
            if info == 0:
                if slot + 1 >= count:
                    raise FormatError("truncated UWOP_ALLOC_LARGE")
                decoded["allocation_size"] = view.u16(rva + (slot + 1) * 2) * 8
                slots = 2
            elif info == 1:
                if slot + 2 >= count:
                    raise FormatError("truncated UWOP_ALLOC_LARGE far form")
                decoded["allocation_size"] = view.u32(rva + (slot + 1) * 2)
                slots = 3
            else:
                decoded["invalid_operation_info"] = info
        elif operation == 2:
            decoded["allocation_size"] = info * 8 + 8
        elif operation == 3:
            decoded["uses_frame_register"] = True
        elif operation in (4, 8):
            if slot + 1 >= count:
                raise FormatError("truncated unwind save operation")
            scale = 8 if operation == 4 else 16
            decoded["register"] = _REG_NAMES[info] if operation == 4 and info < len(_REG_NAMES) else info
            decoded["stack_offset"] = view.u16(rva + (slot + 1) * 2) * scale
            slots = 2
        elif operation in (5, 9):
            if slot + 2 >= count:
                raise FormatError("truncated far unwind save operation")
            decoded["register"] = _REG_NAMES[info] if operation == 5 and info < len(_REG_NAMES) else info
            decoded["stack_offset"] = view.u32(rva + (slot + 1) * 2)
            slots = 3
        elif operation == 10:
            decoded["error_code_pushed"] = bool(info)
        records.append(
            UnwindCodeRecord(
                code_offset=code_offset,
                operation=operation,
                operation_name=_UNWIND_OP_NAMES.get(operation, f"UNKNOWN_{operation}"),
                operation_info=info,
                slots=slots,
                decoded=decoded,
            )
        )
        slot += slots
    return tuple(records)


def parse_x64_unwind(view: PEView) -> tuple[UnwindInfoRecord, ...]:
    """Parse x64 unwind for the current toolkit workflow."""
    if view.architecture != "x86_64":
        return ()
    records: list[UnwindInfoRecord] = []
    for function in view.image.runtime_functions:
        rva = function.unwind_info_rva & ~1
        if not view.valid_rva(rva, 4):
            continue
        first, prolog_size, count, frame = view.read(rva, 4)
        version = first & 0x7
        flags = first >> 3
        if version not in (1, 2, 3) or count > 255:
            continue
        codes_rva = rva + 4
        try:
            codes = _decode_unwind_codes(view, codes_rva, count)
        except FormatError:
            continue
        tail_rva = codes_rva + ((count + 1) & ~1) * 2
        handler_rva: int | None = None
        language_data_rva: int | None = None
        chained: dict[str, int] | None = None
        raw_language: str | None = None
        if flags & 0x4:
            if view.valid_rva(tail_rva, 12):
                begin, end, unwind = struct.unpack("<III", view.read(tail_rva, 12))
                chained = {"begin_rva": begin, "end_rva": end, "unwind_info_rva": unwind}
        elif flags & 0x3:
            if view.valid_rva(tail_rva, 4):
                handler_rva = view.u32(tail_rva)
                language_data_rva = tail_rva + 4
                if view.valid_rva(language_data_rva, 64):
                    raw_language = view.read(language_data_rva, 64).hex()
                else:
                    available = max(0, len(view.data) - view.rva_to_offset(language_data_rva))
                    raw_language = view.read(language_data_rva, min(available, 64)).hex() if available else ""
        records.append(
            UnwindInfoRecord(
                function_begin_rva=function.begin_rva,
                function_end_rva=function.end_rva,
                unwind_info_rva=rva,
                version=version,
                flags=flags,
                prolog_size=prolog_size,
                frame_register=frame & 0x0F,
                frame_offset=(frame >> 4) * 16,
                codes=codes,
                handler_rva=handler_rva,
                language_data_rva=language_data_rva,
                chained_function=chained,
                raw_language_data_hex=raw_language,
            )
        )
    return tuple(records)


def parse_safe_seh(view: PEView) -> tuple[int, ...]:
    """Parse safe seh for the current toolkit workflow."""
    config = view.image.load_config
    if view.architecture != "x86" or config is None or not config.seh_table_va or not config.seh_count:
        return ()
    if config.seh_count > 1_000_000:
        raise FormatError("SafeSEH table count exceeds safety limit")
    table_rva = view.va_to_rva(config.seh_table_va)
    if table_rva is None or not view.valid_rva(table_rva, config.seh_count * 4):
        return ()
    values = tuple(view.u32(table_rva + index * 4) for index in range(config.seh_count))
    return values if list(values) == sorted(values) else ()


def tls_report(view: PEView) -> dict[str, Any] | None:
    """Execute the tls report operation for the current toolkit workflow."""
    tls = view.image.tls
    if tls is None:
        return None
    start_rva = view.va_to_rva(tls.start_raw_data_va) if tls.start_raw_data_va else None
    end_rva = view.va_to_rva(tls.end_raw_data_va) if tls.end_raw_data_va else None
    template = b""
    if start_rva is not None and end_rva is not None and end_rva >= start_rva:
        if view.valid_rva(start_rva, end_rva - start_rva):
            template = view.read(start_rva, end_rva - start_rva)
    callback_vas = list(tls.callbacks_va)
    callback_rvas = [view.va_to_rva(value) for value in callback_vas]
    index_rva = view.va_to_rva(tls.address_of_index_va) if tls.address_of_index_va else None
    return {
        **tls.to_dict(),
        "start_raw_data_rva": start_rva,
        "end_raw_data_rva": end_rva,
        "address_of_index_rva": index_rva,
        "callbacks_rva": callback_rvas,
        "template_size": len(template),
        "template_sha256": sha256_bytes(template),
        "template_hex": template.hex(),
    }


def scan_exception_func_info(view: PEView) -> tuple[dict[str, Any], ...]:
    """Find structurally plausible MSVC EH3 FuncInfo records.

    The records are reported as candidates because handler-specific data layouts
    vary by toolset and EH generation.  No source-level catch semantics are
    asserted from this scan alone.
    """
    magic_values = {0x19930520, 0x19930521, 0x19930522}
    results: list[dict[str, Any]] = []
    for section in view.readonly_data_sections():
        for relative in range(0, max(0, section.raw_size - 36), 4):
            rva = section.virtual_address + relative
            magic = view.u32(rva)
            if magic not in magic_values:
                continue
            raw = [view.u32(rva + index * 4) for index in range(9)]
            max_state = struct.unpack("<i", struct.pack("<I", raw[1]))[0]
            n_try = raw[3]
            n_ip = raw[5]
            if max_state < -1 or max_state > 1_000_000 or n_try > 100_000 or n_ip > 1_000_000:
                continue
            pointer_fields = {"unwind_map": raw[2], "try_block_map": raw[4], "ip_state_map": raw[6], "es_type_list": raw[7]}
            decoded: dict[str, int | None] = {}
            plausible = True
            for name, value in pointer_fields.items():
                if value == 0:
                    decoded[name] = None
                    continue
                candidate = view.encoded_pointer_to_rva(value)
                decoded[name] = candidate
                if candidate is None:
                    plausible = False
                    break
            if not plausible:
                continue
            results.append(
                {
                    "rva": rva,
                    "magic": magic,
                    "max_state": max_state,
                    "unwind_map_rva": decoded["unwind_map"],
                    "try_block_count": n_try,
                    "try_block_map_rva": decoded["try_block_map"],
                    "ip_state_count": n_ip,
                    "ip_state_map_rva": decoded["ip_state_map"],
                    "es_type_list_rva": decoded["es_type_list"],
                    "eh_flags": raw[8],
                    "classification": "structurally_plausible_candidate",
                }
            )
    return tuple(results)



def scan_coff_tls(*, object_paths: Iterable[Path] = ()) -> dict[str, Any]:
    """Inventory COFF TLS template and callback subsections.

    COFF subsection names and relocations are retained as linker evidence.  The
    result does not claim the linked TLS directory or callback order unless a
    linked image independently confirms it.
    """
    entries: list[dict[str, Any]] = []
    for path in object_paths:
        obj = parse_coff(path)
        for section in obj.sections:
            upper = section.name.upper()
            if not (upper.startswith(".TLS$") or upper.startswith(".CRT$XL")):
                continue
            kind = "tls_callback" if upper.startswith(".CRT$XL") else "tls_template"
            relocations = [item.to_dict(obj.machine) for item in section.relocations]
            entries.append(
                {
                    "object": None if obj.path is None else str(obj.path),
                    "section_index": section.index,
                    "section": section.name,
                    "order_key": upper,
                    "kind": kind,
                    "size": len(section.raw_data),
                    "sha256": sha256_bytes(section.raw_data),
                    "raw_hex": section.raw_data.hex(),
                    "relocations": relocations,
                    "referenced_symbols": sorted(
                        {item["symbol_name"] for item in relocations if item.get("symbol_name")}
                    ),
                }
            )
    entries.sort(key=lambda item: (item["order_key"], item["object"] or "", item["section_index"]))
    return {
        "schema_version": 1,
        "object_sections": entries,
        "linked_order_claimed": False,
    }

def scan_static_initializers(
    *,
    object_paths: Iterable[Path] = (),
    map_path: Path | None = None,
) -> dict[str, Any]:
    """Execute the scan static initializers operation for the current toolkit workflow."""
    objects: list[CoffObject] = [parse_coff(path) for path in object_paths]
    object_entries: list[dict[str, Any]] = []
    for obj in objects:
        for section in obj.sections:
            if not section.name.upper().startswith(".CRT$X"):
                continue
            relocations = [item.to_dict(obj.machine) for item in section.relocations]
            object_entries.append(
                {
                    "object": None if obj.path is None else str(obj.path),
                    "section_index": section.index,
                    "section": section.name,
                    "order_key": section.name.upper(),
                    "size": len(section.raw_data),
                    "sha256": sha256_bytes(section.raw_data),
                    "relocations": relocations,
                    "initializer_symbols": sorted(
                        {item["symbol_name"] for item in relocations if item.get("symbol_name")}
                    ),
                }
            )
    linker_map: LinkerMap | None = parse_msvc_map(map_path) if map_path is not None else None
    map_entries: list[dict[str, Any]] = []
    if linker_map is not None:
        crt_segments = {segment.segment: segment for segment in linker_map.segments if segment.name.upper().startswith(".CRT$X")}
        for segment in crt_segments.values():
            map_entries.append({"kind": "segment", **segment.to_dict(), "order_key": segment.name.upper()})
        for contribution in linker_map.contributions:
            if contribution.segment in crt_segments:
                map_entries.append(
                    {
                        "kind": "contribution",
                        **contribution.to_dict(),
                        "section": crt_segments[contribution.segment].name,
                        "order_key": crt_segments[contribution.segment].name.upper(),
                    }
                )
    object_entries.sort(key=lambda item: (item["order_key"], item["object"] or "", item["section_index"]))
    map_entries.sort(key=lambda item: (item["order_key"], item.get("offset", 0)))
    return {
        "schema_version": 1,
        "objects": object_entries,
        "map_entries": map_entries,
        "order_rule": "lexicographic COFF subsection order within .CRT",
        "linked_initializer_targets_claimed": False,
    }


def analyze_msvc_metadata(
    pe_path: Path,
    *,
    object_paths: Iterable[Path] = (),
    map_path: Path | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Execute the analyze msvc metadata operation for the current toolkit workflow."""
    view = PEView(pe_path)
    types = scan_type_descriptors(view)
    locators = scan_complete_object_locators(view, types)
    vtables = scan_vtables(view, locators)
    unwind = parse_x64_unwind(view)
    linker_map = parse_msvc_map(map_path) if map_path is not None else None
    map_symbols_by_rva: dict[int, list[str]] = {}
    if linker_map is not None:
        for public in linker_map.publics:
            if public.rva_plus_base >= view.image.image_base:
                map_symbols_by_rva.setdefault(public.rva_plus_base - view.image.image_base, []).append(public.name)
    unwind_records: list[dict[str, Any]] = []
    for record in unwind:
        item = record.to_dict()
        item["function_symbols"] = sorted(map_symbols_by_rva.get(record.function_begin_rva, []))
        item["handler_symbols"] = [] if record.handler_rva is None else sorted(map_symbols_by_rva.get(record.handler_rva, []))
        unwind_records.append(item)
    vtable_records: list[dict[str, Any]] = []
    for record in vtables:
        item = record.to_dict()
        item["function_symbols"] = [sorted(map_symbols_by_rva.get(rva, [])) for rva in record.function_rvas]
        vtable_records.append(item)
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "msvc_metadata_analysis",
        "image": {
            "path": str(view.path),
            "sha256": view.image.file_sha256,
            "architecture": view.architecture,
            "image_base": view.image.image_base,
        },
        "rtti": {
            "type_descriptors": [record.to_dict() for record in types],
            "complete_object_locators": [record.to_dict() for record in locators],
            "vtables": vtable_records,
        },
        "exceptions": {
            "x64_unwind": unwind_records,
            "safe_seh_rvas": list(parse_safe_seh(view)),
            "func_info_candidates": list(scan_exception_func_info(view)),
        },
        "tls": tls_report(view),
        "coff_tls": scan_coff_tls(object_paths=object_paths),
        "static_initializers": scan_static_initializers(object_paths=object_paths, map_path=map_path),
        "source_level_recovery_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
