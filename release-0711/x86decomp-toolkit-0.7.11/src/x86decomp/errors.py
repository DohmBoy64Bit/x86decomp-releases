"""Typed errors used by the toolkit."""


class X86DecompError(Exception):
    """Base class for user-facing toolkit errors."""


class FormatError(X86DecompError):
    """Raised when an input binary or document violates its contract."""


class ContractError(X86DecompError, ValueError):
    """Raised when structured data violates a toolkit contract.

    The class inherits from both :class:`X86DecompError` and :class:`ValueError`
    so legacy callers catching either public error family continue to work while
    the toolkit exposes a single contract-error identity.
    """


class VerificationError(X86DecompError):
    """Raised when integrity or evidence verification fails."""


class ExternalToolError(X86DecompError):
    """Raised when a configured external tool cannot be executed successfully."""
