"""
Custom classes for Spond data, and methods to create them from dicts returned by
`spond` package.

"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from dateutil import parser


@dataclass
class SpondMember:
    """
    Spond member: an individual's record within a SpondGroup.

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
        return f"[SpondMember '{self.first_name} {self.last_name} {self.uid}']"

    @property  # type: ignore[no-redef]
    def name(self) -> str:
        """
        Return the member's full name
        """
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(member: dict) -> SpondMember:
        """
        Create a SpondMember object from relevant dict.
        """
        assert isinstance(member, dict)
        uid = member["id"]
        created_time = parser.isoparse(member["createdTime"])
        first_name = member["firstName"]
        last_name = member["lastName"]
        roles = member.get("roles", [])
        return SpondMember(uid, created_time, first_name, last_name, roles)


@dataclass
class SpondGroup:
    """
    Spond group.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list)
    # derived from API 'members', but uses object refs instead of uid.
    subgroups: list[SpondSubgroup] = field(default_factory=list)
    # derived from API 'subgroups'

    def __str__(self) -> str:
        return f"[SpondGroup '{self.name}']"

    @staticmethod
    def core_from_dict(group: dict) -> SpondGroup:
        """
        Create a minimal SpondGroup object from the simplest possible dict
        representation.
        """
        assert isinstance(group, dict)
        uid = group["id"]
        name = group["name"]
        return SpondGroup(uid, name)

    @staticmethod
    def from_dict(group_data: dict) -> SpondGroup:
        """
        Create a full-feature SpondGroup object from dict representation.
        """
        spondgroup = SpondGroup.core_from_dict(group_data)

        # create child SpondMembers
        spondgroup.members = [
            SpondMember.from_dict(member) for member in group_data.get("members", [])
        ]
        # create child SpondSubGroups
        spondgroup.subgroups = [
            SpondSubgroup.from_dict(subgroup)
            for subgroup in group_data.get("subGroups", [])
        ]
        for member in group_data.get("members", []):
            member_id = member.get("id")
            for subgroup_id in member.get("subGroups", []):
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
        """
        Return the child subgroup with matching id, or an error
        """
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        raise IndexError

    def member_by_id(self, member_uid: str) -> SpondMember:
        """
        Return the child member with matching id, or an error
        """
        for member in self.members:
            if member.uid == member_uid:
                return member
        raise IndexError


@dataclass()
class SpondSubgroup:
    """
    Spond subgroup.

    Belongs to one SpondGroup.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    parent_group: None | SpondGroup = field(init=False)  # derived
    members: list[SpondMember] = field(default_factory=list)  # derived

    def __post_init__(self) -> None:
        self.parent_group = None

    def __str__(self) -> str:
        return f"[SpondSubgroup '{self.name}']"

    @staticmethod
    def from_dict(subgroup: dict) -> SpondSubgroup:
        """
        Create a SpondSubgroup object from relevant dict.
        """
        assert isinstance(subgroup, dict)
        uid = subgroup["id"]
        name = subgroup["name"]
        return SpondSubgroup(uid, name)


@dataclass
class SpondEvent:
    """
    Spond event.
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
        """
        Alias `heading` for convenience/consistency with other objects
        """
        return self.heading

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(event: dict) -> SpondEvent:
        """
        Create a SpondEvent object from relevant dict.
        """
        assert isinstance(event, dict)
        uid = event["id"]
        heading = event["heading"]
        start_time = parser.isoparse(event["startTimestamp"])
        assert isinstance(event["responses"], dict)
        accepted_uids = event["responses"].get("acceptedIds", [])
        declined_uids = event["responses"].get("declinedIds", [])
        unanswered_uids = event["responses"].get("unansweredIds", [])
        waiting_list_uids = event["responses"].get("waitinglistIds", [])
        unconfirmed_uids = event["responses"].get("unconfirmedIds", [])

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
        return f"<SpondEvent '{self.heading}' on {self.start_time.date()}>"
