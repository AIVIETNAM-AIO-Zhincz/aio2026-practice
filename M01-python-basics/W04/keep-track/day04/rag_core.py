"""Phần lõi RAG cho Project 1.2 — tách ra để app Streamlit và test dùng chung.

Làm theo tutorial: pypdf đọc PDF, chromadb làm vector store, ollama lo embedding + LLM.
chunk_text để riêng vì nó là phần text thuần, không cần model -> test được luôn.
"""

import pypdf

LLM_MODEL = "vicuna:7b-v1.5-q5_1"
EMBED_MODEL = "bge-m3"

PROMPT = """Bạn là trợ lý hỏi đáp. Dùng các đoạn ngữ cảnh dưới đây để trả lời câu hỏi.
Nếu ngữ cảnh không có thông tin, hãy nói là bạn không biết, đừng bịa.
Trả lời ngắn gọn, chính xác, bằng tiếng Việt.

Ngữ cảnh:
{context}

Câu hỏi: {question}

Trả lời:"""


def read_pdf(path):
    reader = pypdf.PdfReader(path)
    # or "" để trang nào chỉ có ảnh (không text) thì khỏi lỗi
    return "\n".join(p.extract_text() or "" for p in reader.pages)


def chunk_text(text, size=1000, overlap=200):
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 1 <= size:
            cur += p + "\n"
        else:
            if cur:
                chunks.append(cur.strip())
            # giữ 200 ký tự cuối của chunk trước làm phần nối, tránh cắt đứt câu
            cur = (cur[-overlap:] + p + "\n") if overlap else (p + "\n")
    if cur.strip():
        chunks.append(cur.strip())
    return chunks


def embed(texts):
    import ollama

    return ollama.embed(model=EMBED_MODEL, input=texts)["embeddings"]


def build_collection(chunks):
    import chromadb

    client = chromadb.Client()
    col = client.get_or_create_collection("rag")
    col.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embed(chunks),
    )
    return col


def retrieve(col, query, k=4):
    res = col.query(query_embeddings=embed([query]), n_results=k)
    return res["documents"][0]


def rag(col, question, k=4):
    import ollama

    context = "\n\n".join(retrieve(col, question, k))
    resp = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": PROMPT.format(context=context, question=question)}],
        options={"temperature": 0},
    )
    return resp["message"]["content"]


if __name__ == "__main__":
    chunks = chunk_text(read_pdf("./YOLOv10_Tutorials.pdf"))
    print("Số chunks:", len(chunks))
    col = build_collection(chunks)
    print(rag(col, "YOLOv10 là gì?"))
