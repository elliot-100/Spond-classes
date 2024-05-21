"""Module containing `Group` class and related `FieldDef` class."""

import sys

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self

from typing import Sequence

from pydantic import BaseModel, Field

from .member import Member
from .role import Role
from .subgroup import Subgroup
from .typing import DictFromJSON


class FieldDef(BaseModel):
    """Custom field definition."""

    uid: str = Field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    name: str


class Group(BaseModel):
    """Represents a group in the Spond system.

    A `Group` has:
    - zero, one or more `Member`s
    - zero, one or more `Role`s
    - zero, one or more `Subgroup`s
    """

    uid: str = Field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    name: str
    """Same name in Spond API."""

    # Mutables which always exist in Spond API data, but may be empty
    members: list[Member]
    """`Member`s belonging to the `Group`.
    Derived from `members` in Spond API.
    May be empty."""
    roles: list[Role]
    """`Role`s belonging to the `Group`.
    Derived from `roles` in Spond API.
    May be empty."""
    subgroups: list[Subgroup] = Field(alias="subGroups")
    """`Subgroup`s belonging to the `Group`.
    Derived from `subGroups` in Spond API.
    May be empty."""
    field_defs: list[FieldDef] = Field(alias="fieldDefs")
    """Custom field definitions.
    Derived from `fieldDefs` in Spond API.
    May be empty."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return f"Group(uid='{self.uid}', name='{self.name}', …)"

    @classmethod
    def from_dict(cls, dict_: DictFromJSON) -> Self:
        """Construct a `Group`.

        Parameters
        ----------
        dict_
            as returned by `spond.spond.Spond.get_group()`
            or from the list returned by `spond.spond.Spond.get_groups()`.

        Returns
        -------
        `Group`

        Raises
        ------
        `TypeError`
            if `dict_` is not a dictionary.
        """
        if not isinstance(dict_, dict):
            err_msg = f"Expected `dict`, got `{dict_.__class__.__name__}`: '{dict}'"
            raise TypeError(err_msg)

        return cls(**dict_)

    def member_by_uid(self, uid: str) -> Member:
        """Return the `Member` with matching `uid`.

        Parameters
        ----------
        uid

        Returns
        -------
        `Member`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(self.members, member_uid)

    def role_by_uid(self, uid: str) -> Role:
        """Return the `Role` with matching `uid`.

        Parameters
        ----------
        uid

        Returns
        -------
        `Role`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(self.roles, role_uid)

    def subgroup_by_uid(self, uid: str) -> Subgroup:
        """Return the `Subgroup` with matching `uid`.

        Parameters
        ----------
        uid

        Returns
        -------
        `Subgroup`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(self.subgroups, subgroup_uid)

    def _instance_by_id(
        self, instances: Sequence[Member | Subgroup | Role], uid: str
    ) -> Member | Subgroup | Role:
        """Return the nested instance with matching `uid`.

        Parameters
        ----------
        uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        for item in instances:
            if item.uid == uid:
                return item
        err_msg = f"No instance found with id='{uid}'."
        raise LookupError(err_msg)

    def members_by_subgroup(self, subgroup: Subgroup) -> list[Member]:
        """Return `Member`s in the `Subgroup`.

        Parameters
        ----------
        subgroup
            `Subgroup` from which to return `Member`s.

        Returns
        -------
        list[`Member`]

        Raises
        ------
        TypeError
            If `subgroup` is not a `Subgroup` instance.
        """
        if not isinstance(subgroup, Subgroup):
            err_msg = "`subgroup` must be a Subgroup."
            raise TypeError(err_msg)
        return [
            member for member in self.members if subgroup.uid in member.subgroup_uids
        ]

    def members_by_role(self, role: Role) -> list[Member]:
        """Return `Member`s with the `Role`.

        Parameters
        ----------
        role
            `Role` from which to return `Member`s.

        Returns
        -------
        list[`Member`]

        Raises
        ------
        TypeError
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
