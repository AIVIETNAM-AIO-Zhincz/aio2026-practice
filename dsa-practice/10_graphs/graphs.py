"""Bài luyện tập TDD: Graphs (đồ thị).

Hoàn thiện các hàm bên dưới để toàn bộ test trong test_graphs.py PASS.
KHÔNG chứa lời giải sẵn — hãy tự cài đặt.
"""


def num_islands(grid: list[list[int]]) -> int:
    """Đếm số đảo trong lưới 0/1 (1=đất, 0=nước), liên thông 4 hướng.

    KHÔNG được sửa grid gốc (dùng tập visited).
    """
    raise NotImplementedError("TODO: cài đặt num_islands")


def build_adjacency_list(n: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    """Dựng danh sách kề cho đồ thị VÔ HƯỚNG, đỉnh 0..n-1.

    Mỗi đỉnh đều có key (list rỗng nếu không có cạnh); hàng xóm sắp tăng dần.
    """
    raise NotImplementedError("TODO: cài đặt build_adjacency_list")


def bfs_order(adj: dict[int, list[int]], start: int) -> list[int]:
    """Trả về thứ tự duyệt BFS từ đỉnh start (hàng xóm theo thứ tự trong adj)."""
    raise NotImplementedError("TODO: cài đặt bfs_order")


def shortest_path(adj: dict[int, list[int]], start: int, goal: int) -> int:
    """Số CẠNH ngắn nhất từ start đến goal bằng BFS.

    Trả -1 nếu không tới được; start == goal trả 0.
    """
    raise NotImplementedError("TODO: cài đặt shortest_path")
