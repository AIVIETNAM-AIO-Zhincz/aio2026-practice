"""Test cho ngram_lm. Chạy: pytest -q"""

import pytest
from ngram_lm import build_model, generate, next_token_probs, predict_next, tokenize

TOKENS = tokenize("a b c a b d a b c")  # "a b" theo sau bởi c, c, d


def test_tokenize():
    assert tokenize("Tích Tiểu  thành") == ["tích", "tiểu", "thành"]


def test_build_va_dem_dung():
    model = build_model(TOKENS, n=3)  # ngữ cảnh 2 từ
    # sau "a b": c xuất hiện 2 lần, d 1 lần
    assert model[("a", "b")] == {"c": 2, "d": 1}


def test_next_token_probs_sap_xep_va_tong_1():
    model = build_model(TOKENS, n=3)
    probs = next_token_probs(model, ["a", "b"])
    assert probs[0] == ("c", pytest.approx(2 / 3))  # cao nhất đứng đầu
    assert sum(p for _, p in probs) == pytest.approx(1.0)


def test_predict_next_chon_cao_nhat():
    model = build_model(TOKENS, n=3)
    assert predict_next(model, ["a", "b"]) == "c"


def test_ngu_canh_la_tra_none():
    model = build_model(TOKENS, n=3)
    assert predict_next(model, ["x", "y"]) is None
    assert next_token_probs(model, ["x", "y"]) == []


def test_n_nho_hon_2_raise():
    with pytest.raises(ValueError):
        build_model(TOKENS, n=1)


def test_generate_dung_lai_khi_ngu_canh_la():
    model = build_model(tokenize("a b c d"), n=2)  # chuỗi tuyến tính, ngữ cảnh 1 từ
    # a->b->c->d, tới "d" không còn từ kế -> dừng dù xin tới 10 từ
    assert generate(model, ["a"], length=10) == ["a", "b", "c", "d"]
