"""Giao diện Streamlit cho RAG Chatbot hỏi đáp PDF.

Dùng lại chunk_text / embed / PROMPT bên rag_core. Chạy:
    streamlit run chatbot_app.py     (nhớ để ollama chạy sẵn)
"""

import os
import tempfile
import time

import chromadb
import ollama
import pypdf
import streamlit as st
from rag_core import LLM_MODEL, PROMPT, chunk_text, embed

# Streamlit chạy lại cả file mỗi lần tương tác -> cất state để khỏi mất
for key, val in {"collection": None, "pdf_name": "", "chat_history": []}.items():
    st.session_state.setdefault(key, val)


def process_pdf(uploaded_file):
    # file upload nằm trong RAM, pypdf cần file thật nên ghi tạm ra ổ rồi xóa
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        path = tmp.name
    text = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(path).pages)
    os.unlink(path)

    chunks = chunk_text(text)
    # tên collection theo timestamp cho khỏi đụng khi đổi file
    col = chromadb.Client().get_or_create_collection(f"rag_{int(time.time())}")
    col.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embed(chunks),
    )
    return col, len(chunks)


def rag(question, collection, k=4):
    res = collection.query(query_embeddings=embed([question]), n_results=k)
    context = "\n\n".join(res["documents"][0])
    resp = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": PROMPT.format(context=context, question=question)}],
        options={"temperature": 0},
    )
    return resp["message"]["content"]


st.set_page_config(page_title="PDF RAG Chatbot", layout="wide", initial_sidebar_state="expanded")
st.title("PDF RAG Assistant: Native")

with st.sidebar:
    st.subheader("Upload tài liệu")
    f = st.file_uploader("Chọn file PDF", type="pdf")
    if f and st.button("Xử lý PDF", use_container_width=True):
        with st.spinner("Đang xử lý..."):
            st.session_state.collection, n = process_pdf(f)
            st.session_state.pdf_name = f.name
            st.session_state.chat_history = []
        st.success(f"{n} chunks")
    st.info(st.session_state.pdf_name if st.session_state.pdf_name else "Chưa có tài liệu")
    if st.button("Xóa lịch sử chat", use_container_width=True):
        st.session_state.chat_history = []

for m in st.session_state.chat_history:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if st.session_state.collection is None:
    st.info("Upload và xử lý PDF trước khi chat.")
    st.chat_input("Nhập câu hỏi...", disabled=True)
else:
    q = st.chat_input("Nhập câu hỏi của bạn...")
    if q:
        st.session_state.chat_history.append({"role": "user", "content": q})
        with st.chat_message("user"):
            st.write(q)
        with st.chat_message("assistant"):
            with st.spinner("Đang suy nghĩ..."):
                ans = rag(q, st.session_state.collection)
            st.write(ans)
        st.session_state.chat_history.append({"role": "assistant", "content": ans})
