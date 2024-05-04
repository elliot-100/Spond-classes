"""Tests for Subgroup class."""

from spond_classes import Subgroup


def test_from_dict(simple_subgroup_data: dict) -> None:
    """Test that Subgroup is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_subgroup = Subgroup(**simple_subgroup_data)

    assert my_subgroup.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_subgroup.name == "Subgroup A1"
    assert str(my_subgroup) == "Subgroup 'Subgroup A1'"
