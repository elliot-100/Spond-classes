"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dateutil import parser

if TYPE_CHECKING:
    from datetime import datetime

    from .spond_role import SpondRole
    from .spond_subgroup import SpondSubgroup


@dataclass
class SpondMember:
    """SpondMember: an individual's record within a SpondGroup.

    Belongs to one SpondGroup.
    May belong to zero, one or more SpondSubgroups within a SpondGroup.
    """

    uid: str  # from API 'id'
    created_time: datetime  # from API 'createdTime'
    first_name: str  # from API 'firstName'
    last_name: str  # from API 'lastName'
    roles: list[SpondRole] = field(default_factory=list)  # from API 'roles'
    subgroups: list[SpondSubgroup] = field(default_factory=list)  # from API 'subGroups'
    name: str = field(init=False)  # derived
    _name: str = field(init=False)

    def __repr__(self: SpondMember) -> str:
        """Return string representation."""
        return f"SpondMember(uid='{self.uid}', first_name='{self.first_name}', last_name='{self.last_name}')"

    def __str__(self: SpondMember) -> str:
        """Return simple human-readable description.

        Last few chars of uid are included because full name is unlikely to be unique.
        """
        return (
            f"SpondMember '{self.first_name} {self.last_name}' "
            f"(uid ends '...{self.uid[-3:]}')"
        )

    @property  # type: ignore[no-redef]
    def name(self: SpondMember) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self: SpondMember, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(member_data: dict) -> SpondMember:
        """Create a SpondMember object from relevant dict."""
        if not isinstance(member_data, dict):
            raise TypeError
        uid = member_data["id"]
        created_time = parser.isoparse(member_data["createdTime"])
        first_name = member_data["firstName"]
        last_name = member_data["lastName"]
        return SpondMember(uid, created_time, first_name, last_name)
