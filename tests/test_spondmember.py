""" Tests for SpondMember class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

from datetime import datetime

import pytest
from dateutil import parser

from spond_classes import DuplicateKeyError, SpondMember


def test_create():
    """
    Test that SpondMember is created from required fields.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    SpondMember.instances = {}
    my_sm = SpondMember("001", datetime(2018, 2, 1, 17, 39), "Colin", "Farrell")
    valid_properties = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
    ]
    actual_properties = list(my_sm.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_sm.uid == "001"
    assert my_sm.created_time == datetime(2018, 2, 1, 17, 39)
    assert my_sm.first_name == "Colin"
    assert my_sm.last_name == "Farrell"
    assert my_sm.name == "Colin Farrell"
    assert my_sm.roles == []


def test_create_with_existing_uid():
    """
    Test that SpondMember is not created, and error is raised if a SpondMember exists
    with the same uid
    """
    SpondMember.instances = {}
    SpondMember("001", datetime(2018, 2, 1, 17, 39), "Colin", "Farrell")
    with pytest.raises(DuplicateKeyError):
        SpondMember("001", datetime(2016, 10, 18, 18, 00), "Cate", "Blanchett")
    assert len(SpondMember.instances) == 1


@pytest.fixture
def simple_member_dict():
    """No roles or profile data"""
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "email": "bg@example.com",
        "firstName": "Brendan",
        "id": "6F63AF02CE05328153ABA477C76E6189",
        "lastName": "Gleason",
        "phoneNumber": "+000000000000",
        "subGroups": [
            "BB6B3C3592C5FC71DBDD5258D45EF6D4",
            "C99299D5F21152D3E3563B4BA9DDFD66",
        ],
    }


@pytest.fixture
def complex_member_dict():
    """With roles and profile data"""
    return {
        "createdTime": "2022-03-24T16:36:29Z",
        "email": "bg@example.com",
        "firstName": "Brendan",
        "id": "4F55DE751066F756FD3BB6D0801F3B85",
        "lastName": "Gleason",
        "phoneNumber": "+000000000000",
        "profile": {
            "contactMethod": "app",
            "email": "bg@example.com",
            "firstName": "Brendan",
            "id": "2D9E5A4BB3B4D06D39DE992515E44282",
            "lastName": "Gleason",
            "phoneNumber": "+447753840542",
        },
        "roles": [
            "29A7724B47ABEE7B3C9DC347E13A50B4",
            "F375A5788FD09DFFD725BDE9DF8ACC04",
        ],
        "subGroups": [
            "F9A075B78AFD29A2A53D39AF53F7C744",
            "7EC4F44D676BA8615E142786048A26AE",
        ],
    }


def test_from_dict_simple(simple_member_dict):
    """
    Test that SpondMember is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sm = SpondMember.from_dict(simple_member_dict)
    valid_properties = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
    ]
    actual_properties = list(my_sm.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_sm.uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_sm.created_time == parser.isoparse("2022-03-24T16:36:29Z")  # TODO: review
    assert my_sm.first_name == "Brendan"
    assert my_sm.last_name == "Gleason"
    assert my_sm.name == "Brendan Gleason"
    assert my_sm.roles == []


def test_from_dict_complex(complex_member_dict):
    """
    Test that SpondMember is created from JSON.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sm = SpondMember.from_dict(complex_member_dict)
    valid_properties = [
        "uid",
        "created_time",
        "first_name",
        "last_name",
        "name",
        "roles",
    ]
    actual_properties = list(my_sm.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_sm.uid == "4F55DE751066F756FD3BB6D0801F3B85"
    assert my_sm.created_time == parser.isoparse("2022-03-24T16:36:29Z")  # TODO: review
    assert my_sm.first_name == "Brendan"
    assert my_sm.last_name == "Gleason"
    assert my_sm.name == "Brendan Gleason"
    assert my_sm.roles == [
        "29A7724B47ABEE7B3C9DC347E13A50B4",
        "F375A5788FD09DFFD725BDE9DF8ACC04",
    ]
