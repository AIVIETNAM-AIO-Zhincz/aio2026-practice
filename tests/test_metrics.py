import pytest

from aiolib.metrics import calculate_f1_score


def test_f1_sample():
    assert round(calculate_f1_score(tp=2, fp=4, fn=5), 2) == 0.31


def test_f1_perfect():
    assert calculate_f1_score(tp=5, fp=0, fn=0) == pytest.approx(1.0)


def test_f1_zero_tp_returns_zero():
    assert calculate_f1_score(tp=0, fp=3, fn=4) == 0.0


def test_f1_rejects_bool():
    with pytest.raises(TypeError):
        calculate_f1_score(tp=True, fp=1, fn=1)


def test_f1_rejects_non_int():
    with pytest.raises(TypeError):
        calculate_f1_score(tp=2.0, fp=1, fn=1)


def test_f1_rejects_negative():
    with pytest.raises(ValueError):
        calculate_f1_score(tp=-1, fp=1, fn=1)
