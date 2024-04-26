"""Group class."""

from __future__ import annotations

from dataclasses import dataclass, field

from .member import Member
from .role import Role
from .subgroup import Subgroup


@dataclass
class Group:
    """Represents a group in the Spond system.

    An individual may have access to multiple Groups, but they are independent: Members,
    Events and Roles are not shared across Groups.

    A Group has zero, one or more Members.
    A Group has zero, one or more Subgroups.
    NB: relationship to Event isn't yet implemented.

    Attributes
    ----------
    uid : str
        id of the Group.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    members : list[Member]
        Members belonging to the Group.
        Derived from 'members' in API, but returns Member instances instead of dicts.
    name : str
        Name of the Group.
        'name' in API.
    roles : list[Role]
        Roles belonging to the Group.
        Derived from 'roles' in API, but returns Role instances instead of dicts.
    subgroups : list[Subgroup]
        The Subgroups belonging to the Group.
        Derived from 'subgroups' in API, but returns Subgroup instances instead
        of dicts.
    """

    # Required params, populated by implicit Group.__init__().
    uid: str
    name: str

    # Populated by `Group.from_dict()`, as they rely on full Group data:
    members: list[Member] = field(default_factory=list, repr=False)
    roles: list[Role] = field(default_factory=list, repr=False)
    subgroups: list[Subgroup] = field(default_factory=list, repr=False)

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Group '{self.name}'"

    @classmethod
    def core_from_dict(cls, group_data: dict) -> Group:
        """Create a minimal Group object (required attributes only) from relevant dict.

        Parameters
        ----------
        group_data
            Dict representing the group, as returned by `spond.get_group()`.
        """
        if not isinstance(group_data, dict):
            raise TypeError
        uid = group_data["id"]
        name = group_data["name"]
        return cls(uid, name)

    @classmethod
    def from_dict(cls, group_data: dict) -> Group:
        """Create a full-featured Group object and child objects from relevant dict.

        Parameters
        ----------
        group_data
            Dict representing the group, as returned by `spond.get_group()`.
        """
        group = cls.core_from_dict(group_data)

        group.members = Group._create_children(group_data, "members", Member)
        group.subgroups = Group._create_children(group_data, "subGroups", Subgroup)
        group.roles = Group._create_children(group_data, "roles", Role)

        for member_data in group_data.get("members", []):
            member_data_id = member_data.get("id")
            member = group.member_by_id(member_data_id)

            for subgroup_data_id in member_data.get("subGroups", []):
                subgroup = group.subgroup_by_id(subgroup_data_id)
                # populate group.members.member.subgroups.subgroup
                member.subgroups.append(subgroup)
                # populate group.subgroups.subgroup.members.member
                subgroup.members.append(member)

            for role_data_id in member_data.get("roles", []):
                role = group.role_by_id(role_data_id)
                # populate group.members.member.roles.role
                member.roles.append(role)
                # populate group.roles.role.members.member
                role.members.append(member)

        return group

    def subgroup_by_id(self, subgroup_uid: str) -> Subgroup:
        """Return the child Subgroup with matching id, or an error.

        Parameters
        ----------
        subgroup_uid
            ID of the subgroup.
        """
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        raise IndexError

    def member_by_id(self, member_uid: str) -> Member:
        """Return the child Member with matching id, or an error.

        Parameters
        ----------
        member_uid
            ID of the member.
        """
        for member in self.members:
            if member.uid == member_uid:
                return member
        raise IndexError

    def role_by_id(self, role_uid: str) -> Role:
        """Return the child Role with matching id, or an error.

        Parameters
        ----------
        role_uid
            ID of the role.
        """
        for role in self.roles:
            if role.uid == role_uid:
                return role
        raise IndexError

    @staticmethod
    def _create_children(
        group_data: dict,
        key: str,
        child_cls: type[Member | Role | Subgroup],
    ) -> list:
        """Create child objects."""
        return [child_cls.from_dict(item) for item in group_data.get(key, [])]
