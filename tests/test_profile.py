"""Tests for Profile class."""

from spond_classes.profile import Profile


def test_from_dict(simple_profile_data: dict) -> None:
    """Test that Profile is created from the simplest possible dict representation.

    Verify values of all attributes.
    """
    my_profile = Profile(**simple_profile_data)
    assert my_profile.uid == "364C188137AD92DC0F32E1A31A0E1731"
    assert str(my_profile) == ("Profile(uid='364C188137AD92DC0F32E1A31A0E1731')")
