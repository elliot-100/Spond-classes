""" Tests for SpondGroup class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

import pytest

from spond_classes import SpondGroup, SpondSubgroup


def test_create():
    """
    Test that SpondSubgroup is created from required fields.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    dummy_sg = SpondGroup("001", "Dummy group")
    my_ssg = SpondSubgroup("001", "My subgroup", dummy_sg)
    valid_properties = [
        "uid",
        "name",
        "members",
        "parent_group",
    ]
    actual_properties = list(my_ssg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_ssg.uid == "001"
    assert my_ssg.name == "My subgroup"
    assert my_ssg.members == []
    assert my_ssg.parent_group is dummy_sg


@pytest.fixture
def subgroup_dict():
    """Partial fragment from the 'groups' (root) -> 'group' -> 'subGroups' node.
    Represents a single subGroup."""

    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
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
        "name": "Subgroup A1",
    }


def test_from_dict(subgroup_dict):
    """
    Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    dummy_sg = SpondGroup("001", "Dummy group")
    my_ssg = SpondSubgroup.from_dict(subgroup_dict, dummy_sg)
    valid_properties = [
        "uid",
        "name",
        "members",
        "parent_group",
    ]
    actual_properties = list(my_ssg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_ssg.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_ssg.name == "Subgroup A1"
    assert my_ssg.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_ssg.parent_group is dummy_sg
