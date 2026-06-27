"""
AIO2026 M01W04 - Streamlit App tính giai thừa — 24/06/2026

Chạy:  streamlit run factorial_app.py
Luyện widget nhập số nguyên + tách hàm xử lý khỏi giao diện.
"""

import streamlit as st


def factorial(n: int) -> int:
    """Giai thừa bằng vòng lặp nhân dồn."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main() -> None:
    """Giao diện nhập n rồi tính n!."""
    st.title("App tính giai thừa")

    n = int(st.number_input("Nhập n:", value=5, step=1, min_value=0))
    if st.button("Tính"):
        st.metric(f"{n}!", factorial(n))


if __name__ == "__main__":
    main()
