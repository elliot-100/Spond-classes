"""Tests for Subgroup class."""

from collections.abc import Hashable

from spond_classes import Subgroup


def test_from_dict(simple_subgroup_data: dict) -> None:
    """Test that Subgroup is created from the simplest possible data dict."""
    # arrange
    # act
    my_subgroup = Subgroup(**simple_subgroup_data)
    # assert
    assert isinstance(my_subgroup, Hashable)
    assert my_subgroup.uid == "S1"
    assert my_subgroup.name == "Subgroup One"
    assert str(my_subgroup) == "Subgroup(uid='S1', name='Subgroup One')"
