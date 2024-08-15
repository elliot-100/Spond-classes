"""Fixtures for test suite."""

import pytest

from . import DictFromJSON

# EXTRACTS FROM EVENTS ENDPOINT:


@pytest.fixture
def simple_event_data() -> DictFromJSON:
    """Simplest possible event data in this implementation.

    For testing Event in isolation.

    Item from 'events' (root).
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

    Item from 'events' (root).
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


# EXTRACTS FROM GROUPS ENDPOINT:


@pytest.fixture
def simple_group_data() -> DictFromJSON:
    """Simplest possible group data in this implementation.

    For testing Group in isolation.

    Item from 'groups' (root).
    """
    return {
        "id": "G1",
        "name": "Group One",
        "members": [],  # assumed always exists, may be empty
        "roles": [],  # assumed always exists, may be empty
        "subGroups": [],  # assumed always exists, may be empty
    }


@pytest.fixture
def complex_group_data() -> DictFromJSON:
    """Group data with all implemented fields populated.

    The Member is in the Subgroup, and has the Role.
    All supported input fields are supplied.
    Item from 'groups' (root).
    """
    return {
        "id": "G2",
        "name": "Group Two",
        "members": [
            {
                "createdTime": "2022-03-24T16:36:29Z",
                "email": "brendan@example.com",
                "firstName": "Brendan",
                "id": "G2M1",
                "lastName": "Gleason",
                "phoneNumber": "+123456789",
                "profile": {
                    "id": "G2M1P1",
                },
                "roles": ["G2R1"],
                "subGroups": ["G2S1"],
            },
        ],
        "roles": [
            {
                "id": "G2R1",
                "name": "Role B2",
            },
        ],
        "subGroups": [
            {
                "id": "G2S1",
                "name": "Subgroup B1",
            },
        ],
    }


@pytest.fixture
def simple_member_data() -> DictFromJSON:
    """Simplest possible member data in this implementation.

    For testing Member in isolation.
    Item from 'groups' (root) -> {group} -> 'members'.
    """
    return {
        "id": "M1",
        "firstName": "Brendan",
        "lastName": "Gleason",
        "subGroups": [],
        "createdTime": "2022-03-24T16:36:29Z",
    }


@pytest.fixture
def complex_member_data() -> DictFromJSON:
    """Member data with all implemented fields populated.

    Item from 'groups' (root) -> {group} -> 'members'.
    """
    return {
        "id": "M2",
        "firstName": "Ciarán",
        "lastName": "Hinds",
        "createdTime": "2022-03-24T16:36:29Z",
        # optional:
        "email": "ciarán@example.com",
        "phoneNumber": "+123456789",
        "profile": {
            "id": "M2P2",
        },
        "roles": [
            "M2R2",
        ],
        "subGroups": [
            "M2S2",
        ],
    }


@pytest.fixture
def simple_profile_data() -> DictFromJSON:
    """Simplest possible profile data in this implementation.

    For testing Profile in isolation.
    Item from 'groups' (root) -> {group} -> 'members' -> {member} -> {profile}
    """
    return {
        "id": "P1",
    }


@pytest.fixture
def simple_role_data() -> DictFromJSON:
    """Simplest possible role data in this implementation.

    For testing Role in isolation.
    Item from 'groups' (root) -> 'roles'.
    """
    return {
        "id": "R1",
        "name": "Role One",
    }


@pytest.fixture
def simple_subgroup_data() -> DictFromJSON:
    """Simplest possible subgroup data in this implementation.

    For testing Subgroup in isolation.
    Item from 'groups' (root) -> {group} -> 'subGroups'
    """
    return {
        "id": "S1",
        "name": "Subgroup One",
    }
