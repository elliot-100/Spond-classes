"""Tests for Event class."""

from datetime import datetime, timezone

from spond_classes import Event
from tests.utils import public_attributes, sets_equal


def test_from_dict(simple_event_data: dict) -> None:
    """Test that Event is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_event = Event.from_dict(simple_event_data)
    valid_attributes = [
        "uid",
        "heading",
        "start_time",
        "accepted_uids",
        "declined_uids",
        "unanswered_uids",
        "waiting_list_uids",
        "unconfirmed_uids",
    ]
    assert sets_equal(public_attributes(my_event), valid_attributes)

    assert my_event.uid == "A390CE5396D2F5C3015F53E171EC59D5"
    assert my_event.heading == "Event 1"
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    assert my_event.accepted_uids == [
        "B24FA75A4CCBC63199A57361E88B0646",
        "C7BCC3B8A95DCF82DFFD27B2B30C8FA2",
    ]
    assert my_event.declined_uids == [
        "B4C5339E366FB5350310F2F8EA069F41",
        "9520035580A968B6BE26BA2AC9EE5617",
    ]
    assert my_event.unanswered_uids == [
        "3E546CDE2EAE242C1B8281C2042B5990",
        "D1F1866D652FDBCC7433602B2CE0017F",
    ]
    assert my_event.waiting_list_uids == [
        "0362B36507E156365471B64574EB6764",
        "AA060BEE5ABB937BD00F4A16C560F267",
    ]
    assert my_event.unconfirmed_uids == [
        "2D1BB37608F09511FD5F280D219DFD97",
        "49C2447E4ADE8005A9652B24F95E4F6F",
    ]
    assert str(my_event) == "Event 'Event 1' on 2021-07-06"
