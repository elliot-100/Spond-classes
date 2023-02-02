""" Tests for SpondGroup class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

import pytest

from spond_classes import DuplicateKeyError, SpondGroup, SpondSubgroup


def test_create():
    """
    Test that SpondSubgroup is created from required fields.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    SpondGroup.instances = {}
    SpondSubgroup.instances = {}
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


def test_create_with_existing_uid():
    """
    Test that SpondSubgroup is not created, and error is raised if a SpondSubgroup exists with
    the same uid
    """
    SpondGroup.instances = {}
    SpondSubgroup.instances = {}
    dummy_group = SpondGroup("001", "Dummy group")
    SpondSubgroup("001", "My subgroup", dummy_group)
    with pytest.raises(DuplicateKeyError):
        SpondSubgroup("001", "Another subgroup", dummy_group)
    assert len(SpondSubgroup.instances) == 1


def test_by_id():
    """Test that SpondSubgroup is returned if id exists."""
    SpondGroup.instances = {}
    SpondSubgroup.instances = {}
    dummy_sg = SpondGroup("001", "Dummy group")
    my_ssg = SpondSubgroup("001", "My subgroup", dummy_sg)
    assert SpondSubgroup.by_id("001") == my_ssg


def test_by_id__negative():
    """Test that error is raised if id doesn't exist."""
    SpondGroup.instances = {}
    SpondSubgroup.instances = {}
    dummy_sg = SpondGroup("001", "Dummy group")
    SpondSubgroup("001", "My subgroup", dummy_sg)
    with pytest.raises(KeyError):
        SpondSubgroup.by_id("002")


@pytest.fixture
def subgroup_dict():
    """Partial fragment from the 'groups' (root) -> 'group' -> 'subGroups' node.
    Represents a single subGroup."""

    return {"id": "8CC576609CF3DCBC44469A799E76B22B", "name": "Subgroup A1"}


def test_from_dict(subgroup_dict):
    """
    Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    SpondGroup.instances = {}
    SpondSubgroup.instances = {}
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
    assert my_ssg.members == []
    assert my_ssg.parent_group is dummy_sg
