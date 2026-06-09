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

## Mã tính năng & truy vết ticket (BẮT BUỘC)

Mỗi nhánh `feature/*` phải bám một **ticket chức năng** có mã rõ ràng; mọi commit phải thể hiện được nó thuộc ticket nào để **truy vết ngược** code ↔ tính năng.

### Mã tính năng

Bám cấu trúc module của repo:

| Loại công việc | Định dạng mã | Ví dụ |
|---|---|---|
| Học theo buổi (`M{NN}-.../W{NN}/`) | `M{NN}-W{NN}[-{chủ_đề}]` | `M01-W01-branching`, `M01-W01-sql` |
| Project Conquer (`conquer/`) | `CQR-{bước_pipeline}` | `CQR-ingestion`, `CQR-validation` |

### Đặt tên nhánh feature

```
feature/{MÃ}-{slug-ngắn}
```

- `feature/M01-W01-branching` · `feature/M01-W01-newton-sqrt` · `feature/CQR-ingestion`
- Một nhánh = một ticket. Không gộp nhiều mã khác nhau vào một `feature/*`.

### Commit phải tham chiếu mã

Chọn **một** trong hai cách (nhất quán trong cùng nhánh):

- **Scope** (ưu tiên): đặt mã vào scope của Conventional Commits
  - `feat(M01-W01): thêm hàm ReLU và test biên`
  - `fix(CQR-ingestion): xử lý file CSV rỗng`
- **Footer** (khi scope khó đặt mã): thêm dòng `Refs: {MÃ}` cuối commit
  - ```
    docs: bổ sung ghi chú PostgreSQL cho notebook SQL

    Refs: M01-W01-sql
    ```

Mỗi commit phải truy được về **đúng một** ticket; tránh commit "lẫn" nhiều tính năng.

### Khi merge feature → develop

```bash
git switch develop
git merge --no-ff feature/M01-W01-branching -m "feat(M01-W01): branching, ReLU, chatbot

Refs: M01-W01-branching"
git branch -d feature/M01-W01-branching
```

Merge commit cũng phải nêu mã (scope hoặc `Refs:`) để mốc tích hợp truy được về ticket.

## Quy ước message khi merge/release

Nguyên tắc chung:

- Luôn merge bằng `--no-ff` để giữ **merge commit** làm mốc lịch sử cho mỗi lần tích hợp/phát hành.
- **Subject** ngắn gọn tiếng Anh theo Conventional Commits; **body** liệt kê thay đổi đáng chú ý kiểu changelog (tiếng Việt được).
- Phần phát hành phải nêu **version `vX.Y.Z`** theo SemVer.
- Không thêm `Co-Authored-By` vào commit/merge message.

### 1) `develop` → `release/X.Y.Z` (cắt nhánh & hoàn thiện)

Tạo `release/X.Y.Z` từ `develop`, sau đó **chỉ** nhận `fix:`/`docs:`/`chore:` để ổn định hoá — **không** thêm `feat:` mới.

```
chore(release): prepare vX.Y.Z

- Gom tính năng cho vX.Y.Z từ develop
- Bump version, cập nhật CHANGELOG
- Chỉ nhận bugfix/polish trên nhánh này
```

### 2) `release/X.Y.Z` → `production` (phát hành chính thức)

```bash
git switch production
git merge --no-ff release/X.Y.Z -m "release: vX.Y.Z

Highlights:
- <thay đổi nổi bật 1>
- <thay đổi 2>

Refs: release/X.Y.Z"

git tag -a vX.Y.Z -m "Release vX.Y.Z — <tóm tắt 1 dòng>"
```

Sau đó **back-merge về `develop`** để đồng bộ (version bump, fix trong release):

```bash
git switch develop
git merge --no-ff release/X.Y.Z -m "chore: back-merge vX.Y.Z into develop"
git branch -d release/X.Y.Z
```

### Tóm tắt subject

| Mối merge | Subject |
|---|---|
| `develop` → `release/*` | `chore(release): prepare vX.Y.Z` |
| `release/*` → `production` | `release: vX.Y.Z` + tag `vX.Y.Z` |
| back-merge → `develop` | `chore: back-merge vX.Y.Z into develop` |
| `hotfix/*` → `production` | `fix: vX.Y.Z <mô tả>` + tag `vX.Y.Z` |

Chi tiết lý thuyết: note `AIO2026M01SK02 - Git Branching Strategy` trong Obsidian vault.
