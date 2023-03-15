"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field

from .spond_member import SpondMember
from .spond_role import SpondRole
from .spond_subgroup import SpondSubgroup


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
        if not isinstance(group_data, dict):
            raise TypeError
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
