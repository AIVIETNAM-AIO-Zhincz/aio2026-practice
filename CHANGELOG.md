# Changelog

Mọi thay đổi đáng chú ý của dự án được ghi tại đây.
Theo [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/) và [SemVer](https://semver.org/lang/vi/).

## [Unreleased]

### Added
- Cấu hình `mypy` (kiểm type tĩnh) trong `pyproject.toml`, pre-commit và CI — enforce type hint cho `aiolib/`.
- Đo độ phủ test bằng `pytest-cov`: report `term-missing`, ngưỡng `--cov-fail-under=100` (đúng tinh thần TDD-NON-NEGOTIABLE).
- `CHANGELOG.md` theo chuẩn Keep a Changelog.

### Changed
- Bổ sung type hint cho các hàm trong `branching.py` và `loops.py` (đồng bộ chuẩn với `aiolib/`).

### Fixed
- `aiolib/activations.py`: khai báo `Callable` cho dict điều phối hàm — mypy bắt được lỗi gọi hàm kiểu không xác định.

## [0.1.0] - 2026-06-05

### Added
- Khởi tạo repo: M01 W01 (branching, loops, basic SQL) + khung pipeline Conquer.
- Thư viện `aiolib` (activations, metrics, trig) kèm test `pytest`.
- Hạ tầng chất lượng: ruff (lint + format), pre-commit, CI GitHub Actions.
- Tài liệu quy trình: constitution, `CLAUDE.md`, `BRANCHING.md` (GitFlow).

[Unreleased]: https://github.com/AIVIETNAM-AIO-Zhincz/aio2026-practice/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AIVIETNAM-AIO-Zhincz/aio2026-practice/releases/tag/v0.1.0
