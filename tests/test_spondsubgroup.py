"""Tests for SpondSubgroup class."""

import pytest

from spond_classes import SpondSubgroup
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that SpondSubgroup is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_subgroup = SpondSubgroup("001", "My subgroup")
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_subgroup), valid_attributes)

    assert my_subgroup.uid == "001"
    assert my_subgroup.name == "My subgroup"
    assert my_subgroup.members == []
    assert str(my_subgroup) == "SpondSubgroup 'My subgroup'"


@pytest.fixture()
def simplest_subgroup_data() -> dict:
    """Represent the simplest possible Subgroup in this implementation.

    Item from 'groups' (root) -> 'group' -> 'subGroups'.
    """
    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
        "name": "Subgroup A1",
    }


def test_from_dict(simplest_subgroup_data: dict) -> None:
    """Test that a minimal SpondSubgroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_subgroup = SpondSubgroup.from_dict(simplest_subgroup_data)
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_subgroup), valid_attributes)

    assert my_subgroup.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_subgroup.name == "Subgroup A1"
    assert my_subgroup.members == []
    assert str(my_subgroup) == "SpondSubgroup 'Subgroup A1'"
