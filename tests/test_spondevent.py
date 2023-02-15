""" Tests for SpondEvent class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

from datetime import datetime

import pytest
from dateutil import parser

from spond_classes import SpondEvent
from tests.utils import public_attributes, sets_equal


def test_create():
    """
    Test that SpondEvent is created from required fields only.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """

    my_se = SpondEvent("001", "My event", datetime(2022, 9, 15, 8, 30))
    valid_attributes = [
        "uid",
        "heading",
        "name",
        "start_time",
        "accepted_uids",
        "declined_uids",
        "unanswered_uids",
        "waiting_list_uids",
        "unconfirmed_uids",
    ]
    assert sets_equal(public_attributes(my_se), valid_attributes)

    assert my_se.uid == "001"
    assert my_se.heading == "My event"
    assert my_se.name == "My event"
    assert my_se.start_time == datetime(2022, 9, 15, 8, 30)
    assert my_se.accepted_uids == []
    assert my_se.declined_uids == []
    assert my_se.unanswered_uids == []
    assert my_se.waiting_list_uids == []
    assert my_se.unconfirmed_uids == []


@pytest.fixture
def event_dict():
    """Partial item from the 'events' dict returned by Spond package
    Represents a single Event."""

    return {
        "id": "A390CE5396D2F5C3015F53E171EC59D5",
        "heading": "Event 1",
        "startTimestamp": "2021-07-06T06:00:00Z",
        "responses": {
            "acceptedIds": [
                "B24FA75A4CCBC63199A57361E88B0646",
                "C7BCC3B8A95DCF82DFFD27B2B30C8FA2",
            ],
            "declinedIds": [
                "B4C5339E366FB5350310F2F8EA069F41",
                "9520035580A968B6BE26BA2AC9EE5617",
            ],
            "unansweredIds": [
                "3E546CDE2EAE242C1B8281C2042B5990",
                "D1F1866D652FDBCC7433602B2CE0017F",
            ],
            "waitinglistIds": [
                "0362B36507E156365471B64574EB6764",
                "AA060BEE5ABB937BD00F4A16C560F267",
            ],
            "unconfirmedIds": [
                "2D1BB37608F09511FD5F280D219DFD97",
                "49C2447E4ADE8005A9652B24F95E4F6F",
            ],
        },
    }


def test_from_dict(event_dict):
    """
    Test that SpondEvent is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_se = SpondEvent.from_dict(event_dict)
    valid_attributes = [
        "uid",
        "heading",
        "name",
        "start_time",
        "accepted_uids",
        "declined_uids",
        "unanswered_uids",
        "waiting_list_uids",
        "unconfirmed_uids",
    ]
    assert sets_equal(public_attributes(my_se), valid_attributes)

    assert my_se.uid == "A390CE5396D2F5C3015F53E171EC59D5"
    assert my_se.heading == "Event 1"
    assert my_se.name == "Event 1"
    assert my_se.start_time == parser.isoparse("2021-07-06T06:00:00Z")
    assert my_se.accepted_uids == [
        "B24FA75A4CCBC63199A57361E88B0646",
        "C7BCC3B8A95DCF82DFFD27B2B30C8FA2",
    ]
    assert my_se.declined_uids == [
        "B4C5339E366FB5350310F2F8EA069F41",
        "9520035580A968B6BE26BA2AC9EE5617",
    ]
    assert my_se.unanswered_uids == [
        "3E546CDE2EAE242C1B8281C2042B5990",
        "D1F1866D652FDBCC7433602B2CE0017F",
    ]
    assert my_se.waiting_list_uids == [
        "0362B36507E156365471B64574EB6764",
        "AA060BEE5ABB937BD00F4A16C560F267",
    ]
    assert my_se.unconfirmed_uids == [
        "2D1BB37608F09511FD5F280D219DFD97",
        "49C2447E4ADE8005A9652B24F95E4F6F",
    ]
