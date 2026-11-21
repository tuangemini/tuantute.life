# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QA) — BÀI GIẢNG 4D V08.7

**Chủ đề:** KHAI PHÓNG NGƯỜI THẦY BÊN TRONG: TỪ CÂU HỎI CHUYỂN HÓA (THÁP 6 TẦNG LOGICAL LEVELS) & KỶ LUẬT HÀNH ĐỘNG ĐẾN DI SẢN SỐ xAI  
**Ngày kiểm định:** 20/11/2026 (Chuẩn bị cho buổi học Tối Thứ Bảy 21/11/2026)  
**Tệp chính:** `D:\Users\Downloads\WEBSITE\KTCS-Khai-Phong-Nguoi-Thay-22-Trang\ktcs-khai-phong-nguoi-thay-22-trang-4d.html`

---

## 1. KẾT QUẢ KIỂM ĐỊNH TỰ ĐỘNG TRÊN CHROME THẬT (CDP PORT 9225 • SERVER PORT 7890)
- **URL kiểm thử:** `http://localhost:7890/ktcs-khai-phong-nguoi-thay-22-trang-4d.html`
- **Lỗi JavaScript (Console / Runtime):** `0` lỗi
- **Lỗi tài nguyên 404 (Local Server 7890):** `0` lỗi
- **Số lượng Slide (`SLIDES.length`):** `22 / 22` trang hiển thị đầy đủ tiêu đề, luận điểm, kịch bản và 3 thẻ bài lật 3D/trang
- **Dữ liệu `#bot-data-v17`:** `22` phần tử (`out`, `title`, `video_prompt`, `prompt`) tương thích `04_Auto_Video_Flow_V20.py`
- **Chuyển đổi 3 Chế độ Bố cục:** `['cinema', 'script-left', 'balanced']` hoạt động mượt mà
- **Thẻ Lật 3D & Tung Hoa:** `flipAllCards(true)` lật đủ `3/3` thẻ kèm hiệu ứng tung hoa & âm thanh đàn hạc
- **Bảng tra cứu `🔺 6 Tầng Tư Duy` (Logical Levels - Robert Dilts):** Mở/đóng, đối chiếu Câu hỏi bị động (*Đời đo mình*) vs Câu hỏi chuyển hóa (*Đây đo đời*) trên 6 tầng và nút nhảy tới Trang 02 hoạt động chuẩn xác
- **Hội Đồng Trí Tuệ AI (`🏛️ Hội Đồng AI`):** Mở cửa sổ PiP, tự đổi nhân vật cố vấn theo từng trang, gửi câu hỏi và nhận phản hồi ngữ nghĩa thành công (`3` tin nhắn trong phiên test)
- **Bảng Vẽ Toàn Màn Hình (`✏️ Vẽ`):** Bật/tắt `#drawCanvas.active` và `#drawToolbar` thành công
- **Âm thanh Edge-TTS & Slow-Mo:** Đã tạo đủ **44/44 tệp MP3** (`slide_01_female.mp3..slide_22_female.mp3` giọng `vi-VN-HoaiMyNeural` và `slide_01_male.mp3..slide_22_male.mp3` giọng `vi-VN-NamMinhNeural`), chuyển đổi giọng Nam/Nữ và tua chậm `0.5x` hoạt động bình thường.

## 2. TÀI NGUYÊN MEDIA & YOUTUBE TIẾNG VIỆT
- **Ảnh Slide & Ảnh Nghệ Thuật 16:9 (`.webp`):** Đã tạo đủ 22 ảnh `media/slides/slide_01.webp..slide_22.webp` và 22 ảnh `media/flow_images/slide_01.webp..slide_22.webp` (1280×720).
- **Video Google Flow (`.mp4`):** Chưa có trình duyệt Google Flow đang mở khi chạy tác vụ, nên đã nhúng sẵn `04_Auto_Video_Flow_V20.py` và `#bot-data-v17` chuẩn 22 trang để Thầy chạy xuất `.mp4` bất cứ lúc nào.
- **22 Video YouTube:** Đã tìm kiếm và xác thực qua YouTube oEmbed API (`200 OK`) cho đủ 22/22 trang.

## 3. XUẤT BẢN GITHUB PAGES (`tuangemini/tuantute.life`)
- Đã đồng bộ lên nhánh `main` của kho `https://github.com/tuangemini/tuantute.life.git` (commit `2edaf62`) tại thư mục con `ktcs-khai-phong-nguoi-thay-22-trang-4d/` và gắn thẻ bài giảng mới lên đầu `index.html` mà **không ghi đè** bất kỳ bài giảng cũ nào (`ktcs-thong-diep-gia-tri-di-san-4d.html` vẫn nguyên vẹn).
