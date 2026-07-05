"""Provide x86decomp.native.matching functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from x86decomp.coff import extract_symbol, parse_coff
from x86decomp.pe import parse_pe
from x86decomp.util import sha256_bytes, sha256_file
from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import NativeStore

DEFAULT_PAD_BYTES = frozenset({0x00, 0x90, 0xCC})


def rva_to_file_offset(image: Any, rva: int) -> int:
    """Implement rva to file offset.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if rva < image.size_of_headers:
        return rva
    for section in image.sections:
        delta = rva - section.virtual_address
        if 0 <= delta < section.raw_size:
            return section.raw_offset + delta
    raise ContractError(f"RVA 0x{rva:x} is not backed by file data")


def extract_candidate(path: Path, *, symbol: str | None = None, size: int | None = None) -> bytes:
    """Extract candidate.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not path.is_file():
        raise ContractError(f"candidate does not exist: {path}")
    if symbol is None:
        return path.read_bytes()
    return extract_symbol(parse_coff(path), symbol, size=size).data


def compare_function_bytes(
    original: bytes,
    candidate: bytes,
    *,
    policy: str = "exact",
    pad_bytes: Iterable[int] = DEFAULT_PAD_BYTES,
    protected_offsets: Iterable[int] = (),
) -> dict[str, Any]:
    """Compare function bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if policy not in {"exact", "trailing-padding"}:
        raise ContractError(f"unsupported comparison policy: {policy}")
    pads = frozenset(int(value) for value in pad_bytes)
    if not pads or any(value < 0 or value > 255 for value in pads):
        raise ContractError("pad bytes must be non-empty byte values")
    protected = frozenset(int(value) for value in protected_offsets)
    common = min(len(original), len(candidate))
    first = next((index for index in range(common) if original[index] != candidate[index]), common)
    exact = original == candidate
    normalized = False
    if not exact and policy == "trailing-padding":
        tail_start = first
        all_tail_padding = (
            all(value in pads for value in original[tail_start:])
            and all(value in pads for value in candidate[tail_start:])
        )
        protected_tail = any(offset >= tail_start for offset in protected)
        normalized = all_tail_padding and not protected_tail
    classification = "exact" if exact else "padding-normalized" if normalized else "mismatch"
    return {
        "classification": classification,
        "equal": exact,
        "replacement_safe": exact or normalized,
        "original_size": len(original),
        "candidate_size": len(candidate),
        "matching_prefix_bytes": first,
        "first_mismatch": None if exact else first,
        "original_sha256": sha256_bytes(original),
        "candidate_sha256": sha256_bytes(candidate),
        "policy": policy,
        "pad_bytes": sorted(pads),
        "protected_offsets": sorted(protected),
        "semantic_equivalence_claimed": False,
    }


class FunctionMatching:
    """Represent function matching state and behavior.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def __init__(self, store: NativeStore):
        """Initialize the instance with the supplied constructor arguments.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        self.store = store; store.initialize()

    def batch(
        self,
        original_path: Path,
        candidates: Iterable[dict[str, Any]],
        *,
        policy: str = "trailing-padding",
        pad_bytes: Iterable[int] = DEFAULT_PAD_BYTES,
        actor: str = "analyst",
    ) -> dict[str, Any]:
        """Implement batch.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        original_path = original_path.resolve()
        image = parse_pe(original_path)
        payload = original_path.read_bytes()
        pads = sorted(set(int(value) for value in pad_bytes))
        run_id = random_id("matchrun"); now = utc_now()
        results: list[dict[str, Any]] = []
        counts: dict[str, int] = {}
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO native_match_runs VALUES(?,?,?,?,?,?,?,?,?)",
                (run_id, str(original_path), sha256_file(original_path), policy, canonical_json(pads), "running", "{}", now, now),
            )
            for item in candidates:
                function_id = str(item["function_id"])
                rva = int(item["rva"], 0) if isinstance(item["rva"], str) else int(item["rva"])
                slot_size = int(item["slot_size"])
                if slot_size <= 0: raise ContractError(f"invalid slot size for {function_id}")
                offset = rva_to_file_offset(image, rva)
                original = payload[offset:offset + slot_size]
                if len(original) != slot_size: raise ContractError(f"slot for {function_id} exceeds file data")
                candidate_path = Path(str(item["candidate_path"])).resolve()
                candidate = extract_candidate(candidate_path, symbol=item.get("symbol"), size=item.get("candidate_size"))
                protected = item.get("protected_offsets", [])
                if len(candidate) > slot_size:
                    comparison = {
                        "classification": "oversized", "equal": False, "replacement_safe": False,
                        "original_size": len(original), "candidate_size": len(candidate), "matching_prefix_bytes": 0,
                        "first_mismatch": slot_size, "original_sha256": sha256_bytes(original),
                        "candidate_sha256": sha256_bytes(candidate), "policy": policy, "pad_bytes": pads,
                        "protected_offsets": list(protected), "semantic_equivalence_claimed": False,
                    }
                else:
                    comparison = compare_function_bytes(original, candidate, policy=policy, pad_bytes=pads, protected_offsets=protected)
                    if len(candidate) < slot_size:
                        remainder = original[len(candidate):]
                        comparison["slot_remainder_preserved"] = len(remainder)
                        comparison["slot_remainder_is_padding"] = all(value in set(pads) for value in remainder)
                        prefix_matches = comparison["matching_prefix_bytes"] == len(candidate)
                        if prefix_matches and not comparison["slot_remainder_is_padding"]:
                            comparison["classification"] = "truncated-nonpadding"
                            comparison["replacement_safe"] = False
                classification = str(comparison["classification"])
                counts[classification] = counts.get(classification, 0) + 1
                match_id = random_id("match")
                details = {**comparison, "symbol": item.get("symbol")}
                connection.execute(
                    "INSERT INTO native_function_matches VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (match_id, run_id, function_id, rva, slot_size, str(candidate_path), sha256_file(candidate_path), len(candidate),
                     classification, comparison.get("first_mismatch"), int(bool(comparison["replacement_safe"])), canonical_json(details), now),
                )
                results.append({"match_id": match_id, "function_id": function_id, "rva": rva, "slot_size": slot_size, "candidate_path": str(candidate_path), **comparison})
            summary = {"total": len(results), "counts": counts, "safe": sum(1 for row in results if row["replacement_safe"]), "fallback": sum(1 for row in results if not row["replacement_safe"])}
            connection.execute("UPDATE native_match_runs SET status='completed',summary_json=?,updated_at=? WHERE run_id=?", (canonical_json(summary), utc_now(), run_id))
            self.store.audit(actor, "native.match.batch", run_id, summary, connection=connection)
        return {"run_id": run_id, "summary": summary, "functions": results}

    def report(self, run_id: str) -> dict[str, Any]:
        """Report the requested operation.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        with self.store.connect() as connection:
            run = connection.execute("SELECT * FROM native_match_runs WHERE run_id=?", (run_id,)).fetchone()
            if run is None: raise KeyError(run_id)
            result = self.store.decode(run, "pad_bytes_json", "summary_json")
            result["functions"] = [self.store.decode(row, "details_json") for row in connection.execute(
                "SELECT * FROM native_function_matches WHERE run_id=? ORDER BY rva", (run_id,)
            )]
            return result

    def mismatches(self, run_id: str) -> list[dict[str, Any]]:
        """Implement mismatches.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return [item for item in self.report(run_id)["functions"] if not item["replacement_safe"]]
