"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

from dateutil import parser


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
        assert isinstance(member_data, dict)
        uid = member_data["id"]
        created_time = parser.isoparse(member_data["createdTime"])
        first_name = member_data["firstName"]
        last_name = member_data["lastName"]
        return SpondMember(uid, created_time, first_name, last_name)


@dataclass
class SpondGroup:
    """SpondGroup.

    May contain zero, one or more SpondMembers.
    May contain zero, one or more SpondSubgroups.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[SpondMember] = field(default_factory=list, repr=False)
    # derived from API 'members', but uses object refs instead of uid.
    subgroups: list[SpondSubgroup] = field(default_factory=list, repr=False)
    # derived from API 'subgroups'
    roles: list[SpondRole] = field(default_factory=list, repr=False)
    # derived from API 'roles'

    def __str__(self: SpondGroup) -> str:
        """Return simple human-readable description."""
        return f"SpondGroup '{self.name}'"

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
        group = SpondGroup.core_from_dict(group_data)

        # create child SpondMembers
        group.members = [
            SpondMember.from_dict(member_data)
            for member_data in group_data.get("members", [])
        ]
        # create child SpondSubgroups
        group.subgroups = [
            SpondSubgroup.from_dict(subgroup_data)
            for subgroup_data in group_data.get("subGroups", [])
        ]
        # create child SpondRoles
        group.roles = [
            SpondRole.from_dict(role) for role in group_data.get("roles", [])
        ]

        for member_data in group_data.get("members", []):
            member_data_id = member_data.get("id")

            for subgroup_data_id in member_data.get("subGroups", []):
                # populate child SpondMembers' subgroup attributes
                group.member_by_id(member_data_id).subgroups.append(
                    group.subgroup_by_id(subgroup_data_id),
                )
                # populate child SpondSubgroups' members attribute
                group.subgroup_by_id(subgroup_data_id).members.append(
                    group.member_by_id(member_data_id),
                )

            for role_data_id in member_data.get("roles", []):
                # populate child SpondMembers' roles attribute
                group.member_by_id(member_data_id).roles.append(
                    group.role_by_id(role_data_id),
                )

                # populate child SpondRoles' members attribute
                group.role_by_id(role_data_id).members.append(
                    group.member_by_id(member_data_id),
                )

        return group

    def subgroup_by_id(self: SpondGroup, subgroup_uid: str) -> SpondSubgroup:
        """Return the child SpondSubgroup with matching id, or an error."""
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        raise IndexError

    def member_by_id(self: SpondGroup, member_uid: str) -> SpondMember:
        """Return the child SpondMember with matching id, or an error."""
        for member in self.members:
            if member.uid == member_uid:
                return member
        raise IndexError

    def role_by_id(self: SpondGroup, role_uid: str) -> SpondRole:
        """Return the child SpondRole with matching id, or an error."""
        for role in self.roles:
            if role.uid == role_uid:
                return role
        raise IndexError


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
        assert isinstance(subgroup_data, dict)
        uid = subgroup_data["id"]
        name = subgroup_data["name"]
        return SpondSubgroup(uid, name)


@dataclass
class SpondEvent:
    """SpondEvent.

    Belongs to one SpondGroup.
    """

    uid: str  # from API 'id'
    heading: str  # from API 'heading'
    start_time: datetime  # from API 'startTimestamp'

    accepted_uids: list = field(default_factory=list, repr=False)
    declined_uids: list = field(default_factory=list, repr=False)
    unanswered_uids: list = field(default_factory=list, repr=False)
    waiting_list_uids: list = field(default_factory=list, repr=False)
    unconfirmed_uids: list = field(default_factory=list, repr=False)
    name: str = field(
        init=False, repr=False
    )  # derived; aliases `heading` for consistency
    # with other objects
    _name: str = field(init=False, repr=False)

    @property  # type: ignore[no-redef]
    def name(self: SpondEvent) -> str:
        """Alias `heading` for convenience/consistency with other objects."""
        return self.heading

    @name.setter
    def name(self: SpondEvent, name: str) -> None:
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

    def __str__(self: SpondEvent) -> str:
        """Return simple human-readable description.

        Date is included because heading is unliklely to be unique.
        """
        return f"SpondEvent '{self.heading}' on {self.start_time.date()}"


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
        assert isinstance(role, dict)
        uid = role["id"]
        name = role["name"]

        return SpondRole(
            uid,
            name,
        )

    def __str__(self: SpondRole) -> str:
        """Return simple human-readable description."""
        return f"SpondRole '{self.name}'"
