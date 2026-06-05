# Branching Strategy — GitFlow

Repo này theo mô hình **GitFlow** (Vincent Driessen, 2010), điều chỉnh: nhánh ổn định đặt tên `production` thay cho `main`/`master`.

## Nhánh dài hạn (long-lived)

| Nhánh | Vai trò |
|---|---|
| `production` | Mã đã phát hành, ổn định. Mỗi lần release gắn `tag` (vd `v0.1.0`). **Default branch.** |
| `develop` | Nhánh tích hợp — gom mọi thay đổi cho phiên bản kế tiếp. **Làm việc hằng ngày ở đây.** |

## Nhánh hỗ trợ (tạm thời — tạo khi cần, xoá sau khi merge)

| Nhánh | Tạo từ | Gộp về | Mục đích |
|---|---|---|---|
| `feature/*` | `develop` | `develop` | Phát triển một tính năng (vd `feature/sample-task`) |
| `release/*` | `develop` | `production` + `develop` | Hoàn thiện trước phát hành (vd `release/0.1.0`) |
| `hotfix/*` | `production` | `production` + `develop` | Sửa lỗi khẩn cấp trên bản đã phát hành (vd `hotfix/sample-fix`) |

> Các nhánh `feature/sample-task`, `release/0.1.0`, `hotfix/sample-fix` hiện có chỉ là **ví dụ minh hoạ**; trong thực tế tạo mới khi cần và xoá sau khi merge.

## Quy trình mẫu

```bash
# Tính năng mới
git switch develop
git switch -c feature/payment
# ... code, commit ...
git switch develop && git merge feature/payment
git branch -d feature/payment

# Phát hành
git switch -c release/1.0.0 develop
# ... test, sửa lỗi nhỏ ...
git switch production && git merge release/1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"
git switch develop && git merge release/1.0.0

# Sửa lỗi khẩn cấp
git switch -c hotfix/1.0.1 production
# ... sửa ...
git switch production && git merge hotfix/1.0.1 && git tag -a v1.0.1 -m "Hotfix 1.0.1"
git switch develop && git merge hotfix/1.0.1
```

Chi tiết lý thuyết: note `AIO2026M01SK02 - Git Branching Strategy` trong Obsidian vault.
