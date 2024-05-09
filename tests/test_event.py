"""Tests for Event class."""

from datetime import datetime, timezone

from spond_classes.event import Event


def test_from_dict_simple(simple_event_data: dict) -> None:
    """Test that Event is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_event = Event(**simple_event_data)

    assert my_event.uid == "A390CE5396D2F5C3015F53E171EC59D5"
    assert my_event.heading == "Event 1"
    assert my_event.recipients.group.name == "EventRecipientsGroup A"
    assert my_event.responses.accepted_uids == []
    assert my_event.responses.declined_uids == []
    assert my_event.responses.unanswered_uids == []
    assert my_event.responses.waiting_list_uids == []
    assert my_event.responses.unconfirmed_uids == []
    assert my_event.start_time == datetime(2021, 7, 6, 6, 0, tzinfo=timezone.utc)
    assert str(my_event) == "Event 'Event 1' on 2021-07-06"


def test_from_dict_complex(complex_event_data: dict) -> None:
    """Test that Event is created from dict.

    Verify values of all attributes.
    """
    my_event = Event(**complex_event_data)

    assert my_event.uid == "36D7F1A46EB2CDED4B6F22D400229822"
    assert my_event.heading == "Event 2"
    assert my_event.recipients.group.uid == "82DA0E2BF349E63736BE7DDB11E07875"
    assert my_event.recipients.group.name == "EventRecipientsGroup B"
    assert (
        my_event.recipients.group.members[0].uid == "45AD12670CAB93101B66CC0F023DA0E3"
    )
    assert my_event.recipients.group.members[0].first_name == "Kerry"
    assert my_event.recipients.group.members[0].last_name == "Condon"
    # Ignore Mypy error:
    #    Item "None" of "EventRecipientsGroupMemberProfile | None" has no attribute
    #    "uid"  [union-attr].
    assert (
        my_event.recipients.group.members[0].profile.uid  # type: ignore[union-attr]
        == "E8547508D5A36795B97278EB3AAFF54A"
    )
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
    assert my_event.start_time == datetime(2022, 11, 4, 6, 0, tzinfo=timezone.utc)
    assert str(my_event) == "Event 'Event 2' on 2022-11-04"
