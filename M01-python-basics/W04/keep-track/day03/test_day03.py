"""Test cho code Day 03. Chạy: pytest -q

Test phần không cần model: metrics, chunk_text, build_prompt, xử lý ảnh.
"""

import cv2
import numpy as np
from image_similarity import process_image, search_similar
from rag_simulation import build_prompt, chunk_text
from vector_metrics import cosine_similarity, cosine_similarity_scores, l1_distance, l2_distance


# ---------- metrics ----------
def test_l1_l2():
    assert l1_distance([0, 0], [3, 4]) == 7.0  # |0-3| + |0-4|
    assert l2_distance([0, 0], [3, 4]) == 5.0  # tam giác 3-4-5


def test_cosine():
    assert cosine_similarity([1, 0], [2, 0]) == 1.0  # cùng hướng
    assert cosine_similarity([1, 0], [0, 5]) == 0.0  # vuông góc
    assert cosine_similarity([0, 0], [1, 2]) == 0.0  # vector 0 -> 0, không ra nan


def test_cosine_scores_xep_hang():
    db = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    scores = cosine_similarity_scores([1.0, 0.0], db)
    assert np.argmax(scores) == 0  # giống dòng 0 nhất


# ---------- ảnh ----------
def _viet_anh(path, value, size=(10, 10)):
    cv2.imwrite(str(path), np.full(size, value, dtype=np.uint8))


def test_process_image_chuan_hoa(tmp_path):
    p = tmp_path / "trang.png"
    _viet_anh(p, 255)
    vec = process_image(str(p), size=(8, 8))
    assert vec.shape == (64,)  # 8x8 duỗi phẳng
    assert vec[0] == 1.0  # pixel 255 -> 1.0


def test_search_tim_dung_anh_giong_nhat(tmp_path):
    ds = tmp_path / "data"
    ds.mkdir()
    _viet_anh(ds / "den.png", 0)
    _viet_anh(ds / "xam.png", 128)
    _viet_anh(ds / "trang.png", 255)
    query = tmp_path / "q.png"
    _viet_anh(query, 130)  # gần xám (128) nhất
    kq = search_similar(str(query), str(ds), size=(8, 8), metric="l2", top_k=1)
    assert kq[0][0] == "xam.png"


# ---------- rag ----------
def test_chunk_text():
    text = " ".join(str(i) for i in range(10))  # "0 1 2 ... 9"
    chunks = chunk_text(text, chunk_size=4, overlap=1)
    assert chunks[0] == "0 1 2 3"
    assert chunks[1].startswith("3")  # gối đầu 1 từ
    assert chunk_text("") == []


def test_build_prompt():
    p = build_prompt("AIO2026 có gì?", ["Khóa AIO2026 gồm 10 module."])
    assert "Ngữ cảnh:" in p and "Câu hỏi:" in p
    assert "Khóa AIO2026 gồm 10 module." in p
