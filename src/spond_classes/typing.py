"""Module containing typing classes."""

from __future__ import annotations

from collections.abc import Iterable
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


def _ensure_iterable_of_dict(value: Any) -> None:
    """Ensure that `value` is an `Iterable` of `dict`s.

    Raises
    ------
    `TypeError`
        if `value` is not a `iter[dict]`.
    """
    if not isinstance(value, Iterable):
        err_msg = f"Expected `Iterable`, got `{value.__class__.__name__}`: '{value}'"
        raise TypeError(err_msg)

    if not all(isinstance(item, dict) for item in value):
        err_msg = (
            f"Expected `Iterable[dict]`, got `{value.__class__.__name__}`: '{value}'"
        )
        raise TypeError(err_msg)
