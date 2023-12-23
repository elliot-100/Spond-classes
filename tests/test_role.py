"""Tests for Role class."""

from spond_classes import Role


def test_from_dict(simple_role_data: dict) -> None:
    """Test that Event is created from dict.

    Verify values of all attributes.
    """
    my_role = Role.from_dict(simple_role_data)

    assert my_role.uid == "001"
    assert (
        my_role.members == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert my_role.name == "My role"
    assert str(my_role) == "Role 'My role'"
