"""Tests for Group class."""

from spond_classes import Group


def test_from_dict_simple(simple_group_data: dict) -> None:
    """Test that Group is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_group = Group(**simple_group_data)

    assert my_group.uid == "8B4A6A9C60397A41D6D2414AFD520152"
    assert my_group.name == "Group A"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "Group 'Group A'"


def test_from_dict_with_member_role_subgroup(complex_group_data: dict) -> None:
    """Test that nested Member, Role, Subgroup are created from dict."""
    # act
    my_group = Group(**complex_group_data)

    assert my_group.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_group.roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_group.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"


def test_member_by_id(complex_group_data: dict) -> None:
    """Test that Member is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_member = my_group.member_by_id("6F63AF02CE05328153ABA477C76E6189")
    assert my_member.uid == "6F63AF02CE05328153ABA477C76E6189"


def test_role_by_id(complex_group_data: dict) -> None:
    """Test that Role is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_role = my_group.role_by_id("29A7724B47ABEE7B3C9DC347E13A50B4")
    assert my_role.uid == "29A7724B47ABEE7B3C9DC347E13A50B4"


def test_subgroup_by_id(complex_group_data: dict) -> None:
    """Test that Subgroup is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_subgroup = my_group.subgroup_by_id("BB6B3C3592C5FC71DBDD5258D45EF6D4")
    assert my_subgroup.uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"
