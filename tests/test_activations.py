import math

import pytest

from aiolib.activations import calculate_activation_function, elu, relu, sigmoid


def test_sigmoid_sample():
    assert round(sigmoid(2), 2) == 0.88


def test_sigmoid_zero():
    assert sigmoid(0) == pytest.approx(0.5)


def test_relu_positive_and_negative():
    assert relu(5) == 5.0
    assert relu(-3) == 0.0
    assert relu(0) == 0.0


def test_elu_negative_sample():
    assert round(elu(-1), 2) == -0.01


def test_elu_positive_is_identity():
    assert elu(3) == 3


def test_dispatch_known_and_unknown():
    assert round(calculate_activation_function(3, "sigmoid"), 2) == 0.95
    assert calculate_activation_function(3, "tanh") is None


def test_sigmoid_matches_math():
    assert sigmoid(1) == pytest.approx(1 / (1 + math.exp(-1)))
