"""Tests for Role class."""

from spond_classes import Role

from . import DictFromJSON


def test_from_dict(simple_role_data: DictFromJSON) -> None:
    """Test that Role is created from the simplest possible data dict."""
    # arrange
    # act
    my_role = Role(**simple_role_data)
    # assert
    assert my_role.uid == "R1"
    assert my_role.name == "Role One"
    assert str(my_role) == "Role(uid='R1', name='Role One')"
