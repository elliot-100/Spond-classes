"""Module containing `Profile` class."""

from pydantic import BaseModel, EmailStr, Field


class Profile(BaseModel):
    """Represents a profile in the Spond system.

    A `Profile` is an individual's account-specific record.

    A `Profile` belongs to a `Member`.
    """

    uid: str = Field(alias="id")
    """`id` in API; aliased as that's a Python built-in, and the Spond package
    uses `uid`."""
    first_name: str = Field(alias="firstName")
    """`firstName` in API."""
    last_name: str = Field(alias="lastName")
    """`lastName` in API."""

    # Optional in API data
    email: EmailStr | None = Field(default=None)
    phone_number: str | None = Field(alias="phoneNumber", default=None)
    """`phoneNumber` in API."""

    def __str__(self) -> str:
        """Return simple human-readable description.

        Includes only key fields in custom order.
        """
        return f"Profile(uid='{self.uid}', full_name='{self.full_name}', …)"

    @property
    def full_name(self) -> str:
        """Return the `Profile`'s full name, for convenience."""
        return f"{self.first_name} {self.last_name}"
