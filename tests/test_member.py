"""Tests for Member class."""

from datetime import datetime, timezone

from spond_classes import Member


def test_from_dict_simple(simple_member_data: dict) -> None:
    """Test that Member is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_member = Member.from_dict(simple_member_data)

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
    assert my_member.profile_uid is None
    assert str(my_member) == "Member 'Brendan Gleason' (uid ends '...189')"

    # Tested as part of complex Group, as it relies on full Group data.
    assert my_member.roles == []
    assert my_member.subgroups == []


def test_from_dict_complex(complex_member_data: dict) -> None:
    """Test that Member is created from dict.

    Verify values of all attributes.
    """
    my_member = Member.from_dict(complex_member_data)

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
    assert my_member.profile_uid == "364C188137AD92DC0F32E1A31A0E1731"
    assert my_member.roles == []

    # Tested as part of complex Group, as it relies on full Group data.
    assert my_member.roles == []
    assert my_member.subgroups == []
