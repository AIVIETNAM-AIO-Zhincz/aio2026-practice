# aio2026-practice Constitution

Hiến chương dự án cho repo thực hành AIO 2026 & project AIO Conquer 2026.
Tài liệu này là **nguồn sự thật về nguyên tắc** — mọi spec, plan, task và code phải tuân theo.

## Core Principles

### I. Test-First (NON-NEGOTIABLE)
Kỷ luật **Test-Driven Development (TDD)** là bắt buộc, không thương lượng.
- Viết test **trước** khi viết code triển khai.
- Tuân thủ chu trình **Red → Green → Refactor**: test phải **đỏ (fail)** trước, rồi mới implement cho **xanh (pass)**, sau đó refactor.
- Ở bước `/speckit-tasks`: task viết test luôn đứng **trước** task implement tương ứng.
- Code "trông đúng" mà không có test chứng minh thì coi như **chưa hoàn thành**.

### II. Spec-Driven (Spec là nguồn sự thật)
- Với feature có phạm vi rõ ràng (đặc biệt trong `conquer/`): **không viết code khi chưa có spec**.
- Trình tự: `constitution → specify → (clarify) → plan → tasks → implement`.
- Spec mô tả *cái gì* cần đúng; test *chứng minh* nó đúng; agent *triển khai*.
- Code practice nhỏ theo buổi học (`M01-.../`) được miễn quy trình spec — làm trực tiếp.

### III. Git Discipline — GitFlow & truy vết
- Tuân theo GitFlow (xem `BRANCHING.md`): làm việc trên `develop`; **không commit thẳng vào `production`**.
- Mỗi feature/spec một nhánh `feature/*` tạo từ `develop`; sửa khẩn cấp dùng `hotfix/*` từ `production`.
- Commit nhỏ, thông điệp theo Conventional Commits (`feat`, `fix`, `docs`, `test`, `refactor`, `chore`).
- Chỉ commit/push khi được yêu cầu.

### IV. Reproducibility (cho pipeline AI/ML)
- Mọi bước pipeline có **input/output rõ ràng**, kiểm soát được lỗi và dễ bảo trì.
- Cố định **random seed**; ghi rõ phiên bản dữ liệu (data versioning) và tham số.
- Chạy lại cùng đầu vào → cùng kết quả. Kết quả phải **đo lường được** bằng metric phù hợp.

### V. Simplicity & YAGNI
- Bắt đầu tối giản; chỉ thêm abstraction/công cụ khi thực sự cần.
- Không thêm IDE chuyên dụng hay framework multi-agent ở giai đoạn học.
- Mọi độ phức tạp phát sinh phải được biện minh trong spec/plan.

## Additional Constraints — Tech Stack

- Ngôn ngữ: **Python 3.10+**. Kiểm thử: **pytest**. Notebook: Colab-friendly.
- Thư viện dữ liệu nền: NumPy, Pandas (và Polars/DuckDB khi cần hiệu năng).
- SQL minh hoạ bằng `sqlite3` trong notebook; chuẩn triển khai là **PostgreSQL**.
- Không commit dữ liệu nặng (đã cấu hình `.gitignore`): `*.csv`, `*.parquet`, `data/`, `models/`.
- Pipeline AI/ML tham chiếu 9 bước: Input → Ingestion → Validation → Preprocessing → Feature Engineering → Model → Evaluation → Output → Monitoring. Vai trò chủ repo: **AI Engineer — Pipeline**.

## Development Workflow — Quality Gates

1. **Spec** (`/speckit-specify`) — chốt phạm vi & tiêu chí chấp nhận.
2. **Plan** (`/speckit-plan`) — kiến trúc, tech choices, ràng buộc.
3. **Tasks** (`/speckit-tasks`) — task **test trước**, implement sau.
4. **Implement** (`/speckit-implement`) — Red → Green → Refactor cho từng task.
5. **Gate trước khi merge:** test xanh hết · tuân thủ hiến chương · spec & code khớp nhau.

## Governance

- Hiến chương này **đứng trên** mọi thói quen làm việc khác; khi xung đột, hiến chương thắng.
- Sửa đổi hiến chương phải ghi rõ lý do, tăng version (semver) và cập nhật ngày.
- Mọi review phải kiểm tra tuân thủ; độ phức tạp phải được biện minh.
- Hướng dẫn vận hành hằng ngày (lệnh build/test/env) nằm ở `CLAUDE.md`.

**Version**: 1.0.0 | **Ratified**: 2026-06-05 | **Last Amended**: 2026-06-05
