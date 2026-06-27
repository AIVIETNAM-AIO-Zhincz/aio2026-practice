"""
AIO2026 M01W04 - Streamlit App phân tích điểm số học sinh (Excel + biểu đồ tròn) — 24/06/2026

Chạy:  streamlit run student_scores_excel_app.py
File Excel đầu vào cần cột `Điểm số`.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def main() -> None:
    """Đọc file Excel điểm số, tính điểm trung bình và vẽ biểu đồ tròn xếp loại."""
    st.title("Phân tích điểm số học sinh")

    file = st.file_uploader("Tải file Excel:", type=["xlsx"])
    if file is None:
        st.info("Hãy tải lên file Excel có cột `Điểm số`.")
        return

    df = pd.read_excel(file)
    diem = df["Điểm số"].dropna()  # lấy cột điểm, bỏ ô trống

    st.metric("Điểm trung bình", round(float(diem.mean()), 2))

    loai = pd.cut(diem, [0, 6.5, 8, 10], labels=["Trung bình", "Khá", "Giỏi"])
    fig, ax = plt.subplots()
    loai.value_counts().plot.pie(autopct="%1.0f%%", ax=ax, ylabel="")
    st.pyplot(fig)


if __name__ == "__main__":
    main()
