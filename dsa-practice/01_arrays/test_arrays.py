"""Test pytest cho bài luyện tập Arrays.

Chạy: `pytest` trong thư mục `dsa-practice/01_arrays/`.
"""

import pytest
from arrays import DynamicArray, Stack, reverse_string, valid_parentheses


# ---------------------------------------------------------------------------
# DynamicArray
# ---------------------------------------------------------------------------
class TestDynamicArray:
    def test_append_get_and_len(self) -> None:
        arr = DynamicArray()
        assert len(arr) == 0
        arr.append(10)
        arr.append(20)
        arr.append(30)
        assert len(arr) == 3
        assert arr.get(0) == 10
        assert arr.get(1) == 20
        assert arr.get(2) == 30

    def test_get_out_of_range_raises(self) -> None:
        arr = DynamicArray()
        arr.append(1)
        with pytest.raises(IndexError):
            arr.get(5)
        with pytest.raises(IndexError):
            arr.get(-100)

    def test_pop_returns_last_and_shrinks(self) -> None:
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        assert arr.pop() == 3
        assert len(arr) == 2
        assert arr.pop() == 2
        assert len(arr) == 1
        assert arr.get(0) == 1

    def test_pop_empty_raises(self) -> None:
        arr = DynamicArray()
        with pytest.raises(IndexError):
            arr.pop()


# ---------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------
class TestStack:
    def test_push_pop_lifo(self) -> None:
        st = Stack()
        st.push(1)
        st.push(2)
        st.push(3)
        assert len(st) == 3
        assert st.pop() == 3
        assert st.pop() == 2
        assert st.pop() == 1
        assert len(st) == 0

    def test_peek_does_not_remove(self) -> None:
        st = Stack()
        st.push(42)
        assert st.peek() == 42
        assert len(st) == 1
        assert st.peek() == 42
        assert len(st) == 1

    def test_is_empty(self) -> None:
        st = Stack()
        assert st.is_empty() is True
        st.push(1)
        assert st.is_empty() is False
        st.pop()
        assert st.is_empty() is True

    def test_pop_empty_raises(self) -> None:
        st = Stack()
        with pytest.raises(IndexError):
            st.pop()

    def test_peek_empty_raises(self) -> None:
        st = Stack()
        with pytest.raises(IndexError):
            st.peek()


# ---------------------------------------------------------------------------
# valid_parentheses
# ---------------------------------------------------------------------------
class TestValidParentheses:
    def test_simple_balanced(self) -> None:
        assert valid_parentheses("()[]{}") is True

    def test_mismatched(self) -> None:
        assert valid_parentheses("(]") is False

    def test_nested_balanced(self) -> None:
        assert valid_parentheses("([{}])") is True

    def test_empty_is_valid(self) -> None:
        assert valid_parentheses("") is True

    def test_single_open(self) -> None:
        assert valid_parentheses("(") is False


# ---------------------------------------------------------------------------
# reverse_string
# ---------------------------------------------------------------------------
class TestReverseString:
    def test_basic(self) -> None:
        assert reverse_string("abc") == "cba"

    def test_empty(self) -> None:
        assert reverse_string("") == ""

    def test_single_char(self) -> None:
        assert reverse_string("x") == "x"
