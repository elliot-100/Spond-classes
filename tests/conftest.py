"""Fixtures for test suite."""

import pytest


@pytest.fixture()
def simple_member_data() -> dict:
    """Represent the simplest possible Member in this implementation.

    For testing Member in isolation.

    Item from 'groups' -> 'group' -> 'members'.

    """
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "email": "brendan@example.com",
        "firstName": "Brendan",
        "id": "6F63AF02CE05328153ABA477C76E6189",
        "lastName": "Gleason",
        "phoneNumber": "+123456789",
        "profile": {
            "id": "364C188137AD92DC0F32E1A31A0E1731",
        },
    }


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

    Item from 'groups' (root) -> 'group' -> 'subGroups'.
    """
    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
        "name": "Subgroup A1",
    }


@pytest.fixture()
def simple_event_data() -> dict:
    """Represent the simplest possible Event in this implementation.

    For testing Event in isolation.

    Item from 'events' (root).
    """
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


@pytest.fixture()
def simple_group_data() -> dict:
    """Represent the simplest possible Group in this implementation.

    For testing Event in isolation.

    Item from 'groups' (root).

    """
    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "name": "Group A",
    }


@pytest.fixture()
def complex_group_data() -> dict:
    """Represent a single Group with a single Member, single Subgroup, single Role.

    The Member is in the Subgroup, and has the Role.

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
        "name": "Group A",
        "subGroups": [
            {
                "id": "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                "name": "Subgroup A1",
            },
        ],
        "roles": [
            {
                "id": "29A7724B47ABEE7B3C9DC347E13A50B4",
                "name": "Role A2",
            },
        ],
    }
