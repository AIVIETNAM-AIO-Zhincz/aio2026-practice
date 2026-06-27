"""Bit Manipulation - bài luyện tập TDD.

Cài đặt các hàm bên dưới để vượt qua test trong test_bit_manipulation.py.
"""


def get_bit(x: int, i: int) -> int:
    """Trả về bit thứ i (0 hoặc 1), i đếm từ 0 ở LSB."""
    raise NotImplementedError("TODO: cài đặt get_bit")


def set_bit(x: int, i: int) -> int:
    """Bật bit thứ i lên 1, trả về số mới."""
    raise NotImplementedError("TODO: cài đặt set_bit")


def clear_bit(x: int, i: int) -> int:
    """Tắt bit thứ i về 0, trả về số mới."""
    raise NotImplementedError("TODO: cài đặt clear_bit")


def toggle_bit(x: int, i: int) -> int:
    """Đảo bit thứ i, trả về số mới."""
    raise NotImplementedError("TODO: cài đặt toggle_bit")


def count_ones(x: int) -> int:
    """Đếm số bit 1 trong x (x >= 0)."""
    raise NotImplementedError("TODO: cài đặt count_ones")


def is_even(x: int) -> bool:
    """Kiểm tra x chẵn hay không, dùng phép bit."""
    raise NotImplementedError("TODO: cài đặt is_even")


def single_number(nums: list[int]) -> int:
    """Tìm phần tử xuất hiện 1 lần (các phần tử khác xuất hiện 2 lần) bằng XOR."""
    raise NotImplementedError("TODO: cài đặt single_number")
