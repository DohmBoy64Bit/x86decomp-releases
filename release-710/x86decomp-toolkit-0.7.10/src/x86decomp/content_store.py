"""Content-addressed immutable artifact storage.

Artifacts are addressed by SHA-256 and written atomically.  Metadata records
are immutable except for the separate reference index, which is transactionally
updated under an advisory file lock.  The store never executes artifacts.
"""

from __future__ import annotations

import contextlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from .errors import ContractError, VerificationError
from .util import atomic_write_bytes, canonical_json_bytes, sha256_bytes, sha256_file, utc_now, write_json


@dataclass(frozen=True)
class StoredArtifact:
    """Store validated stored artifact fields used by toolkit reports and adapters."""
    digest: str
    size: int
    data_path: Path
    metadata_path: Path

    def to_dict(self, *, root: Path | None = None) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        def display(path: Path) -> str:
            """Execute the display operation for the current toolkit workflow."""
            if root is not None:
                try:
                    return path.relative_to(root).as_posix()
                except ValueError:
                    pass
            return path.as_posix()
        return {
            "sha256": self.digest,
            "size": self.size,
            "data_path": display(self.data_path),
            "metadata_path": display(self.metadata_path),
        }


class ContentStore:
    """Immutable SHA-256 store rooted at ``root``."""

    def __init__(self, root: Path):
        """Initialize the instance with validated constructor state."""
        self.root = root.resolve()
        self.objects = self.root / "objects" / "sha256"
        self.metadata = self.root / "metadata"
        self.references_path = self.root / "references.json"
        self.lock_path = self.root / ".lock"
        self.objects.mkdir(parents=True, exist_ok=True)
        self.metadata.mkdir(parents=True, exist_ok=True)
        if not self.references_path.exists():
            write_json(self.references_path, {"schema_version": 1, "references": {}})

    def _paths(self, digest: str) -> tuple[Path, Path]:
        """Support paths processing for internal toolkit callers."""
        self._validate_digest(digest)
        data = self.objects / digest[:2] / digest[2:]
        meta = self.metadata / f"{digest}.json"
        return data, meta

    @staticmethod
    def _validate_digest(digest: str) -> None:
        """Support validate digest processing for internal toolkit callers."""
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ContractError("artifact digest must be a lowercase SHA-256 hex string")

    @contextlib.contextmanager
    def _locked(self) -> Iterator[None]:
        """Cross-process advisory lock using an exclusive lock file.

        The lock is intentionally simple and portable.  A stale lock is never
        silently removed; callers receive a clear error and may inspect it.
        """
        self.root.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as exc:
            raise ContractError(f"content store is locked: {self.lock_path}") from exc
        try:
            os.write(fd, f"pid={os.getpid()}\ncreated_at={utc_now()}\n".encode("utf-8"))
            os.fsync(fd)
            yield
        finally:
            os.close(fd)
            try:
                self.lock_path.unlink()
            except FileNotFoundError:
                pass

    def put_bytes(
        self,
        data: bytes,
        *,
        media_type: str = "application/octet-stream",
        source: str | None = None,
        attributes: dict[str, Any] | None = None,
    ) -> StoredArtifact:
        """Execute the put bytes operation for the current toolkit workflow."""
        digest = sha256_bytes(data)
        data_path, metadata_path = self._paths(digest)
        if data_path.exists():
            if sha256_file(data_path) != digest:
                raise VerificationError(f"stored artifact is corrupt: {digest}")
        else:
            data_path.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_bytes(data_path, data)
        metadata = {
            "schema_version": 1,
            "sha256": digest,
            "size": len(data),
            "media_type": media_type,
            "source": source,
            "attributes": attributes or {},
            "stored_at": utc_now(),
        }
        if not metadata_path.exists():
            write_json(metadata_path, metadata)
        else:
            existing = json.loads(metadata_path.read_text(encoding="utf-8"))
            if existing.get("sha256") != digest or existing.get("size") != len(data):
                raise VerificationError(f"artifact metadata is corrupt: {digest}")
        return StoredArtifact(digest, len(data), data_path, metadata_path)

    def put_file(
        self,
        path: Path,
        *,
        media_type: str = "application/octet-stream",
        attributes: dict[str, Any] | None = None,
    ) -> StoredArtifact:
        """Execute the put file operation for the current toolkit workflow."""
        source = path.resolve()
        if not source.is_file() or source.is_symlink():
            raise ContractError(f"artifact source must be a regular file: {source}")
        return self.put_bytes(
            source.read_bytes(),
            media_type=media_type,
            source=str(source),
            attributes=attributes,
        )

    def get(self, digest: str) -> StoredArtifact:
        """Execute the get operation for the current toolkit workflow."""
        data_path, metadata_path = self._paths(digest)
        if not data_path.is_file() or not metadata_path.is_file():
            raise ContractError(f"unknown artifact: {digest}")
        size = data_path.stat().st_size
        return StoredArtifact(digest, size, data_path, metadata_path)

    def read_bytes(self, digest: str) -> bytes:
        """Read bytes for the current toolkit workflow."""
        artifact = self.get(digest)
        data = artifact.data_path.read_bytes()
        if sha256_bytes(data) != digest:
            raise VerificationError(f"stored artifact is corrupt: {digest}")
        return data

    def add_reference(self, reference: str, digest: str, *, kind: str, owner: str) -> dict[str, Any]:
        """Execute the add reference operation for the current toolkit workflow."""
        self.get(digest)
        if not reference or reference.startswith("/") or ".." in Path(reference).parts:
            raise ContractError("artifact reference must be a confined relative identifier")
        with self._locked():
            value = json.loads(self.references_path.read_text(encoding="utf-8"))
            refs = value.setdefault("references", {})
            refs[reference] = {
                "sha256": digest,
                "kind": kind,
                "owner": owner,
                "updated_at": utc_now(),
            }
            write_json(self.references_path, value)
        return refs[reference]

    def remove_reference(self, reference: str) -> bool:
        """Remove reference for the current toolkit workflow."""
        with self._locked():
            value = json.loads(self.references_path.read_text(encoding="utf-8"))
            refs = value.setdefault("references", {})
            removed = refs.pop(reference, None) is not None
            write_json(self.references_path, value)
        return removed

    def referenced_digests(self) -> set[str]:
        """Execute the referenced digests operation for the current toolkit workflow."""
        value = json.loads(self.references_path.read_text(encoding="utf-8"))
        refs = value.get("references", {})
        if not isinstance(refs, dict):
            raise ContractError("content-store references file is invalid")
        return {str(item["sha256"]) for item in refs.values() if isinstance(item, dict) and "sha256" in item}

    def verify(self) -> dict[str, Any]:
        """Verify verify for the current toolkit workflow."""
        failures: list[str] = []
        checked = 0
        for metadata_path in sorted(self.metadata.glob("*.json")):
            try:
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                digest = metadata["sha256"]
                data_path, expected_metadata = self._paths(digest)
                if expected_metadata != metadata_path:
                    failures.append(f"misnamed metadata: {metadata_path.name}")
                    continue
                if not data_path.is_file():
                    failures.append(f"missing object: {digest}")
                    continue
                checked += 1
                if sha256_file(data_path) != digest:
                    failures.append(f"object hash mismatch: {digest}")
                if data_path.stat().st_size != metadata.get("size"):
                    failures.append(f"object size mismatch: {digest}")
            except Exception as exc:  # report all corrupt records
                failures.append(f"metadata error {metadata_path.name}: {exc}")
        try:
            refs = self.referenced_digests()
            for digest in refs:
                data_path, metadata_path = self._paths(digest)
                if not data_path.is_file() or not metadata_path.is_file():
                    failures.append(f"dangling reference: {digest}")
        except Exception as exc:
            failures.append(f"reference index error: {exc}")
        return {"valid": not failures, "objects_checked": checked, "failures": failures}

    def garbage_collect(self, *, dry_run: bool = True) -> dict[str, Any]:
        """Execute the garbage collect operation for the current toolkit workflow."""
        referenced = self.referenced_digests()
        candidates: list[dict[str, Any]] = []
        for metadata_path in sorted(self.metadata.glob("*.json")):
            digest = metadata_path.stem
            if digest in referenced:
                continue
            data_path, _ = self._paths(digest)
            size = data_path.stat().st_size if data_path.exists() else 0
            candidates.append({"sha256": digest, "size": size})
        if not dry_run and candidates:
            with self._locked():
                for item in candidates:
                    data_path, metadata_path = self._paths(item["sha256"])
                    data_path.unlink(missing_ok=True)
                    metadata_path.unlink(missing_ok=True)
                    try:
                        data_path.parent.rmdir()
                    except OSError:
                        pass
        return {
            "dry_run": dry_run,
            "candidate_count": len(candidates),
            "candidate_bytes": sum(item["size"] for item in candidates),
            "candidates": candidates,
        }

    def export_index(self) -> dict[str, Any]:
        """Execute the export index operation for the current toolkit workflow."""
        artifacts: list[dict[str, Any]] = []
        for metadata_path in sorted(self.metadata.glob("*.json")):
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            artifacts.append(metadata)
        references = json.loads(self.references_path.read_text(encoding="utf-8"))
        payload = {"schema_version": 1, "artifacts": artifacts, "references": references.get("references", {})}
        payload["index_sha256"] = sha256_bytes(canonical_json_bytes(payload))
        return payload
