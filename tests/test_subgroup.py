"""Tests for Subgroup class."""

from spond_classes import Subgroup

from . import DictFromJSON


def test_from_dict(simple_subgroup_data: DictFromJSON) -> None:
    """Test that Subgroup is created from the simplest possible data dict."""
    # arrange
    # act
    my_subgroup = Subgroup.model_validate(simple_subgroup_data)
    # assert
    assert my_subgroup.uid == "S1"
    assert my_subgroup.name == "Subgroup One"
    assert str(my_subgroup) == "Subgroup(uid='S1', name='Subgroup One')"
