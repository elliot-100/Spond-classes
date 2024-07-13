"""Tests for Event class."""

from datetime import datetime, timezone

from spond_classes import Event, EventType


def test_from_dict_simple(simple_event_data: dict) -> None:
    """Test that Event is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_event = Event(**simple_event_data)

    assert my_event.uid == "E001"
    assert my_event.heading == "Event 1"
    assert my_event.type is EventType.EVENT
    assert my_event.url == "https://spond.com/client/sponds/E001/"
    assert my_event.responses.accepted_uids == []
    assert my_event.responses.declined_uids == []
    assert my_event.responses.unanswered_uids == []
    assert my_event.responses.waiting_list_uids == []
    assert my_event.responses.unconfirmed_uids == []
    assert my_event.created_time == datetime(2020, 12, 31, 19, 0, tzinfo=timezone.utc)
    assert my_event.end_time == datetime(2024, 8, 15, 11, 0, tzinfo=timezone.utc)
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    assert str(my_event) == (
        "Event("
        "uid='E001', "
        "heading='Event 1', "
        "start_time: 2021-07-06 06:00:00+00:00, "
        "…)"
    )


def test_from_dict_complex(complex_event_data: dict) -> None:
    """Test that Event is created from dict.

    Verify values of all attributes.
    """
    my_event = Event(**complex_event_data)

    assert my_event.uid == "E002"
    assert my_event.cancelled is True
    assert my_event.heading == "Event 2"
    assert my_event.type is EventType.RECURRING
    assert my_event.url == "https://spond.com/client/sponds/E002/"
    assert my_event.responses.accepted_uids == [
        "B24FA75A4CCBC63199A57361E88B0646",
    ]
    assert my_event.responses.declined_uids == [
        "B4C5339E366FB5350310F2F8EA069F41",
    ]
    assert my_event.responses.unanswered_uids == [
        "3E546CDE2EAE242C1B8281C2042B5990",
    ]
    assert my_event.responses.waiting_list_uids == [
        "0362B36507E156365471B64574EB6764",
    ]
    assert my_event.responses.unconfirmed_uids == [
        "2D1BB37608F09511FD5F280D219DFD97",
    ]
    assert my_event.created_time == datetime(2019, 4, 24, 19, 0, tzinfo=timezone.utc)
    assert my_event.end_time == datetime(2024, 8, 15, 11, 0, tzinfo=timezone.utc)
    assert my_event.start_time == datetime(2022, 11, 4, 6, 0, tzinfo=timezone.utc)
    assert str(my_event) == (
        "Event("
        "uid='E002', "
        "heading='Event 2', "
        "start_time: 2022-11-04 06:00:00+00:00, "
        "…)"
    )
