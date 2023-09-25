"""Event class."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dateutil import parser

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class Event:
    """Represents an event in the Spond system.

    NB: relationship to Group isn't yet implemented.
    NB: relationship to Member (rather than just their ids) isn't yet implemented.

    Attributes
    ----------
    uid : str
        id of the Event.
        'id' in API, but 'id' is a reserved term and the `spond` package uses `uid`.
    heading : str
        Name or title of the Event.
        'heading' in API.
    start_time : datetime.
        Datetime at which the Event starts.
        Derived from 'startTimestamp' in API, but returns a datetime instead of
        a string.
    accepted_uids : list[str]
        `responses` -> `acceptedIds` in API.
    declined_uids : list[str]
        `responses` -> `declinedIds` in API.
    unanswered_uids : list[str]
        `responses` -> `unansweredIds` in API.
    unconfirmed_uids : list[str]
        `responses` -> `unconfirmedIds` in API.
    waiting_list_uids : list[str]
        `responses` -> `waitinglistIds` in API.
    """

    # Required params, populated by implicit Event.__init__().
    uid: str
    heading: str
    start_time: datetime

    # Populated by `Event.from_dict()`, as they rely on full Event data:
    accepted_uids: list = field(default_factory=list, repr=False)
    declined_uids: list = field(default_factory=list, repr=False)
    unanswered_uids: list = field(default_factory=list, repr=False)
    waiting_list_uids: list = field(default_factory=list, repr=False)
    unconfirmed_uids: list = field(default_factory=list, repr=False)

    @staticmethod
    def from_dict(event_data: dict) -> Event:
        """Create an Event object from relevant dict.

        Parameters
        ----------
        event_data
            Dict representing the event, as returned by `spond.get_event()`.
        """
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

        Date is included because heading is unlikely to be unique.
        """
        return f"Event '{self.heading}' on {self.start_time.date()}"
