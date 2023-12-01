import pytest
from src.y23.day_01 import part1, part2

def test_part1():
    p1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
    ]
    res = part1(p1)
    assert res == 281

def test_part2():
    p2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
    ]
    res = part2(p2)
    assert res == 122