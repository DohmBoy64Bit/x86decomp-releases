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
            """Render a path relative to ``root`` when possible, else as a POSIX string."""
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
        """Initialize ContentStore with `root`."""
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
        """Return the object and metadata paths for a digest after validating it.

        Args:
            digest: A lowercase SHA-256 hex digest.

        Returns:
            A ``(data_path, metadata_path)`` tuple.

        Raises:
            ContractError: If ``digest`` is not a valid SHA-256 hex string.
        """
        self._validate_digest(digest)
        data = self.objects / digest[:2] / digest[2:]
        meta = self.metadata / f"{digest}.json"
        return data, meta

    @staticmethod
    def _validate_digest(digest: str) -> None:
        """Validate that a digest is a 64-character lowercase SHA-256 hex string.

        Args:
            digest: The digest to validate.

        Raises:
            ContractError: If the digest is malformed.
        """
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
        """Store raw bytes content-addressed by SHA-256 and record its metadata.

        Writing is idempotent: an existing object is verified rather than rewritten, and
        existing metadata is checked for consistency instead of overwritten.

        Args:
            data: The bytes to store.
            media_type: The MIME type recorded in metadata.
            source: Optional source description recorded in metadata.
            attributes: Optional extra attributes recorded in metadata.

        Returns:
            A :class:`StoredArtifact` describing the stored object.

        Raises:
            VerificationError: If an existing object or metadata record is corrupt or
                inconsistent with ``data``.
        """
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
        """Read a regular file and store its contents via :meth:`put_bytes`.

        Args:
            path: Path to the file to store.
            media_type: The MIME type recorded in metadata.
            attributes: Optional extra attributes recorded in metadata.

        Returns:
            A :class:`StoredArtifact` describing the stored object.

        Raises:
            ContractError: If ``path`` is not a regular file or is a symlink.
        """
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
        """Return the :class:`StoredArtifact` for a stored digest.

        Args:
            digest: The SHA-256 digest of the artifact.

        Returns:
            The stored artifact metadata.

        Raises:
            ContractError: If the digest is invalid or the artifact is not present.
        """
        data_path, metadata_path = self._paths(digest)
        if not data_path.is_file() or not metadata_path.is_file():
            raise ContractError(f"unknown artifact: {digest}")
        size = data_path.stat().st_size
        return StoredArtifact(digest, size, data_path, metadata_path)

    def read_bytes(self, digest: str) -> bytes:
        """Return the stored bytes for a digest, re-verifying their hash.

        Args:
            digest: The SHA-256 digest of the artifact.

        Returns:
            The raw artifact bytes.

        Raises:
            ContractError: If the artifact is not present.
            VerificationError: If the stored bytes do not hash to ``digest``.
        """
        artifact = self.get(digest)
        data = artifact.data_path.read_bytes()
        if sha256_bytes(data) != digest:
            raise VerificationError(f"stored artifact is corrupt: {digest}")
        return data

    def add_reference(self, reference: str, digest: str, *, kind: str, owner: str) -> dict[str, Any]:
        """Record a named reference to a stored artifact in the reference index.

        The update is performed under the store's advisory lock.

        Args:
            reference: A confined relative identifier naming the reference.
            digest: The digest the reference points to; must already exist.
            kind: A caller-defined reference category.
            owner: The owner recorded for the reference.

        Returns:
            The stored reference record.

        Raises:
            ContractError: If the artifact is unknown or the reference is absolute or
                contains ``..`` components.
        """
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
        """Remove a named reference from the index under the advisory lock.

        Args:
            reference: The reference identifier to remove.

        Returns:
            ``True`` if a reference was removed, ``False`` if it was absent.
        """
        with self._locked():
            value = json.loads(self.references_path.read_text(encoding="utf-8"))
            refs = value.setdefault("references", {})
            removed = refs.pop(reference, None) is not None
            write_json(self.references_path, value)
        return removed

    def referenced_digests(self) -> set[str]:
        """Return the set of digests currently named by the reference index.

        Returns:
            The set of referenced SHA-256 digests.

        Raises:
            ContractError: If the references file is not a valid mapping.
        """
        value = json.loads(self.references_path.read_text(encoding="utf-8"))
        refs = value.get("references", {})
        if not isinstance(refs, dict):
            raise ContractError("content-store references file is invalid")
        return {str(item["sha256"]) for item in refs.values() if isinstance(item, dict) and "sha256" in item}

    def verify(self) -> dict[str, Any]:
        """Check every metadata record and reference for integrity.

        Verifies object presence, hash, size, and metadata naming, and detects dangling
        references. Corrupt records are collected rather than raised.

        Returns:
            A dict with ``valid``, ``objects_checked``, and a ``failures`` list.
        """
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
        """Identify (and optionally delete) unreferenced objects and metadata.

        Deletion, when performed, runs under the store's advisory lock.

        Args:
            dry_run: If ``True`` (default), only report candidates without deleting.

        Returns:
            A dict with ``dry_run``, ``candidate_count``, ``candidate_bytes``, and the
            ``candidates`` list.
        """
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
        """Build a self-describing index of all artifacts and references.

        Returns:
            A dict of artifact metadata and references, with an ``index_sha256`` digest
            over the canonical JSON encoding of the payload.
        """
        artifacts: list[dict[str, Any]] = []
        for metadata_path in sorted(self.metadata.glob("*.json")):
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            artifacts.append(metadata)
        references = json.loads(self.references_path.read_text(encoding="utf-8"))
        payload = {"schema_version": 1, "artifacts": artifacts, "references": references.get("references", {})}
        payload["index_sha256"] = sha256_bytes(canonical_json_bytes(payload))
        return payload
