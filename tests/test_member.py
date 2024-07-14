"""Tests for Member class."""

from datetime import datetime, timezone

from spond_classes import Member


def test_from_dict_simple(simple_member_data: dict) -> None:
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
    assert str(my_member) == ("Member(uid='M1', full_name='Brendan Gleason', …)")
    assert my_member.full_name == "Brendan Gleason"


def test_from_dict_full(complex_member_data: dict) -> None:
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
    assert str(my_member) == ("Member(uid='M2', full_name='Ciarán Hinds', …)")
    assert my_member.full_name == "Ciarán Hinds"
