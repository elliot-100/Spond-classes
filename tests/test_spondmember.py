"""
Tests for SpondMember class.
"""

from datetime import datetime

import pytest
from dateutil import parser

from spond_classes import SpondMember
from tests.utils import public_attributes, sets_equal


def test_create():
    """
    Test that SpondMember is created from required fields only.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sm = SpondMember("001", datetime(2018, 2, 1, 17, 39), "Colin", "Farrell")
    valid_attributes = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
        "subgroups",
    ]

    assert sets_equal(public_attributes(my_sm), valid_attributes)

    assert my_sm.uid == "001"
    assert my_sm.created_time == datetime(2018, 2, 1, 17, 39)
    assert my_sm.first_name == "Colin"
    assert my_sm.last_name == "Farrell"
    assert my_sm.name == "Colin Farrell"
    assert my_sm.roles == []
    assert my_sm.subgroups == []


@pytest.fixture
def simplest_member_dict():
    """
    Partial fragment from the 'groups -> group -> members' node.
    Represents the simplest possible Member.
    """
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "firstName": "Brendan",
        "id": "6F63AF02CE05328153ABA477C76E6189",
        "lastName": "Gleason",
    }


def test_from_dict_simplest(simplest_member_dict):
    """
    Test that SpondMember is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sm = SpondMember.from_dict(simplest_member_dict)
    valid_attributes = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_sm), valid_attributes)

    assert my_sm.uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_sm.created_time == parser.isoparse("2022-03-24T16:36:29Z")  # TODO: review
    assert my_sm.first_name == "Brendan"
    assert my_sm.last_name == "Gleason"
    assert my_sm.name == "Brendan Gleason"
    assert my_sm.roles == []
    assert my_sm.subgroups == []
