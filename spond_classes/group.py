"""Module containing `Group` class."""

from typing import TypeVar

from pydantic import BaseModel, Field

from .member import Member
from .role import Role
from .subgroup import Subgroup

T = TypeVar("T", Member, Role, Subgroup)


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
            If ID is not found.
        """
        result = self._nested_instance_by_id(Member, member_uid)
        if not isinstance(result, Member):
            raise TypeError
        return result

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
            If ID is not found.
        """
        result = self._nested_instance_by_id(Role, role_uid)
        if not isinstance(result, Role):
            raise TypeError
        return result

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
            If ID is not found.
        """
        result = self._nested_instance_by_id(Subgroup, subgroup_uid)
        if not isinstance(result, Subgroup):
            raise TypeError
        return result

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

    def _nested_instance_by_id(
        self,
        nested_class: T,
        uid: str,
    ) -> Member | Role | Subgroup:
        """Return the nested instance with matching ID."""
        if isinstance(nested_class, Member):
            gen = (m for m in self.members if m.uid == uid)
        elif isinstance(nested_class, Role):
            gen = (r for r in self.roles if r.uid == uid)
        elif isinstance(nested_class, Subgroup):
            gen = (s for s in self.subgroups if s.uid == uid)
        else:
            raise TypeError
        result = next(gen, None)
        if result:
            return result
        err_msg = f"No `{nested_class.__qualname__}` found with id='{uid}'."
        raise LookupError(err_msg)
