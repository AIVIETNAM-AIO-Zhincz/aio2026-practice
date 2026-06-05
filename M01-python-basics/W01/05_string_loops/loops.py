"""
AIO2026 M01W01 - Basic Python (String and Loops) — 05/06/2026
Vòng lặp for/while, biến tích luỹ, các ví dụ ước lượng.
"""
import math


def estimate_pi_leibniz(n=1000):
    """Ước lượng Pi bằng chuỗi Gregory-Leibniz."""
    pi = 0
    for i in range(1, n):
        pi += (-1) ** (i + 1) / (2 * i - 1)
    return pi * 4


def estimate_e(n=20):
    """Ước lượng số e = 1 + 1/1! + 1/2! + ... + 1/n!"""
    e, fact = 1.0, 1
    for i in range(1, n + 1):
        fact *= i
        e += 1 / fact
    return e


def sqrt_newton(a, n=5):
    """Căn bậc hai bằng phương pháp Newton."""
    result = a / 2.0
    for _ in range(n):
        result = (result + a / result) / 2.0
    return result


def factorial(n):
    """Giai thừa bằng vòng lặp nhân dồn."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Pi ~", estimate_pi_leibniz())   # ~3.1416
    print("e  ~", estimate_e())             # ~2.71828
    print("sqrt(9)  =", sqrt_newton(9))     # 3.0
    print("sqrt(16) =", sqrt_newton(16))    # ~4.0
    print("5! =", factorial(5))             # 120
    print("math check:", math.pi, math.e)
