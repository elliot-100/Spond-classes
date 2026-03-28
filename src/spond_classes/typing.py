"""Module containing typing classes."""

from typing import Any, TypeAlias

DictFromJSON: TypeAlias = dict[str, Any]
"""Simple type alias to annotate dicts returned from Spond API calls."""


def _ensure_dict(value: Any) -> None:
    """Ensure that `value` is a `dict`.

    Raises
    ------
    `TypeError`
        if `value` is not a `dict`.
    """
    if not isinstance(value, dict):
        err_msg = f"Expected `dict`, got `{value.__class__.__name__}`: '{value}'"
        raise TypeError(err_msg)
