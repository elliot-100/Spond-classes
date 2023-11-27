"""Tests for Member class."""

from datetime import datetime, timezone

from spond_classes import Member
from tests.utils import public_attributes, sets_equal


def test_from_dict_simple(simple_member_data: dict) -> None:
    """Test that Member is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    valid_attributes = [
        "uid",
        "created_time",
        "email",
        "first_name",
        "last_name",
        "full_name",
        "phone_number",
        "profile_uid",
        "roles",
        "subgroups",
    ]
    # act
    my_member = Member.from_dict(simple_member_data)

    assert sets_equal(public_attributes(my_member), valid_attributes)
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
    assert my_member.email == "brendan@example.com"
    assert my_member.first_name == "Brendan"
    assert my_member.last_name == "Gleason"
    assert my_member.full_name == "Brendan Gleason"
    assert my_member.phone_number == "+123456789"
    assert my_member.profile_uid == "364C188137AD92DC0F32E1A31A0E1731"
    assert (
        my_member.roles == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert (
        my_member.subgroups == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert str(my_member) == "Member 'Brendan Gleason' (uid ends '...189')"
