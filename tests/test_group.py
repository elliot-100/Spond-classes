"""Tests for Group class."""

from spond_classes import Group
from tests.utils import public_attributes, sets_equal


def test_from_dict(simple_group_data: dict) -> None:
    """Test that a Group is created from the simplest possible dict representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    valid_attributes = [
        "uid",
        "name",
        "members",
        "subgroups",
        "roles",
    ]
    # act
    my_group = Group.core_from_dict(simple_group_data)

    assert sets_equal(public_attributes(my_group), valid_attributes)
    assert my_group.uid == "20EA715745389FCDED2C280A8ACB74A6"
    assert my_group.name == "Group A"
    assert (
        my_group.members == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert (
        my_group.roles == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert (
        my_group.subgroups == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert str(my_group) == "Group 'Group A'"
