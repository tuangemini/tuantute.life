# -*- coding: utf-8 -*-
"""
KTCS 4D Universal Engine (KTCSxAI)
Hệ thống kiến tạo bài giảng HTML 4D Cinema 16:9 tự hành toàn năng
Tác giả: Tổng Chỉ Huy Tự Hành AI • Thầy Tuấn Tử Tế (Nguyễn Anh Tuấn)
"""

import os
import re
import json
import shutil
from pathlib import Path
from PIL import Image

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

# ---------------------------------------------------------------------------
# 1. QUY TẮC KHÓA TỪ MỒ CÔI TUYỆT ĐỐI (ORPHAN WORDS LOCKING)
# ---------------------------------------------------------------------------
def lock_orphan_words(text, max_len=42):
    """
    Khóa từ mồ côi:
    1. Chèn non-breaking space (\u00a0) trước từ cuối cùng để không bao giờ rớt 1 chữ.
    2. Nếu dòng dài vượt quá max_len, chủ động tách thành 2 dòng cân đối bằng thẻ <br>.
    """
    if not text:
        return ""
    text = text.strip()
    words = text.split()
    if len(words) <= 2:
        return text

    # Nếu câu dài hơn max_len, tách đôi cân bằng
    if len(text) > max_len and "<br>" not in text:
        mid_idx = len(words) // 2
        line1 = " ".join(words[:mid_idx])
        line2_words = words[mid_idx:]
        if len(line2_words) >= 2:
            line2 = " ".join(line2_words[:-1]) + "\u00a0" + line2_words[-1]
        else:
            line2 = " ".join(line2_words)
        return f"{line1}:<br>{line2}" if ":" in line1 else f"{line1}<br>{line2}"

    # Khóa 2 từ cuối cùng
    return " ".join(words[:-1]) + "\u00a0" + words[-1]

# ---------------------------------------------------------------------------
# 2. NGÂN HÀNG TRI THỨC 8 LĨNH VỰC ĐÀO TẠO ĐA NGUYÊN (DOMAIN KNOWLEDGE BANKS)
# ---------------------------------------------------------------------------
DOMAIN_FRAMEWORKS = {
    "triet_ly_song": {
        "name": "Thân - Tâm - Trí & Di Sản Vượt Thời Gian",
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

# ---------------------------------------------------------------------------
# 3. TRÍCH XUẤT TRANG PDF THÀNH ẢNH WEBP 16:9 SIÊU NÉT (PYMUPDF)
# ---------------------------------------------------------------------------
def extract_pdf_deck(pdf_path, output_dir, scale=2.5):
    """
    Trích xuất N trang PDF thành ảnh WebP 16:9 và đọc text từng trang.
    Trả về danh sách dict: [{'page': 1, 'image_path': '...', 'text': '...'}]
    """
    if not fitz:
        raise RuntimeError("PyMuPDF (fitz) chưa được cài đặt!")
    
    os.makedirs(output_dir, exist_ok=True)
    slides_img_dir = os.path.join(output_dir, "media", "slides")
    os.makedirs(slides_img_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    extracted = []

    print(f"📄 Tìm thấy {total_pages} trang trong tệp PDF: {pdf_path}")
    
    for i in range(total_pages):
        page_num = i + 1
        page = doc[i]
        text = page.get_text("text").strip()

        # Render 16:9 high-res pixmap
        matrix = fitz.Matrix(scale, scale)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        
        # Save temp PNG then optimize to WebP
        tmp_png = os.path.join(slides_img_dir, f"slide_{page_num:02d}.png")
        final_webp = os.path.join(slides_img_dir, f"slide_{page_num:02d}.webp")
        pix.save(tmp_png)
        
        with Image.open(tmp_png) as img:
            img.save(final_webp, "WEBP", quality=92)
        
        rel_webp_path = f"media/slides/slide_{page_num:02d}.webp"
        extracted.append({
            "page": page_num,
            "image": rel_webp_path,
            "full_path": final_webp,
            "text": text
        })
        print(f"  [✓] Trang {page_num:02d}/{total_pages:02d} -> {final_webp}")

    doc.close()
    return extracted

# ---------------------------------------------------------------------------
# 4. TỔNG HỢP NỘI DUNG 4D TỰ HÀNH THEO CHỦ ĐỀ & LĨNH VỰC
# ---------------------------------------------------------------------------
def synthesize_4d_slides(topic, domain_key="triet_ly_song", extracted_pages=None, target_count=15, trainer_name="Nguyễn Anh Tuấn (Tuấn Tử Tế)"):
    """
    Sinh trọn vẹn dữ liệu N trang bài giảng 4D:
    - Tiêu đề & Tag
    - 2-3 Luận điểm cốt lõi (Khóa từ mồ côi)
    - 3 Thẻ lật 3D chuyển hóa
    - Kịch bản Não Trái & Não Phải
    - Prompts Google Flow 16:9
    """
    fw = DOMAIN_FRAMEWORKS.get(domain_key, DOMAIN_FRAMEWORKS["tong_quat"])
    count = len(extracted_pages) if extracted_pages else target_count
    slides = []

    for i in range(count):
        idx = i + 1
        page_text = extracted_pages[i]["text"] if (extracted_pages and i < len(extracted_pages)) else ""
        img_path = extracted_pages[i]["image"] if (extracted_pages and i < len(extracted_pages)) else f"media/slides/slide_{idx:02d}.webp"

        # Phân tầng giai đoạn bài giảng
        phase_ratio = idx / count
        if phase_ratio <= 0.2:
            tag_prefix = "🧭 KHỞI ĐẦU & BỐI CẢNH"
            stage_name = "Thức Tỉnh Nhận Thức"
        elif phase_ratio <= 0.5:
            tag_prefix = "💡 NỀN TẢNG CỐT LÕI"
            stage_name = "Khám Phá Chiều Sâu"
        elif phase_ratio <= 0.8:
            tag_prefix = "⚡ ĐỘT PHÁ & CHUYỂN HÓA"
            stage_name = "Hành Động Thực Chiến"
        else:
            tag_prefix = "👑 ĐÚC KẾT & DI SẢN"
            stage_name = "Kiến Tạo Giá Trị Vĩnh Cửu"

        tag = f"{tag_prefix} • TRANG {idx} / {count}"

        # Trích xuất hoặc sinh tiêu đề
        if page_text:
            lines = [l.strip() for l in page_text.splitlines() if l.strip()]
            raw_title = lines[0] if lines else f"{topic} - Phần {idx}"
            if len(raw_title) > 60: raw_title = raw_title[:57] + "..."
        else:
            raw_title = f"{topic}: {stage_name} - Phần {idx:02d}"

        title = lock_orphan_words(raw_title)

        # 2-3 Luận điểm
        if page_text and len(lines) > 2:
            b1 = lock_orphan_words(lines[1][:80])
            b2 = lock_orphan_words(lines[2][:80])
            b3 = lock_orphan_words(lines[3][:80]) if len(lines) > 3 else lock_orphan_words(f"Ứng dụng nguyên lý {fw['keywords'][idx % len(fw['keywords'])]} vào thực tế.")
        else:
            kw = fw['keywords'][idx % len(fw['keywords'])]
            b1 = lock_orphan_words(f"Thấu suốt nguyên lý cốt lõi về {kw} trong bối cảnh thực tiễn.")
            b2 = lock_orphan_words(f"Chuyển hóa nhận thức từ thụ động sang chủ động kiến tạo giá trị.")
            b3 = lock_orphan_words(f"Xây dựng hành vi nhất quán, tạo đòn bẩy đột phá bền vững.")

        # 3 Thẻ bài lật 3D chuyển hóa
        flip_templates = fw["cards_contrast"]
        flip_cards = []
        for c_idx in range(3):
            c_data = flip_templates[c_idx % len(flip_templates)]
            flip_cards.append({
                "front_emoji": c_data[0],
                "front": lock_orphan_words(c_data[1]),
                "back_emoji": c_data[2],
                "back": lock_orphan_words(c_data[3])
            })

        # Kịch bản Não Trái & Não Phải
        script = (
            f"Chào mừng quý vị đến với Trang {idx:02d}: '{raw_title}'. "
            f"Về mặt khoa học và phân tích tư duy (Não Trái): Chúng ta cần nắm vững {fw['left_brain_focus']}, "
            f"nơi mọi kết quả đều được định hình bởi quy luật nhân quả và tính hệ thống rõ ràng. "
            f"Nhưng để thông điệp này thực sự đi sâu vào tiềm thức và chạm đến trái tim (Não Phải): "
            f"Hãy nhìn vào câu chuyện chuyển hóa thực tế. Khi chúng ta đối diện với thử thách bằng {fw['right_brain_focus']}, "
            f"nghịch cảnh không còn là rào cản mà trở thành bệ phóng vĩ đại nhất. "
            f"Câu hỏi lớn dành cho bạn ở trang này: Bạn sẽ chọn giữ nguyên thói quen cũ hay dũng cảm bước qua cánh cửa chuyển hóa ngay hôm nay?"
        )

        # Prompts Google Flow 16:9 Seamless Loop
        flow_prompt = (
            f"Cinematic 16:9 seamless loop, UHD, ultra-detailed. A visually striking scene representing {raw_title} in the context of {fw['name']}. "
            f"Visual elements: {fw['keywords'][idx % len(fw['keywords'])]}, soft warm golden hour light, harmonious blend of human wisdom and modern atmospheric aesthetic, inspiring mood, high-end cinema grading."
        )
        flow_video_prompt = (
            f"Cinematic 16:9 4-second seamless loop video. Gentle camera motion, ethereal glowing particles, dynamic transformation symbolizing breakthrough from challenge to wisdom. UHD, 60fps."
        )

        slides.append({
            "slide_number": idx,
            "tag": tag,
            "title": title,
            "raw_title": raw_title,
            "image": img_path,
            "video": f"media/videos/slide_{idx:02d}.mp4",
            "audio_female": f"media/audio/slide_{idx:02d}_female.mp3",
            "audio_male": f"media/audio/slide_{idx:02d}_male.mp3",
            "bullets": [b1, b2, b3],
            "flipCards": flip_cards,
            "script": script,
            "flowPrompt": flow_prompt,
            "flow_video_prompt": flow_video_prompt,
            "has_video": False,
            "image_flow": f"media/flow_images/slide_{idx:02d}.webp",
            "image_pdf": img_path,
            "youtube_url": "https://www.youtube.com/watch?v=UF8uR6Z6KLc",
            "flow_video_url": "https://flow.google.com/shared/video/572b1a60-d2e4-4059-b5a0-947337bc96c5"
        })

    return slides

# ---------------------------------------------------------------------------
# 5. HÀM TỔNG XUẤT BẢN BÀI GIẢNG 4D CINEMA (MASTER BUILDER)
# ---------------------------------------------------------------------------
def build_4d_cinema_lecture(topic, domain_key, output_dir, pdf_path=None, target_count=15, trainer_name="Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI"):
    """
    Xuất bản trọn gói một bài giảng 4D Cinema hoàn hảo:
    - Trích xuất PDF (nếu có)
    - Tạo slides_data.json
    - Tạo prompts_google_flow.txt và .json
    - Sinh file HTML 4D Cinema 16:9
    - Tạo file MO_BAI_GIANG_4D.bat
    """
    os.makedirs(output_dir, exist_ok=True)
    media_dir = os.path.join(output_dir, "media")
    for sub in ["slides", "videos", "flow_images", "flow_videos", "audio"]:
        os.makedirs(os.path.join(media_dir, sub), exist_ok=True)

    extracted_pages = None
    if pdf_path and os.path.exists(pdf_path):
        extracted_pages = extract_pdf_deck(pdf_path, output_dir)
        total_slides = len(extracted_pages)
    else:
        total_slides = target_count

    # 1. Synthesize 4D slides data
    slides = synthesize_4d_slides(topic, domain_key, extracted_pages, total_slides, trainer_name)

    # 2. Save slides_data.json
    json_path = os.path.join(output_dir, "slides_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(slides, f, ensure_ascii=False, indent=2)

    # 3. Export Google Flow Prompts
    txt_lines = []
    prompts_json = []
    for s in slides:
        idx = s["slide_number"]
        txt_lines.append(f"=== SLIDE {idx:02d}: {s['raw_title']} ===")
        txt_lines.append(f"[IMAGE PROMPT]: {s['flowPrompt']}")
        txt_lines.append(f"[VIDEO PROMPT]: {s['flow_video_prompt']}")
        txt_lines.append("")
        prompts_json.append({
            "slide": idx,
            "title": s["raw_title"],
            "image_prompt": s["flowPrompt"],
            "video_prompt": s["flow_video_prompt"]
        })

    with open(os.path.join(output_dir, "prompts_google_flow.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines))
    with open(os.path.join(output_dir, "prompts_google_flow.json"), "w", encoding="utf-8") as f:
        json.dump(prompts_json, f, ensure_ascii=False, indent=2)

    # 4. Generate HTML file from master template
    template_path = r"C:\Users\PC\Downloads\TRAIN THE TRAINERS\.agents\skills\ktcs-4d-training\templates\ktcs_4d_cinema_template.html"
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("{{LECTURE_TITLE}}", topic)
    html = html.replace("{{TRAINER_NAME}}", trainer_name)
    html = html.replace("{{HEADER_BADGE}}", f"KTCSxAI • ĐÀO TẠO 4D CINEMA: {topic.upper()}")
    html = html.replace("{{SUBTITLE_INFO}}", f"Trọn bộ {total_slides} Trang Chuẩn Rạp Chiếu 16:9")
    html = html.replace("{{SLIDES_JSON}}", json.dumps(slides, ensure_ascii=False, indent=2))

    html_out = os.path.join(output_dir, "index.html")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html)
        
    # Also save with topic slug name
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', topic.lower()).strip('-')
    topic_html = os.path.join(output_dir, f"{slug}-4d.html")
    with open(topic_html, "w", encoding="utf-8") as f:
        f.write(html)

    # 5. Create 1-click launcher BAT
    bat_content = f"""@echo off
cd /d "%~dp0"
chcp 65001 > nul
title {topic} - KTCSxAI 4D CINEMA
echo ========================================================
echo   KHOI DONG BAI GIANG 4D CINEMA 16:9 TRAP CHIEU
echo   Chu de: {topic}
echo   Giang vien: {trainer_name}
echo ========================================================
echo.
start "" "chrome.exe" --start-fullscreen "file:///%~dp0index.html"
exit
"""
    with open(os.path.join(output_dir, "MO_BAI_GIANG_4D.bat"), "w", encoding="utf-8") as f:
        f.write(bat_content)

    print(f"\n🎉 [HOÀN TẤT] Bài giảng 4D Cinema đã được kiến tạo tại:\n📁 {output_dir}")
    print(f"🎬 Mở trình chiếu: {html_out}")
    return {
        "output_dir": output_dir,
        "html_path": html_out,
        "total_slides": total_slides,
        "slides": slides
    }
