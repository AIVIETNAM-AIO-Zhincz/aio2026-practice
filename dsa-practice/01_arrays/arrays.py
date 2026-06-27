"""Bài luyện tập TDD — chủ đề Arrays (mảng động, ngăn xếp, ứng dụng).

Người học tự cài đặt thân các hàm/method (đang là NotImplementedError).
Chạy `pytest` trong thư mục này; mục tiêu là làm cho tất cả test xanh.
"""

from __future__ import annotations


class DynamicArray:
    """Mảng động đơn giản bọc quanh list của Python.

    Mục đích: hiểu cách một mảng có thể thay đổi kích thước hoạt động.
    """

    def __init__(self) -> None:
        """Khởi tạo mảng rỗng.

        Input: không.
        Output: không (tạo bộ nhớ nội bộ rỗng).
        """
        self._data: list[int] = []

    def append(self, value: int) -> None:
        """Thêm một phần tử vào cuối mảng.

        Input: value (int) — giá trị cần thêm.
        Output: không.
        """
        self._data.append(value)

    def get(self, index: int) -> int:
        """Lấy phần tử tại vị trí index.

        Input: index (int) — chỉ số (0-based).
        Output: int — phần tử tại index.
        Lỗi: IndexError nếu index ngoài phạm vi.
        """
        if 0 <= index < len(self._data):
            return self._data[index]
        raise IndexError("Index out of bounds")

    def pop(self) -> int:
        """Bỏ và trả về phần tử cuối cùng của mảng.

        Input: không.
        Output: int — phần tử cuối vừa bị bỏ.
        Lỗi: IndexError nếu mảng rỗng.
        """
        if not self._data:
            raise IndexError("pop from empty array")
        return self._data.pop()

    def __len__(self) -> int:
        """Trả về số phần tử hiện có trong mảng.

        Input: không.
        Output: int — độ dài mảng.
        """
        return len(self._data)


class Stack:
    """Ngăn xếp (LIFO — Last In, First Out).

    Mục đích: hiểu cấu trúc ngăn xếp và ứng dụng của nó.
    """

    def __init__(self) -> None:
        """Khởi tạo ngăn xếp rỗng.

        Input: không.
        Output: không.
        """
        self._data: list[int] = []

    def push(self, value: int) -> None:
        """Đẩy một phần tử vào đỉnh ngăn xếp.

        Input: value (int) — giá trị cần đẩy vào.
        Output: không.
        """
        raise NotImplementedError("TODO: đẩy value vào đỉnh ngăn xếp")

    def pop(self) -> int:
        """Lấy ra và trả về phần tử ở đỉnh ngăn xếp.

        Input: không.
        Output: int — phần tử ở đỉnh vừa bị lấy ra.
        Lỗi: IndexError nếu ngăn xếp rỗng.
        """
        raise NotImplementedError("TODO: lấy và trả về phần tử đỉnh, raise IndexError nếu rỗng")

    def peek(self) -> int:
        """Xem phần tử ở đỉnh ngăn xếp mà KHÔNG lấy ra.

        Input: không.
        Output: int — phần tử ở đỉnh.
        Lỗi: IndexError nếu ngăn xếp rỗng.
        """
        raise NotImplementedError("TODO: trả về phần tử đỉnh không xoá, raise IndexError nếu rỗng")

    def is_empty(self) -> bool:
        """Kiểm tra ngăn xếp có rỗng hay không.

        Input: không.
        Output: bool — True nếu rỗng, ngược lại False.
        """
        raise NotImplementedError("TODO: trả về True nếu ngăn xếp rỗng")

    def __len__(self) -> int:
        """Trả về số phần tử trong ngăn xếp.

        Input: không.
        Output: int — số phần tử.
        """
        raise NotImplementedError("TODO: trả về số phần tử trong ngăn xếp")


def valid_parentheses(s: str) -> bool:
    """Kiểm tra chuỗi ngoặc `()[]{}` có cân bằng hay không.

    Input: s (str) — chuỗi chỉ chứa các ký tự ngoặc.
    Output: bool — True nếu các ngoặc đóng/mở khớp và lồng đúng, ngược lại False.
    """
    raise NotImplementedError("TODO: dùng stack đẩy ngoặc mở, khớp với ngoặc đóng tương ứng")


def reverse_string(s: str) -> str:
    """Đảo ngược một chuỗi.

    Input: s (str) — chuỗi cần đảo.
    Output: str — chuỗi đã đảo thứ tự ký tự.
    Gợi ý: có thể dùng stack (đẩy từng ký tự rồi lấy ra).
    """
    raise NotImplementedError("TODO: đảo ngược chuỗi, gợi ý dùng stack")
