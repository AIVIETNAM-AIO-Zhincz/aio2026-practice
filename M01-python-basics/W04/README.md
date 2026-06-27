# M01W04 — Day 01: Streamlit & Text Pre-Processing (NLP)

Buổi 24/06/2026 (Project 1.1 — NLP Streamlit). 4 bài code:

## 01_streamlit
| File | Bài | Chạy |
|---|---|---|
| `student_scores_app.py` | 1. Phân tích điểm số học sinh (CSV → bảng/biểu đồ/thống kê) | `streamlit run student_scores_app.py` |
| `power_function_app.py` | 2. Tính hàm lũy thừa | `streamlit run power_function_app.py` |

## 02_text_preprocessing
| File | Bài | Chạy |
|---|---|---|
| `text_collection.py` | 3. Web scraping thu thập văn bản (requests + BeautifulSoup, dantri) | `python text_collection.py` |
| `preprocess.py` | 4. Pipeline tiền xử lý thuần (NFC → lower → bỏ dấu câu → tokenize → bỏ stopword) | `python preprocess.py` |
| `preprocessing_app.py` | 4. App Streamlit dùng pipeline trên | `streamlit run preprocessing_app.py` |
| `test_preprocess.py` | Test cho pipeline | `pytest` |

> Bài làm thêm 5 (Spelling correction + Translation) thuộc Project 1.1 — xem repo notes / `AIO2026M01 - Project 1.1`.

## Cài thư viện
```bash
pip install -r requirements.txt   # đã thêm streamlit, requests, beautifulsoup4, nltk
```
