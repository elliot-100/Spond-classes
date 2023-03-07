"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from dateutil import parser


@dataclass
class SpondMember:
    """Spond member: an individual's record within a SpondGroup.

    Belongs to one SpondGroup.
    May belong to zero, one or more SpondSubgroups within a SpondGroup.
    """

    uid: str  # from API 'id'
    created_time: datetime  # from API 'createdTime'
    first_name: str  # from API 'firstName'
    last_name: str  # from API 'lastName'
    roles: list[str] = field(default_factory=list)  # from API 'roles'
    subgroups: list[SpondSubgroup] = field(default_factory=list)  # from API 'subGroups'
    name: str = field(init=False)  # derived
    _name: str = field(init=False, repr=False)

    def __str__(self) -> str:
        """Return human-readable description.

        uid is included because full name is unlikely to be unique.
        """
        return f"[SpondMember '{self.first_name} {self.last_name} {self.uid}']"

    @property  # type: ignore[no-redef]
    def name(self) -> str:
        """Return the member's full name."""
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(member_data: dict) -> SpondMember:
        """Create a SpondMember object from relevant dict."""
        assert isinstance(member_data, dict)
        uid = member_data["id"]
        created_time = parser.isoparse(member_data["createdTime"])
        first_name = member_data["firstName"]
        last_name = member_data["lastName"]
        roles = member_data.get("roles", [])
        return SpondMember(uid, created_time, first_name, last_name, roles)


@dataclass
class SpondGroup:
    """Spond group.

    May contain zero, one or more SpondMembers.
    May contain zero, one or more SpondSubgroups.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list)
    # derived from API 'members', but uses object refs instead of uid.
    subgroups: list[SpondSubgroup] = field(default_factory=list)
    # derived from API 'subgroups'.

    def __str__(self) -> str:
        """Return human-readable description."""
        return f"[SpondGroup '{self.name}']"

    @staticmethod
    def core_from_dict(group_data: dict) -> SpondGroup:
        """Create a SpondGroup object from the simplest possible dict representation."""
        assert isinstance(group_data, dict)
        uid = group_data["id"]
        name = group_data["name"]
        return SpondGroup(uid, name)

    @staticmethod
    def from_dict(group_data: dict) -> SpondGroup:
        """Create a full-feature SpondGroup object from dict representation."""
        spondgroup = SpondGroup.core_from_dict(group_data)

        # create child SpondMembers
        spondgroup.members = [
            SpondMember.from_dict(member_data)
            for member_data in group_data.get("members", [])
        ]
        # create child SpondSubGroups
        spondgroup.subgroups = [
            SpondSubgroup.from_dict(subgroup_data)
            for subgroup_data in group_data.get("subGroups", [])
        ]
        for member_data in group_data.get("members", []):
            member_id = member_data.get("id")
            for subgroup_id in member_data.get("subGroups", []):
                # populate child SpondMembers' subgroup attributes
                spondgroup.member_by_id(member_id).subgroups.append(
                    spondgroup.subgroup_by_id(subgroup_id)
                )
                # populate child SpondSubgroups' members attribute
                spondgroup.subgroup_by_id(subgroup_id).members.append(
                    spondgroup.member_by_id(member_id)
                )

        return spondgroup

    def subgroup_by_id(self, subgroup_uid: str) -> SpondSubgroup:
        """Return the child subgroup with matching id, or an error."""
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        raise IndexError

    def member_by_id(self, member_uid: str) -> SpondMember:
        """Return the child member with matching id, or an error."""
        for member in self.members:
            if member.uid == member_uid:
                return member
        raise IndexError


@dataclass()
class SpondSubgroup:
    """Spond subgroup.

    Belongs to one SpondGroup.
    May contain zero, one or more SpondMembers.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list)  # derived

    def __str__(self) -> str:
        """Return human-readable description."""
        return f"[SpondSubgroup '{self.name}']"

    @staticmethod
    def from_dict(subgroup_data: dict) -> SpondSubgroup:
        """Create a SpondSubgroup object from relevant dict."""
        assert isinstance(subgroup_data, dict)
        uid = subgroup_data["id"]
        name = subgroup_data["name"]
        return SpondSubgroup(uid, name)


@dataclass
class SpondEvent:
    """Spond event.

    Belongs to one SpondGroup.
    """

    uid: str  # from API 'id'
    heading: str  # from API 'heading'
    start_time: datetime  # from API 'startTimestamp'

    accepted_uids: list = field(default_factory=list)
    declined_uids: list = field(default_factory=list)
    unanswered_uids: list = field(default_factory=list)
    waiting_list_uids: list = field(default_factory=list)
    unconfirmed_uids: list = field(default_factory=list)
    name: str = field(init=False)  # derived; aliases `heading` for consistency
    # with other objects
    _name: str = field(init=False, repr=False)

    @property  # type: ignore[no-redef]
    def name(self) -> str:
        """Alias `heading` for convenience/consistency with other objects."""
        return self.heading

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(event_data: dict) -> SpondEvent:
        """Create a SpondEvent object from relevant dict."""
        assert isinstance(event_data, dict)
        uid = event_data["id"]
        heading = event_data["heading"]
        start_time = parser.isoparse(event_data["startTimestamp"])
        assert isinstance(event_data["responses"], dict)
        accepted_uids = event_data["responses"].get("acceptedIds", [])
        declined_uids = event_data["responses"].get("declinedIds", [])
        unanswered_uids = event_data["responses"].get("unansweredIds", [])
        waiting_list_uids = event_data["responses"].get("waitinglistIds", [])
        unconfirmed_uids = event_data["responses"].get("unconfirmedIds", [])

        return SpondEvent(
            uid,
            heading,
            start_time,
            accepted_uids,
            declined_uids,
            unanswered_uids,
            waiting_list_uids,
            unconfirmed_uids,
        )

    def __str__(self) -> str:
        """Return human-readable description.

        Date is included because heading is unliklely to be unique.
        """
        return f"[SpondEvent '{self.heading}' on {self.start_time.date()}]"
