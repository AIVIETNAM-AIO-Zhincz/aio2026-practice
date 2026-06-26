import pytest
from dynamic_programming import climb_stairs, house_robber, unique_paths


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
    ],
)
def test_climb_stairs(n: int, expected: int) -> None:
    assert climb_stairs(n) == expected


@pytest.mark.parametrize(
    "m, n, expected",
    [
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 6),
        (3, 7, 28),
        (3, 2, 3),
    ],
)
def test_unique_paths(m: int, n: int, expected: int) -> None:
    assert unique_paths(m, n) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),
        ([5], 5),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1, 2, 3, 1], 4),
    ],
)
def test_house_robber(nums: list[int], expected: int) -> None:
    assert house_robber(nums) == expected
