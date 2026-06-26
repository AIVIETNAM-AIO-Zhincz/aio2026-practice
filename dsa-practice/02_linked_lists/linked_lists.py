"""Bài luyện tập TDD: Linked Lists (danh sách liên kết).

Người học cài đặt thân các method (thay `raise NotImplementedError`).
Riêng class node (`ListNode`) đã được cài sẵn đầy đủ để test dựng được.
"""

from __future__ import annotations


class ListNode:
    """Node của danh sách liên kết đơn (đã cài sẵn đầy đủ)."""

    def __init__(self, val: int, next: ListNode | None = None) -> None:
        """Khởi tạo node với giá trị `val` và con trỏ `next`."""
        self.val: int = val
        self.next: ListNode | None = next


class SinglyLinkedList:
    """Danh sách liên kết đơn."""

    def __init__(self) -> None:
        """Khởi tạo danh sách rỗng."""
        self.head: ListNode | None = None
        self._size: int = 0

    def append(self, val: int) -> None:
        """Thêm `val` vào cuối danh sách."""
        raise NotImplementedError("TODO: cài đặt append")

    def prepend(self, val: int) -> None:
        """Thêm `val` vào đầu danh sách."""
        raise NotImplementedError("TODO: cài đặt prepend")

    def get(self, index: int) -> int:
        """Trả về giá trị tại `index`; IndexError nếu ngoài phạm vi."""
        raise NotImplementedError("TODO: cài đặt get")

    def remove(self, val: int) -> bool:
        """Xoá lần xuất hiện đầu của `val`; trả True nếu xoá được."""
        raise NotImplementedError("TODO: cài đặt remove")

    def to_list(self) -> list[int]:
        """Trả về list các giá trị theo thứ tự từ đầu đến cuối."""
        raise NotImplementedError("TODO: cài đặt to_list")

    def __len__(self) -> int:
        """Trả về số phần tử trong danh sách."""
        raise NotImplementedError("TODO: cài đặt __len__")


class DoublyLinkedList:
    """Danh sách liên kết đôi."""

    def __init__(self) -> None:
        """Khởi tạo danh sách rỗng."""
        self.head: _DNode | None = None
        self.tail: _DNode | None = None
        self._size: int = 0

    def push_front(self, val: int) -> None:
        """Thêm `val` vào đầu danh sách."""
        raise NotImplementedError("TODO: cài đặt push_front")

    def push_back(self, val: int) -> None:
        """Thêm `val` vào cuối danh sách."""
        raise NotImplementedError("TODO: cài đặt push_back")

    def pop_front(self) -> int:
        """Xoá và trả về phần tử đầu; IndexError nếu rỗng."""
        raise NotImplementedError("TODO: cài đặt pop_front")

    def pop_back(self) -> int:
        """Xoá và trả về phần tử cuối; IndexError nếu rỗng."""
        raise NotImplementedError("TODO: cài đặt pop_back")

    def to_list(self) -> list[int]:
        """Trả về list các giá trị theo thứ tự từ đầu đến cuối."""
        raise NotImplementedError("TODO: cài đặt to_list")

    def __len__(self) -> int:
        """Trả về số phần tử trong danh sách."""
        raise NotImplementedError("TODO: cài đặt __len__")


class _DNode:
    """Node của danh sách liên kết đôi (đã cài sẵn đầy đủ)."""

    def __init__(
        self,
        val: int,
        prev: _DNode | None = None,
        next: _DNode | None = None,
    ) -> None:
        """Khởi tạo node đôi với con trỏ `prev` và `next`."""
        self.val: int = val
        self.prev: _DNode | None = prev
        self.next: _DNode | None = next


class Queue:
    """Hàng đợi FIFO (cài đặt trên danh sách liên kết)."""

    def __init__(self) -> None:
        """Khởi tạo hàng đợi rỗng."""
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self._size: int = 0

    def enqueue(self, val: int) -> None:
        """Thêm `val` vào cuối hàng đợi."""
        raise NotImplementedError("TODO: cài đặt enqueue")

    def dequeue(self) -> int:
        """Lấy và trả về phần tử đầu hàng đợi; IndexError nếu rỗng."""
        raise NotImplementedError("TODO: cài đặt dequeue")

    def is_empty(self) -> bool:
        """Trả về True nếu hàng đợi rỗng."""
        raise NotImplementedError("TODO: cài đặt is_empty")

    def __len__(self) -> int:
        """Trả về số phần tử trong hàng đợi."""
        raise NotImplementedError("TODO: cài đặt __len__")
