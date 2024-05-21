"""Tests for Group class."""

import pytest

from spond_classes.group import Group


def test_from_dict_simple(simple_group_data: dict) -> None:
    """Test that Group is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    # arrange

    # act
    my_group = Group(**simple_group_data)

    # assert
    assert my_group.uid == "8B4A6A9C60397A41D6D2414AFD520152"
    assert my_group.name == "Group A"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "Group 'Group A'"


def test_from_dict_with_member_role_subgroup(complex_group_data: dict) -> None:
    """Test that nested Member, Role, Subgroup are created from dict."""
    # arrange

    # act
    my_group = Group(**complex_group_data)

    # assert
    assert my_group.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    assert my_group.roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_group.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"


def test_member_by_id__happy_path(complex_group_data: dict) -> None:
    """Test that Member is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_member = my_group.member_by_id("6F63AF02CE05328153ABA477C76E6189")

    # assert
    assert my_member.uid == "6F63AF02CE05328153ABA477C76E6189"


def test_member_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: dict,
) -> None:
    """Test that LookupError is raised when uid can't be matched against a Member."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    with pytest.raises(LookupError):
        my_member = my_group.member_by_id("DUMMY_ID")


def test_role_by_id__happy_path(complex_group_data: dict) -> None:
    """Test that Role is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_role = my_group.role_by_id("29A7724B47ABEE7B3C9DC347E13A50B4")

    # assert
    assert my_role.uid == "29A7724B47ABEE7B3C9DC347E13A50B4"


def test_role_by_id__unmatched_id_raises_lookup_error(complex_group_data: dict) -> None:
    """Test that LookupError is raised when uid can't be matched against a Role."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    with pytest.raises(LookupError):
        my_role = my_group.role_by_id("DUMMY_ID")


def test_subgroup_by_id__happy_path(complex_group_data: dict) -> None:
    """Test that Subgroup is returned from a valid uid."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    my_subgroup = my_group.subgroup_by_id("BB6B3C3592C5FC71DBDD5258D45EF6D4")

    # assert
    assert my_subgroup.uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"


def test_subgroup_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: dict,
) -> None:
    """Test that LookupError is raised when uid can't be matched against a Subgroup."""
    # arrange
    my_group = Group(**complex_group_data)

    # act
    with pytest.raises(LookupError):
        my_subgroup = my_group.subgroup_by_id("DUMMY_ID")


def test_members_by_subgroup__happy_path(complex_group_data: dict) -> None:
    """Test that Members are returned from a valid Subgroup."""
    # arrange
    my_group = Group(**complex_group_data)
    my_subgroup = my_group.subgroup_by_id("BB6B3C3592C5FC71DBDD5258D45EF6D4")

    # act
    my_subgroup_members = my_group.members_by_subgroup(my_subgroup)

    # assert
    assert my_subgroup_members[0].uid == "6F63AF02CE05328153ABA477C76E6189"


def test_members_by_subgroup__not_subgroup_raises_type_error(
    complex_group_data: dict,
) -> None:
    """Test that TypeError is raised if `subgroup` isn't a Subgroup."""
    # arrange
    my_group = Group(**complex_group_data)
    role_not_subgroup = my_group.role_by_id("29A7724B47ABEE7B3C9DC347E13A50B4")

    # act
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_subgroup_members = my_group.members_by_subgroup(role_not_subgroup)  # type: ignore[arg-type]


def test_members_by_role__happy_path(complex_group_data: dict) -> None:
    """Test that Members are returned from a valid Role."""
    # arrange
    my_group = Group(**complex_group_data)
    my_role = my_group.role_by_id("29A7724B47ABEE7B3C9DC347E13A50B4")

    # act
    my_role_members = my_group.members_by_role(my_role)

    # assert
    assert my_role_members[0].uid == "6F63AF02CE05328153ABA477C76E6189"


def test_members_by_role__not_role_raises_type_error(
    complex_group_data: dict,
) -> None:
    """Test that TypeError is raised if `role` isn't a Role."""
    # arrange
    my_group = Group(**complex_group_data)
    subgroup_not_role = my_group.subgroup_by_id("BB6B3C3592C5FC71DBDD5258D45EF6D4")

    # act
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_role_members = my_group.members_by_role(subgroup_not_role)  # type: ignore[arg-type]
