"""Tests for SpondMember class."""

from datetime import datetime, timezone

from spond_classes import SpondMember
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that SpondMember is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_member = SpondMember(
        "001",
        datetime(2018, 2, 1, 17, 39, tzinfo=timezone.utc),
        "Colin",
        "Farrell",
    )
    valid_attributes = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
        "subgroups",
    ]

    assert sets_equal(public_attributes(my_member), valid_attributes)

    assert my_member.uid == "001"
    assert my_member.created_time == datetime(2018, 2, 1, 17, 39, tzinfo=timezone.utc)
    assert my_member.first_name == "Colin"
    assert my_member.last_name == "Farrell"
    assert my_member.name == "Colin Farrell"
    assert my_member.roles == []
    assert my_member.subgroups == []
    assert str(my_member) == "SpondMember 'Colin Farrell' (uid ends '...001')"


def test_from_dict_simplest(simplest_member_data: dict) -> None:
    """Test that SpondMember is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_member = SpondMember.from_dict(simplest_member_data)
    valid_attributes = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_member), valid_attributes)

    assert my_member.uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_member.created_time == datetime(
        2022, 3, 24, 16, 36, 29, tzinfo=timezone.utc
    )
    assert my_member.first_name == "Brendan"
    assert my_member.last_name == "Gleason"
    assert my_member.name == "Brendan Gleason"
    assert my_member.roles == []
    assert my_member.subgroups == []
    assert str(my_member) == "SpondMember 'Brendan Gleason' (uid ends '...189')"
