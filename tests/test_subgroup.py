"""Tests for Subgroup class."""

import pytest

from spond_classes import Subgroup
from spond_classes.types_ import DictFromJSON


@pytest.fixture
def simple_subgroup_data() -> DictFromJSON:
    """Simplest possible subgroup data in this implementation.

    Mocks dict returned by `Spond.get_group()['subGroups'][n]`.
    """
    return {
        "id": "S1",
        "name": "Subgroup One",
    }


def test_from_dict(simple_subgroup_data: DictFromJSON) -> None:
    """Test that Subgroup is created from the simplest possible data dict."""
    # arrange
    # act
    my_subgroup = Subgroup(**simple_subgroup_data)
    # assert
    assert my_subgroup.uid == "S1"
    assert my_subgroup.name == "Subgroup One"
    assert str(my_subgroup) == "Subgroup(uid='S1', name='Subgroup One')"
