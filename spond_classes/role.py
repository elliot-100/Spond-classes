"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

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

    @staticmethod
    def from_dict(role: dict) -> Role:
        """Create a Role object from relevant dict."""
        if not isinstance(role, dict):
            raise TypeError
        uid = role["id"]
        name = role["name"]

        return Role(
            uid,
            name,
        )

    def __str__(self: Role) -> str:
        """Return simple human-readable description."""
        return f"Role '{self.name}'"
