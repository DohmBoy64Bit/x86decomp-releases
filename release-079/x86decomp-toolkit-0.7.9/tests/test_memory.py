"""Provide tests.test_memory functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from x86decomp.memory import ProjectMemory


class MemoryTests(unittest.TestCase):
    """Implement the MemoryTests class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def test_hash_chain(self) -> None:
        """Verify hash chain.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with tempfile.TemporaryDirectory() as temp:
            memory = ProjectMemory(Path(temp))
            memory.append(actor="test", category="decision", summary="First")
            memory.append(actor="test", category="fact", summary="Second")
            result = memory.verify()
            self.assertTrue(result["valid"], result["failures"])
            self.assertTrue(memory.rendered_path.is_file())

    def test_tamper_detection(self) -> None:
        """Verify tamper detection.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
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
