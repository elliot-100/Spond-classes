"""Module containing `Group` class."""

from collections.abc import Sequence
from typing import TypeGuard, TypeVar

from pydantic import BaseModel, Field

from .member import Member
from .role import Role
from .subgroup import Subgroup

T = TypeVar("T")


def is_sequence_member_role_subgroup(
    val: Sequence[object],
) -> TypeGuard[Sequence[Member | Role | Subgroup]]:
    """Determine whether all in the list are ..."""
    return (
        all(isinstance(x, Member) for x in val)
        or all(isinstance(x, Role) for x in val)
        or all(isinstance(x, Subgroup) for x in val)
    )


class Group(BaseModel):
    """Represents a group in the Spond system.

    Groups data is retrieved from the `groups` API endpoint.

    A `Group` has zero, one or more nested `Member`s; zero, one or more nested `Role`s;
    zero, one or more nested `Subgroup`s.
    """

    uid: str = Field(alias="id")
    """`id` in API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    name: str

    # Lists which always exist in API data, but may be empty
    members: list[Member]
    """`Member`s belonging to the `Group`. Derived from `members` in API."""
    roles: list[Role]
    """`Role`s belonging to the `Group`. Derived from `roles` in API."""
    subgroups: list[Subgroup] = Field(alias="subGroups")
    """`Subgroup`s belonging to the `Group`. Derived from `subGroups` in API."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return f"Group(uid='{self.uid}', name='{self.name}', …)"

    def member_by_id(self, member_uid: str) -> Member:
        """Return the nested `Member` with matching ID.

        Parameters
        ----------
        member_uid
            ID to look up.

        Returns
        -------
        `Member`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(member_uid, Member, self.members)

    def role_by_id(self, role_uid: str) -> Role:
        """Return the nested `Role` with matching ID.

        Parameters
        ----------
        role_uid
            ID to look up.

        Returns
        -------
        `Role`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(role_uid, Role, self.roles)

    def subgroup_by_id(self, subgroup_uid: str) -> Subgroup:
        """Return the nested `Subgroup` with matching ID.

        Parameters
        ----------
        subgroup_uid
            ID to look up.

        Returns
        -------
        `Subgroup`

        Raises
        ------
        LookupError
            If `uid` is not found.
        """
        return self._instance_by_id(subgroup_uid, Subgroup, self.subgroups)

    def _instance_by_id(
        self,
        uid: str,
        cls: T,
        instances: list[T],
    ) -> T:
        """Return the nested instance with matching `uid`.

        Parameters
        ----------
        uid
            ID to look up.

        Raises
        ------
        LookupError if uid is not found.
        """
        if not isinstance(cls, Member | Role | Subgroup):
            raise TypeError
        if not is_sequence_member_role_subgroup(instances):
            raise TypeError
        for instance in instances:
            if instance.uid == uid:
                return instance
        err_msg = f"No {cls} found with id='{uid}'."
        raise LookupError(err_msg)

    def members_by_subgroup(self, subgroup: Subgroup) -> list[Member]:
        """Return `Member`s in the nested `Subgroup`.

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
        """Return `Member`s with the nested `Role`.

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
