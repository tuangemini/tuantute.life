---
name: ktcs-4d-training
description: >-
  Tự động hóa toàn diện quy trình chuyển đổi tài liệu đào tạo, NotebookLM PDF hoặc chủ đề bài giảng
  thành ứng dụng trình chiếu HTML 4D Cinema 16:9 hoàn chỉnh với âm thanh Edge-TTS Nam/Nữ tiếng Việt,
  thẻ lật 3D chuyển hóa, kịch bản Não Trái & Não Phải, Hội Đồng Trí Tuệ AI, và xuất bản GitHub Pages.
---

# KỸ NĂNG: KIẾN TẠO BÀI GIẢNG HTML 4D TỰ HÀNH (KTCSxAI)

Kỹ năng này là cẩm nang tiêu chuẩn của Tổng Chỉ Huy Tự Hành AI và các thế hệ học viên, giảng viên
của **Thầy Tuấn Tử Tế (Nguyễn Anh Tuấn - Chương trình Kiến Tạo Cuộc Sống xAI / KTCSxAI)**.

---

## 🌟 NGUYÊN TẮC BÀN GIAO TỐI THƯỢNG CHO ÔNG CHỦ TUẤN TỬ TẾ

1. **LUÔN ĐƯA NGAY LIÊN KẾT TRỰC TIẾP TRONG MỌI CÂU TRẢ LỜI**:
   - Mọi câu trả lời sau khi hoàn tất công việc PHẢI đính kèm đường link `file:///...` có thể nhấp chuột trực tiếp:
     - Ứng dụng bài giảng HTML 4D: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/ktcs-thong-diep-gia-tri-di-san-4d.html`
     - Bảng điều khiển Giảng viên: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/CHAY_KTCS_TRAINER_HUB.bat`
     - Công cụ Auto Google Flow: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/CHAY_AUTO_FLOW.bat`
     - Thư mục làm việc: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/`
     - Dữ liệu 30 slide: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/slides_30_data.json`
     - Thư mục Media: `file:///c:/Users/PC/Downloads/TRAIN%20THE%20TRAINERS/media/`
   - Kèm theo đường link trực tuyến trên GitHub Pages: `https://tuantute.life/ktcs-thong-diep-gia-tri-di-san-4d.html`.

2. **GIAO SẢN PHẨM HOÀN CHỈNH, CHẠY ĐƯỢC NGAY KHÔNG CẦN CÀI ĐẶT THÊM**:
   - Trình chiếu mở được trực tiếp trên Google Chrome, Edge hoặc bất kỳ trình duyệt nào.
   - Âm thanh tiếng Việt hoạt động Offline 100% (60 file MP3 Nam/Nữ).
   - Tự động fallback Web Speech API nếu thiết bị mất kết nối mạng.

---

## 🏛️ KIẾN TRÚC KỸ THUẬT V07 TIÊU CHUẨN

### 1. Bố Cục 3 Khoang Độc Lập (3-Slot Layout) & Khắc Phục Triệt Để Lỗi Chuyển Bố Cục
- Tuyệt đối không dùng `appendChild` trực tiếp vào phần tử cha đang chuyển động để tránh lỗi `DOMException: Failed to execute 'appendChild' on 'Node': The new child element contains the parent`.
- Luôn định nghĩa 3 khoang tiếp nhận cố định:
  - `#leftSlotContainer`: Khoang dưới khung ảnh 16:9 ở cột trái.
  - `#rightCardsSlot`: Khoang thẻ lật ở cột phải.
  - `#rightScriptSlot`: Khoang kịch bản ở cột phải.
- Hai khối linh hoạt: `#cardSectionWrapper` và `#scriptBoxContainer`:
  - **`Chế độ Cân Bằng`**: Thẻ lật $\rightarrow$ `#leftSlotContainer`; Kịch bản $\rightarrow$ `#rightScriptSlot`.
  - **`Chế độ Chiếu Rạp`**: Khung ảnh trái mở rộng; Thẻ lật $\rightarrow$ `#rightCardsSlot`; Kịch bản $\rightarrow$ `#rightScriptSlot`.
  - **`Chế độ Kịch Bản Dưới Ảnh`**: Kịch bản $\rightarrow$ `#leftSlotContainer`; Thẻ lật $\rightarrow$ `#rightCardsSlot`.

### 2. Hệ Thống Hoàn Tác & Làm Lại (Undo / Redo: `Ctrl + Z` & `Ctrl + Y`)
- Mọi thao tác thay đổi trạng thái (chuyển layout, đổi slide, chuyển nguồn media) đều được lưu vào ngăn xếp `historyStack`.
- Hỗ trợ phím tắt chuẩn quốc tế:
  - **`Ctrl + Z`**: Hoàn tác trạng thái trước đó.
  - **`Ctrl + Y`** hoặc **`Ctrl + Shift + Z`**: Tái hiện trạng thái sau đó.
- Nút bấm trực quan `[↺ Hoàn tác]` và `[↻ Làm lại]` đặt ngay trên thanh công cụ Header.

### 3. Cơ Chế Sao Chép Bất Kỳ Khối Nội Dung Nào (Click-to-Copy Anywhere)
- Mọi khối nội dung (`.copyable-block`): Tiêu đề, Luận điểm, Thẻ lật, Lời giảng, Câu hỏi, Prompt:
  - Người dùng click vào là tự động copy text sạch (đã lọc thẻ HTML).
  - Khối bừng sáng viền xanh ngọc neon (`#10b981`), kèm huy hiệu nổi: `✓ Đã sao chép!`.
  - Phát âm thanh click nhẹ, tự động biến mất và hoàn trả giao diện sau 1.3 giây.
  - Hạn chế mở cửa sổ/tab mới không cần thiết để giữ trải nghiệm tập trung.
- Nút **`[✨ Prompt Slide Này]`**: Click là chép ngay câu lệnh Google Flow 16:9, nút chuyển sang `✓ Đã Chép Prompt!` màu xanh ngọc, không mở modal rườm rà.
- Nút **`[📋 Copy]`** trên kịch bản: Đổi sang `✓ Đã chép!` kèm thông báo nổi êm ái.

### 4. Tích Hợp Video Google Flow (4 Giây Tiết Kiệm Tín Dụng) & 30 Video YouTube
- **Google Flow Video (4s Seamless Loop)**:
  - Khuyến nghị học viên chỉ tạo video **4 giây** trên Google Flow để tối ưu hóa tín dụng.
  - Hỗ trợ gắn link chia sẻ Google Flow (`https://flow.google.com/shared/video/...`).
  - Hiển thị rạp chiếu 4D với nút mở xem trực tiếp trên Google Flow hoặc tải về máy để chạy offline.
- **YouTube Curated Playback**:
  - Tích hợp sẵn 30 video YouTube truyền cảm hứng, chiều sâu triết lý và khoa học não bộ phù hợp 100% với từng slide trong `slides_30_data.json`.
  - Cho phép người dùng tùy ý đổi link YouTube cho từng trang bằng nút `[🔗 Gắn Link]`.
- **Bật/Tắt Âm Thanh Gốc Của Video (`Mute / Unmute`)**:
  - Nút `[🔊 Tiếng: BẬT]` / `[🔇 Tiếng: TẮT]` ngay trên góc khung Media (phím tắt **`M`**).
  - Cho phép chạy video loop 4D đồng thời với **Thuyết minh tiếng Việt chuẩn (Nam Minh / Hoài My)** và **Nhạc thiền 432Hz**.

### 5. Thẻ Lật 3D Chuyển Hóa Với Emojis & Tương Phản Sâu Sắc
- Chiều cao thẻ `138px`, bổ sung cặp biểu tượng cảm xúc đối lập:
  - **Mặt trước (`TRƯỚC CHUYỂN HÓA`)**: Biểu tượng nỗi đau / rào cản (`🌧️`, `⏳`, `🥀`, `🌪️`, `⛓️`, `🧱`...) với viền hồng đỏ cảnh tỉnh.
  - **Mặt sau (`TRỞ THÀNH DI SẢN`)**: Biểu tượng đột phá / vượt thời gian (`☀️`, `💎`, `👑`, `🚀`, `🌟`, `🕊️`...) với ánh sáng kim cương, viền xanh lục bảo và hiệu ứng quét sáng 3D Sheen.
  - Nút copy `📋` riêng cho từng mặt thẻ.

### 6. Cuộn Mượt Mà Cả Hai Bên Cột (Smooth Scroll)
- Cả hai cột (khung ảnh/thẻ lật bên trái và nội dung bài giảng bên phải) đều có `scroll-behavior: smooth` và `overscroll-behavior: contain`.
- Thanh cuộn tùy chỉnh `7px` màu vàng kim bo tròn, dễ dàng lăn chuột hoặc vuốt chạm cảm ứng mà không bị kẹt hay cắt xén nội dung.

---

## 🚀 QUY TRÌNH 6 BƯỚC THỰC THI CHUẨN MỰC

1. **Bước 01: Thu thập PDF & Xuất ảnh 16:9**: Dùng `pymupdf` đếm đủ $N$ trang và xuất WebP $2048 \times 1152$.
2. **Bước 02: Trích xuất nội dung & Khóa từ mồ côi**: Đồng bộ $N$ trang PDF = $N$ trang HTML. Khóa từ mồ côi tuyệt đối bằng `<br>`.
3. **Bước 03: Tạo âm thanh tiếng Việt Offline**: Chạy `edge-tts` với 2 giọng `vi-VN-NamMinhNeural` và `vi-VN-HoaiMyNeural` cho toàn bộ $N$ trang.
4. **Bước 04: Nạp Media Google Flow**: Chạy `google_flow_batch_agent.py` quét thư mục Downloads, đổi tên, tối ưu WebP/MP4 16:9 và nạp vào `media/`.
5. **Bước 05: Giao diện 4D Rạp Chiếu**: Draggable Splitter, 3-slot layout, Hội Đồng AI PIP nổi, Bút vẽ Whiteboard, Tần số 432Hz.
6. **Bước 06: Kiểm định & Bàn giao**: Kiểm tra 0 lỗi DOM, 0 từ mồ côi, đồng bộ sang GitHub Pages `tuantute.life` và cung cấp link mở trực tiếp cho Thầy.

---

## ⌨️ BẢNG PHÍM TẮT THAO TÁC NHANH

| Phím tắt | Tác vụ |
| :---: | :--- |
| **`Ctrl + Z`** | Hoàn tác thao tác trước (Bố cục, Slide, Media) |
| **`Ctrl + Y`** / **`Ctrl + Shift + Z`** | Làm lại thao tác kế tiếp |
| **`M`** | Bật / Tắt âm thanh gốc của Video (`Mute / Unmute`) |
| **`Space`** / **`→`** / **`PageDown`** | Sang trang tiếp theo |
| **`←`** / **`PageUp`** | Quay lại trang trước |
| **`K`** | Bật / Tắt thuyết minh tiếng Việt Edge-TTS |
