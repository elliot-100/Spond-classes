"""Tests for Event class."""

from datetime import datetime, timezone

from spond_classes import Event, EventType

from . import DictFromJSON


def test_from_dict_simple(simple_event_data: DictFromJSON) -> None:
    """Test that Event is created from the simplest possible data."""
    # arrange
    # act
    my_event = Event.model_validate(simple_event_data)
    # assert
    assert my_event.uid == "E1"
    assert my_event.heading == "Event One"
    assert my_event.responses.accepted_uids == []
    assert my_event.responses.declined_uids == []
    assert my_event.responses.unanswered_uids == []
    assert my_event.responses.waiting_list_uids == []
    assert my_event.responses.unconfirmed_uids == []
    assert my_event.type is EventType.EVENT
    assert my_event.created_time == datetime(2020, 12, 31, 19, 0, tzinfo=timezone.utc)
    assert my_event.end_time == datetime(2024, 8, 15, 11, 0, tzinfo=timezone.utc)
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    # - optional:
    assert my_event.cancelled is None
    assert my_event.invite_time is None
    # - properties:
    assert str(my_event) == (
        "Event("
        "uid='E1', "
        "heading='Event One', "
        "start_time: 2021-07-06 06:00:00+00:00, "
        "…)"
    )
    assert my_event.url == "https://spond.com/client/sponds/E1/"


def test_from_dict_complex(complex_event_data: DictFromJSON) -> None:
    """Test that Event is created from dict with all supported attributes.

    Verify values of all attributes.
    """
    # arrange
    # act
    my_event = Event.model_validate(complex_event_data)
    # assert
    assert my_event.uid == "E2"
    assert my_event.heading == "Event Two"
    assert my_event.responses.accepted_uids == ["AC1"]
    assert my_event.responses.declined_uids == ["DC1"]
    assert my_event.responses.unanswered_uids == ["UA1"]
    assert my_event.responses.waiting_list_uids == ["WL1"]
    assert my_event.responses.unconfirmed_uids == ["UC1"]
    assert my_event.type is EventType.RECURRING
    assert my_event.created_time == datetime(2019, 4, 24, 19, 0, tzinfo=timezone.utc)
    assert my_event.end_time == datetime(2024, 8, 15, 11, 0, tzinfo=timezone.utc)
    assert my_event.start_time == datetime(2022, 11, 4, 6, 0, tzinfo=timezone.utc)
    # - optional:
    assert my_event.cancelled is True
    assert my_event.invite_time == datetime(2021, 1, 4, 6, 0, tzinfo=timezone.utc)
    # - properties:
    assert str(my_event) == (
        "Event("
        "uid='E2', "
        "heading='Event Two', "
        "start_time: 2022-11-04 06:00:00+00:00, "
        "…)"
    )
    assert my_event.url == "https://spond.com/client/sponds/E2/"
