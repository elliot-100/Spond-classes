"""Tests for Event class."""

from datetime import datetime, timezone

from spond_classes import Event, Group


def test_from_dict_simple(simple_event_data: dict) -> None:
    """Test that Event is created from dict.

    Verify values of all attributes.
    """
    my_event = Event.from_dict(simple_event_data)

    assert my_event.uid == "A390CE5396D2F5C3015F53E171EC59D5"
    assert my_event.heading == "Event 1"
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    assert my_event.accepted_uids == []
    assert my_event.declined_uids == []
    assert my_event.unanswered_uids == []
    assert my_event.waiting_list_uids == []
    assert my_event.unconfirmed_uids == []
    assert str(my_event) == "Event 'Event 1' on 2021-07-06"


def test_from_dict_complex(complex_event_data: dict) -> None:
    """Test that Event is created from dict.

    Verify values of all attributes.
    """
    my_event = Event.from_dict(complex_event_data)

    assert my_event.uid == "A390CE5396D2F5C3015F53E171EC59D5"
    assert my_event.heading == "Event 1"
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    assert my_event.accepted_uids == ["6F63AF02CE05328153ABA477C76E6189"]
    assert my_event.declined_uids == ["B4C5339E366FB5350310F2F8EA069F41"]
    assert my_event.unanswered_uids == ["3E546CDE2EAE242C1B8281C2042B5990"]
    assert my_event.waiting_list_uids == ["0362B36507E156365471B64574EB6764"]
    assert my_event.unconfirmed_uids == ["2D1BB37608F09511FD5F280D219DFD97"]
    assert str(my_event) == "Event 'Event 1' on 2021-07-06"


def test_get_responses__accepted(
    complex_event_data: dict,
    complex_group_data: dict,
) -> None:
    """Test that 'accepted' Members  instances are returned."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    my_event = Event.from_dict(complex_event_data)

    # act
    accepted_members = my_event.get_responses(Event.ResponseCategory.ACCEPTED, my_group)
    declined_members = my_event.get_responses(Event.ResponseCategory.DECLINED, my_group)
    unanswered_members = my_event.get_responses(
        Event.ResponseCategory.UNANSWERED, my_group,
    )
    waiting_list_members = my_event.get_responses(
        Event.ResponseCategory.WAITING_LIST, my_group,
    )
    unconfirmed_members = my_event.get_responses(
        Event.ResponseCategory.UNCONFIRMED, my_group,
    )

    assert accepted_members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert declined_members[0].uid == "B4C5339E366FB5350310F2F8EA069F41"
    assert unanswered_members[0].uid == "3E546CDE2EAE242C1B8281C2042B5990"
    assert waiting_list_members[0].uid == "0362B36507E156365471B64574EB6764"
    assert unconfirmed_members[0].uid == "2D1BB37608F09511FD5F280D219DFD97"
