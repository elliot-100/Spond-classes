"""
Tests for SpondGroup class and child classes.
"""

import pytest

from spond_classes import SpondGroup
from tests.utils import public_attributes, sets_equal


def test_create():
    """
    Test that SpondGroup is created from required fields only.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sg = SpondGroup("001", "My group")
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_sg), valid_attributes)

    assert my_sg.uid == "001"
    assert my_sg.name == "My group"
    assert my_sg.members == []
    assert my_sg.subgroups == []


@pytest.fixture
def simplest_group_dict():
    """
    Partial fragment from the 'groups' (root) node.
    Represents the simplest possible Group.
    """

    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "name": "Group A",
    }


def test_core_from_dict_simplest(simplest_group_dict):
    """
    Test that a minimal SpondGroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sg = SpondGroup.core_from_dict(simplest_group_dict)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_sg), valid_attributes)

    assert my_sg.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_sg.name == "Group A"
    assert my_sg.members == []
    assert my_sg.subgroups == []


def test_from_dict_simplest(simplest_group_dict):
    """
    Test that a minimal SpondGroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.

    NB: this should produce exactly the same output as
    `test_core_from_dict_simple(simplest_group_dict)`

    """
    my_sg = SpondGroup.core_from_dict(simplest_group_dict)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_sg), valid_attributes)

    assert my_sg.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_sg.name == "Group A"
    assert my_sg.members == []
    assert my_sg.subgroups == []


@pytest.fixture
def complex_group_dict():
    """
    Partial fragment from the 'groups' (root) node.
    Represents a single Group with a single Member and a single Subgroup. The Member is
    also in the Subgroup.
    """

    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "members": [
            {
                "createdTime": "2022-03-24T16:36:29Z",
                "firstName": "Brendan",
                "id": "6F63AF02CE05328153ABA477C76E6189",
                "lastName": "Gleason",
                "roles": [
                    "29A7724B47ABEE7B3C9DC347E13A50B4",
                ],
                "subGroups": [
                    "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                ],
            },
        ],
        "name": "Group A",
        "subGroups": [
            {
                "id": "BB6B3C3592C5FC71DBDD5258D45EF6D4",
                "name": "Subgroup A1",
            }
        ],
    }


def test_from_dict_complex(complex_group_dict):
    """
    Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_sg = SpondGroup.from_dict(complex_group_dict)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_sg), valid_attributes)

    # Assertions for SpondGroup attributes
    assert my_sg.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_sg.name == "Group A"

    # Assertions for SpondGroup.members -> SpondMember by attribute
    assert my_sg.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_sg.members[0].roles[0] == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_sg.members[0].subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"

    # Assertions for SpondGroup.subgroups -> SpondSubgroup by attribute
    assert my_sg.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"
    # Test attributes not handled by simple SpondMember tests
    assert my_sg.subgroups[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # Assertions by identity
    assert my_sg.members[0] in my_sg.members
    assert my_sg.members[0].subgroups[0] in my_sg.subgroups
    assert my_sg.members[0] in my_sg.subgroups[0].members

