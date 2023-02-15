""" Tests for SpondMember class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
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
    ]

    assert sets_equal(public_attributes(my_sm), valid_attributes)

    assert my_sm.uid == "001"
    assert my_sm.created_time == datetime(2018, 2, 1, 17, 39)
    assert my_sm.first_name == "Colin"
    assert my_sm.last_name == "Farrell"
    assert my_sm.name == "Colin Farrell"
    assert my_sm.roles == []


@pytest.fixture
def simplest_member_dict():
    """
    Represents the simplest possible member node.
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
    ]
    assert sets_equal(public_attributes(my_sm), valid_attributes)

    assert my_sm.uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_sm.created_time == parser.isoparse("2022-03-24T16:36:29Z")  # TODO: review
    assert my_sm.first_name == "Brendan"
    assert my_sm.last_name == "Gleason"
    assert my_sm.name == "Brendan Gleason"
    assert my_sm.roles == []


@pytest.fixture
def complex_member_dict():
    """With roles and profile data"""
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "firstName": "Brendan",
        "id": "4F55DE751066F756FD3BB6D0801F3B85",
        "lastName": "Gleason",
        "roles": [
            "29A7724B47ABEE7B3C9DC347E13A50B4",
        ],
    }


def test_from_dict_complex(complex_member_dict):
    """
    Test that SpondMember is created from JSON.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sm = SpondMember.from_dict(complex_member_dict)
    valid_attributes = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
    ]
    assert sets_equal(public_attributes(my_sm), valid_attributes)

    assert my_sm.uid == "4F55DE751066F756FD3BB6D0801F3B85"
    assert my_sm.created_time == parser.isoparse("2022-03-24T16:36:29Z")  # TODO: review
    assert my_sm.first_name == "Brendan"
    assert my_sm.last_name == "Gleason"
    assert my_sm.name == "Brendan Gleason"
    assert my_sm.roles == [
        "29A7724B47ABEE7B3C9DC347E13A50B4",
    ]
