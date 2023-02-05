""" Tests for SpondSubgroup class.

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
    my_ssg = SpondSubgroup("001", "My subgroup")
    valid_properties = [
        "uid",
        "name",
        "parent_group",
    ]
    actual_properties = list(my_ssg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_ssg.uid == "001"
    assert my_ssg.name == "My subgroup"
    assert my_ssg.parent_group is None


@pytest.fixture
def subgroup_dict():
    """Partial fragment from the 'groups' (root) -> 'group' -> 'subGroups' node.
    Represents a single subGroup."""

    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
        "name": "Subgroup A1",
    }


def test_from_dict(subgroup_dict):
    """
    Test that SpondSubgroup is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_ssg = SpondSubgroup.from_dict(subgroup_dict)
    valid_properties = [
        "uid",
        "name",
        "parent_group",
    ]
    actual_properties = list(my_ssg.__dict__.keys())
    assert sorted(actual_properties) == sorted(valid_properties)

    assert my_ssg.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_ssg.name == "Subgroup A1"
