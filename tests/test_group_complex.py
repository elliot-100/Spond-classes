"""Tests for derivations from full Group data."""

from spond_classes import Group


def test_from_dict_complex(complex_group_data: dict) -> None:
    """Test that child Member, Role, Subgroup are created from dict."""

    #act
    my_group = Group.from_dict(complex_group_data)

    # Group.members -> Member
    assert my_group.members[0].uid == "6F63AF02CE05328153ABA477C76E6189"
    # Test attributes not handled by simple Member tests
    assert my_group.members[0].roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    assert my_group.members[0].subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"

    # Group.subgroups -> Subgroup
    assert my_group.subgroups[0].uid == "BB6B3C3592C5FC71DBDD5258D45EF6D4"
    # Test attributes not handled by simple Subgroup tests
    assert my_group.subgroups[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # Group.subgroups -> Role
    assert my_group.roles[0].uid == "29A7724B47ABEE7B3C9DC347E13A50B4"
    # Test attributes not handled by simple Role tests
    assert my_group.roles[0].members[0].uid == "6F63AF02CE05328153ABA477C76E6189"

    # Assertions by inclusion
    assert my_group.members[0] in my_group.roles[0].members
    assert my_group.members[0] in my_group.subgroups[0].members
    assert my_group.subgroups[0].members[0] in my_group.members
    assert my_group.roles[0].members[0] in my_group.members

    assert my_group.roles[0] in my_group.members[0].roles
    assert my_group.roles[0] in my_group.subgroups[0].members[0].roles
    assert my_group.members[0].roles[0] in my_group.roles

    assert my_group.subgroups[0] in my_group.members[0].subgroups
    assert my_group.members[0].subgroups[0] in my_group.subgroups
