"""
AIO2026 M01W04 - NLP App Streamlit tiền xử lý văn bản — 24/06/2026

Chạy:  streamlit run preprocessing_app.py
Dùng lại pipeline thuần ở preprocess.py, ghép stopword tiếng Anh từ nltk.
"""

import nltk
import streamlit as st
from nltk.corpus import stopwords
from preprocess import preprocess


@st.cache_resource
def load_stopwords() -> frozenset[str]:
    """Tải bộ stopword tiếng Anh của nltk (1 lần, cache lại)."""
    nltk.download("stopwords", quiet=True)
    return frozenset(stopwords.words("english"))


def main() -> None:
    """Giao diện nhập văn bản → làm sạch → hiển thị token."""
    st.title("Tiền xử lý văn bản (NLP)")

    sw = load_stopwords()
    raw = st.text_area("Dán văn bản (hoặc nối từ bước web scraping):")

    if st.button("Làm sạch") and raw.strip():
        tokens = preprocess(raw, sw)
        st.subheader("Token sạch")
        st.write(tokens)
        st.metric("Số token", len(tokens))


if __name__ == "__main__":
    main()
