"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dateutil import parser

if TYPE_CHECKING:
    from datetime import datetime

    from .role import Role
    from .subgroup import Subgroup


@dataclass
class Member:
    """Member: an individual's record within a Group.

    Belongs to one Group.
    May belong to zero, one or more SpondSubgroups within a Group.
    """

    uid: str  # from API 'id'
    created_time: datetime  # from API 'createdTime'
    first_name: str  # from API 'firstName'
    last_name: str  # from API 'lastName'
    roles: list[Role] = field(default_factory=list)  # from API 'roles'
    subgroups: list[Subgroup] = field(default_factory=list)  # from API 'subGroups'

    def __repr__(self: Member) -> str:
        """Return string representation."""
        return f"Member(uid='{self.uid}', first_name='{self.first_name}', last_name='{self.last_name}')"

    def __str__(self: Member) -> str:
        """Return simple human-readable description.

        Last few chars of uid are included because full name is unlikely to be unique.
        """
        return (
            f"Member '{self.first_name} {self.last_name}' "
            f"(uid ends '...{self.uid[-3:]}')"
        )

    @property  # type: ignore[no-redef]
    def full_name(self: Member) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def from_dict(member_data: dict) -> Member:
        """Create a Member object from relevant dict."""
        if not isinstance(member_data, dict):
            raise TypeError
        uid = member_data["id"]
        created_time = parser.isoparse(member_data["createdTime"])
        first_name = member_data["firstName"]
        last_name = member_data["lastName"]
        return Member(uid, created_time, first_name, last_name)
