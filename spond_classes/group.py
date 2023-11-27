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
            member = group.get_child_by_id(member_data_id, Member)

            for subgroup_data_id in member_data.get("subGroups", []):
                subgroup = group.get_child_by_id(subgroup_data_id, Subgroup)
                # populate group.members.member.subgroups.subgroup
                member.subgroups.append(subgroup)
                # populate group.subgroups.subgroup.members.member
                subgroup.members.append(member)

            for role_data_id in member_data.get("roles", []):
                role = group.get_child_by_id(role_data_id, Role)
                # populate group.members.member.roles.role
                member.roles.append(role)
                # populate group.roles.role.members.member
                role.members.append(member)

        return group

    def get_child_by_id(
        self,
        child_uid: str,
        child_type: type,
    ) -> Member | Subgroup | Role:
        """Return the child object with matching id, or an error.

        Parameters
        ----------
        child_uid
            ID of the child object.
        child_type
            Type of the child object (Member, Subgroup, or Role).
        """
        child_attr_map = {
            Member: self.members,
            Subgroup: self.subgroups,
            Role: self.roles,
        }
        if child_type not in child_attr_map.keys():
            error_message = f"Unknown child type: {child_type}"
            raise ValueError(error_message)
        child_list = child_attr_map.get(child_type)
        for child in child_list:
            if child.uid == child_uid:
                return child
        error_message = f"Child {child_type} with ID {child_uid} not found."
        raise IndexError(error_message)

    def subgroup_by_id(self, uid: str) -> Subgroup:
        """Return the child Subgroup with matching id, or an error.

        For convenience/backward compatibility, may be removed.

        Parameters
        ----------
        uid
            ID of the subgroup.
        """
        return self.get_child_by_id(uid, Subgroup)

    def member_by_id(self, uid: str) -> Member:
        """Return the child Member with matching id, or an error.

        For convenience/backward compatibility, may be removed.

        Parameters
        ----------
        uid
            ID of the member.
        """
        return self.get_child_by_id(uid, Member)

    def role_by_id(self, uid: str) -> Role:
        """Return the child Role with matching id, or an error.

        For convenience/backward compatibility, may be removed.

        Parameters
        ----------
        uid
            ID of the role.
        """
        return self.get_child_by_id(uid, Role)

    @staticmethod
    def _create_children(
        group_data: dict,
        key: str,
        child_cls: type[Member | Role | Subgroup],
    ) -> list:
        """Create child objects."""
        return [child_cls.from_dict(item) for item in group_data.get(key, [])]
