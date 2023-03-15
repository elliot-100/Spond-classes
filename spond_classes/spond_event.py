"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dateutil import parser

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class SpondEvent:
    """SpondEvent.

    Belongs to one SpondGroup.
    """

    uid: str  # from API 'id'
    heading: str  # from API 'heading'
    start_time: datetime  # from API 'startTimestamp'

    accepted_uids: list = field(default_factory=list, repr=False)
    declined_uids: list = field(default_factory=list, repr=False)
    unanswered_uids: list = field(default_factory=list, repr=False)
    waiting_list_uids: list = field(default_factory=list, repr=False)
    unconfirmed_uids: list = field(default_factory=list, repr=False)
    name: str = field(
        init=False, repr=False
    )  # derived; aliases `heading` for consistency
    # with other objects
    _name: str = field(init=False, repr=False)

    @property  # type: ignore[no-redef]
    def name(self: SpondEvent) -> str:
        """Alias `heading` for convenience/consistency with other objects."""
        return self.heading

    @name.setter
    def name(self: SpondEvent, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(event_data: dict) -> SpondEvent:
        """Create a SpondEvent object from relevant dict."""
        if not isinstance(event_data, dict):
            raise TypeError
        uid = event_data["id"]
        heading = event_data["heading"]
        start_time = parser.isoparse(event_data["startTimestamp"])
        if not isinstance(event_data["responses"], dict):
            raise TypeError
        accepted_uids = event_data["responses"].get("acceptedIds", [])
        declined_uids = event_data["responses"].get("declinedIds", [])
        unanswered_uids = event_data["responses"].get("unansweredIds", [])
        waiting_list_uids = event_data["responses"].get("waitinglistIds", [])
        unconfirmed_uids = event_data["responses"].get("unconfirmedIds", [])

        return SpondEvent(
            uid,
            heading,
            start_time,
            accepted_uids,
            declined_uids,
            unanswered_uids,
            waiting_list_uids,
            unconfirmed_uids,
        )

    def __str__(self: SpondEvent) -> str:
        """Return simple human-readable description.

        Date is included because heading is unliklely to be unique.
        """
        return f"SpondEvent '{self.heading}' on {self.start_time.date()}"
