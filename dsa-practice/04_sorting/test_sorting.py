"""Test pytest cho các thuật toán sắp xếp."""

import pytest
from sorting import bucket_sort, insertion_sort, merge_sort, quick_sort

SORT_FNS = [insertion_sort, merge_sort, quick_sort, bucket_sort]

CASES = [
    ([], []),
    ([5], [5]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
]


@pytest.mark.parametrize("sort_fn", SORT_FNS)
@pytest.mark.parametrize("data, expected", CASES)
def test_sort_returns_ascending(sort_fn, data, expected):
    """Mỗi thuật toán phải trả về danh sách đã sắp tăng dần đúng kết quả."""
    assert sort_fn(list(data)) == expected


@pytest.mark.parametrize("sort_fn", SORT_FNS)
def test_sort_does_not_mutate_input(sort_fn):
    """Hàm không được sửa đổi danh sách đầu vào."""
    data = [5, 2, 9, 1, 5, 6]
    original = data.copy()
    sort_fn(data)
    assert data == original


@pytest.mark.parametrize("sort_fn", SORT_FNS)
def test_sort_returns_new_list(sort_fn):
    """Kết quả phải là một đối tượng danh sách MỚI, không phải input."""
    data = [3, 1, 2]
    result = sort_fn(data)
    assert result is not data
