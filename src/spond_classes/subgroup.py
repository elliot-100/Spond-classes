"""Module containing `Subgroup` class."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Subgroup(BaseModel):
    """Represents a subgroup in the Spond system.

    A `Subgroup` belongs to a `Group`.

    Use `Group.members_by_subgroup()` to get subordinate `Member`s.
    """

    uid: str = Field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    name: str
    """Same name in Spond API."""

    def __str__(self) -> str:
        """Return simple human-readable description."""
        return f"{self.__class__.__name__}(uid='{self.uid}', name='{self.name}')"
