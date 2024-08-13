"""Tests for Group class."""

import pytest

from spond_classes import Group

from . import DictFromJSON


def test_from_dict_simple(simple_group_data: DictFromJSON) -> None:
    """Test that Group is created from the simplest possible data."""
    # arrange
    # act
    my_group = Group.model_validate(simple_group_data)
    # assert
    assert my_group.uid == "G1"
    assert my_group.name == "Group One"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "Group(uid='G1', name='Group One', …)"


def test_from_dict_with_member_role_subgroup(complex_group_data: DictFromJSON) -> None:
    """Test that nested Member, Role, Subgroup are created from dict."""
    # arrange
    # act
    my_group = Group.model_validate(complex_group_data)
    # assert
    assert my_group.uid == "G2"
    assert my_group.members[0].uid == "G2M1"
    assert my_group.roles[0].uid == "G2R1"
    assert my_group.subgroups[0].uid == "G2S1"


def test_member_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Member is returned from a valid uid."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # act
    my_member = my_group.member_by_id("G2M1")
    # assert
    assert my_member.uid == "G2M1"


def test_member_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when uid can't be matched against a Member."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_member = my_group.member_by_id("DUMMY_ID")  # act


def test_role_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Role is returned from a valid uid."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # act
    my_role = my_group.role_by_id("G2R1")
    # assert
    assert my_role.uid == "G2R1"


def test_role_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when uid can't be matched against a Role."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_role = my_group.role_by_id("DUMMY_ID")  # act


def test_subgroup_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Subgroup is returned from a valid uid."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # act
    my_subgroup = my_group.subgroup_by_id("G2S1")
    # assert
    assert my_subgroup.uid == "G2S1"


def test_subgroup_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when uid can't be matched against a Subgroup."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_subgroup = my_group.subgroup_by_id("DUMMY_ID")  # act


def test_members_by_subgroup__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Members are returned from a valid Subgroup."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    my_subgroup = my_group.subgroup_by_id("G2S1")
    # act
    my_subgroup_members = my_group.members_by_subgroup(my_subgroup)
    # assert
    assert my_subgroup_members[0].uid == "G2M1"


def test_members_by_subgroup__not_subgroup_raises_type_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that TypeError is raised if `subgroup` isn't a Subgroup."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    role_not_subgroup = my_group.role_by_id("G2R1")
    # assert
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_subgroup_members = my_group.members_by_subgroup(
            role_not_subgroup  # type: ignore[arg-type]
        )


def test_members_by_role__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Members are returned from a valid Role."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    my_role = my_group.role_by_id("G2R1")
    # act
    my_role_members = my_group.members_by_role(my_role)
    # assert
    assert my_role_members[0].uid == "G2M1"


def test_members_by_role__not_role_raises_type_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that TypeError is raised if `role` isn't a Role."""
    # arrange
    my_group = Group.model_validate(complex_group_data)
    subgroup_not_role = my_group.subgroup_by_id("G2S1")
    # act
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_role_members = my_group.members_by_role(
            subgroup_not_role  # type: ignore[arg-type]
        )
