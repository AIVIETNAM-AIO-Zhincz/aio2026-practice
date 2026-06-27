# KEEP TRACK — Module 01 (W04)

Code trong thử thách cá nhân **KEEP TRACK** (AIO2026 M01) — mỗi ngày một bài. Notes lý thuyết để ở Obsidian vault, đây là phần code chạy được.

## day03 — Vector Database, RAG & tìm ảnh tương đồng
- `vector_metrics.py` — L1 / L2 / cosine.
- `image_similarity.py` — ảnh → vector → tìm ảnh giống nhất (OpenCV).
- `rag_simulation.py` — mô phỏng RAG: chunk → embed → retrieve (cosine) → dựng prompt.
- `test_day03.py` · `Data/` (ảnh mẫu) · `AIO2026_M01_Day03_Colab.ipynb`.

## day04 — Project 1.2: Chatbot RAG hỏi đáp PDF
- `rag_core.py` — pipeline lõi (pypdf + ChromaDB + Ollama).
- `chatbot_app.py` — app Streamlit (upload PDF + hỏi đáp).
- `test_day04.py` · `README.md` · `AIO2026_M01_Day04_Colab.ipynb`.

## Chạy test
```bash
pip install -r day03/requirements.txt -r day04/requirements.txt
# -o addopts="" để bỏ gate coverage của aiolib (cấu hình ở pyproject gốc)
pytest day03/test_day03.py day04/test_day04.py -o addopts=""
```
