"""
AIO2026 M01W04 - NLP Text Collection (web scraping) — 24/06/2026

Thu thập văn bản đầu vào cho pipeline NLP bằng requests + BeautifulSoup
(cào báo dantri.com.vn). Đây là khâu 0 của mọi dự án NLP thực tế.

Lưu ý: tôn trọng robots.txt, đặt User-Agent, thêm delay khi cào nhiều trang.
Cấu trúc HTML của trang đổi thì các selector (class_=...) sẽ phải cập nhật.
"""

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "test"}
TIMEOUT = 10


def get_link_dantri(url: str) -> list[str]:
    """Lấy danh sách URL bài viết từ một trang chuyên mục dantri."""
    html = requests.get(url, headers=HEADERS, timeout=TIMEOUT).text
    soup = BeautifulSoup(html, "html.parser")

    urls: list[str] = []
    div = soup.find(class_="article list")
    if div is None:
        return urls
    for article in div.find_all(class_="article-item"):
        thumb = article.find(class_="article-thumb")
        a_tag = thumb.find("a", href=True) if thumb else None
        if a_tag:
            urls.append(urljoin(url, a_tag["href"]))  # ghép thành URL tuyệt đối
    return urls


def get_content_dantri(url: str) -> str:
    """Lấy nội dung văn bản (các thẻ <p>) của một bài viết dantri."""
    html = requests.get(url, headers=HEADERS, timeout=TIMEOUT).text
    soup = BeautifulSoup(html, "html.parser")

    div_tag = soup.find(class_="singular-content")
    if div_tag is None:
        return ""
    article: list[str] = []
    for p_tag in div_tag.find_all("p"):
        article.extend(p_tag.stripped_strings)  # bỏ khoảng trắng thừa
    return " ".join(article)


if __name__ == "__main__":
    links = get_link_dantri("https://dantri.com.vn/kinh-doanh/trang-2.htm")
    print(f"Tìm thấy {len(links)} link")  # ~20 link
    if links:
        text = get_content_dantri(links[0])
        print(text[:300], "...")  # 300 ký tự đầu của bài đầu tiên
