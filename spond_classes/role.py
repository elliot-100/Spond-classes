"""Module containing `Role` class."""

from typing import Self

from attrs import define, field
from cattrs import Converter
from cattrs.gen import make_dict_structure_fn

from .types_ import DictFromJSON


@define
class Role:
    """Represents a role in the Spond system.

    A `Role` belongs to a `Group`.

    Use `Group.members_by_role()` to get subordinate `Member`s.
    """

    uid: str = field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    name: str

    @classmethod
    def from_dict(cls, dict_: DictFromJSON) -> Self:
        c = Converter()
        hook = make_dict_structure_fn(cls, c, _cattrs_use_alias=True)
        c.register_structure_hook(cls, hook)
        return c.structure(dict_, cls)

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"Role(uid='{self.uid}', name='{self.name}')"
