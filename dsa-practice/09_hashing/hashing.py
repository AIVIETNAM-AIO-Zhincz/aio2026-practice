"""Bài luyện tập Hashing (bảng băm).

Tự cài bảng băm bằng CHAINING (danh sách liên kết / list các bucket).
KHÔNG dùng dict built-in của Python cho HashMap.
Key và value đều là int cho đơn giản.
"""


class HashMap:
    """Bảng băm ánh xạ key:int -> value:int, dùng chaining để xử lý va chạm."""

    def __init__(self) -> None:
        """Khởi tạo bảng băm rỗng."""
        raise NotImplementedError("TODO: khởi tạo các bucket và biến đếm size")

    def put(self, key: int, value: int) -> None:
        """Thêm key mới hoặc cập nhật value nếu key đã tồn tại."""
        raise NotImplementedError("TODO: cài put (thêm/cập nhật), rehash khi cần")

    def get(self, key: int) -> int:
        """Trả về value của key; raise KeyError nếu không có."""
        raise NotImplementedError("TODO: cài get, raise KeyError nếu vắng")

    def remove(self, key: int) -> None:
        """Xoá key; raise KeyError nếu không có."""
        raise NotImplementedError("TODO: cài remove, raise KeyError nếu vắng")

    def __contains__(self, key: int) -> bool:
        """Kiểm tra key có trong bảng băm hay không."""
        raise NotImplementedError("TODO: cài kiểm tra tồn tại key")

    def __len__(self) -> int:
        """Trả về số cặp key-value hiện có."""
        raise NotImplementedError("TODO: trả về số phần tử")


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Trả cặp chỉ số (i, j) với i<j sao cho nums[i]+nums[j]==target.

    Giả định có đúng 1 đáp án. Dùng hash map để đạt O(n).
    """
    raise NotImplementedError("TODO: cài two_sum bằng hash map, O(n)")


def count_frequency(items: list[int]) -> dict[int, int]:
    """Đếm số lần xuất hiện của mỗi phần tử trong items."""
    raise NotImplementedError("TODO: cài đếm tần suất")
