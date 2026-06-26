from bit_manipulation import (
    clear_bit,
    count_ones,
    get_bit,
    is_even,
    set_bit,
    single_number,
    toggle_bit,
)


def test_get_bit():
    assert get_bit(0b1010, 1) == 1
    assert get_bit(0b1010, 0) == 0
    assert get_bit(0b1010, 3) == 1
    assert get_bit(0b1010, 2) == 0


def test_set_bit():
    assert set_bit(0b1010, 0) == 0b1011  # 11
    assert set_bit(0b1010, 1) == 0b1010  # 10, đã bật sẵn


def test_clear_bit():
    assert clear_bit(0b1010, 1) == 0b1000  # 8
    assert clear_bit(0b1010, 0) == 0b1010  # 10, đã tắt sẵn


def test_toggle_bit():
    assert toggle_bit(0b1010, 0) == 0b1011  # 11
    assert toggle_bit(0b1010, 1) == 0b1000  # 8


def test_count_ones():
    assert count_ones(0) == 0
    assert count_ones(0b1011) == 3
    assert count_ones(255) == 8
    assert count_ones(1023) == 10


def test_is_even():
    assert is_even(0) is True
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(1) is False


def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([7]) == 7
