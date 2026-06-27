"""
AIO2026 M01W04 - Streamlit App phân tích điểm số học sinh — 24/06/2026

Chạy:  streamlit run student_scores_app.py
File CSV đầu vào cần 2 cột: `ten`, `diem`.
"""

import pandas as pd
import streamlit as st


def xep_loai(diem: float) -> str:
    """Xếp loại học lực theo điểm: >=8 Giỏi, >=6.5 Khá, còn lại Trung bình."""
    if diem >= 8:
        return "Giỏi"
    if diem >= 6.5:
        return "Khá"
    return "Trung bình"


def main() -> None:
    """Giao diện Streamlit: tải CSV điểm → bảng, biểu đồ, thống kê."""
    st.title("Phân tích điểm số học sinh")

    file = st.file_uploader("Tải file CSV (cột: ten, diem):", type=["csv"])
    if file is None:
        st.info("Hãy tải lên file CSV có cột `ten` và `diem`.")
        return

    df = pd.read_csv(file)
    df["xep_loai"] = df["diem"].apply(xep_loai)

    st.dataframe(df)
    st.bar_chart(df.set_index("ten")["diem"])

    c1, c2, c3 = st.columns(3)
    c1.metric("Sĩ số", len(df))
    c2.metric("Điểm TB", round(float(df["diem"].mean()), 2))
    c3.metric("Cao nhất", float(df["diem"].max()))


if __name__ == "__main__":
    main()
