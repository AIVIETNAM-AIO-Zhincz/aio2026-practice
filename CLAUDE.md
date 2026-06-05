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

## Commit message

Tiếng Anh ngắn gọn theo Conventional Commits khi hợp lý (`feat:`, `fix:`, `docs:`, `refactor:`).
