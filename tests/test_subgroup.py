"""Tests for Subgroup class."""

from spond_classes import Subgroup


def test_from_dict(simple_subgroup_data: dict) -> None:
    """Test that a Subgroup is created from the simplest possible
    dict representation.
    """
    my_subgroup = Subgroup.from_dict(simple_subgroup_data)

    assert my_subgroup.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_subgroup.name == "Subgroup A1"
    assert (
        my_subgroup.members == []
    )  # Tested as part of complex Group, as it relies on full Group data.
    assert str(my_subgroup) == "Subgroup 'Subgroup A1'"
