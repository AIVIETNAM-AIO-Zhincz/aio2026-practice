"""Bài luyện tập TDD: Binary Search.

Hãy cài đặt các hàm dưới đây sao cho toàn bộ test trong
``test_binary_search.py`` đều pass. Chưa có lời giải sẵn.
"""


def binary_search(arr: list[int], target: int) -> int:
    """Tìm ``target`` trong ``arr`` (đã sắp tăng dần) bằng tìm kiếm nhị phân.

    Trả về chỉ số của ``target``, hoặc ``-1`` nếu không có. Độ phức tạp O(log n).
    """
    raise NotImplementedError("TODO: cài đặt binary_search bằng tìm kiếm nhị phân")


def integer_sqrt(n: int) -> int:
    """Căn bậc hai nguyên (floor) của ``n >= 0`` bằng binary search.

    Ví dụ ``integer_sqrt(10) == 3``. Ném ``ValueError`` nếu ``n < 0``.
    """
    raise NotImplementedError("TODO: cài đặt integer_sqrt bằng tìm kiếm nhị phân")


def search_insert(arr: list[int], target: int) -> int:
    """Vị trí cần chèn ``target`` để ``arr`` vẫn tăng dần.

    Nếu ``target`` đã có, trả về chỉ số trái nhất. Dùng tìm kiếm nhị phân.
    """
    raise NotImplementedError("TODO: cài đặt search_insert bằng tìm kiếm nhị phân")
