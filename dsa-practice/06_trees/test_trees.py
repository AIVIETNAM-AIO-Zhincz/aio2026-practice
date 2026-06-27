"""Test pytest cho các thao tác trên Binary Search Tree."""

from trees import (
    TreeNode,
    bst_insert,
    bst_remove,
    bst_search,
    inorder,
    level_order,
    postorder,
    preorder,
)

VALUES = [5, 3, 7, 2, 4, 6, 8]


def build_tree(values: list[int] = VALUES) -> "TreeNode | None":
    """Dựng BST bằng cách chèn lần lượt các giá trị."""
    root: TreeNode | None = None
    for v in values:
        root = bst_insert(root, v)
    return root


# --- Traversals ---


def test_inorder_increasing() -> None:
    assert inorder(build_tree()) == [2, 3, 4, 5, 6, 7, 8]


def test_preorder() -> None:
    assert preorder(build_tree()) == [5, 3, 2, 4, 7, 6, 8]


def test_postorder() -> None:
    assert postorder(build_tree()) == [2, 4, 3, 6, 8, 7, 5]


def test_level_order() -> None:
    assert level_order(build_tree()) == [5, 3, 7, 2, 4, 6, 8]


# --- Search ---


def test_search_found() -> None:
    root = build_tree()
    assert bst_search(root, 4) is True
    assert bst_search(root, 6) is True


def test_search_not_found() -> None:
    assert bst_search(build_tree(), 99) is False


def test_search_empty() -> None:
    assert bst_search(None, 5) is False


# --- Remove ---


def test_remove_leaf() -> None:
    root = build_tree()
    root = bst_remove(root, 2)
    assert inorder(root) == [3, 4, 5, 6, 7, 8]


def test_remove_one_child() -> None:
    # Cây nghiêng: 5 -> 8 -> 6; xoá 8 (1 con là 6).
    root = build_tree([5, 8, 6])
    root = bst_remove(root, 8)
    assert inorder(root) == [5, 6]
    assert bst_search(root, 8) is False


def test_remove_two_children() -> None:
    root = build_tree()
    root = bst_remove(root, 3)  # node 3 có 2 con (2 và 4)
    result = inorder(root)
    assert result == sorted(result)
    assert 3 not in result


def test_remove_root() -> None:
    root = build_tree()
    root = bst_remove(root, 5)  # root có 2 con
    result = inorder(root)
    assert result == sorted(result)
    assert 5 not in result


# --- Empty tree ---


def test_inorder_empty() -> None:
    assert inorder(None) == []


def test_level_order_empty() -> None:
    assert level_order(None) == []
