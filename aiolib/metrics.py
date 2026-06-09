"""Độ đo đánh giá mô hình phân loại — TA-Exercise M01W01 (F1-Score)."""


def _check_count(name: str, value: object) -> int:
    """Xác thực một tham số đếm: phải là int (không phải bool) và không âm."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be int")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return value


def calculate_f1_score(tp: int, fp: int, fn: int) -> float:
    """Tính F1-Score từ true positive / false positive / false negative.

    F1 = 2 * P * R / (P + R), với P = TP/(TP+FP), R = TP/(TP+FN).
    Trả 0.0 khi không thể tính (mẫu số 0 hoặc TP = 0).
    """
    _check_count("tp", tp)
    _check_count("fp", fp)
    _check_count("fn", fn)

    if tp == 0 or (tp + fp) == 0 or (tp + fn) == 0:
        return 0.0

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * precision * recall / (precision + recall)
