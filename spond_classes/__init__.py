"""
# Introduction

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python [`spond`](https://github.com/Olen/Spond/) package gets data from
the Spond API and returns `dict` objects.

This unofficial Python [`spond-classes`](https://github.com/elliot-100/Spond-classes)
package parses those `dict`s to [Pydantic](https://docs.pydantic.dev/) class instances.

# Key classes

These are the classes intended for direct user instantiation:

- `Event` via `Event.from_dict()`
- `Group` via `Group.from_dict()`
"""

# Explicitly import classes and functions into the package namespace to define the API.

from . import typing
from .event import Event, Responses
from .group import Group
from .member import Member
from .profile_ import Profile
from .role import Role
from .subgroup import Subgroup

__all__ = [
    "Event",
    "Responses",
    "Group",
    "Member",
    "Profile",
    "Role",
    "Subgroup",
    "typing",
]
