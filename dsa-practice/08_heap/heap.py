"""Bài luyện tập TDD: Min-Heap / Priority Queue.

Người học tự cài đặt (KHÔNG dùng module heapq).
Gợi ý: dùng list làm cây nhị phân; sift up khi push, sift down khi pop.
"""


class MinHeap:
    """Min-Heap: phần tử nhỏ nhất luôn ở đỉnh."""

    def __init__(self) -> None:
        """Khởi tạo heap rỗng."""
        self._data: list[int] = []

    def push(self, value: int) -> None:
        """Thêm phần tử vào heap (sift up)."""
        raise NotImplementedError("TODO: thêm value rồi sift up để giữ tính chất heap")

    def pop(self) -> int:
        """Lấy và xoá phần tử NHỎ NHẤT (IndexError nếu rỗng)."""
        raise NotImplementedError("TODO: đổi đỉnh với cuối, xoá cuối, sift down")

    def peek(self) -> int:
        """Xem phần tử nhỏ nhất mà không xoá (IndexError nếu rỗng)."""
        raise NotImplementedError("TODO: trả về phần tử ở đỉnh heap")

    def __len__(self) -> int:
        """Số phần tử hiện có trong heap."""
        raise NotImplementedError("TODO: trả về số phần tử trong heap")

    @classmethod
    def heapify(cls, values: list[int]) -> "MinHeap":
        """Dựng heap từ danh sách cho trước."""
        raise NotImplementedError(
            "TODO: dựng heap từ values (push lần lượt hoặc sift down từ giữa)"
        )


def k_smallest(nums: list[int], k: int) -> list[int]:
    """Trả về k phần tử NHỎ NHẤT của nums, sắp TĂNG DẦN."""
    raise NotImplementedError("TODO: dùng MinHeap để lấy k phần tử nhỏ nhất theo thứ tự tăng dần")
