"""Mô phỏng cơ chế RAG (Day 03).

3 bước: Indexing (văn bản -> vector) -> Retrieval (chọn đoạn gần nhất bằng cosine)
-> Generation (nhét ngữ cảnh vào prompt cho LLM trả lời có căn cứ).

Embedding dùng sentence-transformers (mô hình tiếng Việt), load khi chạy thật.
"""

import numpy as np
from vector_metrics import cosine_similarity_scores


def chunk_text(text, chunk_size=50, overlap=10):
    """Cắt văn bản thành đoạn ~chunk_size TỪ, gối đầu overlap từ giữa 2 đoạn."""
    words = text.split()
    if not words:
        return []
    step = chunk_size - overlap
    chunks = []
    for i in range(0, len(words), step):
        chunks.append(" ".join(words[i : i + chunk_size]))
        if i + chunk_size >= len(words):  # đã lấy hết từ thì dừng, khỏi tạo đoạn rỗng
            break
    return chunks


def embed(texts, model=None):
    """Encode list văn bản thành vector. Không truyền model thì tự load sbert tiếng Việt."""
    if model is None:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("keepitreal/vietnamese-sbert")
    return np.asarray(model.encode(texts))


def retrieve(query, documents, vector_db, model=None, top_k=1):
    """Trả về top_k (tài liệu, điểm cosine) liên quan nhất tới câu hỏi."""
    q = embed([query], model)[0]
    scores = cosine_similarity_scores(q, vector_db)
    idx = np.argsort(scores)[::-1][: min(top_k, len(documents))]  # clamp top_k
    return [(documents[i], float(scores[i])) for i in idx]


def build_prompt(query, contexts):
    """Ghép ngữ cảnh đã tìm được vào khung prompt, buộc trả lời theo ngữ cảnh."""
    ctx = "\n".join(f"- {c}" for c in contexts)
    return (
        "Dựa vào ngữ cảnh dưới đây để trả lời câu hỏi.\n"
        "Không dùng thông tin bên ngoài. Nếu ngữ cảnh không đủ, trả lời 'Không đủ thông tin'.\n\n"
        f"Ngữ cảnh:\n{ctx}\n\nCâu hỏi: {query}\nTrả lời:"
    )


if __name__ == "__main__":
    documents = [
        "Khóa học AIO2026 gồm có 10 module chuyên sâu về Trí tuệ Nhân tạo.",
        "Tài liệu hướng dẫn thủ tục đăng ký nhập học và đóng học phí trực tuyến.",
        "Hướng dẫn cấu trúc dữ liệu và giải thuật với Python để xử lý mảng.",
    ]
    vector_db = embed(documents)
    query = "Khóa học AIO2026 có bao nhiêu phần?"
    contexts = [doc for doc, _ in retrieve(query, documents, vector_db)]
    print(build_prompt(query, contexts))
