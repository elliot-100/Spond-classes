"""Tests for Subgroup class."""


from spond_classes import Subgroup
from tests.utils import public_attributes, sets_equal


def test_create() -> None:
    """Test that Subgroup is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_subgroup = Subgroup("001", "My subgroup")
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_subgroup), valid_attributes)

    assert my_subgroup.uid == "001"
    assert my_subgroup.name == "My subgroup"
    assert my_subgroup.members == []
    assert str(my_subgroup) == "Subgroup 'My subgroup'"


def test_from_dict(simplest_subgroup_data: dict) -> None:
    """Test that a minimal Subgroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_subgroup = Subgroup.from_dict(simplest_subgroup_data)
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_subgroup), valid_attributes)

    assert my_subgroup.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_subgroup.name == "Subgroup A1"
    assert my_subgroup.members == []
    assert str(my_subgroup) == "Subgroup 'Subgroup A1'"
