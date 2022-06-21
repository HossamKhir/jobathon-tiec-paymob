#! /usr/bin/env python3
from inverter import invert


def test_invert_none():
    inverted = invert(None)
    assert inverted == ""


def test_invert_empty():
    inverted = invert("")
    assert inverted == ""


def test_invert_single_character():
    string = "s"
    inverted = invert(string)
    assert inverted is string


def test_invert_long_string():
    string = "longer than one character"
    result = string[::-1]
    inverted = invert(string)
    assert inverted == result
