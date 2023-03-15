"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .spond_member import SpondMember


@dataclass
class SpondRole:
    """Spond role.

    Belongs to one SpondGroup.
    A SpondMember may have zero, one or more SpondRoles.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list, repr=False)  # derived

    @staticmethod
    def from_dict(role: dict) -> SpondRole:
        """Create a SpondRole object from relevant dict."""
        if not isinstance(role, dict):
            raise TypeError
        uid = role["id"]
        name = role["name"]

        return SpondRole(
            uid,
            name,
        )

    def __str__(self: SpondRole) -> str:
        """Return simple human-readable description."""
        return f"SpondRole '{self.name}'"
