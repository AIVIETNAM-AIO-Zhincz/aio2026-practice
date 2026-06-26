import pytest
from hashing import HashMap, count_frequency, two_sum

# ----- HashMap -----


def test_put_then_get():
    m = HashMap()
    m.put(1, 100)
    assert m.get(1) == 100


def test_put_updates_value():
    m = HashMap()
    m.put(1, 100)
    m.put(1, 200)
    assert m.get(1) == 200


def test_contains_true_false():
    m = HashMap()
    m.put(5, 50)
    assert 5 in m
    assert 6 not in m


def test_len_basic():
    m = HashMap()
    assert len(m) == 0
    m.put(1, 10)
    m.put(2, 20)
    assert len(m) == 2


def test_len_not_increase_on_update():
    m = HashMap()
    m.put(1, 10)
    m.put(1, 99)
    assert len(m) == 1


def test_get_missing_raises_keyerror():
    m = HashMap()
    with pytest.raises(KeyError):
        m.get(42)


def test_remove_missing_raises_keyerror():
    m = HashMap()
    with pytest.raises(KeyError):
        m.remove(42)


def test_remove_then_absent_and_len_decreases():
    m = HashMap()
    m.put(1, 10)
    m.put(2, 20)
    m.remove(1)
    assert 1 not in m
    assert len(m) == 1


def test_many_keys_collision_and_rehash():
    m = HashMap()
    for k in range(21):
        m.put(k, k * 10)
    assert len(m) == 21
    for k in range(21):
        assert m.get(k) == k * 10


# ----- two_sum -----


def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_middle():
    assert two_sum([3, 2, 4], 6) == (1, 2)


def test_two_sum_duplicate():
    assert two_sum([3, 3], 6) == (0, 1)


# ----- count_frequency -----


def test_count_frequency_basic():
    assert count_frequency([1, 1, 2, 3, 3, 3]) == {1: 2, 2: 1, 3: 3}


def test_count_frequency_empty():
    assert count_frequency([]) == {}
