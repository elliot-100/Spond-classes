"""Tests for Profile class."""

from spond_classes.profile import Profile

from . import DictFromJSON


def test_from_dict(simple_profile_data: DictFromJSON) -> None:
    """Test that Profile is created from the simplest possible data dict."""
    # arrange
    # act
    my_profile = Profile.model_validate(simple_profile_data)
    # assert
    assert my_profile.uid == "P1"
    assert str(my_profile) == "Profile(uid='P1')"
