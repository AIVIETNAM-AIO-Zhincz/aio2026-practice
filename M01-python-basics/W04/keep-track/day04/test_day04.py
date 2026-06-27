"""Test cho chunk_text + PROMPT (phần không cần model). Chạy: pytest -q"""

from rag_core import PROMPT, chunk_text


def test_gop_cac_doan_ngan():
    text = "\n".join(f"dong {i}" for i in range(10))
    chunks = chunk_text(text, size=30, overlap=5)
    assert len(chunks) >= 2
    assert all(c.strip() for c in chunks)  # không có chunk rỗng


def test_text_rong_thi_khong_co_chunk():
    assert chunk_text("   \n  \n  ") == []


def test_doan_ngan_gon_1_chunk():
    assert chunk_text("xin chào", size=1000) == ["xin chào"]


def test_overlap_noi_phan_duoi_chunk_truoc():
    text = "AAAAA\nBBBBB\nCCCCC"
    chunks = chunk_text(text, size=8, overlap=4)
    assert len(chunks) >= 2
    # chunk sau dính phần đuôi của chunk trước (overlap), không bắt đầu sạch ở "BBBBB"
    assert "AAA" in chunks[1]


def test_prompt_co_cho_dien_context_va_cau_hoi():
    p = PROMPT.format(context="YOLO là model detect vật thể", question="YOLO là gì?")
    assert "YOLO là model detect vật thể" in p
    assert "YOLO là gì?" in p
    assert "đừng bịa" in p  # dòng chống bịa phải còn
