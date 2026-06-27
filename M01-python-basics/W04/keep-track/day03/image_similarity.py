"""Tìm ảnh tương đồng với OpenCV (Day 03).

Mỗi ảnh -> ảnh xám -> resize 64x64 -> duỗi phẳng thành vector -> chuẩn hóa [0,1]
-> so khoảng cách với ảnh query. L1/L2 nhỏ nhất, hoặc cosine lớn nhất = giống nhất.
"""

import os

import cv2
from vector_metrics import cosine_similarity, l1_distance, l2_distance

SUPPORTED = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def process_image(path, size=(64, 64)):
    """Đọc 1 ảnh -> vector đặc trưng đã chuẩn hóa về [0,1]."""
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # đọc thẳng ảnh xám
    if img is None:  # file thiếu hoặc hỏng
        raise ValueError(f"Không đọc được ảnh: {path}")
    img = cv2.resize(img, size)  # đưa mọi ảnh về cùng kích thước
    return img.flatten().astype(float) / 255.0  # 2D -> 1D, pixel [0,255] -> [0,1]


def search_similar(query_path, dataset_dir, size=(64, 64), metric="l2", top_k=3):
    """Quét cả thư mục, trả về top_k (tên_file, điểm) ảnh giống ảnh query nhất."""
    fn = {"l1": l1_distance, "l2": l2_distance, "cosine": cosine_similarity}[metric]
    higher_better = metric == "cosine"  # cosine cao = giống; L1/L2 thấp = giống
    q = process_image(query_path, size)

    results = []
    for name in sorted(os.listdir(dataset_dir)):
        if not name.lower().endswith(SUPPORTED):
            continue
        try:
            v = process_image(os.path.join(dataset_dir, name), size)
        except ValueError:
            continue  # ảnh hỏng thì bỏ qua, đừng làm dừng cả vòng
        results.append((name, fn(q, v)))

    results.sort(key=lambda x: x[1], reverse=higher_better)
    return results[:top_k]


if __name__ == "__main__":
    for name, score in search_similar("Data/query.jpg", "Data/images_folder", metric="l2"):
        print(name, round(score, 4))
