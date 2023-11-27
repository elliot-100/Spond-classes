"""Tests for Role class."""

from spond_classes import Role
from tests.utils import public_attributes, sets_equal


def test_from_dict(simple_role_data: dict) -> None:
    """Test that Event is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    valid_attributes = [
        "uid",
        "members",
        "name",
    ]
    # act
    my_role = Role.from_dict(simple_role_data)

    assert sets_equal(public_attributes(my_role), valid_attributes)
    assert my_role.uid == "001"
    assert (
        my_role.members == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert my_role.name == "My role"
    assert str(my_role) == "Role 'My role'"
