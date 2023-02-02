""" Tests for SpondGroup class.

Note: To generate a representative 32-character hex string ID:
    secrets.token_hex(16).upper()
"""

import pytest

from spond_classes import DuplicateKeyError, SpondGroup


def test_create():
    """
    Test that SpondGroup is created from required fields.
    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    SpondGroup.instances = {}
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


def test_create_with_existing_uid():
    """
    Test that SpondGroup is not created, and error is raised if a SpondGroup exists with
    the same uid
    """
    SpondGroup.instances = {}
    SpondGroup("001", "My group")
    with pytest.raises(DuplicateKeyError):
        SpondGroup("001", "Another group")
    assert len(SpondGroup.instances) == 1


def test_by_id():
    """Test that SpondGroup is returned if id exists."""
    SpondGroup.instances = {}
    my_sg = SpondGroup("001", "my_sg")
    assert SpondGroup.by_id("001") == my_sg


def test_by_id__negative():
    """Test that error is raised if id doesn't exist."""
    SpondGroup.instances = {}
    SpondGroup("001", "my_sg")
    with pytest.raises(KeyError):
        SpondGroup.by_id("002")


@pytest.fixture
def group_dict():
    """Partial fragment from the 'groups' (root) node.
    Represents a single Group."""

    return {
        "id": "20EA715745389FCDED2C280A8ACB74A6",
        "members": [],
        "name": "Group A",
        "subGroups": [],
    }


def test_from_dict(group_dict):
    """
    Test that SpondGroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    SpondGroup.instances = {}
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
    assert my_sg.members == []
    assert my_sg.subgroups == []
