"""Member class."""
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
    """Represents a member in the Spond system.

    A Member is an individual's record within a Group.

    A Member belongs to one Group.
    A Member has zero, one or more Roles.
    NB: relationship to Events isn't yet implemented.

    Attributes
    ----------
    uid : str
        id of the Member.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    created_time : datetime
        Derived from 'createdTime' in API, but returns a datetime instead of a string.
    email : str
        'email' in API.
    first_name : str
        'firstName' in API.
    last_name : str
        'lastName' in API.
    phone_number : str
        'phoneNumber' in API.
    profile_uid : str
        `profile` -> `id` in API.
    roles : list[Role]
        The Member's Roles.
        'roles' in API.
    subgroups : list[Subgroup]
        The Member's Subgroups.
        Derived from 'subGroups' in API.
    full_name : str
        The Member's full name.
        Provided for convenience.
    """

    # Populated by implicit Member.__init__().
    uid: str
    created_time: datetime
    email: str | None
    first_name: str
    last_name: str
    phone_number: str | None
    profile_uid: str | None

    # Populated by `Group.from_dict()`, as they rely on full Group data:
    roles: list[Role] = field(default_factory=list)
    subgroups: list[Subgroup] = field(default_factory=list)

    def __repr__(self: Member) -> str:
        """Return string representation."""
        return (
            f"Member(uid='{self.uid}', first_name='{self.first_name}', "
            f"last_name='{self.last_name}')"
        )

    def __str__(self: Member) -> str:
        """Return simple human-readable description.

        Last few chars of uid are included because full name is unlikely to be unique.
        """
        return (
            f"Member '{self.first_name} {self.last_name}' "
            f"(uid ends '...{self.uid[-3:]}')"
        )

    @property
    def full_name(self: Member) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def from_dict(member_data: dict) -> Member:
        """Create a Member object from relevant dict.

        Parameters
        ----------
        member_data
            Dict representing the member, as returned by `spond.get_person()`.
        """
        if not isinstance(member_data, dict):
            raise TypeError
        uid = member_data["id"]
        created_time = parser.isoparse(member_data["createdTime"])
        first_name = member_data["firstName"]
        last_name = member_data["lastName"]

        # Handle data that may be missing/private
        email = member_data.get("email")
        phone_number = member_data.get("phoneNumber")
        profile = member_data.get("profile")
        if profile:
            profile_uid = profile["id"]
        else:
            profile_uid = None

        return Member(
            uid,
            created_time,
            email,
            first_name,
            last_name,
            phone_number,
            profile_uid,
        )
