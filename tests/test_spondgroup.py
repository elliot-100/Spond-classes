""" Tests for SpondGroup class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

import pytest

from spond_classes import SpondGroup


def test_create():
    """
    Test that SpondGroup is created from required fields.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sg = SpondGroup("001", "My group")
    valid_properties = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    actual_properties = list(my_sg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_sg.uid == "001"
    assert my_sg.name == "My group"
    assert my_sg.members == []
    assert my_sg.subgroups == []


@pytest.fixture
def group_dict():
    """Partial fragment from the 'groups' (root) node.
    Represents a single Group."""

    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "members": [
            {
                "createdTime": "2022-03-24T16:36:29Z",
                "email": "bg@example.com",
                "firstName": "Brendan",
                "id": "6F63AF02CE05328153ABA477C76E6189",
                "lastName": "Gleason",
                "phoneNumber": "+000000000000",
                "subGroups": [
                    "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                ],
            },
        ],
        "name": "Group A",
        "subGroups": [],
    }


def test_from_dict(group_dict):
    """
    Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sg = SpondGroup.from_dict(group_dict)
    valid_properties = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    actual_properties = list(my_sg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_sg.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_sg.name == "Group A"
    assert my_sg.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_sg.subgroups == []
