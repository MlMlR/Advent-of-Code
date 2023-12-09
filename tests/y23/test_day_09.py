import pytest
from src.y23.day_09 import part1, part2, previous

def test_part1():
    data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    ]
    res = part1(data)
    assert res == 114

def test_part2():
    data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    ]
    res = part2(data)
    assert res == 2

def test_previous():
    data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45]
    ]
    res = previous(data[0])
    assert res == -3
    res = previous(data[1])
    assert res == 0
    res = previous(data[2])
    assert res == 5