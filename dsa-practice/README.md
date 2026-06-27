# DSA Practice — Luyện tập Cấu trúc dữ liệu & Giải thuật

Khu luyện tập theo lối **TDD**: mỗi chủ đề có một file cài đặt với các hàm/class **để trống** (`raise NotImplementedError`) và một file test `pytest` định nghĩa sẵn kết quả mong đợi. Nhiệm vụ của bạn: **tự implement cho test xanh**.

Bám theo giáo trình NeetCode *Algorithms and Data Structures for Beginners*. Lý thuyết nằm ở Obsidian vault: `05 - Learning/04 - Tech/DSA for Beginners/` (track 12 chủ đề tương ứng).

## Cách luyện

```bash
# Từ thư mục gốc repo
cd dsa-practice

# Chạy toàn bộ (đỏ vì chưa implement)
pytest

# Chạy đúng 1 chủ đề đang luyện
pytest 01_arrays

# Chạy 1 test cụ thể, hiện chi tiết
pytest 01_arrays/test_arrays.py -v
```

> ⚠️ Phải `cd dsa-practice` trước khi chạy `pytest`. Khu này có `pytest.ini` riêng để **không vướng** gate `--cov=aiolib --cov-fail-under=100` của repo gốc.

Quy trình mỗi bài: đọc docstring + đọc test để hiểu yêu cầu → xoá `raise NotImplementedError` → viết code → chạy `pytest` cho tới khi xanh → đối chiếu lý thuyết trong note Obsidian.

## Các chủ đề

| # | Thư mục | Nội dung luyện | Note lý thuyết |
|---|---------|----------------|----------------|
| 01 | `01_arrays/` | Dynamic Array, Stack, valid parentheses | [[01 - Arrays]] |
| 02 | `02_linked_lists/` | Singly/Doubly Linked List, Queue | [[02 - Linked Lists]] |
| 03 | `03_recursion/` | Factorial, Fibonacci, tổng đệ quy | [[03 - Recursion]] |
| 04 | `04_sorting/` | Insertion, Merge, Quick, Bucket sort | [[04 - Sorting]] |
| 05 | `05_binary_search/` | Binary search, integer sqrt | [[05 - Binary Search]] |
| 06 | `06_trees/` | BST insert/search/remove, DFS, BFS | [[06 - Trees]] |
| 07 | `07_backtracking/` | Subsets, permutations, tree maze | [[07 - Backtracking]] |
| 08 | `08_heap/` | MinHeap, heapify, k phần tử nhỏ nhất | [[08 - Heap & Priority Queue]] |
| 09 | `09_hashing/` | HashMap (chaining), two-sum, đếm tần suất | [[09 - Hashing]] |
| 10 | `10_graphs/` | Đếm đảo (DFS), BFS đường ngắn nhất, adjacency list | [[10 - Graphs]] |
| 11 | `11_dynamic_programming/` | Climb stairs, unique paths, house robber | [[11 - Dynamic Programming]] |
| 12 | `12_bit_manipulation/` | get/set/clear/toggle bit, đếm bit, single number | [[12 - Bit Manipulation]] |

## Quy ước (theo CLAUDE.md repo)

- Python: PEP 8, line ≤ 100, **type hint** + **docstring tiếng Việt** cho hàm public.
- Hàm thuần, dễ test; demo đặt trong `if __name__ == "__main__":`.
- Test: mỗi hàm có ít nhất 1 case thường + 1 case biên.
