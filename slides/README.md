# slides/

Bản **copy local** của toàn bộ slide / tài liệu PDF khoá AIO2026 + AIO Conquer 2026, để tiện tra cứu ngay trong repo khi code.

> [!important]
> Toàn bộ thư mục này **được `.gitignore`** (`slides/**`) — chỉ riêng `README.md` được commit.
> Slide **không** đẩy lên remote (tránh nặng repo + bản quyền tài liệu khoá học). Bản gốc đầy đủ ở OneDrive và được index trong Obsidian vault.

## Nguồn & cách đồng bộ

Mirror từ `OneDrive/AIO2026/` (giữ nguyên cấu trúc thư mục), chỉ lấy `.pdf` + `.txt`:

```bash
SRC="$HOME/Library/CloudStorage/OneDrive-Personal/AIO2026"
DST="$HOME/Documents/GitHub/aio2026-practice/slides"
rsync -a --include='*/' --include='*.pdf' --include='*.txt' --exclude='*' "$SRC/" "$DST/"
find "$DST" -type d -empty -delete   # dọn thư mục rỗng
```

Chạy lại lệnh trên mỗi khi tải slide buổi mới về OneDrive là `slides/` tự cập nhật.

## Cấu trúc hiện có (local, không commit)

```
slides/
├── AIO Conquer 2026/Advisor Roles/   # 5 slide vai trò (AIE Pipeline/Data/Model, Tech Leader, QA)
├── M01-SelfLearning-DSA/             # [slide-01..04] Big O, Brute Force, Recursion, D&C + DP
├── M01-Skills-for-Coders/            # 01 Git/GitHub, 02 Branching, 03 Agile, 04 Jira (+ link YouTube .txt)
├── M01W01/                           # Module 1 - Week 1 (theo từng buổi D01..D07)
│   ├── 00 - Reading & StudyGuide/    # StudyGuide, Reading (Common Errors, Colab)
│   ├── D01 - Orientation/            # Website Guide
│   ├── D02 - Tabular & Time-series/  # Slide + Quiz (+Solution)
│   ├── D03 - Basic Python/           # Slide + Quiz + Reading
│   ├── D04 - Basic SQL/              # Slide + Quiz + Reading
│   ├── D05 - String and Loops/       # Slide + Quiz + Reading (FOR/WHILE)
│   ├── D06 - Teamwork Tools/         # Slide
│   └── D07 - TA-Exercise/            # Slide + Quiz + Description (Activation Functions)
├── M01W02/                           # Module 1 - Week 2
│   ├── 00 - Reading & StudyGuide/
│   └── D08 - Office Hours/
└── Methodology/                      # bổ sung từ AIO2025 (clean code & ways of working)
```

> [!note]
> Thư mục chứa cả **Slide + Quiz + Reading + StudyGuide** (mirror trọn bộ tài liệu PDF, không chỉ slide) để khỏi sót khi cần tra cứu.
