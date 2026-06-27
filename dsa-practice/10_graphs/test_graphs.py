from graphs import bfs_order, build_adjacency_list, num_islands, shortest_path

# ----- num_islands -----


def test_num_islands_empty():
    assert num_islands([]) == 0


def test_num_islands_all_water():
    assert num_islands([[0, 0], [0, 0]]) == 0


def test_num_islands_single():
    assert num_islands([[1, 1], [1, 1]]) == 1


def test_num_islands_two():
    grid = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1]]
    assert num_islands(grid) == 2


def test_num_islands_does_not_mutate():
    grid = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1]]
    original = [row[:] for row in grid]
    num_islands(grid)
    assert grid == original


# ----- build_adjacency_list -----


def test_build_adjacency_list_basic():
    adj = build_adjacency_list(4, [(0, 1), (0, 2), (1, 2), (2, 3)])
    assert adj == {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}


def test_build_adjacency_list_isolated():
    adj = build_adjacency_list(3, [])
    assert adj == {0: [], 1: [], 2: []}


# ----- bfs_order -----


def test_bfs_order():
    adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    assert bfs_order(adj, 0) == [0, 1, 2, 3]


# ----- shortest_path -----


def test_shortest_path_basic():
    adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    assert shortest_path(adj, 0, 3) == 2


def test_shortest_path_same_node():
    adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    assert shortest_path(adj, 0, 0) == 0


def test_shortest_path_unreachable():
    adj = {0: [1], 1: [0], 2: []}
    assert shortest_path(adj, 0, 2) == -1
