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


@pytest.fixture
def complex_profile_data() -> DictFromJSON:
    """Profile data with all implemented fields populated.

    Mocks dict returned by `Spond.get_group()['members'][n][profile]`.
    """
    return {
        "id": "P2",
        "firstName": "Salma",
        "lastName": "Hayek",
        "email": "s_hayek@example.com",
        "phoneNumber": "+123456790",
    }


def test_from_dict(simple_profile_data: DictFromJSON) -> None:
    """Test that Profile is created from the simplest possible data dict."""
    # arrange
    # act
    my_profile = Profile(**simple_profile_data)
    # assert
    assert my_profile.uid == "P1"
    assert str(my_profile) == "Profile(uid='P1', full_name='Morgan Freeman', …)"


def test_from_dict_additional_fields(complex_profile_data: DictFromJSON) -> None:
    """Test that Profile can be created with additional supported data."""
    # arrange
    # act
    my_profile = Profile(**complex_profile_data)
    # assert
    # - optional:
    assert my_profile.email == "s_hayek@example.com"
    assert my_profile.phone_number == "+123456790"
