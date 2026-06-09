# aio2026-practice

Repo thực hành khoá **AI Việt Nam — AIO 2026** (Basic Python for AI and Data Science) và project **AIO Conquer 2026**.

Notes lý thuyết lưu ở Obsidian vault; repo này chứa **code thực hành** theo từng buổi.

## Phương pháp làm việc — Spec-Driven Development (Agent OS)

Bộ công cụ tối thiểu: **Agent OS (khung) + Claude Code (động cơ) + Git/GitFlow + kỷ luật TDD**.

| Thành phần | Vai trò | Loại |
|---|---|---|
| **Agent OS** | Standards + spec workflow (đạo diễn); slash command cho Claude Code | Công cụ (cài qua `~/agent-os/scripts/project-install.sh`) |
| **Claude Code** | Agent thực thi, sinh & sửa code (diễn viên) | Công cụ |
| **Git / GitFlow** | Branch hiện tại = feature context; cô lập & truy vết | Công cụ (xem `BRANCHING.md`) |
| **TDD** | Test chứng minh spec đúng — viết test trước, implement sau | **Kỷ luật**, không phải phần mềm |
| **`CLAUDE.md`** | Context bền vững: lệnh build/test, quy ước môi trường | File |

**Nguyên tắc:** Standards + Spec nói *cái gì* cần đúng → Test *chứng minh* nó đúng → Claude Code *implement*. Luôn tạo **task viết test trước**, rồi mới task implement.

**Phạm vi áp dụng:** dùng Agent OS chủ yếu cho **project có spec rõ ràng** (`conquer/` — pipeline AI/ML). Code practice nhỏ theo từng buổi (`M01-.../`) làm thoải mái, không cần spec.

**Agent OS (v3.0):**
- `agent-os/standards/` — coding standards của project (được commit, dùng chung cả team).
- `.claude/commands/agent-os/` — slash command cho Claude Code (`.claude/` **gitignore**; mỗi người tự chạy `project-install.sh` để có).
- Lệnh chính: `/discover-standards` (rút pattern từ codebase) · `/inject-standards` · `/plan-product` · `/shape-spec`.

> Cài lại trên máy khác: `cd ~ && git clone https://github.com/buildermethods/agent-os.git && rm -rf ~/agent-os/.git`, rồi trong repo chạy `~/agent-os/scripts/project-install.sh`.

## Cấu trúc

```
aiolib/                   # Thư viện hàm thực hành (có test) — activations, metrics, trig
tests/                    # Test pytest cho aiolib (TDD)
M01-python-basics/        # Module 1 — Toán cơ bản & lập trình Python (02/06 → 05/07/2026)
└── W01/
    ├── 03_branching/        # biến, hàm, if-elif-else, ReLU, rule-based chatbot
    ├── 04_basic_sql/        # CREATE/INSERT/SELECT/WHERE/JOIN (PostgreSQL)
    └── 05_string_loops/     # for/while, range, accumulator, ước lượng Pi/e, Newton sqrt
conquer/                  # Project AIO Conquer 2026 (vai trò: Tech Leader — điều phối nhóm)
slides/                   # Slide buổi học (gitignore — chỉ giữ README)
.github/workflows/ci.yml  # CI: lint + format check + test
```

## Môi trường

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt          # thư viện chạy notebook
pip install -r requirements-dev.txt      # công cụ dev (ruff, pytest, pre-commit)
pre-commit install                       # bật hook chặn lỗi trước khi commit
```

Runtime ghim ở `.python-version` (Python 3.10).

## Chất lượng code & CI

Quy chuẩn chạy **cả ở local lẫn CI** (tránh "lint trên máy tôi thì pass"):

```bash
ruff check .          # lint
ruff format .         # format (tương thích Black, line-length 100)
pytest                # chạy test
```

- **Pre-commit** (`.pre-commit-config.yaml`): tự lint/format + dọn whitespace/EOF khi commit.
- **GitHub Actions** (`.github/workflows/ci.yml`): trên push/PR vào `production`/`develop` → `ruff check` → `ruff format --check` → `pytest`.
- **TDD:** viết test trước trong `tests/` (`test_*.py`), implement trong `aiolib/` sau.

> Checklist nền tảng khi khởi tạo repo: xem note `DevProd 5 - Repo Setup Checklist` trong Obsidian vault.

## Tiến độ Module 1

- [x] W01 — Reading & StudyGuide, Tabular/Time-series, Basic Python, SQL, String & Loops
- [ ] W02 — Image/Video · List · SQL Retrieval · Dictionary/Histogram · Coding Methodology
- [ ] W03 — Text/Audio · OOP · SQL Cleaning · Graph/Tree · Git/GitHub
- [ ] W04 — Project 1.1 (Streamlit) · Project 1.2 (AI-assisted DS) · Exam (28/06)
- [ ] W05 — GitHub Submission · Blog/Report · Conquer Presentation (05/07)
