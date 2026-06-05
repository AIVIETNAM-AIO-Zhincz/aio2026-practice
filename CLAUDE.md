# CLAUDE.md

Hướng dẫn cho Claude Code khi làm việc trong repo này.

## Dự án

Repo thực hành khoá **AI Việt Nam — AIO 2026** (Basic Python for AI and Data Science) và project **AIO Conquer 2026**. Chủ repo giữ vai trò **AI Engineer - Pipeline** trong team Conquer.

Notes lý thuyết nằm ở Obsidian vault (ngoài repo); repo này chứa **code thực hành** theo từng buổi học.

## Cấu trúc

```
M01-python-basics/W01/   # Module 1 - mỗi thư mục con là 1 buổi
├── 03_branching/        # if-elif-else, ReLU, chatbot   (.py + .ipynb)
├── 04_basic_sql/        # SQL: sqlite cho Colab + .sql gốc PostgreSQL
└── 05_string_loops/     # for/while, Pi/e, Newton sqrt  (.py + .ipynb)
conquer/                 # project AIO Conquer (pipeline AI/ML)
```

Đặt code buổi mới theo mẫu: `M{NN}-.../W{NN}/{thứ tự}_{chủ đề}/`.

## Quy trình Git — GitFlow (BẮT BUỘC tuân theo)

Xem `BRANCHING.md`. Tóm tắt:

- `production` — nhánh ổn định (default), chỉ nhận release/hotfix, gắn tag `vX.Y.Z`.
- `develop` — nhánh tích hợp, **làm việc hằng ngày ở đây**.
- `feature/*` (từ `develop`) · `release/*` (từ `develop`) · `hotfix/*` (từ `production`).

**KHÔNG commit thẳng vào `production`.** Tính năng mới → tạo `feature/*` từ `develop`. Chỉ commit/push khi người dùng yêu cầu.

## Quy ước

- Python: viết code rõ ràng, docstring tiếng Việt ngắn gọn cho hàm; ưu tiên ví dụ chạy được, in kết quả kỳ vọng kèm comment.
- Notebook `.ipynb`: Colab-friendly (dùng thư viện có sẵn; SQL minh hoạ bằng `sqlite3`, ghi chú khác biệt PostgreSQL).
- `.gitignore` đã loại dữ liệu nặng (`*.csv`, `*.parquet`, `data/`, `models/`) — không commit dữ liệu lớn.

## Môi trường

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Coding Standards

Định nghĩa một lần, agent tuân theo cho mọi spec/code (mượn ý "standards layer" của Agent OS, đặt trong khung Spec Kit).

**Python**
- Tuân thủ **PEP 8**; thụt lề 4 dấu cách; dòng tối đa ~100 ký tự.
- Đặt tên: `snake_case` cho hàm/biến, `PascalCase` cho class, `UPPER_SNAKE` cho hằng số.
- **Type hint** cho tham số và giá trị trả về của hàm public.
- **Docstring** tiếng Việt ngắn gọn cho mỗi hàm/class (mô tả mục đích, input/output).
- Ưu tiên hàm thuần (pure function), dễ test; tránh side-effect ẩn.
- `if __name__ == "__main__":` cho phần demo/chạy thử, không để code chạy ở cấp module.

**Cấu trúc & thư viện**
- Mỗi buổi học một thư mục `M{NN}-.../W{NN}/{thứ tự}_{chủ đề}/`.
- Thư viện nền: NumPy, Pandas (Polars/DuckDB khi cần hiệu năng). Không thêm dependency mới khi chưa cần (YAGNI).
- Dữ liệu nặng không commit (`.gitignore` đã cấu hình).

**Test (theo constitution — TDD)**
- Test đặt cùng cấp hoặc trong `tests/`, đặt tên `test_*.py`, chạy bằng `pytest`.
- Viết test **trước**; mỗi hàm có ít nhất một test cho case thường + case biên.

**Notebook**
- Colab-friendly: dùng thư viện có sẵn; SQL minh hoạ bằng `sqlite3`, ghi chú khác biệt PostgreSQL.
- Cell markdown mô tả ngắn trước mỗi cụm code; in kết quả kỳ vọng kèm comment.

> Nguyên tắc bất biến nằm ở `.specify/memory/constitution.md`; mục này là chuẩn vận hành chi tiết.

## Commit message

Tiếng Anh ngắn gọn theo Conventional Commits khi hợp lý (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
