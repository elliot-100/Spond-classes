"""Module containing `Profile` class."""

from __future__ import annotations

import sys

if sys.version_info < (3, 11):
    from typing_extensions import Self

else:
    from typing import Self

from typing import TYPE_CHECKING

from pydantic import BaseModel, EmailStr, Field

from spond_classes.typing import _ensure_dict

if TYPE_CHECKING:
    from .typing import DictFromJSON


class Profile(BaseModel):
    """Represents a profile in the Spond system.

    A `Profile` is an individual's account-specific record.

    A `Profile` belongs to a `Member`.
    """

    uid: str = Field(alias="id")
    """`id` in Spond API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    first_name: str = Field(alias="firstName")
    """`firstName` in Spond API."""
    last_name: str = Field(alias="lastName")
    """`lastName` in Spond API."""

    # Optional in Spond API data
    email: EmailStr | None = Field(default=None)
    """Same name in Spond API. Not always present."""
    phone_number: str | None = Field(alias="phoneNumber", default=None)
    """`phoneNumber` in Spond API.
    Not always present."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return (
            f"{self.__class__.__name__}(uid='{self.uid}', "
            f"full_name='{self.full_name}', …)"
        )

    @property
    def full_name(self) -> str:
        """Return the `Profile`'s full name, for convenience."""
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, dict_: DictFromJSON) -> Self:
        """Construct a `Profile`.

        Parameters
        ----------
        dict_
            as returned by `spond.spond.Spond.get_profile()`.

        Returns
        -------
        `Group`

        Raises
        ------
        `TypeError`
            if `dict_` is not a `dict`.
        """
        _ensure_dict(dict_)
        return cls(**dict_)
