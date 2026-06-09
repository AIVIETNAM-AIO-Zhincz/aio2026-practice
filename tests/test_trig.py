import math

import pytest

from aiolib.trig import approx_sin, factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_approx_sin_converges():
    # n càng lớn càng gần sin thật
    x = 1.0
    err_low = abs(approx_sin(x, 1) - math.sin(x))
    err_high = abs(approx_sin(x, 7) - math.sin(x))
    assert err_high < err_low
    assert approx_sin(x, 10) == pytest.approx(math.sin(x), abs=1e-6)


def test_approx_sin_n0_is_linear():
    assert approx_sin(2.0, 0) == 2.0
