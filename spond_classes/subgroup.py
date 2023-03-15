"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .member import Member


@dataclass
class Subgroup:
    """Subgroup.

    Belongs to one Group.
    May contain zero, one or more SpondMembers.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[Member] = field(default_factory=list, repr=False)  # derived

    def __str__(self: Subgroup) -> str:
        """Return simple human-readable description."""
        return f"Subgroup '{self.name}'"

    @staticmethod
    def from_dict(subgroup_data: dict) -> Subgroup:
        """Create a Subgroup object from relevant dict."""
        if not isinstance(subgroup_data, dict):
            raise TypeError
        uid = subgroup_data["id"]
        name = subgroup_data["name"]
        return Subgroup(uid, name)
