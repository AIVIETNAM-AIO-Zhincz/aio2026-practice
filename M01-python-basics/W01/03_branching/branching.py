"""
AIO2026 M01W01 - Basic Python (Branching) — 03/06/2026
Biến, hàm, rẽ nhánh if-elif-else; ví dụ ReLU.
"""


def relu(x: float) -> float:
    """Rectified Linear Unit: giữ giá trị dương, ép âm về 0."""
    result = 0.0
    if x > 0:
        result = x
    return result


def classify(score: float) -> str:
    """Phân loại điểm bằng if-elif-else."""
    if score >= 8:
        return "Giỏi"
    elif score >= 6.5:
        return "Khá"
    elif score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


if __name__ == "__main__":
    data = [1, 5, -4, 3, -2]
    print("ReLU:", [relu(x) for x in data])  # [1, 5, 0.0, 3, 0.0]
    print(classify(7.0))  # Khá
