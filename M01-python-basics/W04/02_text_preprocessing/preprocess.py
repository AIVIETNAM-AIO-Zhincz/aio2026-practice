"""
AIO2026 M01W04 - NLP Pipeline tiền xử lý văn bản — 24/06/2026

Các hàm thuần (pure) cho pipeline kinh điển:
    chuẩn hoá Unicode → lowercasing → bỏ dấu câu → tokenize → bỏ stopword.
Tách riêng phần logic để dễ test (xem test_preprocess.py); phần giao diện ở
preprocessing_app.py.
"""

import re
import string
import unicodedata

# Vài stopword tiếng Anh tối thiểu để demo; thực tế dùng nltk.corpus.stopwords.
DEFAULT_STOPWORDS: frozenset[str] = frozenset(
    {"the", "a", "an", "is", "are", "to", "of", "and", "in", "it"}
)


def normalize_unicode(text: str) -> str:
    """Chuẩn hoá Unicode về dạng NFC (gộp NFC/NFD nhìn-giống-nhau làm một)."""
    return unicodedata.normalize("NFC", text)


def to_lowercase(text: str) -> str:
    """Đưa toàn bộ về chữ thường (case folding)."""
    return text.lower()


def remove_punctuation(text: str) -> str:
    """Bỏ dấu câu ASCII, đồng thời gộp khoảng trắng thừa."""
    text = text.translate(str.maketrans("", "", string.punctuation))
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    """Tách văn bản thành token theo khoảng trắng (đơn giản, không cần nltk)."""
    return text.split()


def remove_stopwords(tokens: list[str], stopwords: frozenset[str]) -> list[str]:
    """Loại các token nằm trong tập stopword."""
    return [t for t in tokens if t not in stopwords]


def preprocess(text: str, stopwords: frozenset[str] = DEFAULT_STOPWORDS) -> list[str]:
    """Chạy trọn pipeline tiền xử lý, trả về danh sách token sạch."""
    text = normalize_unicode(text)
    text = to_lowercase(text)
    text = remove_punctuation(text)
    tokens = tokenize(text)
    return remove_stopwords(tokens, stopwords)


if __name__ == "__main__":
    raw = "The cats are RUNNING quickly!!! :)"
    print(preprocess(raw))  # ['cats', 'running', 'quickly']
