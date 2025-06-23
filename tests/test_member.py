"""Tests for Member class."""

from datetime import datetime, timezone

import pytest

from spond_classes import Member
from spond_classes.typing import DictFromJSON


@pytest.fixture
def simple_member_data() -> DictFromJSON:
    """Simplest possible member data in this implementation.

    Mocks dict returned by `Spond.get_group()['members'][n]`.
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

    Mocks dict returned by `Spond.get_group()['members'][n]`.
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
            "firstName": "",
            "lastName": "",
            # optional:
            "email": "ciarán2@example.com",
            "phoneNumber": "+123456790",
        },
        "roles": [
            "M2R2",
        ],
        "subGroups": [
            "M2S2",
        ],
    }


def test_from_dict_simple(simple_member_data: DictFromJSON) -> None:
    """Test that Member is created from the simplest possible data."""
    # arrange
    # act
    my_member = Member(**simple_member_data)
    # assert
    assert my_member.uid == "M1"
    assert my_member.created_time == datetime(
        2022, 3, 24, 16, 36, 29, tzinfo=timezone.utc
    )
    assert my_member.first_name == "Brendan"
    assert my_member.last_name == "Gleason"
    # - optionally populated:
    assert my_member.subgroup_uids == []
    # - optional:
    assert my_member.email is None
    assert my_member.phone_number is None
    assert my_member.profile is None
    assert my_member.role_uids is None
    # - properties:
    assert str(my_member) == "Member(uid='M1', full_name='Brendan Gleason', …)"
    assert my_member.full_name == "Brendan Gleason"


def test_from_dict_full(complex_member_data: DictFromJSON) -> None:
    """Test that Member is created from dict with all supported attributes."""
    # arrange
    # act
    my_member = Member(**complex_member_data)
    # assert
    assert my_member.uid == "M2"
    assert my_member.created_time == datetime(
        2022, 3, 24, 16, 36, 29, tzinfo=timezone.utc
    )
    assert my_member.first_name == "Ciarán"
    assert my_member.last_name == "Hinds"
    # - optionally populated:
    assert my_member.subgroup_uids[0] == "M2S2"
    # - optional:
    assert my_member.email == "ciarán@example.com"
    assert my_member.phone_number == "+123456789"
    # Ignore Mypy errors:
    #   Item "None" of "Profile | None" has no attribute "uid"  [union-attr]
    assert (
        my_member.profile.uid  # type: ignore[union-attr]
        == "M2P2"
    )
    assert (
        my_member.role_uids[0]  # type: ignore[index]
        == "M2R2"
    )
    # - properties:
    assert str(my_member) == "Member(uid='M2', full_name='Ciarán Hinds', …)"
    assert my_member.full_name == "Ciarán Hinds"
