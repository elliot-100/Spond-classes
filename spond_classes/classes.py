"""
Custom classes for Spond data, and methods to create them from dicts returned by
`spond` package.

"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Dict, List

from dateutil import parser


class DuplicateKeyError(ValueError):
    """ """


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
    name: str = field(init=False)  # derived
    roles: List[str] = field(default_factory=list)  # from API 'roles'

    instances: ClassVar[Dict[str, SpondMember]] = {}

    def __post_init__(self):
        self.name = f"{self.first_name} {self.last_name}"
        if self.uid not in self.__class__.instances:
            self.__class__.instances[self.uid] = self
        else:
            raise DuplicateKeyError(
                f"{self.__class__} instance with uid='{self.uid}' already exists."
            )

    def __str__(self):
        return f"[SpondMember '{self.first_name} {self.last_name} {self.uid}']"

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
    members: List[SpondMember] = field(default_factory=list)
    # derived from API 'members', but uses object refs instead of uid.
    subgroups: List[SpondSubgroup] = field(default_factory=list)
    # not yet implemented

    instances: ClassVar[Dict[str, SpondGroup]] = {}

    def __post_init__(self):
        if self.uid not in self.__class__.instances:
            self.__class__.instances[self.uid] = self
        else:
            raise DuplicateKeyError(
                f"{self.__class__} instance with uid='{self.uid}' already exists."
            )

    def __str__(self):
        return f"[SpondGroup '{self.name}']"

    @staticmethod
    def from_dict(group: dict) -> SpondGroup:
        """
        Create a SpondGroup object from relevant dict.
        """
        assert isinstance(group, dict)
        uid = group["id"]
        name = group["name"]
        members = [SpondMember.from_dict(member) for member in group.get("members", [])]
        return SpondGroup(uid, name, members)

    @classmethod
    def by_id(cls, group_uid: str) -> SpondGroup:
        """
        Return the SpondGroup matching the uid, or an error.

        Parameters
        ----------
        group_uid : str

        Returns
        -------
        SpondGroup

        """
        return SpondGroup.instances[group_uid]


@dataclass()
class SpondSubgroup:
    """
    Spond subgroup.

    Belongs to one SpondGroup.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    parent_group: SpondGroup  # derived
    members: List[SpondMember] = field(default_factory=list)  # derived

    instances: ClassVar[Dict[str, SpondSubgroup]] = {}

    def __post_init__(self):
        if self.uid not in self.__class__.instances:
            self.__class__.instances[self.uid] = self
        else:
            raise DuplicateKeyError(
                f"{self.__class__} instance with uid='{self.uid}' already exists."
            )

    @staticmethod
    def from_dict(subgroup: dict, parent_group: SpondGroup) -> SpondSubgroup:
        """
        Create a SpondSubgroup object from relevant dict.
        """
        assert isinstance(subgroup, dict)
        uid = subgroup["id"]
        name = subgroup["name"]
        members = [
            SpondMember.from_dict(member) for member in subgroup.get("members", [])
        ]
        return SpondSubgroup(uid, name, parent_group, members)

    def __str__(self):
        return f"[SpondSubgroup '{self.name}']"

    @classmethod
    def by_id(cls, subgroup_uid: str) -> SpondSubgroup:
        """
        Return the SpondSubgroup matching the uid, or an error.

        Parameters
        ----------
        subgroup_uid : str

        Returns
        -------
        SpondSubgroup

        """
        return SpondSubgroup.instances[subgroup_uid]


@dataclass
class SpondEvent:
    """
    Spond event.
    """

    uid: str  # from API 'id'
    heading: str  # from API 'heading'
    name: str = field(init=False)  # derived; aliases `heading` for consistency
    # with other objects
    start_time: datetime  # from API 'startTimestamp'

    accepted_uids: list = field(default_factory=list)
    declined_uids: list = field(default_factory=list)
    unanswered_uids: list = field(default_factory=list)
    waiting_list_uids: list = field(default_factory=list)
    unconfirmed_uids: list = field(default_factory=list)

    instances: ClassVar[Dict[str, SpondEvent]] = {}

    def __post_init__(self):
        if self.uid not in self.__class__.instances:
            self.__class__.instances[self.uid] = self
        else:
            raise DuplicateKeyError(
                f"{self.__class__} instance with uid='{self.uid}' already exists."
            )

        self.name = self.heading

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
