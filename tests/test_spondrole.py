"""Tests for SpondRole class."""

import pytest

from spond_classes import SpondRole
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that SpondRole is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_role = SpondRole("001", "My role")
    valid_attributes = [
        "uid",
        "members",
        "name",
    ]
    assert sets_equal(public_attributes(my_role), valid_attributes)

    assert my_role.uid == "001"
    assert my_role.members == []
    assert my_role.name == "My role"
    assert str(my_role) == "[SpondRole 'My role']"


@pytest.fixture()
def role_dict():
    """Represent the simplest possible Role in this implementation.

    Item from 'groups' (root) -> 'roles'.
    """
    return {
        "id": "001",
        "name": "My role",
    }


def test_from_dict(role_dict):
    """Test that SpondEvent is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_role = SpondRole.from_dict(role_dict)
    valid_attributes = [
        "uid",
        "members",
        "name",
    ]
    assert sets_equal(public_attributes(my_role), valid_attributes)

    assert my_role.uid == "001"
    assert my_role.members == []
    assert my_role.name == "My role"
    assert str(my_role) == "[SpondRole 'My role']"
