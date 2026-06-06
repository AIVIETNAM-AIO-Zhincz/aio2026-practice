"""Hàm kích hoạt (activation functions) — TA-Exercise M01W01.

Gồm sigmoid, ReLU, ELU và một hàm điều phối theo tên.
"""

import math


def sigmoid(x: float) -> float:
    """Sigmoid: 1 / (1 + e^(-x)), nén giá trị về khoảng (0, 1)."""
    return 1.0 / (1.0 + math.exp(-x))


def relu(x: float) -> float:
    """ReLU = max(0, x): giữ giá trị dương, ép âm về 0."""
    return float(x) if x > 0 else 0.0


def elu(x: float, alpha: float = 0.01) -> float:
    """ELU: x nếu x >= 0; alpha * (e^x - 1) nếu x < 0."""
    return x if x >= 0 else alpha * (math.exp(x) - 1)


def calculate_activation_function(x: float, act_name: str) -> float | None:
    """Tính hàm kích hoạt theo tên. Trả None nếu act_name không hợp lệ."""
    funcs = {"sigmoid": sigmoid, "relu": relu, "elu": elu}
    func = funcs.get(act_name)
    return func(x) if func is not None else None
