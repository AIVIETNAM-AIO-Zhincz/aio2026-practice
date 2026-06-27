# Day 05 — Demo next-token prediction (n-gram)

Buổi lý thuyết LLMs (Pre-training GPT). Để minh họa ý cốt lõi — **language model = đoán token tiếp theo bằng xác suất có điều kiện `P(token | ngữ cảnh)`** — mình làm một mô hình n-gram đếm tần suất bằng Python thuần (không mạng nơ-ron, không thư viện ngoài).

## File
- `ngram_lm.py` — `tokenize`, `build_model`, `next_token_probs`, `predict_next`, `generate`. Chạy thẳng: `python ngram_lm.py`.
- `test_day05.py` — test các hàm.

## Ý tưởng
Đếm trên văn bản: với mỗi ngữ cảnh (n-1 từ trước), những từ nào hay theo sau và bao nhiêu lần. Xác suất từ kế = (số lần từ đó theo sau) / (tổng số lần ngữ cảnh xuất hiện) → đúng tinh thần `P(xₙ | x₁…xₙ₋₁)` trong bài, chỉ khác là LLM thật học bằng mạng nơ-ron thay vì đếm.

```python
from ngram_lm import build_model, tokenize, predict_next
model = build_model(tokenize("tích tiểu thành đại . tích tiểu thành đại"), n=4)
predict_next(model, ["tích", "tiểu", "thành"])   # -> "đại"
```

## Chạy
```bash
pip install -r requirements.txt
python ngram_lm.py     # xem demo
pytest -q              # chạy test
```

## Giới hạn (để thấy vì sao cần LLM thật)
- Ngữ cảnh lạ (chưa từng xuất hiện y hệt) → chịu, trả `None`. LLM học theo *nghĩa* nên tổng quát hơn.
- Chỉ nhớ đúng `n-1` từ; tăng `n` thì cần dữ liệu nhiều hơn nữa mới đủ thống kê.
