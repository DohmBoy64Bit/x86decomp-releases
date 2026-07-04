"""Relocation-aware assembly materialization capabilities."""

from .annotation import render_annotated_assembly, render_byte_assembly
from .materialize import materialize_function
from .relocations import RelocationResolver
from .store import AssemblyStore

__all__ = [
    "RelocationResolver",
    "AssemblyStore",
    "materialize_function",
    "render_annotated_assembly",
    "render_byte_assembly",
]
SCHEMA_EXTENSION_VERSION = 7
