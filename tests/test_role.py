"""Tests for Role class."""


from spond_classes import Role
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that Role is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_role = Role("001", "My role")
    valid_attributes = [
        "uid",
        "members",
        "name",
    ]
    assert sets_equal(public_attributes(my_role), valid_attributes)

    assert my_role.uid == "001"
    assert my_role.members == []
    assert my_role.name == "My role"
    assert str(my_role) == "Role 'My role'"


def test_from_dict(role_data: dict) -> None:
    """Test that Event is created from dict.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_role = Role.from_dict(role_data)
    valid_attributes = [
        "uid",
        "members",
        "name",
    ]
    assert sets_equal(public_attributes(my_role), valid_attributes)

    assert my_role.uid == "001"
    assert my_role.members == []
    assert my_role.name == "My role"
    assert str(my_role) == "Role 'My role'"
