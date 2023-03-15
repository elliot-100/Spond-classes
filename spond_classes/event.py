"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dateutil import parser

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class Event:
    """Event.

    Belongs to one Group.
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
    def name(self: Event) -> str:
        """Alias `heading` for convenience/consistency with other objects."""
        return self.heading

    @name.setter
    def name(self: Event, name: str) -> None:
        self._name = name

    @staticmethod
    def from_dict(event_data: dict) -> Event:
        """Create a Event object from relevant dict."""
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

        return Event(
            uid,
            heading,
            start_time,
            accepted_uids,
            declined_uids,
            unanswered_uids,
            waiting_list_uids,
            unconfirmed_uids,
        )

    def __str__(self: Event) -> str:
        """Return simple human-readable description.

        Date is included because heading is unliklely to be unique.
        """
        return f"Event '{self.heading}' on {self.start_time.date()}"
