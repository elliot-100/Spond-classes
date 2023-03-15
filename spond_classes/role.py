"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .member import Member


@dataclass
class Role:
    """Spond role.

    Belongs to one Group.
    A Member may have zero, one or more SpondRoles.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[Member] = field(default_factory=list, repr=False)  # derived

    @staticmethod
    def from_dict(role: dict) -> Role:
        """Create a Role object from relevant dict."""
        if not isinstance(role, dict):
            raise TypeError
        uid = role["id"]
        name = role["name"]

        return Role(
            uid,
            name,
        )

    def __str__(self: Role) -> str:
        """Return simple human-readable description."""
        return f"Role '{self.name}'"
