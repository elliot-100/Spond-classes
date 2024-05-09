"""Group class."""

from pydantic import BaseModel, Field

from .member import Member
from .role import Role
from .subgroup import Subgroup


class Group(BaseModel):
    """Represents a group in the Spond system.

    A Group has zero, one or more Members.

    Attributes
    ----------
    uid : str
        id of the Group.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    members : list[Member]
        Members belonging to the Group.
        'members' in API.
    name : str
        Name of the Group.
        'name' in API.
    roles : list[Role]
        Roles belonging to the Group.
        'roles' in API.
    subgroups : list[Subgroup]
        The Subgroups belonging to the Group.
        'subgroups' in API.
    """

    uid: str = Field(alias="id")
    name: str

    # Lists which always exist in API data, but may be empty
    members: list[Member]
    roles: list[Role]
    subgroups: list[Subgroup] = Field(alias="subGroups")

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Group '{self.name}'"

    def member_by_id(self, member_uid: str) -> Member:
        """Return the nested Member with matching uid.

        Parameters
        ----------
        member_uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        for member in self.members:
            if member.uid == member_uid:
                return member
        err_msg = f"No Member found with id='{member_uid}'."
        raise LookupError(err_msg)

    def role_by_id(self, role_uid: str) -> Role:
        """Return the nested Role with matching uid.

        Parameters
        ----------
        role_uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        for role in self.roles:
            if role.uid == role_uid:
                return role
        err_msg = f"No Role found with id='{role_uid}'."
        raise LookupError(err_msg)

    def subgroup_by_id(self, subgroup_uid: str) -> Subgroup:
        """Return the nested Subgroup with matching uid.

        Parameters
        ----------
        subgroup_uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        err_msg = f"No Subgroup found with id='{subgroup_uid}'."
        raise LookupError(err_msg)

    def members_by_subgroup(self, subgroup: Subgroup) -> list[Member]:
        """Return members in the nested Subgroup.

        Parameters
        ----------
        subgroup
            Subgroup from which to return Members.
        """
        return [
            member for member in self.members if subgroup.uid in member.subgroup_uids
        ]

    def members_by_role(self, role: Role) -> list[Member]:
        """Return members in the nested Role.

        Parameters
        ----------
        role
            Role from which to return Members.
        """
        return [
            member
            for member in self.members
            if member.role_uids and role.uid in member.role_uids
        ]
