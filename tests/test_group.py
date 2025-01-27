"""Tests for Group class."""

import pytest

from spond_classes import Group
from spond_classes.types_ import DictFromJSON


@pytest.fixture
def simple_group_data() -> DictFromJSON:
    """Simplest possible group data in this implementation.

    Mocks dict returned by `Spond.get_group()` or `Spond.get_groups()[n].`
    """
    return {
        "id": "G1",
        "name": "Group One",
        "members": [],  # assumed always exists, may be empty
        "roles": [],  # assumed always exists, may be empty
        "subGroups": [],  # assumed always exists, may be empty
    }


@pytest.fixture
def complex_group_data() -> DictFromJSON:
    """Group data with all implemented fields populated.

    Mocks dict returned by `Spond.get_group()` or `Spond.get_groups()[n].`

    The Member is in the Subgroup, and has the Role.
    """
    return {
        "id": "G2",
        "name": "Group Two",
        "members": [
            {
                "id": "G2M1",
                "createdTime": "2022-03-24T16:36:29Z",
                "email": "brendan@example.com",
                "firstName": "Brendan",
                "lastName": "Gleason",
                "phoneNumber": "+123456789",
                # optional:
                "profile": {
                    "id": "G2M1P1",
                    "firstName": "Bren",
                    "lastName": "Gleason",
                    # optional:
                    "email": "brendan-home@example.com",
                    "phoneNumber": "+123456791",
                },
                "roles": ["G2R1"],
                "subGroups": ["G2S1"],
            },
        ],
        "roles": [
            {
                "id": "G2R1",
                "name": "Role B2",
            },
        ],
        "subGroups": [
            {
                "id": "G2S1",
                "name": "Subgroup B1",
            },
        ],
    }


def test_from_dict_simple(simple_group_data: DictFromJSON) -> None:
    """Test that Group is created from the simplest possible data."""
    # arrange
    # act
    my_group = Group.from_dict(simple_group_data)
    # assert
    assert my_group.uid == "G1"
    assert my_group.name == "Group One"
    assert my_group.members == []
    assert my_group.roles == []
    assert my_group.subgroups == []
    assert str(my_group) == "Group(uid='G1', name='Group One', …)"


def test_from_dict_with_member_role_subgroup(complex_group_data: DictFromJSON) -> None:
    """Test that subordinate Member, Role, Subgroup are created from dict."""
    # arrange
    # act
    my_group = Group.from_dict(complex_group_data)
    # assert
    assert my_group.uid == "G2"
    assert my_group.members[0].uid == "G2M1"
    assert my_group.roles[0].uid == "G2R1"
    assert my_group.subgroups[0].uid == "G2S1"


def test_member_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that subordinate Member is returned from a valid uid."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # act
    my_member = my_group.member_by_id("G2M1")
    # assert
    assert my_member.uid == "G2M1"


def test_member_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there is no matching subordinate Member."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_member = my_group.member_by_id("DUMMY_ID")  # act


def test_member_by_id__no_members_raises_lookup_error(
    simple_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there are no subordinate Members."""
    # arrange
    my_group = Group.from_dict(simple_group_data)
    # assert
    assert my_group.members == []
    with pytest.raises(LookupError):
        my_member = my_group.member_by_id("DUMMY_ID")  # act


def test_role_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that subordinate Role is returned from a valid uid."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # act
    my_role = my_group.role_by_id("G2R1")
    # assert
    assert my_role.uid == "G2R1"


def test_role_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there is no matching subordinate Role."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_role = my_group.role_by_id("DUMMY_ID")  # act


def test_role_by_id__no_roles_raises_lookup_error(
    simple_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there are no subordinate Roles."""
    # arrange
    my_group = Group.from_dict(simple_group_data)
    # assert
    assert my_group.roles == []
    with pytest.raises(LookupError):
        my_role = my_group.role_by_id("DUMMY_ID")  # act


def test_subgroup_by_id__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that subordinate Subgroup is returned from a valid uid."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # act
    my_subgroup = my_group.subgroup_by_id("G2S1")
    # assert
    assert my_subgroup.uid == "G2S1"


def test_subgroup_by_id__unmatched_id_raises_lookup_error(
    complex_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there is no matching
    subordinate Subgroup.
    """
    # arrange
    my_group = Group.from_dict(complex_group_data)
    # assert
    with pytest.raises(LookupError):
        my_subgroup = my_group.subgroup_by_id("DUMMY_ID")  # act


def test_subgroup_by_id__no_subgroups_raises_lookup_error(
    simple_group_data: DictFromJSON,
) -> None:
    """Test that LookupError is raised when there are no subordinate Subgroups."""
    # arrange
    my_group = Group.from_dict(simple_group_data)
    # assert
    assert my_group.subgroups == []
    with pytest.raises(LookupError):
        my_subgroup = my_group.subgroup_by_id("DUMMY_ID")  # act


def test_members_by_subgroup__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Members are returned from a valid subordinate Subgroup."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
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
    my_group = Group.from_dict(complex_group_data)
    role_not_subgroup = my_group.role_by_id("G2R1")
    # assert
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_subgroup_members = my_group.members_by_subgroup(
            role_not_subgroup  # type: ignore[arg-type]
        )


def test_members_by_role__happy_path(complex_group_data: DictFromJSON) -> None:
    """Test that Members are returned from a valid subordinate Role."""
    # arrange
    my_group = Group.from_dict(complex_group_data)
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
    my_group = Group.from_dict(complex_group_data)
    subgroup_not_role = my_group.subgroup_by_id("G2S1")
    # act
    with pytest.raises(TypeError):
        # Ignore Mypy error - test purposely passes incompatible type
        my_role_members = my_group.members_by_role(
            subgroup_not_role  # type: ignore[arg-type]
        )
