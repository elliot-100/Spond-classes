"""Tests for Group class and child classes."""

from spond_classes import Group
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that Group is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = Group("001", "My group")
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
    assert str(my_group) == "Group 'My group'"


def test_core_from_dict_simplest(simplest_group_data: dict) -> None:
    """Test that a Group is created from the simplest possible dict representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = Group.core_from_dict(simplest_group_data)
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
    assert str(my_group) == "Group 'Group A'"


def test_from_dict_simplest(simplest_group_data: dict) -> None:
    """Test that a Group is created from the simplest possible dict representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.

    NB: this should produce exactly the same output as
    `test_core_from_dict_simple(simplest_group_dict)`

    """
    my_group = Group.core_from_dict(simplest_group_data)
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
    assert str(my_group) == "Group 'Group A'"


def test_from_dict_complex(complex_group_data: dict) -> None:
    """Test that Group is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_group = Group.from_dict(complex_group_data)
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
    assert str(my_group) == "Group 'Group A'"

    # Group.members -> Member
    assert my_group.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    # Test attributes not handled by simple Member tests
    assert my_group.members[0].roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_group.members[0].subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"

    # Group.subgroups -> Subgroup
    assert my_group.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"
    # Test attributes not handled by simple Subgroup tests
    assert my_group.subgroups[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # Group.subgroups -> Role
    assert my_group.roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    # Test attributes not handled by simple Role tests
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
