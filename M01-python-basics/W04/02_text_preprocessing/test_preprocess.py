"""Test cho pipeline tiền xử lý văn bản (preprocess.py)."""

from preprocess import (
    normalize_unicode,
    preprocess,
    remove_punctuation,
    remove_stopwords,
    tokenize,
)


def test_normalize_unicode_nfc_nfd_equal() -> None:
    """NFD và NFC của cùng một chữ phải chuẩn hoá về cùng chuỗi."""
    import unicodedata

    nfc = "ế"
    nfd = unicodedata.normalize("NFD", nfc)
    assert nfc != nfd  # khác nhau ở mức byte
    assert normalize_unicode(nfd) == normalize_unicode(nfc)


def test_remove_punctuation_gop_khoang_trang() -> None:
    assert remove_punctuation("Tốt!!!   :)  quá") == "Tốt quá"


def test_tokenize_split_theo_khoang_trang() -> None:
    assert tokenize("toi hoc ai") == ["toi", "hoc", "ai"]


def test_remove_stopwords() -> None:
    assert remove_stopwords(["the", "cat"], frozenset({"the"})) == ["cat"]


def test_preprocess_case_thuong() -> None:
    """Pipeline đầy đủ trên câu tiếng Anh có nhiễu."""
    raw = "The cats are RUNNING quickly!!! :)"
    assert preprocess(raw) == ["cats", "running", "quickly"]


def test_preprocess_case_bien_rong() -> None:
    """Chuỗi rỗng / chỉ dấu câu → danh sách rỗng."""
    assert preprocess("") == []
    assert preprocess("!!! ???") == []
