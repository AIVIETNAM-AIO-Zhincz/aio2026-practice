"""Bài luyện tập TDD: Cây nhị phân tìm kiếm (Binary Search Tree).

Cài đặt các hàm thao tác trên BST sao cho test trong test_trees.py PASS.
"""


class TreeNode:
    """Nút của cây nhị phân."""

    def __init__(
        self,
        val: int,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def bst_insert(root: "TreeNode | None", val: int) -> TreeNode:
    """Chèn val vào BST, trả về root."""
    raise NotImplementedError("TODO: cài đặt bst_insert")


def bst_search(root: "TreeNode | None", val: int) -> bool:
    """Trả về True nếu val có trong BST."""
    raise NotImplementedError("TODO: cài đặt bst_search")


def bst_remove(root: "TreeNode | None", val: int) -> "TreeNode | None":
    """Xoá val khỏi BST (xử lý 3 trường hợp), trả về root."""
    raise NotImplementedError("TODO: cài đặt bst_remove")


def inorder(root: "TreeNode | None") -> list[int]:
    """Duyệt trung thứ tự (trái - gốc - phải)."""
    raise NotImplementedError("TODO: cài đặt inorder")


def preorder(root: "TreeNode | None") -> list[int]:
    """Duyệt tiền thứ tự (gốc - trái - phải)."""
    raise NotImplementedError("TODO: cài đặt preorder")


def postorder(root: "TreeNode | None") -> list[int]:
    """Duyệt hậu thứ tự (trái - phải - gốc)."""
    raise NotImplementedError("TODO: cài đặt postorder")


def level_order(root: "TreeNode | None") -> list[int]:
    """Duyệt theo mức (BFS), trái sang phải."""
    raise NotImplementedError("TODO: cài đặt level_order")
