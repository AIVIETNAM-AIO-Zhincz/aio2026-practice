"""
AIO2026 M01W04 - Streamlit App tính hàm lũy thừa — 24/06/2026

Chạy:  streamlit run power_function_app.py
Luyện widget nhập số (st.number_input) + nút bấm (st.button).
"""

import streamlit as st


def power(base: float, exponent: int) -> float:
    """Tính lũy thừa base^exponent."""
    return base**exponent


def main() -> None:
    """Giao diện Streamlit nhập cơ số & số mũ rồi tính lũy thừa."""
    st.title("App tính hàm lũy thừa")

    base = st.number_input("Cơ số a:", value=2.0)
    exponent = int(st.number_input("Số mũ n:", value=10, step=1))

    if st.button("Tính"):
        st.metric(f"{base} ^ {exponent}", power(base, exponent))


if __name__ == "__main__":
    main()
