import pytest
from heap import MinHeap, k_smallest


class TestMinHeap:
    def test_peek_tra_ve_phan_tu_nho_nhat(self) -> None:
        h = MinHeap()
        for v in [5, 3, 8, 1, 9, 2]:
            h.push(v)
        assert h.peek() == 1

    def test_pop_cho_day_tang_dan(self) -> None:
        h = MinHeap()
        for v in [5, 3, 8, 1, 9, 2]:
            h.push(v)
        ket_qua = [h.pop() for _ in range(6)]
        assert ket_qua == [1, 2, 3, 5, 8, 9]

    def test_len_giam_dung_sau_moi_pop(self) -> None:
        h = MinHeap()
        for v in [5, 3, 8, 1, 9, 2]:
            h.push(v)
        assert len(h) == 6
        for con_lai in range(5, -1, -1):
            h.pop()
            assert len(h) == con_lai

    def test_pop_khi_rong_raise(self) -> None:
        h = MinHeap()
        with pytest.raises(IndexError):
            h.pop()

    def test_peek_khi_rong_raise(self) -> None:
        h = MinHeap()
        with pytest.raises(IndexError):
            h.peek()


class TestHeapify:
    def test_heapify_pop_cho_day_tang_dan(self) -> None:
        h = MinHeap.heapify([4, 1, 7, 3, 8, 5])
        ket_qua = [h.pop() for _ in range(6)]
        assert ket_qua == [1, 3, 4, 5, 7, 8]


class TestKSmallest:
    def test_lay_3_phan_tu_nho_nhat(self) -> None:
        assert k_smallest([5, 2, 9, 1, 7, 3], 3) == [1, 2, 3]

    def test_k_bang_0_tra_ve_rong(self) -> None:
        assert k_smallest([5, 2, 9, 1, 7, 3], 0) == []

    def test_k_lon_hon_hoac_bang_len_tra_ve_toan_bo_da_sap(self) -> None:
        assert k_smallest([5, 2, 9, 1, 7, 3], 6) == [1, 2, 3, 5, 7, 9]
        assert k_smallest([5, 2, 9, 1, 7, 3], 10) == [1, 2, 3, 5, 7, 9]

    def test_mang_rong_va_k_bang_0(self) -> None:
        assert k_smallest([], 0) == []
