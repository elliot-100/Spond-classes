"""Tests for Profile class."""

import pytest

from spond_classes import Profile
from spond_classes.types import DictFromJSON


@pytest.fixture
def simple_profile_data() -> DictFromJSON:
    """Simplest possible profile data in this implementation.

    Mocks dict returned by `Spond.get_group()['members'][n][profile]`.
    """
    return {
        "id": "P1",
        "firstName": "Morgan",
        "lastName": "Freeman",
    }


def test_from_dict(simple_profile_data: DictFromJSON) -> None:
    """Test that Profile is created from the simplest possible data dict."""
    # arrange
    # act
    my_profile = Profile(**simple_profile_data)
    # assert
    assert my_profile.uid == "P1"
    assert str(my_profile) == "Profile(uid='P1', full_name='Morgan Freeman', …)"
