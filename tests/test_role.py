"""Tests for Role class."""

from spond_classes.role import Role


def test_from_dict(simple_role_data: dict) -> None:
    """Test that Event is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_role = Role(**simple_role_data)

    assert my_role.uid == "001"
    assert my_role.name == "My role"
    assert str(my_role) == "Role 'My role'"
