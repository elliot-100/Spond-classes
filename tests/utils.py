"""
Utilities for testing
"""


from inspect import getmembers
from types import FunctionType


def public_attributes(obj) -> list:
    members = getmembers(type(obj))
    methods = {
        name for name, value in members if isinstance(value, FunctionType)
    }
    return [
        name
        for name in dir(obj)
        if name[0] != "_" and name not in methods and hasattr(obj, name)
    ]

def sets_equal(obj1: list, obj2: list) -> bool:
    return set(obj1) == set(obj2)