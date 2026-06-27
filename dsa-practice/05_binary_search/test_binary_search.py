import pytest
from binary_search import binary_search, integer_sqrt, search_insert


class TestBinarySearch:
    def test_tim_thay_o_giua(self):
        assert binary_search([1, 3, 5, 7, 9], 5) == 2

    def test_tim_thay_o_dau(self):
        assert binary_search([1, 3, 5, 7, 9], 1) == 0

    def test_tim_thay_o_cuoi(self):
        assert binary_search([1, 3, 5, 7, 9], 9) == 4

    def test_khong_co_o_giua(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1

    def test_khong_co_vuot_can(self):
        assert binary_search([1, 3, 5, 7, 9], 10) == -1

    def test_mang_rong(self):
        assert binary_search([], 1) == -1

    def test_mot_phan_tu_tim_thay(self):
        assert binary_search([2], 2) == 0

    def test_mot_phan_tu_khong_co(self):
        assert binary_search([2], 3) == -1


class TestIntegerSqrt:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (4, 2),
            (10, 3),
            (15, 3),
            (16, 4),
            (99, 9),
        ],
    )
    def test_cac_gia_tri(self, n, expected):
        assert integer_sqrt(n) == expected

    def test_n_am_raise(self):
        with pytest.raises(ValueError):
            integer_sqrt(-1)


class TestSearchInsert:
    @pytest.mark.parametrize(
        "target, expected",
        [
            (5, 2),
            (2, 1),
            (7, 4),
            (0, 0),
        ],
    )
    def test_chen_vao_mang(self, target, expected):
        assert search_insert([1, 3, 5, 6], target) == expected

    def test_target_trung_tra_trai_nhat(self):
        assert search_insert([1, 2, 2, 3], 2) == 1
