"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .spond_member import SpondMember


@dataclass
class SpondSubgroup:
    """SpondSubgroup.

    Belongs to one SpondGroup.
    May contain zero, one or more SpondMembers.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list, repr=False)  # derived

    def __str__(self: SpondSubgroup) -> str:
        """Return simple human-readable description."""
        return f"SpondSubgroup '{self.name}'"

    @staticmethod
    def from_dict(subgroup_data: dict) -> SpondSubgroup:
        """Create a SpondSubgroup object from relevant dict."""
        if not isinstance(subgroup_data, dict):
            raise TypeError
        uid = subgroup_data["id"]
        name = subgroup_data["name"]
        return SpondSubgroup(uid, name)
