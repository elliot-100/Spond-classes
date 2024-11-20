"""Module containing typing classes."""

from typing import Any, TypeAlias

DictFromJSON: TypeAlias = dict[str, Any]
"""Simple type alias to annotate dicts returned by `Spond.get...()` calls."""
