"""Mấy hàm đo khoảng cách / độ giống giữa 2 vector (Day 03).

Dùng chung cho bài tìm ảnh tương đồng và bài mô phỏng RAG.
"""

import numpy as np


def l1_distance(v1, v2):
    """L1 (Manhattan) = tổng |hiệu|. Nhỏ = giống."""
    v1, v2 = np.asarray(v1, float), np.asarray(v2, float)
    return float(np.sum(np.abs(v1 - v2)))


def l2_distance(v1, v2):
    """L2 (Euclid) = độ dài đường thẳng giữa 2 vector. Nhỏ = giống."""
    v1, v2 = np.asarray(v1, float), np.asarray(v2, float)
    return float(np.linalg.norm(v1 - v2))


def cosine_similarity(v1, v2):
    """Cos góc giữa 2 vector, trong [-1, 1]. Gần 1 = giống."""
    v1, v2 = np.asarray(v1, float), np.asarray(v2, float)
    na, nb = np.linalg.norm(v1), np.linalg.norm(v2)
    if na == 0 or nb == 0:  # vector 0 -> góc không xác định, coi như không giống
        return 0.0
    return float(np.dot(v1, v2) / (na * nb))


def cosine_similarity_scores(query_vec, db_matrix):
    """Cosine của 1 vector query với từng dòng của ma trận. Dùng cho bước retrieve."""
    q = np.asarray(query_vec, float)
    db = np.asarray(db_matrix, float)
    if db.shape[0] == 0:
        return np.empty(0)
    denom = np.linalg.norm(db, axis=1) * np.linalg.norm(q)
    denom[denom == 0] = 1e-10  # tránh chia 0
    return db @ q / denom
