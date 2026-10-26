#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động chuyển đổi bài đào tạo từ NotebookLM -> Cập nhật data.json -> Git Commit & Push lên tuantute.life
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime

# Đảm bảo in tiếng Việt và Emoji mượt mà trên Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Đường dẫn thư mục hiện tại
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON_PATH = os.path.join(SCRIPT_DIR, "data.json")
SOURCES_DIR = os.path.join(SCRIPT_DIR, "notebooklm_sources")

# Đảm bảo thư mục nguồn tồn tại
os.makedirs(SOURCES_DIR, exist_ok=True)

# Danh sách ảnh mặc định sang trọng theo chủ đề
DEFAULT_IMAGES = [
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1200&q=80"
]

def parse_notebooklm_content(raw_text: str, default_topic: str = "AI THỰC CHIẾN"):
    """
    Phân tích văn bản ghi chú/đào tạo từ NotebookLM thành cấu trúc bài viết
    """
    lines = [line.strip() for line in raw_text.strip().split("\n") if line.strip()]
    if not lines:
        raise ValueError("Nội dung bài viết từ NotebookLM trống!")

    # 1. Tìm tiêu đề (thường là dòng đầu tiên hoặc sau dấu #)
    title = lines[0].lstrip("#").strip()
    content_lines = lines[1:]

    # 2. Tìm trích dẫn (quote) hoặc câu châm ngôn
    quote = ""
    quote_candidates = [l for l in content_lines if l.startswith(">") or "châm ngôn" in l.lower() or "bài học" in l.lower() or "thước đo" in l.lower()]
    if quote_candidates:
        quote = quote_candidates[0].lstrip(">").strip()
        # Loại bỏ quote khỏi content_lines để tránh lặp
        content_lines = [l for l in content_lines if l != quote_candidates[0]]

    # 3. Tạo nội dung tóm tắt
    body_text = " ".join([l.lstrip("-*• ") for l in content_lines if not l.startswith("#")])
    if len(body_text) > 400:
        # Tóm gọn đoạn mở đầu ấn tượng
        sentences = re.split(r'(?<=[.!?]) +', body_text)
        content = " ".join(sentences[:3])
    else:
        content = body_text if body_text else title

    # Nếu chưa có quote thì sinh quote mặc định từ triết lý Tuấn Tử Tế
    if not quote:
        quote = "Từ kiến thức hàn lâm trong sách vở trở thành năng lực số thực chiến — Sự rộng lượng là thước đo trình độ sống!"

    # 4. Xác định ngày và chủ đề
    today_str = datetime.now().strftime("%d/%m/%Y")
    topic = default_topic.upper()
    if "tư duy" in raw_text.lower() or "thân tâm trí" in raw_text.lower():
        topic = "PHÁT TRIỂN BẢN THÂN"
    elif "ai" in raw_text.lower() or "chatgpt" in raw_text.lower() or "gemini" in raw_text.lower():
        topic = "KỶ NGUYÊN TRÍ TUỆ AI"
    elif "doanh nghiệp" in raw_text.lower() or "lãnh đạo" in raw_text.lower():
        topic = "QUẢN TRỊ & KẾT NỐI"

    date_str = f"{today_str} • {topic}"

    # Chọn ảnh ngẫu nhiên hoặc theo thứ tự
    import random
    media_url = random.choice(DEFAULT_IMAGES)

    return {
        "date": date_str,
        "title": title,
        "mediaUrl": media_url,
        "content": content,
        "quote": quote
    }

def add_post_to_data_json(new_post: dict) -> bool:
    """
    Thêm bài viết mới vào đầu danh sách posts trong data.json
    """
    if not os.path.exists(DATA_JSON_PATH):
        print(f"❌ Không tìm thấy file: {DATA_JSON_PATH}")
        return False

    with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    posts = data.get("posts", [])
    
    # Kiểm tra trùng tiêu đề
    for p in posts:
        if p.get("title", "").strip().lower() == new_post["title"].strip().lower():
            print(f"⚠️ Bài viết '{new_post['title']}' đã tồn tại trong data.json!")
            return False

    # Thêm lên đầu danh sách
    posts.insert(0, new_post)
    data["posts"] = posts

    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã thêm bài viết mới vào data.json: '{new_post['title']}'")
    return True

def git_commit_and_push(commit_msg: str):
    """
    Tự động git add, git commit và git push lên GitHub repository
    """
    try:
        print("\n🚀 Đang tự động đẩy lên GitHub (tuantute.life)...")
        # 1. Git Add
        subprocess.run(["git", "add", "data.json", "index.html"], cwd=SCRIPT_DIR, check=True)
        
        # 2. Git Commit
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=SCRIPT_DIR, check=True)
        
        # 3. Git Push
        res = subprocess.run(["git", "push", "origin", "main"], cwd=SCRIPT_DIR, capture_output=True, text=True)
        if res.returncode == 0:
            print("🎉 THÀNH CÔNG! Đã đẩy bài viết lên GitHub thành công.")
            print("🌐 Trang web tuantute.life đang cập nhật (khoảng 30-60 giây): https://tuantute.life/")
            return True
        else:
            print(f"⚠️ Lỗi khi git push: {res.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi lệnh Git: {e}")
        return False

def process_file(file_path: str):
    """Xử lý 1 file tài liệu xuất từ NotebookLM"""
    print(f"\n📄 Đang đọc file: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    post = parse_notebooklm_content(text)
    if add_post_to_data_json(post):
        commit_msg = f"Auto-post NotebookLM: {post['title']}"
        git_commit_and_push(commit_msg)

def scan_sources_folder():
    """Quét thư mục notebooklm_sources để tự động xuất bản các file mới"""
    files = [f for f in os.listdir(SOURCES_DIR) if f.endswith(".txt") or f.endswith(".md")]
    if not files:
        print(f"📂 Thư mục trống: {SOURCES_DIR}")
        print("💡 Hãy thả các file ghi chú (.txt hoặc .md) xuất từ NotebookLM vào thư mục trên và chạy lại script!")
        return False

    for file_name in files:
        full_path = os.path.join(SOURCES_DIR, file_name)
        process_file(full_path)
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("🌟 BỘ TỰ ĐỘNG ĐĂNG BÀI ĐÀO TẠO TỪ NOTEBOOKLM LÊN TUANTUTE.LIFE 🌟")
    print("=" * 60)

    if len(sys.argv) > 1:
        # Nếu truyền đường dẫn file qua tham số dòng lệnh
        target_file = sys.argv[1]
        if os.path.exists(target_file):
            process_file(target_file)
        else:
            print(f"❌ Không tìm thấy file: {target_file}")
    else:
        # Quét thư mục sources trước
        success = scan_sources_folder()
        if not success:
            print("\n📝 Hoặc bạn có thể dán nội dung bài đào tạo trực tiếp tại đây:")
            print("(Nhập xong bấm Enter rồi gõ 'END' và bấm Enter để tiến hành đăng):")
            lines = []
            while True:
                try:
                    line = input()
                    if line.strip() == "END":
                        break
                    lines.append(line)
                except EOFError:
                    break
            
            raw_input = "\n".join(lines).strip()
            if raw_input:
                post = parse_notebooklm_content(raw_input)
                if add_post_to_data_json(post):
                    commit_msg = f"Auto-post NotebookLM: {post['title']}"
                    git_commit_and_push(commit_msg)
            else:
                print("Đã hủy thao tác.")
