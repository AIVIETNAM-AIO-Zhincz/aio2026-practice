# Tech Stack

## Frontend

- **Streamlit** (ưu tiên cho giai đoạn đầu — nhanh, hợp Python) hoặc **React + Tailwind** khi cần UI hoàn chỉnh.
- Biểu đồ: `matplotlib` / `plotly`.

## Backend

- **Python 3.11+**, **FastAPI** + Pydantic.
- Middleware **Auth + RBAC** (kiểm tra quyền server-side mọi request).
- Auth: **JSON Web Token (JWT)** access + refresh, OAuth2 (Google), TOTP 2FA, băm mật khẩu bằng argon2/bcrypt.

## Database

- **PostgreSQL** (production) + **SQLAlchemy**; **SQLite** cho dev.
- Mọi thực thể gắn `space_id` (lọc theo không gian + kiểm tra quyền).

## AI

- **scikit-learn** — phân loại giao dịch, phát hiện bất thường, dự báo (regression/time-series).
- **Large Language Model (OpenAI)** — nhập ngôn ngữ tự nhiên, gợi ý tiết kiệm, trợ lý hỏi-đáp (tool-calling/RAG trên DB). Có fallback rule, không để LLM tự bịa số.

## Other

- **Testing:** `pytest` (TDD — viết test trước).
- **Chất lượng code:** `black`, `ruff`.
- **Hạ tầng:** Docker, GitHub Actions (CI/CD), deploy Render/Railway/VPS.
- **Version control:** Git + GitFlow (xem `BRANCHING.md`).
