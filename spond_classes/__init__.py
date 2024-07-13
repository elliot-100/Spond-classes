"""Main module."""

# Explicitly import all classes and functions into the package namespace.

from .event import Event, EventType
from .group import Group
from .member import Member
from .role import Role
from .subgroup import Subgroup

__all__ = [
    "Event",
    "EventType",
    "Group",
    "Member",
    "Role",
    "Subgroup",
]
