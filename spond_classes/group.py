"""Module for `Group` class."""

from pydantic import BaseModel, Field

from .member import Member
from .role import Role
from .subgroup import Subgroup


class Group(BaseModel):
    """Represents a group in the Spond system.

    `Group`s are retrieved from the `groups` API endpoint.

    A Group has zero, one or more nested Members.
    A Group has zero, one or more nested Roles.
    A Group has zero, one or more nested Subgroups.
    A `Group` has zero, one or more nested `spond_classes.member.Member`s;

    Attributes
    ----------
    uid : str
        id of the `Group`.

        `id` in API, but that's a reserved term and the `spond` package uses `uid`.

    members : list[Member]
        Members belonging to the Group.
        'members' in API.

        `members` in API.

    name : str
        Name of the `Group`.

        `name` in API.

    roles : list[Role]
        Roles belonging to the Group.
        'roles' in API.

        Derived from `roles` in API.

    subgroups : list[Subgroup]
        The Subgroups belonging to the Group.
        'subgroups' in API.

        Derived from `subGroups` in API.
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
        """Return the nested `Member` with matching ID.

        Parameters
        ----------
        member_uid : str
            ID to look up.

        Returns
        -------
        `Member`

        Raises
        ------
        `LookupError`
            If `uid` is not found.
        """
        for member in self.members:
            if member.uid == member_uid:
                return member
        err_msg = f"No Member found with id='{member_uid}'."
        raise LookupError(err_msg)

    def role_by_id(self, role_uid: str) -> Role:
        """Return the nested `Role` with matching ID.

        Parameters
        ----------
        role_uid : str
            ID to look up.

        Returns
        -------
        `Role`

        Raises
        ------
        `LookupError`
            If `uid` is not found.
        """
        for role in self.roles:
            if role.uid == role_uid:
                return role
        err_msg = f"No Role found with id='{role_uid}'."
        raise LookupError(err_msg)

    def subgroup_by_id(self, subgroup_uid: str) -> Subgroup:
        """Return the nested `Subgroup` with matching ID.

        Parameters
        ----------
        subgroup_uid : str
            ID to look up.

        Returns
        -------
        `Subgroup`

        Raises
        ------
        `LookupError`
            If `uid` is not found.
        """
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        err_msg = f"No Subgroup found with id='{subgroup_uid}'."
        raise LookupError(err_msg)

    def members_by_subgroup(self, subgroup: Subgroup) -> list[Member]:
        """Return `Member`s in the nested `Subgroup`.

        Parameters
        ----------
        subgroup
            Subgroup from which to return Members.

        Returns
        -------
        `list[Member]`

        Raises
        ------
        `TypeError`
            If `subgroup` is not a `Subgroup` instance.
        """
        if not isinstance(subgroup, Subgroup):
            err_msg = "`subgroup` must be a Subgroup."
            raise TypeError(err_msg)
        return [
            member for member in self.members if subgroup.uid in member.subgroup_uids
        ]

    def members_by_role(self, role: Role) -> list[Member]:
        """Return `Member`s with the nested
        `spond_classes.role.Role`.

        Parameters
        ----------
        role
            Role from which to return Members.
             `spond_classes.member.Member`s.

        Returns
        -------
         `list[Member]`

        Raises
        ------
        `TypeError`
            If `role` is not a `Role` instance.
        """
        if not isinstance(role, Role):
            err_msg = "`role` must be a Role."
            raise TypeError(err_msg)
        return [
            member
            for member in self.members
            if member.role_uids and role.uid in member.role_uids
        ]
