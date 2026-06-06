"""Ước lượng hàm lượng giác bằng chuỗi Taylor — TA-Exercise M01W01."""


def factorial(k: int) -> int:
    """Tính k! = 1*2*...*k (0! = 1! = 1)."""
    result = 1
    for j in range(2, k + 1):
        result *= j
    return result


def approx_sin(x: float, n: int) -> float:
    """Xấp xỉ sin(x) bằng (n+1) số hạng đầu của chuỗi Taylor.

    sin(x) ≈ sum_{i=0}^{n} (-1)^i * x^(2i+1) / (2i+1)!
    n càng lớn càng chính xác.
    """
    total = 0.0
    for i in range(n + 1):
        total += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return total
