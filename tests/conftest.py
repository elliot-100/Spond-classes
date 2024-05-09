"""Fixtures for test suite."""

import pytest

# EXTRACTS FROM GROUPS ENDPOINT:


@pytest.fixture()
def simple_role_data() -> dict:
    """Represent the simplest possible Role in this implementation.

    For testing Role in isolation.
    Item from 'groups' (root) -> 'roles'.
    """
    return {
        "id": "001",
        "name": "My role",
    }


@pytest.fixture()
def simple_subgroup_data() -> dict:
    """Represent the simplest possible Subgroup in this implementation.

    For testing Subgroup in isolation.
    Item from 'groups' (root) -> {group} -> 'subGroups'
    """
    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
        "name": "Subgroup A1",
    }


@pytest.fixture()
def simple_profile_data() -> dict:
    """Represent the simplest possible Profile in this implementation.

    For testing Profile in isolation.
    Item from 'groups' (root) -> {group} -> 'members' -> {member} -> {profile}
    """
    return {
        "id": "364C188137AD92DC0F32E1A31A0E1731",
    }


@pytest.fixture()
def simple_member_data() -> dict:
    """Represent the simplest possible Member in this implementation.

    For testing Member in isolation.
    Item from 'groups' (root) -> {group} -> 'members'.
    """
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        # email is optional
        "firstName": "Brendan",
        "id": "6F63AF02CE05328153ABA477C76E6189",
        "lastName": "Gleason",
        # phoneNumber is optional
        # profile is optional
        # roles is optional
        "subGroups": [],
    }


@pytest.fixture()
def member_with_profile_data() -> dict:
    """Represent a single Member with Profile.

    All supported input fields are supplied.
    Item from 'groups' (root) -> {group} -> 'members'.
    """
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "email": "ciarán@example.com",
        "firstName": "Ciarán",
        "id": "F59D764E4CE0B643DF4C0CF5E5B2B059",
        "lastName": "Hinds",
        "phoneNumber": "+123456789",
        "profile": {
            "id": "364C188137AD92DC0F32E1A31A0E1731",
        },
        "roles": [
            "F2DFF55011800E66CDDAF2FD8A72039B",
        ],
        "subGroups": [
            "9E95A326090B256E2E9DAA6C0114E1D8",
        ],
    }


@pytest.fixture()
def simple_group_data() -> dict:
    """Represent the simplest possible Group in this implementation.

    Item from 'groups' (root).
    """
    return {
        "id": "8B4A6A9C60397A41D6D2414AFD520152",
        "name": "Group A",
        "members": [],  # assumed always exists, may be empty
        "roles": [],  # assumed always exists, may be empty
        "subGroups": [],  # assumed always exists, may be empty
    }


@pytest.fixture()
def complex_group_data() -> dict:
    """Represent a single Group with a single Member, single Subgroup, single Role.

    The Member is in the Subgroup, and has the Role.
    All supported input fields are supplied.
    Item from 'groups' (root).
    """
    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "members": [
            {
                "createdTime": "2022-03-24T16:36:29Z",
                "email": "brendan@example.com",
                "firstName": "Brendan",
                "id": "6F63AF02CE05328153ABA477C76E6189",
                "lastName": "Gleason",
                "phoneNumber": "+123456789",
                "profile": {
                    "id": "364C188137AD92DC0F32E1A31A0E1731",
                },
                "roles": [
                    "29A7724B47ABEE7B3C9DC347E13A50B4",
                ],
                "subGroups": [
                    "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                ],
            },
        ],
        "name": "Group B",
        "subGroups": [
            {
                "id": "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                "name": "Subgroup B1",
            },
        ],
        "roles": [
            {
                "id": "29A7724B47ABEE7B3C9DC347E13A50B4",
                "name": "Role B2",
            },
        ],
    }


# EXTRACTS FROM EVENTS ENDPOINT:


@pytest.fixture()
def simple_event_data() -> dict:
    """Represent the simplest possible Event in this implementation.

    Item from 'events' (root).
    """
    return {
        "id": "A390CE5396D2F5C3015F53E171EC59D5",
        "heading": "Event 1",
        "startTimestamp": "2021-07-06T06:00:00Z",
        "responses": {
            "acceptedIds": [],
            "declinedIds": [],
            "unansweredIds": [],
            "waitinglistIds": [],
            "unconfirmedIds": [],
        },
    }


@pytest.fixture()
def complex_event_data() -> dict:
    """Represent the simplest possible Event in this implementation.

    All supported input fields are supplied.
    Item from 'events' (root).
    """
    return {
        "id": "36D7F1A46EB2CDED4B6F22D400229822",
        "heading": "Event 2",
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
        "startTimestamp": "2022-11-04T06:00:00Z",
    }
