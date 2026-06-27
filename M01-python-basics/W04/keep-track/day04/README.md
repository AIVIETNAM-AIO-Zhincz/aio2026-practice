# Day 04 — Project 1.2: RAG Chatbot hỏi đáp PDF

Chatbot trả lời câu hỏi dựa trên nội dung 1 file PDF, làm theo tutorial bằng `pypdf` + `chromadb` + `ollama` + `streamlit`.

Pipeline: `PDF → chunk → embedding → vector DB → retrieve → prompt → LLM → answer`

## File
- `rag_core.py` — các hàm lõi: `read_pdf`, `chunk_text`, `embed`, `build_collection`, `retrieve`, `rag`. Chạy thẳng được (`python rag_core.py`).
- `chatbot_app.py` — app Streamlit (upload PDF + hỏi đáp + lưu lịch sử), dùng lại hàm bên `rag_core`.
- `test_day04.py` — test `chunk_text` + `PROMPT` (phần không cần model).

## Chạy
```bash
pip install -r requirements.txt
# cài Ollama (ollama.com) rồi:
ollama pull bge-m3
ollama pull vicuna:7b-v1.5-q5_1

pytest -q                       # test (không cần Ollama)
streamlit run chatbot_app.py    # app web, mở http://localhost:8501
```

## Tham số hay chỉnh
- `size` (chunk_size, mặc định 1000): nhỏ quá thiếu ngữ cảnh, to quá lẫn nhiễu.
- `overlap` (200, ~20%): giữ ngữ cảnh ở ranh giới 2 chunk.
- `k` (4): số đoạn đưa cho LLM.
- `temperature` (0): để ổn định, hợp hỏi đáp.

## Lỗi hay gặp
- Tổng ký tự ≈ 0 → PDF là ảnh scan, cần OCR.
- Bot bịa dù context có → siết prompt "đừng bịa", đổi model, để `temperature=0`.
- `ollama` lỗi kết nối → chưa chạy `ollama serve` hoặc chưa pull model.
- Chạy chậm → máy không có GPU, thử model nhẹ (`qwen2.5:3b`, `nomic-embed-text`).

## Nâng cấp
- `chromadb.PersistentClient(path="./chroma_db")` để khỏi embedding lại.
- Hiện nguồn: in các chunk context kèm câu trả lời.
- Hybrid Search: BM25 + cosine.
