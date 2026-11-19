# -*- coding: utf-8 -*-
"""
KTCS 4D Universal Engine V09 (Multi-Modal Fusion • Self-Evolving • AI + Smart Offline)
Hệ thống kiến tạo bài giảng HTML 4D Cinema 16:9 tự hành toàn năng.
Hỗ trợ phối hợp ĐA DẠNG TÀI LIỆU cùng lúc:
  - Chủ đề tự do / Văn bản dán trực tiếp
  - .PDF (NotebookLM, Canva, PowerPoint)
  - .HTML / .HTM
  - .TXT / .MD
  - .JSON (dữ liệu slide hoặc cấu trúc bất kỳ)
  - Hình ảnh (.PNG, .JPG, .JPEG, .WEBP, .SVG, .GIF)
  - Video (.MP4, .WEBM, .MOV)
Tác giả: Tổng Chỉ Huy Tự Hành AI • Thầy Tuấn Tử Tế (Nguyễn Anh Tuấn)
"""

import os
import re
import json
import shutil
import html as html_lib
import datetime
import urllib.request
from pathlib import Path
from PIL import Image

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

ENGINE_DIR = Path(__file__).resolve().parent
SKILL_DIR = ENGINE_DIR.parent
TEMPLATE_PATH = SKILL_DIR / "templates" / "ktcs_4d_cinema_template.html"
EVOLUTION_LOG_PATH = SKILL_DIR / "evolution_log.json"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"}
VIDEO_EXTS = {".mp4", ".webm", ".mov"}

# ---------------------------------------------------------------------------
# 1. QUY TẮC KHÓA TỪ MỒ CÔI TUYỆT ĐỐI (ORPHAN WORDS LOCKING)
# ---------------------------------------------------------------------------
def lock_orphan_words(text, max_len=46):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', str(text)).strip()
    words = text.split()
    if len(words) <= 2:
        return text

    if len(text) > max_len and "<br>" not in text:
        mid_idx = len(words) // 2
        line1 = " ".join(words[:mid_idx])
        line2_words = words[mid_idx:]
        if len(line2_words) >= 2:
            line2 = " ".join(line2_words[:-1]) + "\u00a0" + line2_words[-1]
        else:
            line2 = " ".join(line2_words)
        return f"{line1}<br>{line2}"

    return " ".join(words[:-1]) + "\u00a0" + words[-1]

# ---------------------------------------------------------------------------
# 2. KHO VIDEO YOUTUBE TIẾNG VIỆT ĐÃ XÁC THỰC (ƯU TIÊN NGƯỜI TRUNG NIÊN VN)
# ---------------------------------------------------------------------------
VERIFIED_VN_YOUTUBE_BANK = [
    {"url": "https://www.youtube.com/watch?v=_jGU_GvHsMM", "title": "[Thuyết Minh] Bài phát biểu hay nhất của Steve Jobs (ĐH Stanford)", "author": "Tuan Look", "domains": ["triet_ly_song", "lanh_dao", "tong_quat"]},
    {"url": "https://www.youtube.com/watch?v=oNEZ0og693U", "title": "[VN] The 5AM Club - Câu Lạc Bộ 5 Giờ Sáng | Tóm tắt sách", "author": "Tia Sách", "domains": ["suc_khoe", "triet_ly_song", "tong_quat"]},
    {"url": "https://www.youtube.com/watch?v=tiOuQe7_UhU", "title": "Con Đường Duy Nhất Giúp Bạn Thoát Khỏi Cuộc Đời Tầm Thường | Jim Rohn", "author": "Cổng Trí Tuệ", "domains": ["triet_ly_song", "ban_hang", "tai_chinh"]},
    {"url": "https://www.youtube.com/watch?v=uu4kOe-pty0", "title": "Giá Trị Của 3 Gốc: Đạo Đức - Trí Tuệ - Nghị Lực | Trần Việt Quân", "author": "Trần Việt Quân", "domains": ["triet_ly_song", "giao_duc", "lanh_dao"]},
    {"url": "https://www.youtube.com/watch?v=cIOOxnN8oA8", "title": "Điều Gì Thực Sự Xảy Ra Khi Bạn Kỷ Luật Liên Tục Trong 90 Ngày?", "author": "Đàn Ông Trung Niên", "domains": ["suc_khoe", "triet_ly_song"]},
    {"url": "https://www.youtube.com/watch?v=-Q4f2L-JKlQ", "title": "[Sách nói] Não trái não phải - Phần 1 | Bizbooks Audio", "author": "Bizbooks Audio", "domains": ["giao_duc", "triet_ly_song"]},
    {"url": "https://www.youtube.com/watch?v=Dm5hxsDFMo8", "title": "[Sách Nói] Storytelling - Lay Động Lòng Người Bằng Chuyện Kể", "author": "Fonos", "domains": ["ban_hang", "giao_duc", "lanh_dao"]},
    {"url": "https://www.youtube.com/watch?v=LS1kG6DFdvM", "title": "Tóm tắt sách BẮT ĐẦU VỚI CÂU HỎI TẠI SAO - Simon Sinek", "author": "MICCO Bookee", "domains": ["lanh_dao", "ban_hang", "tong_quat"]},
    {"url": "https://www.youtube.com/watch?v=Bi_Rz8fDPuw", "title": "[VN] Made to Stick - Tạo ra thông điệp kết dính | Tóm tắt sách", "author": "Tia Sách", "domains": ["giao_duc", "ban_hang", "triet_ly_song"]},
    {"url": "https://www.youtube.com/watch?v=Rniy1-Yw9VU", "title": "Tóm tắt sách: ĐẮC NHÂN TÂM (Dale Carnegie) | Nghệ thuật giao tiếp", "author": "Tóm tắt sách cùng Tany", "domains": ["ban_hang", "lanh_dao", "giao_duc"]},
    {"url": "https://www.youtube.com/watch?v=xKeWCbSQRTU", "title": "[Tóm Tắt Sách] ĐI TÌM LẼ SỐNG | Viktor Frankl", "author": "Sách Tinh Gọn", "domains": ["triet_ly_song", "suc_khoe"]},
    {"url": "https://www.youtube.com/watch?v=CjrqXNg75zA", "title": "3 Báu Vật Cuộc Đời - Thầy Hiền Trí, Tủ Sách Hay, Nhóm Bạn Tốt | Trần Việt Quân", "author": "Trần Việt Quân", "domains": ["giao_duc", "triet_ly_song", "lanh_dao"]},
    {"url": "https://www.youtube.com/watch?v=bxzlOB9k-F4", "title": "Tư Duy Viết Prompt Cho Người Mới Bắt Đầu (Trọn bộ + Dễ hiểu) | Thái Vân Linh", "author": "Thái Vân Linh", "domains": ["cong_nghe_ai", "giao_duc"]},
    {"url": "https://www.youtube.com/watch?v=Z43_i13E7kE", "title": "Trí tuệ nhân tạo AI có cảm xúc và tri giác? | Better Version", "author": "Better Version", "domains": ["cong_nghe_ai", "triet_ly_song"]},
    {"url": "https://www.youtube.com/watch?v=mPtfYVyhA3c", "title": "Ứng dụng ChatGPT thực chiến vào công việc & gia đình", "author": "Ngọc AI Thực Chiến", "domains": ["cong_nghe_ai", "tong_quat"]},
    {"url": "https://www.youtube.com/watch?v=OeE5IFMQi5w", "title": "Thầy Minh Niệm - Thuận Tự Nhiên Đời Tự Khắc Bình Yên", "author": "Radio Chữa Lành", "domains": ["triet_ly_song", "suc_khoe"]},
    {"url": "https://www.youtube.com/watch?v=h96coGHH0gk", "title": "Thầy Minh Niệm - Hãy Sống Cho Mình Đúng Nghĩa", "author": "Radio Chữa Lành", "domains": ["triet_ly_song", "suc_khoe", "tai_chinh"]},
    {"url": "https://www.youtube.com/watch?v=_YIYGWH9NPM", "title": "[VTTC Vietsub] Chấm màu xanh nhạt (Pale Blue Dot) - Carl Sagan", "author": "vttcnews", "domains": ["triet_ly_song", "tong_quat"]},
]

# ---------------------------------------------------------------------------
# 3. HỆ THỐNG NHẬT KÝ HỌC HỎI & TIẾN HÓA TỰ HÀNH
# ---------------------------------------------------------------------------
DEFAULT_EVOLUTION_LOG = {
    "version": "V09.0 Multi-Modal Self-Evolving",
    "updated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "lessons_learned": [],
    "learned_youtube_bank": [],
    "build_history": []
}

def load_evolution_log():
    if EVOLUTION_LOG_PATH.exists():
        try:
            with open(EVOLUTION_LOG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    save_evolution_log(DEFAULT_EVOLUTION_LOG)
    return json.loads(json.dumps(DEFAULT_EVOLUTION_LOG))

def save_evolution_log(log_data):
    log_data["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    EVOLUTION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EVOLUTION_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

def record_lesson_learned(category, insight):
    log = load_evolution_log()
    log.setdefault("lessons_learned", []).insert(0, {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category": category.strip() or "Tối Ưu Hệ Thống",
        "insight": insight.strip()
    })
    save_evolution_log(log)
    return log

def verify_and_add_youtube(url, domain="tong_quat"):
    m = re.search(r'(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})', url)
    if not m:
        return {"ok": False, "error": "Không nhận diện được mã video YouTube (11 ký tự)."}
    vid = m.group(1)
    clean_url = f"https://www.youtube.com/watch?v={vid}"
    oembed = f"https://www.youtube.com/oembed?url={clean_url}&format=json"
    try:
        req = urllib.request.Request(oembed, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            info = json.loads(resp.read().decode("utf-8"))
        entry = {
            "url": clean_url,
            "title": info.get("title", "Video YouTube Tiếng Việt"),
            "author": info.get("author_name", "YouTube VN"),
            "domains": [domain]
        }
        log = load_evolution_log()
        bank = log.setdefault("learned_youtube_bank", [])
        if not any(x.get("url") == clean_url for x in bank):
            bank.insert(0, entry)
        save_evolution_log(log)
        return {"ok": True, "entry": entry}
    except Exception as e:
        return {"ok": False, "error": f"Video không tồn tại hoặc không cho nhúng: {e}"}

def get_youtube_for_slide(domain_key, idx):
    log = load_evolution_log()
    combined = list(log.get("learned_youtube_bank", [])) + list(VERIFIED_VN_YOUTUBE_BANK)
    matched = [v for v in combined if domain_key in v.get("domains", [])]
    pool = matched if matched else combined
    return pool[idx % len(pool)]

# ---------------------------------------------------------------------------
# 4. NGÂN HÀNG TRI THỨC 8 LĨNH VỰC + TỰ ĐỘNG NHẬN DIỆN CHỦ ĐỀ
# ---------------------------------------------------------------------------
DOMAIN_FRAMEWORKS = {
    "triet_ly_song": {
        "name": "Thân - Tâm - Trí & Di Sản Vượt Thời Gian",
        "match_terms": ["di sản", "ý nghĩa", "lẽ sống", "tâm", "bình an", "hạnh phúc", "thiền", "triết lý", "giá trị sống", "trung niên"],
        "keywords": ["Ý nghĩa", "Giá trị", "Di sản", "Nội tâm", "Bình an", "Khai sáng"],
        "left_brain_focus": "Quy luật tự nhiên, tâm lý học hành vi, cấu trúc sinh học não bộ",
        "right_brain_focus": "Điển tích lịch sử (Nobel, Gandhi, Van Gogh, Edison), triết lý phương Đông",
        "cards_contrast": [
            ("🌧️", "Loay hoay trong vô định, sống mòn không dấu ấn", "☀️", "Thức tỉnh sứ mệnh, kiến tạo giá trị vĩnh cửu"),
            ("⏳", "Để thời gian trôi qua trong tiếc nuối và hoài nghi", "💎", "Làm chủ từng phút giây, biến nghịch cảnh thành chất liệu"),
            ("🥀", "Theo đuổi hào nhoáng nhất thời bên ngoài", "👑", "Xây dựng thành trì nội tâm vững chãi vượt thời gian")
        ]
    },
    "lanh_dao": {
        "name": "Lãnh Đạo Vượt Bão & Quản Trị Đội Ngũ",
        "match_terms": ["lãnh đạo", "quản trị", "đội ngũ", "nhân sự", "văn hóa doanh nghiệp", "kpi", "giám đốc", "sếp", "ủy quyền"],
        "keywords": ["Tầm nhìn", "Văn hóa", "Gắn kết", "Ủy quyền", "Tạo động lực", "Đột phá"],
        "left_brain_focus": "Chỉ số KPI, quy trình tinh gọn, cơ chế phản hồi 360, ma trận Eisenhower",
        "right_brain_focus": "Nghệ thuật đắc nhân tâm, câu chuyện lãnh đạo thời chiến, sự thấu cảm",
        "cards_contrast": [
            ("🌧️", "Quản lý bằng kiểm soát và nỗi sợ hãi", "☀️", "Lãnh đạo bằng niềm tin, truyền cảm hứng và sự trao quyền"),
            ("⏳", "Đội ngũ rời rạc, làm việc thụ động chờ chỉ đạo", "💎", "Hợp nhất sức mạnh, tự chủ hành động vì mục tiêu chung"),
            ("🥀", "Lúng túng trước khủng hoảng và biến động thị trường", "👑", "Bình tĩnh định hướng, biến thách thức thành bàn đạp bứt phá")
        ]
    },
    "ban_hang": {
        "name": "Bán Hàng Giá Trị Cao & Nghệ Thuật Kể Chuyện (Storyselling)",
        "match_terms": ["bán hàng", "sale", "khách hàng", "marketing", "chốt đơn", "thương hiệu", "kể chuyện", "storytelling"],
        "keywords": ["Thấu hiểu", "Khao khát", "Nỗi đau", "Chạm cảm xúc", "Chốt đơn", "Đồng hành"],
        "left_brain_focus": "Phễu chuyển đổi, công thức FAB, phân tích ROI, kỹ thuật xử lý từ chối",
        "right_brain_focus": "Storytelling chạm não phải, khơi gợi khát khao thầm kín, xây dựng lòng tin",
        "cards_contrast": [
            ("🌧️", "Nài ép bán tính năng, khách hàng lảng tránh và từ chối", "☀️", "Trở thành cố vấn tin cậy, khách hàng chủ động tìm đến"),
            ("⏳", "Cạnh tranh bằng hạ giá, bào mòn biên lợi nhuận", "💎", "Bán giá trị độc bản, khách hàng trân quý và trung thành"),
            ("🥀", "Chốt đơn gượng gạo, giao dịch kết thúc sau một lần mua", "👑", "Đồng hành trọn đời, khách hàng tự nguyện giới thiệu bạn bè")
        ]
    },
    "cong_nghe_ai": {
        "name": "Kiến Trúc Sư AI & Làm Chủ Kỷ Nguyên Trí Tuệ Nhân Tạo",
        "match_terms": ["ai", "chatgpt", "gemini", "prompt", "trí tuệ nhân tạo", "công nghệ", "tự động hóa", "số hóa", "agent"],
        "keywords": ["Tự động hóa", "Kỹ nghệ Prompt", "Quy trình AI", "Nhân bản", "Năng suất", "Sáng tạo"],
        "left_brain_focus": "Mô hình ngôn ngữ lớn, chuỗi lệnh Agents, tự động hóa quy trình (RPA)",
        "right_brain_focus": "Cảm xúc và trực giác con người dẫn dắt AI, nhân bản giá trị nhân văn",
        "cards_contrast": [
            ("🌧️", "Hoang mang sợ AI cướp việc, làm việc thủ công quá tải", "☀️", "Làm chủ AI như trợ lý đắc lực, tăng tốc hiệu suất gấp 10 lần"),
            ("⏳", "Gõ lệnh ngô nghê, nhận kết quả chung chung vô hồn", "💎", "Thiết kế bối cảnh 4 Đúng, nhận câu trả lời xuất sắc vượt trội"),
            ("🥀", "Bị công nghệ dẫn dắt và phân tâm liên tục", "👑", "Trở thành Kiến Trúc Sư AI, kiến tạo di sản số lâu dài")
        ]
    },
    "giao_duc": {
        "name": "Đào Tạo Giảng Viên & Sư Phạm Chuyển Hóa (Train the Trainer)",
        "match_terms": ["giảng viên", "đào tạo", "sư phạm", "train the trainer", "học viên", "bài giảng", "giáo dục", "thuyết trình"],
        "keywords": ["Sư phạm", "Truyền cảm hứng", "Tương tác", "Chuyển hóa", "Trải nghiệm", "Đúc kết"],
        "left_brain_focus": "Mô hình học tập Kolb, thang đo Bloom, thiết kế bài giảng 4 MAT",
        "right_brain_focus": "Năng lượng sân khấu, chạm trái tim người học, tạo môi trường an toàn",
        "cards_contrast": [
            ("🌧️", "Thao thao bất tuyệt một chiều, học viên ngủ gật và quên sạch", "☀️", "Tổ chức không gian trải nghiệm 4D, học viên hào hứng thực hành"),
            ("⏳", "Nhồi nhét lý thuyết suông, thiếu tính ứng dụng thực tế", "💎", "Đúc kết công thức cô đọng, áp dụng ra kết quả ngay trong buổi học"),
            ("🥀", "Giảng viên mệt mỏi, năng lượng cạn kiệt sau mỗi khóa", "👑", "Tự hành chuyển giao, học viên trở thành hạt nhân lan tỏa")
        ]
    },
    "tai_chinh": {
        "name": "Tài Chính Cá Nhân Vững Bền & Thịnh Vượng Đích Thực",
        "match_terms": ["tài chính", "tiền", "đầu tư", "tài sản", "dòng tiền", "thịnh vượng", "tự do tài chính", "tiết kiệm"],
        "keywords": ["Dòng tiền", "Tài sản", "Tiêu sản", "Lãi kép", "Tự do", "Đầu tư"],
        "left_brain_focus": "Báo cáo tài chính cá nhân, quy tắc 6 chiếc lọ, lãi suất kép, quản trị rủi ro",
        "right_brain_focus": "Tâm thức thịnh vượng, lòng biết ơn dòng tiền, sự hào phóng thông thái",
        "cards_contrast": [
            ("🌧️", "Kiếm bao nhiêu tiêu bấy nhiêu, vòng xoáy nợ nần bất an", "☀️", "Làm chủ dòng tiền, kiến tạo các nguồn thu nhập thặng dư"),
            ("⏳", "Mua tiêu sản tưởng là tài sản, tài chính kiệt quệ khi biến cố", "💎", "Tích lũy tài sản sinh lời, tận dụng sức mạnh lãi kép kỳ diệu"),
            ("🥀", "Ám ảnh bởi đồng tiền, đánh mất sức khỏe và gia đình", "👑", "Thịnh vượng đích thực: Tự do tài chính gắn liền với an lạc")
        ]
    },
    "suc_khoe": {
        "name": "Sinh Khí Trẻ Hóa & Sức Khỏe Toàn Diện Thân Tâm",
        "match_terms": ["sức khỏe", "sinh khí", "trẻ hóa", "giấc ngủ", "dinh dưỡng", "vận động", "thể dục", "chữa lành", "y tế"],
        "keywords": ["Sinh khí", "Giấc ngủ", "Dinh dưỡng", "Rèn luyện", "Trẻ hóa", "Miễn dịch"],
        "left_brain_focus": "Nhịp sinh học Circadian, hormone Endorphin & Dopamine, chỉ số VO2 Max",
        "right_brain_focus": "Kết nối Mẹ Thiên Nhiên, thiền định chánh niệm, năng lượng tình yêu thương",
        "cards_contrast": [
            ("🌧️", "Thức khuya dậy muộn, cơ thể uể oải, sinh khí cạn kiệt", "☀️", "Kỷ luật bình minh, nạp đầy năng lượng tươi mới mỗi sớm mai"),
            ("⏳", "Ăn uống vô tội vạ, lười vận động, bệnh tật tích tụ âm thầm", "💎", "Dinh dưỡng thuần khiết, vận động khoa học, cơ thể nhẹ nhõm linh hoạt"),
            ("🥀", "Căng thẳng kéo dài, tâm trí rối bời, mất ngủ triền miên", "👑", "Tâm an vạn sự an, hơi thở sâu lắng nuôi dưỡng từng tế bào")
        ]
    },
    "tong_quat": {
        "name": "Chương Trình Đào Tạo Đột Phá & Chuyển Hóa Toàn Diện",
        "match_terms": [],
        "keywords": ["Đột phá", "Giải pháp", "Hành động", "Chuyển hóa", "Cam kết", "Thành công"],
        "left_brain_focus": "Quy trình từng bước, số liệu minh chứng, phương pháp luận rõ ràng",
        "right_brain_focus": "Câu chuyện cảm hứng, khát vọng vươn lên, bài học đắt giá",
        "cards_contrast": [
            ("🌧️", "Vướng mắc rào cản cũ, loay hoay tìm lối đi", "☀️", "Khai mở tầm nhìn mới, nắm bắt giải pháp đột phá"),
            ("⏳", "Chần chừ do dự, để cơ hội trôi qua tầm tay", "💎", "Hành động quyết liệt, tạo kết quả rõ rệt tức thì"),
            ("🥀", "Đơn độc vật lộn với thách thức", "👑", "Cộng hưởng sức mạnh, cùng nhau tiến xa vượt bậc")
        ]
    }
}

def auto_detect_domain(topic, sample_text=""):
    """Tự động nhận diện lĩnh vực phù hợp nhất dựa trên chủ đề và nội dung đầu vào."""
    blob = f"{topic} {sample_text}".lower()
    best_key, best_score = "triet_ly_song", 0
    for key, fw in DOMAIN_FRAMEWORKS.items():
        score = sum(2 if term in blob else 0 for term in fw.get("match_terms", []))
        if score > best_score:
            best_score = score
            best_key = key
    return best_key if best_score > 0 else "tong_quat"

# ---------------------------------------------------------------------------
# 5. TRÍCH XUẤT ĐA ĐỊNH DẠNG (.PDF, .HTML, .TXT, .MD, .JSON, ẢNH, VIDEO)
# ---------------------------------------------------------------------------
def extract_pdf_deck(pdf_path, output_dir, start_idx=1, scale=2.2):
    if not fitz:
        raise RuntimeError("PyMuPDF (fitz) chưa được cài đặt!")
    slides_img_dir = os.path.join(output_dir, "media", "slides")
    os.makedirs(slides_img_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    extracted = []
    for i in range(len(doc)):
        page_num = start_idx + i
        page = doc[i]
        text = page.get_text("text").strip()
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        tmp_png = os.path.join(slides_img_dir, f"slide_{page_num:02d}.png")
        final_webp = os.path.join(slides_img_dir, f"slide_{page_num:02d}.webp")
        pix.save(tmp_png)
        with Image.open(tmp_png) as img:
            img.save(final_webp, "WEBP", quality=90)
        extracted.append({
            "page": page_num,
            "image": f"media/slides/slide_{page_num:02d}.webp",
            "full_path": final_webp,
            "text": text
        })
    doc.close()
    return extracted

def extract_html_or_text_sections(raw_content, is_html=False, target_count=15):
    text = raw_content or ""
    if is_html:
        text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '\n', text, flags=re.S | re.I)
        text = re.sub(r'<h[1-3][^>]*>(.*?)</h[1-3]>', r'\n### \1\n', text, flags=re.S | re.I)
        text = re.sub(r'<(p|li|div|br)[^>]*>', '\n', text, flags=re.I)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = html_lib.unescape(text)

    raw_sections = re.split(r'\n(?=#{1,3}\s+)', text.strip())
    sections = []
    for sec in raw_sections:
        cleaned = "\n".join(line.strip().lstrip("#").strip() for line in sec.splitlines() if line.strip())
        if len(cleaned) >= 12:
            sections.append(cleaned)

    if len(sections) < 3:
        paras = [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if len(p.strip()) >= 12]
        if len(paras) >= 2:
            sections = paras
        else:
            lines = [l.strip() for l in text.splitlines() if len(l.strip()) >= 8]
            chunk_size = max(1, len(lines) // max(1, target_count))
            sections = ["\n".join(lines[i:i+chunk_size]) for i in range(0, len(lines), chunk_size)]

    if not sections:
        return []
    return [{"text": sec_text} for sec_text in sections[:30]]

def extract_json_sections(raw_content):
    """Phân tách bất kỳ file .JSON nào (mảng slide hoặc object cấu trúc) thành danh sách trang."""
    try:
        data = json.loads(raw_content)
    except Exception:
        return extract_html_or_text_sections(raw_content, is_html=False)

    items = []
    if isinstance(data, dict):
        if isinstance(data.get("slides"), list):
            items = data["slides"]
        elif isinstance(data.get("sections"), list):
            items = data["sections"]
        else:
            items = [{"raw_title": k, "text": json.dumps(v, ensure_ascii=False)} for k, v in data.items()]
    elif isinstance(data, list):
        items = data

    sections = []
    for item in items[:30]:
        if isinstance(item, dict):
            title = item.get("raw_title") or item.get("title") or item.get("heading") or ""
            bullets = item.get("bullets") or item.get("points") or []
            script = item.get("script") or item.get("content") or item.get("description") or ""
            lines = [str(title)] + [str(b) for b in bullets] + ([str(script)] if script else [])
            sections.append({
                "text": "\n".join(l.strip() for l in lines if str(l).strip()),
                "preset": item
            })
        else:
            sections.append({"text": str(item)})
    return sections

def generate_svg_placeholder_image(output_dir, idx, title, tag, accent="#f59e0b"):
    slides_dir = os.path.join(output_dir, "media", "slides")
    os.makedirs(slides_dir, exist_ok=True)
    svg_path = os.path.join(slides_dir, f"slide_{idx:02d}.svg")
    safe_title = html_lib.escape(title.replace("<br>", " "))[:75]
    safe_tag = html_lib.escape(tag)[:60]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1280" height="720" fill="url(#bg)"/>
  <circle cx="640" cy="340" r="360" fill="url(#glow)"/>
  <rect x="70" y="60" width="1140" height="600" rx="28" fill="none" stroke="{accent}" stroke-opacity="0.35" stroke-width="2"/>
  <text x="640" y="170" text-anchor="middle" fill="#fbbf24" font-family="Segoe UI, sans-serif" font-size="26" font-weight="700">{safe_tag}</text>
  <text x="640" y="360" text-anchor="middle" fill="#f8fafc" font-family="Segoe UI, sans-serif" font-size="46" font-weight="800">{safe_title}</text>
  <text x="640" y="575" text-anchor="middle" fill="#94a3b8" font-family="Segoe UI, sans-serif" font-size="22">KTCSxAI • 4D CINEMA 16:9 • TRUYỀN CẢM HỨNG &amp; CHUYỂN HÓA</text>
</svg>'''
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    return f"media/slides/slide_{idx:02d}.svg"

# ---------------------------------------------------------------------------
# 6. TÍCH HỢP AI TÙY CHỌN (GEMINI REST API) + SMART OFFLINE FALLBACK
# ---------------------------------------------------------------------------
def try_gemini_enrich_slides(topic, domain_key, base_slides, api_key=None):
    key = api_key or os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        return base_slides, False
    try:
        prompt = (
            f"Bạn là chuyên gia đào tạo người trung niên Việt Nam (38-58 tuổi) theo phong cách Thầy Tuấn Tử Tế (KTCSxAI).\n"
            f"Chủ đề: {topic}. Lĩnh vực: {domain_key}. Số trang: {len(base_slides)}.\n"
            f"Trả về JSON array gồm {len(base_slides)} phần tử, mỗi phần tử có: "
            f'"title" (ngắn gọn truyền cảm hứng), "bullets" (mảng 3 thông điệp sâu sắc), "script" (lời giảng 3-4 câu chạm Não Trái & Não Phải). '
            f"Chỉ trả về JSON thuần túy."
        )
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
        payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        raw_txt = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        raw_txt = re.sub(r'^```json\s*|\s*```$', '', raw_txt, flags=re.S)
        ai_items = json.loads(raw_txt)
        if isinstance(ai_items, list):
            for i, item in enumerate(ai_items[:len(base_slides)]):
                if item.get("title"):
                    base_slides[i]["raw_title"] = item["title"]
                    base_slides[i]["title"] = lock_orphan_words(item["title"])
                if isinstance(item.get("bullets"), list) and item["bullets"]:
                    base_slides[i]["bullets"] = [lock_orphan_words(b) for b in item["bullets"][:4]]
                if item.get("script"):
                    base_slides[i]["script"] = item["script"]
            return base_slides, True
    except Exception:
        pass
    return base_slides, False

# ---------------------------------------------------------------------------
# 7. TỔNG HỢP NỘI DUNG 4D ĐA PHƯƠNG THỨC
# ---------------------------------------------------------------------------
def synthesize_4d_slides(topic, domain_key="auto", extracted_pages=None, target_count=15,
                         trainer_name="Nguyễn Anh Tuấn (Tuấn Tử Tế)", output_dir=None, api_key=None):
    sample_text = " ".join(p.get("text", "")[:200] for p in (extracted_pages or [])[:5])
    if not domain_key or domain_key == "auto":
        domain_key = auto_detect_domain(topic, sample_text)

    fw = DOMAIN_FRAMEWORKS.get(domain_key, DOMAIN_FRAMEWORKS["tong_quat"])
    count = len(extracted_pages) if extracted_pages else target_count
    slides = []
    accents = ["#f59e0b", "#10b981", "#06b6d4", "#ec4899", "#8b5cf6"]

    for i in range(count):
        idx = i + 1
        page_obj = extracted_pages[i] if (extracted_pages and i < len(extracted_pages)) else {}
        page_text = page_obj.get("text", "")
        preset = page_obj.get("preset", {}) if isinstance(page_obj.get("preset"), dict) else {}

        phase_ratio = idx / count
        if phase_ratio <= 0.2:
            tag_prefix, stage_name = "🧭 KHỞI ĐẦU & THỨC TỈNH", "Thức Tỉnh Nhận Thức"
        elif phase_ratio <= 0.5:
            tag_prefix, stage_name = "💡 NỀN TẢNG CỐT LÕI", "Khám Phá Chiều Sâu"
        elif phase_ratio <= 0.8:
            tag_prefix, stage_name = "⚡ ĐỘT PHÁ & CHUYỂN HÓA", "Hành Động Thực Chiến"
        else:
            tag_prefix, stage_name = "👑 ĐÚC KẾT & DI SẢN", "Kiến Tạo Giá Trị Vĩnh Cửu"

        tag = preset.get("tag") or f"{tag_prefix} • TRANG {idx} / {count}"

        if page_text:
            lines = [l.strip() for l in page_text.splitlines() if l.strip()]
            raw_title = preset.get("raw_title") or (lines[0] if lines else f"{topic} - Phần {idx}")
            if len(raw_title) > 68:
                raw_title = raw_title[:65] + "..."
        else:
            lines = []
            raw_title = f"{topic}: {stage_name} (Phần {idx:02d})"

        title = lock_orphan_words(raw_title)

        # Resolve image: PDF/Custom Image -> SVG artistic placeholder
        if page_obj.get("image"):
            img_path = page_obj["image"]
        elif output_dir:
            img_path = generate_svg_placeholder_image(output_dir, idx, raw_title, tag, accents[i % len(accents)])
        else:
            img_path = f"media/slides/slide_{idx:02d}.webp"

        kw = fw['keywords'][idx % len(fw['keywords'])]
        if isinstance(preset.get("bullets"), list) and preset["bullets"]:
            bullets = [lock_orphan_words(b) for b in preset["bullets"][:4]]
        elif lines and len(lines) >= 3:
            b1 = lock_orphan_words(lines[1][:115])
            b2 = lock_orphan_words(lines[2][:115])
            b3 = lock_orphan_words(lines[3][:115]) if len(lines) > 3 else lock_orphan_words(f"Ứng dụng nguyên lý {kw} để tạo chuyển hóa bền vững mỗi ngày.")
            bullets = [b1, b2, b3]
        else:
            bullets = [
                lock_orphan_words(f"Thấu suốt nguyên lý cốt lõi về {kw} trong hành trình {topic}."),
                lock_orphan_words(f"Chuyển hóa tư duy từ thói quen cũ sang hành động chủ động, đầy cảm hứng."),
                lock_orphan_words(f"Thực hành ngay những bước nhỏ vững chãi để kiến tạo giá trị vượt thời gian.")
            ]

        if isinstance(preset.get("flipCards"), list) and preset["flipCards"]:
            flip_cards = preset["flipCards"]
        else:
            flip_templates = fw["cards_contrast"]
            flip_cards = []
            for c_idx in range(3):
                c_data = flip_templates[(c_idx + i) % len(flip_templates)]
                flip_cards.append({
                    "front_emoji": c_data[0],
                    "front": "TRƯỚC: " + lock_orphan_words(c_data[1]),
                    "back_emoji": c_data[2],
                    "back": "TRỞ THÀNH: " + lock_orphan_words(c_data[3])
                })

        yt_info = get_youtube_for_slide(domain_key, i)
        video_path = page_obj.get("video") or preset.get("video") or f"media/videos/slide_{idx:02d}.mp4"
        has_video = bool(page_obj.get("video") or preset.get("has_video"))

        script = preset.get("script") or (
            f"Chào mừng quý anh chị đến với Trang {idx:02d}: '{raw_title}'. "
            f"Về mặt khoa học và cấu trúc tư duy (Não Trái): Chúng ta cùng thấu suốt {fw['left_brain_focus']}, "
            f"nơi mọi kết quả đều bắt nguồn từ nhân quả rõ ràng và kỷ luật nhỏ bé mỗi ngày. "
            f"Và để thông điệp này chạm thật sâu vào trái tim (Não Phải): "
            f"Hãy chiêm nghiệm qua {fw['right_brain_focus']}. Ở độ tuổi chín muồi của cuộc đời, "
            f"mỗi trải nghiệm dù thuận lợi hay thử thách đều là viên ngọc quý để ta kiến tạo di sản. "
            f"Câu hỏi chạm tâm dành cho bạn ngay lúc này: Hôm nay bạn sẽ chọn bước đi nhỏ nào để bắt đầu chuyển hóa?"
        )

        slides.append({
            "slide_number": idx,
            "tag": tag,
            "title": title,
            "raw_title": raw_title,
            "image": img_path,
            "video": video_path,
            "audio_female": f"media/audio/slide_{idx:02d}_female.mp3",
            "audio_male": f"media/audio/slide_{idx:02d}_male.mp3",
            "bullets": bullets,
            "flipCards": flip_cards,
            "script": script,
            "flowPrompt": f"Cinematic 16:9 seamless loop, UHD. Warm inspiring visual representing {raw_title} in {fw['name']}. Golden hour light, Vietnamese inspiring aesthetic.",
            "flow_video_prompt": "Cinematic 16:9 4-second seamless loop video. Gentle camera push-in, floating golden particles, uplifting transformation. UHD 60fps.",
            "has_video": has_video,
            "image_flow": img_path,
            "image_pdf": img_path,
            "youtube_url": preset.get("youtube_url") or yt_info["url"],
            "youtube_title": preset.get("youtube_title") or yt_info["title"],
            "youtube_author": yt_info.get("author", "YouTube VN"),
            "flow_video_url": "https://flow.google.com/shared/video/572b1a60-d2e4-4059-b5a0-947337bc96c5"
        })

    slides, used_ai = try_gemini_enrich_slides(topic, domain_key, slides, api_key=api_key)
    return slides, used_ai, domain_key

# ---------------------------------------------------------------------------
# 8. HÀM TỔNG XUẤT BẢN BÀI GIẢNG 4D CINEMA V09 (FUSION MULTI-FORMAT)
# ---------------------------------------------------------------------------
def build_4d_cinema_lecture(topic, domain_key="auto", output_dir="", pdf_path=None, source_file=None,
                            source_files=None, raw_text=None, target_count=15,
                            trainer_name="Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI", api_key=None):
    os.makedirs(output_dir, exist_ok=True)
    media_dir = os.path.join(output_dir, "media")
    for sub in ["slides", "videos", "flow_images", "flow_videos", "audio"]:
        os.makedirs(os.path.join(media_dir, sub), exist_ok=True)

    # Collect all file paths (single or multi-file fusion)
    all_files = []
    for f in ([source_file, pdf_path] + (source_files or [])):
        if f and str(f).strip() and os.path.exists(str(f).strip()):
            p = str(f).strip()
            if p not in all_files:
                all_files.append(p)

    doc_pages = []
    extra_images = []
    extra_videos = []
    input_types = []

    for fpath in all_files:
        ext = Path(fpath).suffix.lower()
        if ext == ".pdf":
            input_types.append("pdf")
            doc_pages.extend(extract_pdf_deck(fpath, output_dir, start_idx=len(doc_pages) + 1))
        elif ext in [".html", ".htm"]:
            input_types.append("html")
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                doc_pages.extend(extract_html_or_text_sections(f.read(), is_html=True, target_count=target_count))
        elif ext in [".txt", ".md"]:
            input_types.append(ext.lstrip("."))
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                doc_pages.extend(extract_html_or_text_sections(f.read(), is_html=False, target_count=target_count))
        elif ext == ".json":
            input_types.append("json")
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                doc_pages.extend(extract_json_sections(f.read()))
        elif ext in IMAGE_EXTS:
            input_types.append("image")
            dest_name = f"custom_img_{len(extra_images) + 1:02d}{ext}"
            shutil.copy2(fpath, os.path.join(media_dir, "slides", dest_name))
            extra_images.append((f"media/slides/{dest_name}", Path(fpath).stem))
        elif ext in VIDEO_EXTS:
            input_types.append("video")
            dest_name = f"custom_vid_{len(extra_videos) + 1:02d}{ext}"
            shutil.copy2(fpath, os.path.join(media_dir, "videos", dest_name))
            extra_videos.append((f"media/videos/{dest_name}", Path(fpath).stem))

    if raw_text and raw_text.strip():
        input_types.append("text")
        is_html = "<html" in raw_text.lower() or "<p>" in raw_text.lower() or "<h1" in raw_text.lower()
        doc_pages.extend(extract_html_or_text_sections(raw_text, is_html=is_html, target_count=target_count))

    # Fuse extra images & videos into doc_pages (or create slides if only images/videos were provided!)
    if not doc_pages and (extra_images or extra_videos):
        total = max(len(extra_images), len(extra_videos), 1)
        for i in range(total):
            img_rel, img_stem = extra_images[i] if i < len(extra_images) else (None, "")
            vid_rel, vid_stem = extra_videos[i] if i < len(extra_videos) else (None, "")
            label = vid_stem or img_stem or f"{topic} - Phần {i + 1}"
            doc_pages.append({"text": f"{topic}: {label}", "image": img_rel, "video": vid_rel})
    else:
        for i, (img_rel, _) in enumerate(extra_images):
            if i < len(doc_pages) and not doc_pages[i].get("image"):
                doc_pages[i]["image"] = img_rel
            elif i >= len(doc_pages):
                doc_pages.append({"text": f"{topic} - Minh Họa {i + 1}", "image": img_rel})
        for i, (vid_rel, _) in enumerate(extra_videos):
            if i < len(doc_pages):
                doc_pages[i]["video"] = vid_rel
            else:
                doc_pages.append({"text": f"{topic} - Video {i + 1}", "video": vid_rel})

    extracted_pages = doc_pages[:30] if doc_pages else None
    total_slides = len(extracted_pages) if extracted_pages else target_count
    input_type_str = "+".join(dict.fromkeys(input_types)) if input_types else "topic"

    slides, used_ai, resolved_domain = synthesize_4d_slides(
        topic=topic,
        domain_key=domain_key,
        extracted_pages=extracted_pages,
        target_count=total_slides,
        trainer_name=trainer_name,
        output_dir=output_dir,
        api_key=api_key
    )

    with open(os.path.join(output_dir, "slides_data.json"), "w", encoding="utf-8") as f:
        json.dump(slides, f, ensure_ascii=False, indent=2)

    # Export Google Flow Prompts
    txt_lines, prompts_json = [], []
    for s in slides:
        idx = s["slide_number"]
        txt_lines.extend([
            f"=== SLIDE {idx:02d}: {s['raw_title']} ===",
            f"[IMAGE PROMPT]: {s['flowPrompt']}",
            f"[VIDEO PROMPT]: {s['flow_video_prompt']}",
            ""
        ])
        prompts_json.append({"slide": idx, "title": s["raw_title"], "image_prompt": s["flowPrompt"], "video_prompt": s["flow_video_prompt"]})
    with open(os.path.join(output_dir, "prompts_google_flow.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines))
    with open(os.path.join(output_dir, "prompts_google_flow.json"), "w", encoding="utf-8") as f:
        json.dump(prompts_json, f, ensure_ascii=False, indent=2)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html_out_text = f.read()

    html_out_text = html_out_text.replace("{{LECTURE_TITLE}}", topic)
    html_out_text = html_out_text.replace("{{TRAINER_NAME}}", trainer_name)
    html_out_text = html_out_text.replace("{{HEADER_BADGE}}", f"KTCSxAI • 4D CINEMA V09: {topic.upper()}")
    html_out_text = html_out_text.replace("{{SUBTITLE_INFO}}", f"Trọn bộ {total_slides} Trang Chuẩn Rạp Chiếu 16:9")
    html_out_text = html_out_text.replace("{{SLIDES_JSON}}", json.dumps(slides, ensure_ascii=False, indent=2))

    html_out = os.path.join(output_dir, "index.html")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html_out_text)

    slug = re.sub(r'[^a-zA-Z0-9]+', '-', topic.lower()).strip('-') or "bai-giang"
    with open(os.path.join(output_dir, f"{slug}-4d.html"), "w", encoding="utf-8") as f:
        f.write(html_out_text)

    bridge_src = Path(r"c:\Users\PC\Downloads\TRAIN THE TRAINERS\yt-bridge.html")
    if bridge_src.exists():
        shutil.copy2(bridge_src, os.path.join(output_dir, "yt-bridge.html"))

    bat_content = f"""@echo off
cd /d "%~dp0"
chcp 65001 > nul
title {topic} - KTCSxAI 4D CINEMA V09
start "" "http://localhost:7890/{Path(output_dir).name}/index.html"
python -m http.server 7890
"""
    with open(os.path.join(output_dir, "MO_BAI_GIANG_4D.bat"), "w", encoding="utf-8") as f:
        f.write(bat_content)

    log = load_evolution_log()
    log["version"] = "V09.0 Multi-Modal Self-Evolving"
    log.setdefault("build_history", []).insert(0, {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "topic": topic,
        "domain": resolved_domain,
        "input_type": input_type_str,
        "total_slides": total_slides,
        "mode": "Gemini AI" if used_ai else "Smart Offline Fusion",
        "output_dir": output_dir
    })
    log["build_history"] = log["build_history"][:50]
    save_evolution_log(log)

    return {
        "output_dir": output_dir,
        "html_path": html_out,
        "total_slides": total_slides,
        "used_ai": used_ai,
        "input_type": input_type_str,
        "domain": resolved_domain,
        "slides": slides
    }
