"""Tests for SpondGroup class and child classes."""

import pytest

from spond_classes import SpondGroup
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that SpondGroup is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = SpondGroup("001", "My group")
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
        "roles",
    ]
    assert sets_equal(public_attributes(my_group), valid_attributes)

    assert my_group.uid == "001"
    assert my_group.members == []
    assert my_group.name == "My group"
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "[SpondGroup 'My group']"


@pytest.fixture()
def simplest_group_data() -> dict:
    """Represent the simplest possible Group in this implementation.

    Item from 'groups' (root).

    """
    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "name": "Group A",
    }


def test_core_from_dict_simplest(simplest_group_data: dict) -> None:
    """Test that a SpondGroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = SpondGroup.core_from_dict(simplest_group_data)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
        "roles",
    ]
    assert sets_equal(public_attributes(my_group), valid_attributes)

    assert my_group.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_group.name == "Group A"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "[SpondGroup 'Group A']"


def test_from_dict_simplest(simplest_group_data: dict) -> None:
    """Test that a minimal SpondGroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.

    NB: this should produce exactly the same output as
    `test_core_from_dict_simple(simplest_group_dict)`

    """
    my_group = SpondGroup.core_from_dict(simplest_group_data)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
        "roles",
    ]
    assert sets_equal(public_attributes(my_group), valid_attributes)

    assert my_group.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_group.name == "Group A"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "[SpondGroup 'Group A']"


@pytest.fixture()
def complex_group_data() -> dict:
    """Represent a single Group with a single Member, single Subgroup, single Role.

    The Member is in the Subgroup, and has the Role.

    Item from 'groups' (root).
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
            },
        ],
        "roles": [
            {
                "id": "29A7724B47ABEE7B3C9DC347E13A50B4",
                "name": "Role A2",
            },
        ],
    }


def test_from_dict_complex(complex_group_data: dict) -> None:
    """Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = SpondGroup.from_dict(complex_group_data)
    valid_attributes = [
        "uid",
        "name",
        "members",
        "roles",
        "subgroups",
    ]
    assert sets_equal(public_attributes(my_group), valid_attributes)

    # Group attributes
    assert my_group.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_group.name == "Group A"
    assert str(my_group) == "[SpondGroup 'Group A']"

    # SpondGroup.members -> SpondMember
    assert my_group.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    # Test attributes not handled by simple SpondMember tests
    assert my_group.members[0].roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_group.members[0].subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"

    # SpondGroup.subgroups -> SpondSubgroup
    assert my_group.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"
    # Test attributes not handled by simple SpondSubgroup tests
    assert my_group.subgroups[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # SpondGroup.subgroups -> SpondRole
    assert my_group.roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    # Test attributes not handled by simple SpondRole tests
    assert my_group.roles[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # Assertions by inclusion
    assert my_group.members[0] in my_group.roles[0].members
    assert my_group.members[0] in my_group.subgroups[0].members
    assert my_group.subgroups[0].members[0] in my_group.members
    assert my_group.roles[0].members[0] in my_group.members

    assert my_group.roles[0] in my_group.members[0].roles
    assert my_group.roles[0] in my_group.subgroups[0].members[0].roles
    assert my_group.members[0].roles[0] in my_group.roles

    assert my_group.subgroups[0] in my_group.members[0].subgroups
    assert my_group.members[0].subgroups[0] in my_group.subgroups
