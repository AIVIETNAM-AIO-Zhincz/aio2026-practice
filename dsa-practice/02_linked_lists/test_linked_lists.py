"""Test pytest cho bài luyện tập Linked Lists."""

import pytest
from linked_lists import DoublyLinkedList, Queue, SinglyLinkedList

# ----------------------------- SinglyLinkedList -----------------------------


def test_singly_append_giu_thu_tu_va_len() -> None:
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.append(v)
    assert lst.to_list() == [1, 2, 3]
    assert len(lst) == 3


def test_singly_prepend_them_vao_dau() -> None:
    lst = SinglyLinkedList()
    lst.append(2)
    lst.prepend(1)
    lst.prepend(0)
    assert lst.to_list() == [0, 1, 2]
    assert len(lst) == 3


def test_singly_get_dung_index() -> None:
    lst = SinglyLinkedList()
    for v in (10, 20, 30):
        lst.append(v)
    assert lst.get(0) == 10
    assert lst.get(1) == 20
    assert lst.get(2) == 30


def test_singly_get_ngoai_pham_vi_raise() -> None:
    lst = SinglyLinkedList()
    lst.append(1)
    with pytest.raises(IndexError):
        lst.get(5)
    with pytest.raises(IndexError):
        lst.get(-1)


def test_singly_remove_ton_tai() -> None:
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.append(v)
    assert lst.remove(2) is True
    assert lst.to_list() == [1, 3]
    assert len(lst) == 2


def test_singly_remove_khong_ton_tai() -> None:
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.append(v)
    assert lst.remove(99) is False
    assert lst.to_list() == [1, 2, 3]
    assert len(lst) == 3


def test_singly_remove_phan_tu_dau() -> None:
    lst = SinglyLinkedList()
    for v in (1, 2, 3):
        lst.append(v)
    assert lst.remove(1) is True
    assert lst.to_list() == [2, 3]


def test_singly_rong() -> None:
    lst = SinglyLinkedList()
    assert lst.to_list() == []
    assert len(lst) == 0
    assert lst.remove(1) is False


# ----------------------------- DoublyLinkedList -----------------------------


def test_doubly_push_back() -> None:
    lst = DoublyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.to_list() == [1, 2, 3]
    assert len(lst) == 3


def test_doubly_push_front() -> None:
    lst = DoublyLinkedList()
    for v in (1, 2, 3):
        lst.push_front(v)
    assert lst.to_list() == [3, 2, 1]
    assert len(lst) == 3


def test_doubly_pop_front() -> None:
    lst = DoublyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.pop_front() == 1
    assert lst.to_list() == [2, 3]
    assert len(lst) == 2


def test_doubly_pop_back() -> None:
    lst = DoublyLinkedList()
    for v in (1, 2, 3):
        lst.push_back(v)
    assert lst.pop_back() == 3
    assert lst.to_list() == [1, 2]
    assert len(lst) == 2


def test_doubly_pop_den_rong() -> None:
    lst = DoublyLinkedList()
    lst.push_back(1)
    assert lst.pop_front() == 1
    assert lst.to_list() == []
    assert len(lst) == 0


def test_doubly_pop_front_rong_raise() -> None:
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.pop_front()


def test_doubly_pop_back_rong_raise() -> None:
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.pop_back()


# --------------------------------- Queue -----------------------------------


def test_queue_fifo() -> None:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_queue_is_empty() -> None:
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False
    q.dequeue()
    assert q.is_empty() is True


def test_queue_len() -> None:
    q = Queue()
    assert len(q) == 0
    q.enqueue(1)
    q.enqueue(2)
    assert len(q) == 2
    q.dequeue()
    assert len(q) == 1


def test_queue_dequeue_rong_raise() -> None:
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
