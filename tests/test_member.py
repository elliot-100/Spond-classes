"""Tests for Member class."""

from datetime import datetime, timezone

from spond_classes import Member


def test_from_dict_simple(simple_member_data: dict) -> None:
    """Test that Member is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_member = Member(**simple_member_data)

    assert my_member.uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_member.created_time == datetime(
        2022,
        3,
        24,
        16,
        36,
        29,
        tzinfo=timezone.utc,
    )
    assert my_member.email is None
    assert my_member.first_name == "Brendan"
    assert my_member.last_name == "Gleason"
    assert my_member.full_name == "Brendan Gleason"
    assert my_member.phone_number is None
    assert my_member.profile is None
    assert my_member.role_uids == []
    assert my_member.subgroup_uids == []
    assert str(my_member) == "Member 'Brendan Gleason' (uid ends '...189')"


def test_from_dict_with_profile(member_with_profile_data: dict) -> None:
    """Test that Member is created from dict.

    Verify values of all attributes.
    """
    my_member = Member(**member_with_profile_data)

    assert my_member.uid == "F59D764E4CE0B643DF4C0CF5E5B2B059"
    assert my_member.created_time == datetime(
        2022,
        3,
        24,
        16,
        36,
        29,
        tzinfo=timezone.utc,
    )
    assert my_member.email == "ciarán@example.com"
    assert my_member.first_name == "Ciarán"
    assert my_member.last_name == "Hinds"
    assert my_member.full_name == "Ciarán Hinds"
    assert my_member.phone_number == "+123456789"
    # Ignore Mypy error:
    #   Item "None" of "Profile | None" has no attribute "uid"  [union-attr]
    assert (
        my_member.profile.uid  # type: ignore[union-attr]
        == "364C188137AD92DC0F32E1A31A0E1731"
    )
    assert my_member.role_uids[0] == "F2DFF55011800E66CDDAF2FD8A72039B"
    assert my_member.subgroup_uids[0] == "9E95A326090B256E2E9DAA6C0114E1D8"
    assert str(my_member) == "Member 'Ciarán Hinds' (uid ends '...059')"
