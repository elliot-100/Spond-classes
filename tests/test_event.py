"""Tests for Event class."""

from datetime import datetime, timezone

import pytest

from spond_classes import Event, EventType, Match, MatchType
from spond_classes.types import DictFromJSON


@pytest.fixture
def simple_event_data() -> DictFromJSON:
    """Simplest possible event data in this implementation.

    Mocks dict returned by `Spond.get_event()` or `Spond.get_events()[n].`
    """
    return {
        "id": "E1",
        "heading": "Event One",
        "responses": {
            "acceptedIds": [],
            "declinedIds": [],
            "unansweredIds": [],
            "waitinglistIds": [],
            "unconfirmedIds": [],
        },
        "type": "EVENT",
        "createdTime": "2020-12-31T19:00:00Z",
        "endTimestamp": "2024-08-15T11:00:00Z",
        "startTimestamp": "2021-07-06T06:00:00Z",
    }


@pytest.fixture
def complex_event_data() -> DictFromJSON:
    """Event data with all implemented fields populated.

    Mocks dict returned by `Spond.get_event()` or `Spond.get_events()[n].`
    """
    return {
        "id": "E2",
        "heading": "Event Two",
        "responses": {
            "acceptedIds": ["AC1"],
            "declinedIds": ["DC1"],
            "unansweredIds": ["UA1"],
            "waitinglistIds": ["WL1"],
            "unconfirmedIds": ["UC1"],
        },
        "type": "RECURRING",
        "createdTime": "2019-04-24T19:00:00Z",
        "endTimestamp": "2024-08-15T11:00:00Z",
        "startTimestamp": "2022-11-04T06:00:00Z",
        # optional:
        "cancelled": "True",
        "inviteTime": "2021-01-04T06:00:00Z",
    }


@pytest.fixture
def match_data() -> DictFromJSON:
    """Event data with match fields populated.

    Mocks dict returned by `Spond.get_event()` or `Spond.get_events()[n].`
    """
    return {
        "id": "M1",
        "heading": "Match One",
        "responses": {
            "acceptedIds": [],
            "declinedIds": [],
            "unansweredIds": [],
            "waitinglistIds": [],
            "unconfirmedIds": [],
        },
        "type": "EVENT",
        "createdTime": "2020-12-31T19:00:00Z",
        "endTimestamp": "2024-08-15T11:00:00Z",
        "startTimestamp": "2021-07-06T06:00:00Z",
        "matchEvent": True,
        "matchInfo": {
            "opponentName": "Hasle-Løren Hvit",
            "opponentScore": 6,
            "scoresFinal": True,
            "scoresPublic": True,
            "scoresSet": True,
            "scoresSetEver": True,
            "teamName": "Grüner lilla",
            "teamScore": 11,
            "type": "AWAY",
        },
    }


def test_from_dict_simple(simple_event_data: DictFromJSON) -> None:
    """Test that Event is created from the simplest possible data."""
    # arrange
    # act
    my_event = Event.from_dict(simple_event_data)
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


def test_from_dict_additional_fields(complex_event_data: DictFromJSON) -> None:
    """Test that Event can be created with additional supported data."""
    # arrange
    # act
    my_event = Event.from_dict(complex_event_data)
    # assert
    # - optionally populated:
    assert my_event.responses.accepted_uids == ["AC1"]
    assert my_event.responses.declined_uids == ["DC1"]
    assert my_event.responses.unanswered_uids == ["UA1"]
    assert my_event.responses.waiting_list_uids == ["WL1"]
    assert my_event.responses.unconfirmed_uids == ["UC1"]
    # - optional:
    assert my_event.cancelled is True
    assert my_event.invite_time == datetime(2021, 1, 4, 6, 0, tzinfo=timezone.utc)


def test_match_from_dict(match_data: DictFromJSON) -> None:
    """Test that Match can be created from event data with additional match data."""
    # arrange
    # act
    my_match = Match.from_dict(match_data)
    # assert
    assert isinstance(my_match, Event)
    assert isinstance(my_match, Match)
    assert my_match.match_event is True
    assert my_match.match_info.opponent_name == "Hasle-Løren Hvit"
    assert my_match.match_info.opponent_score == 6
    assert my_match.match_info.scores_final is True
    assert my_match.match_info.scores_public is True
    assert my_match.match_info.scores_set is True
    assert my_match.match_info.scores_set_ever is True
    assert my_match.match_info.team_name == "Grüner lilla"
    assert my_match.match_info.team_score == 11
    assert my_match.match_info.type is MatchType.AWAY
    assert str(my_match) == (
        "Match("
        "uid='M1', "
        "heading='Match One', "
        "start_time: 2021-07-06 06:00:00+00:00, "
        "…)"
    )
