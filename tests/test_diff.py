from diff import *


def test_both_empty_returns_empty():
    assert diff("", "") == ""


def test_identical_old_and_new_returns_0_prepended():
    old = "a"
    new = "a"
    assert diff(old, new) == "0 a"

    old = "a\nb"
    new = "a\nb"
    assert diff(old, new) == "0 a\n0 b"


def test_line_in_new_not_in_old_returns_plus_prepended():
    old = ""
    new = "a"
    assert diff(old, new) == "+ a"

    old = "a"
    new = "a\nb"
    assert diff(old, new) == "0 a\n+ b"

    old = "a"
    new = "b\na"
    assert diff(old, new) == "+ b\n0 a"


def test_line_in_old_not_in_new_returns_minus_prepended():
    old = "a"
    new = ""
    assert diff(old, new) == "- a"

    old = "a\nb"
    new = "a"
    assert diff(old, new) == "0 a\n- b"

    old = "b\na"
    new = "a"
    assert diff(old, new) == "- b\n0 a"


def test_one_cloned_lines_removed_returns_minus_prepended():
    old = "b\nb"
    new = "b"
    assert diff(old, new) == "0 b\n- b"

    old = "a\nb\nb"
    new = "a\nb"
    assert diff(old, new) == "0 a\n0 b\n- b"

    old = "b\nb\na"
    new = "b\na"
    assert diff(old, new) == "0 b\n- b\n0 a"


def test_one_cloned_line_inserted_returns_correct_plus_prepended():
    old = "b"
    new = "b\nb"
    assert diff(old, new) == "0 b\n+ b"

    old = "b\na"
    new = "b\nb\na"
    assert diff(old, new) == "0 b\n+ b\n0 a"


def test_multiple_cloned_lines_removed_returns_correct_minus_prepended():
    old = "b\nb\nb\na"
    new = "b\na"
    assert diff(old, new) == "0 b\n- b\n- b\n0 a"


def test_multiple_cloned_lines_inserted_returns_correct_plus_prepended():
    old = "b\na"
    new = "b\nb\nb\na"
    assert diff(old, new) == "0 b\n+ b\n+ b\n0 a"
