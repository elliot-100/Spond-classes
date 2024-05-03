"""Role class."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from typing_extensions import Self

if TYPE_CHECKING:
    from .member import Member


@dataclass
class Role:
    """Represents a role in the Spond system.

    A Role belongs to one Group.
    A Member has zero, one or more Roles.

    Attributes
    ----------
    uid : str
        id of the Role.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    name : str
        Name of the Role.
        'name' in API.
    members : list[Member]
        Members with the Role.
    """

    # Required params, populated by implicit Role.__init__().
    uid: str
    name: str

    # Populated by `Group.from_dict()`, as they rely on full Group data:
    members: list[Member] = field(default_factory=list, repr=False)

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Role '{self.name}'"

    @classmethod
    def from_dict(cls, role_data: dict) -> Self:
        """Create a Role object from relevant dict.

        Parameters
        ----------
        role_data
            Dict representing the role.
        """
        if not isinstance(role_data, dict):
            raise TypeError
        uid = role_data["id"]
        name = role_data["name"]

        return cls(
            uid,
            name,
        )
