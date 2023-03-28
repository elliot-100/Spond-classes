"""Subgroup class."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .member import Member


@dataclass
class Subgroup:
    """Subgroup.

    Belongs to one Group.
    May contain zero, one or more SpondMembers.

    Attributes
    ----------
    uid : str
        id of the Subgroup.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    name : str
        Name of the Subgroup.
        'name' in API.
    members : list[Member]
        Members of the Subgroup.
    """

    # Required params, populated by implicit Subgroup.__init__().
    uid: str
    name: str

    # Populated by `Group.from_dict()`, as they rely on full Group data:
    members: list[Member] = field(default_factory=list, repr=False)

    def __str__(self: Subgroup) -> str:
        """Return simple human-readable description."""
        return f"Subgroup '{self.name}'"

    @staticmethod
    def from_dict(subgroup_data: dict) -> Subgroup:
        """Create a Subgroup object from relevant dict.

        Parameters
        ----------
        subgroup_data
            Dict representing the subgroup.
        """
        if not isinstance(subgroup_data, dict):
            raise TypeError
        uid = subgroup_data["id"]
        name = subgroup_data["name"]
        return Subgroup(uid, name)
