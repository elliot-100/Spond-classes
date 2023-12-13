"""Utilities for testing."""
from __future__ import annotations
from inspect import getmembers
from types import FunctionType


def public_attributes(obj: object) -> list[str]:
    """Return the public attributes of an object."""
    members = getmembers(type(obj))
    methods = {name for name, value in members if isinstance(value, FunctionType)}
    return [
        name
        for name in dir(obj)
        if name[0] != "_" and name not in methods and hasattr(obj, name)
    ]


def sets_equal(obj1: list[str], obj2: list[str]) -> bool:
    """Compare two lists, ignoring order."""
    return set(obj1) == set(obj2)
