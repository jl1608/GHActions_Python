import pytest

def add_two(a: int, b: int) -> int:
    return a + b


def test_add_two():
    assert add_two(1, 2) == 3