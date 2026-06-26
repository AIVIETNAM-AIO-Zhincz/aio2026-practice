"""Test pytest cho bài luyện tập Recursion."""

import pytest
from recursion import factorial, fib, power, sum_to_n


def test_factorial_thuong():
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_bien():
    assert factorial(0) == 1


def test_factorial_am():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fib_thuong():
    assert fib(2) == 1
    assert fib(6) == 8
    assert fib(10) == 55


def test_fib_bien():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_am():
    with pytest.raises(ValueError):
        fib(-1)


def test_sum_to_n_thuong():
    assert sum_to_n(5) == 15
    assert sum_to_n(100) == 5050


def test_sum_to_n_bien():
    assert sum_to_n(0) == 0


def test_power_thuong():
    assert power(2, 10) == 1024
    assert power(5, 3) == 125


def test_power_bien():
    assert power(2, 0) == 1
