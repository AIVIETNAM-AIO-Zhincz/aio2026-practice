"""Demo next-token prediction bằng mô hình n-gram đếm tần suất (Day 05).

Minh họa ý chính buổi học: language model = đoán token tiếp theo dựa trên ngữ cảnh
trước đó, qua xác suất có điều kiện P(token | mấy từ trước). Không dùng mạng nơ-ron,
chỉ đếm tần suất bằng Python thuần cho thấy rõ bản chất.
"""

from collections import Counter, defaultdict


def tokenize(text):
    # tách theo khoảng trắng + về chữ thường, đủ cho demo
    return text.lower().split()


def build_model(tokens, n=2):
    """Với mỗi ngữ cảnh (n-1 từ trước), đếm những từ hay theo sau.

    Trả về dict: context (tuple) -> Counter các từ kế tiếp.
    """
    if n < 2:
        raise ValueError("n phải >= 2 (cần ít nhất 1 từ ngữ cảnh).")
    model = defaultdict(Counter)
    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i : i + n - 1])
        nxt = tokens[i + n - 1]
        model[context][nxt] += 1
    return model


def next_token_probs(model, context):
    """List (token, xác suất) cho từ tiếp theo, sắp giảm dần. Rỗng nếu chưa thấy ngữ cảnh."""
    counter = model.get(tuple(context))
    if not counter:
        return []
    total = sum(counter.values())
    return [(tok, c / total) for tok, c in counter.most_common()]


def predict_next(model, context):
    """Từ tiếp theo xác suất cao nhất. None nếu ngữ cảnh chưa từng gặp."""
    probs = next_token_probs(model, context)
    return probs[0][0] if probs else None


def generate(model, start, length=10):
    """Sinh tiếp 'length' từ: cứ đoán từ kế rồi nối vào ngữ cảnh, lặp lại."""
    if not model:
        return list(start)
    ctx_len = len(next(iter(model)))  # số từ ngữ cảnh = n-1
    out = list(start)
    for _ in range(length):
        nxt = predict_next(model, out[-ctx_len:])
        if nxt is None:  # ngữ cảnh lạ -> dừng
            break
        out.append(nxt)
    return out


if __name__ == "__main__":
    corpus = (
        "tích tiểu thành đại . có công mài sắt có ngày nên kim . "
        "tích tiểu thành đại là bài học quý . "
        "tôi đang học về language model . tôi đang học về ai ."
    )
    model = build_model(tokenize(corpus), n=4)  # ngữ cảnh 3 từ

    ctx = ["tích", "tiểu", "thành"]
    print("Ngữ cảnh:", " ".join(ctx))
    print("Đoán từ kế:", predict_next(model, ctx))
    print("Xác suất các ứng viên:", next_token_probs(model, ctx))
    print("Sinh thử:", " ".join(generate(model, ["tôi", "đang", "học"], length=4)))
