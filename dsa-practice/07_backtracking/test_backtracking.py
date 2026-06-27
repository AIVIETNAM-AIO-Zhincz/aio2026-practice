"""Test pytest cho bài luyện tập Backtracking.

Thứ tự kết quả không quan trọng nên ta chuẩn hoá trước khi so sánh.
"""

from backtracking import combination_sum, permutations, subsets


def normalize(list_of_lists: list[list[int]]) -> list[list[int]]:
    """Chuẩn hoá: sort từng tổ hợp con rồi sort danh sách kết quả."""
    return sorted([sorted(x) for x in list_of_lists])


# ----- subsets -----


def test_subsets_empty():
    assert subsets([]) == [[]]


def test_subsets_single():
    assert normalize(subsets([1])) == normalize([[], [1]])


def test_subsets_two():
    assert normalize(subsets([1, 2])) == normalize([[], [1], [2], [1, 2]])


def test_subsets_three():
    result = subsets([1, 2, 3])
    assert len(result) == 8
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert normalize(result) == normalize(expected)


# ----- permutations -----


def test_permutations_single():
    assert normalize(permutations([1])) == normalize([[1]])


def test_permutations_two():
    assert normalize(permutations([1, 2])) == normalize([[1, 2], [2, 1]])


def test_permutations_three():
    result = permutations([1, 2, 3])
    assert len(result) == 6
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert normalize(result) == normalize(expected)


# ----- combination_sum -----


def test_combination_sum_basic():
    assert normalize(combination_sum([2, 3, 6, 7], 7)) == normalize([[7], [2, 2, 3]])


def test_combination_sum_no_solution():
    assert combination_sum([2], 1) == []


def test_combination_sum_repeat():
    assert normalize(combination_sum([2, 3], 6)) == normalize([[2, 2, 2], [3, 3]])
