"""Verify the current toolkit behavior covered by `tests/test_memory.py`."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from x86decomp.memory import ProjectMemory


class MemoryTests(unittest.TestCase):
    """Coordinate memory tests behavior for the current toolkit workflow."""
    def test_hash_chain(self) -> None:
        """Verify hash chain behavior."""
        with tempfile.TemporaryDirectory() as temp:
            memory = ProjectMemory(Path(temp))
            memory.append(actor="test", category="decision", summary="First")
            memory.append(actor="test", category="fact", summary="Second")
            result = memory.verify()
            self.assertTrue(result["valid"], result["failures"])
            self.assertTrue(memory.rendered_path.is_file())

    def test_tamper_detection(self) -> None:
        """Verify tamper detection behavior."""
        with tempfile.TemporaryDirectory() as temp:
            memory = ProjectMemory(Path(temp))
            memory.append(actor="test", category="decision", summary="Original")
            lines = memory.events_path.read_text(encoding="utf-8").splitlines()
            event = json.loads(lines[0])
            event["summary"] = "Tampered"
            memory.events_path.write_text(json.dumps(event) + "\n", encoding="utf-8")
            result = memory.verify()
            self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
