"""Main module."""

# Explicitly import classes and functions into the package namespace to define the API.

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
