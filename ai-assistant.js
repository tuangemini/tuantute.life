/**
 * AI ASSISTANT CHATBOT (DEEPSEEK & GOOGLE GEMINI) - TUẤN TỬ TẾ (tuantute.life)
 * Tự động giải đáp 24/7 mọi thắc mắc về Anh Nguyễn Anh Tuấn (Tuấn Tử Tế Từ Tâm),
 * triết lý sống tử tế, sự rộng lượng, hệ sinh thái GTO Media,
 * Hội Doanh Nhân Trẻ Khánh Hòa, kiến tạo cuộc sống kỷ nguyên AI và gia đình.
 */

(function () {
  'use strict';

  // Mã hóa Base64 an toàn cho key hệ thống mặc định
  const DEFAULT_DEEPSEEK_KEY = atob('c2stNmJjZDIxMDJhZTQ1NDIxYWE5NjlkNjE3MmM2MzA2NGY=');
  const DEFAULT_GEMINI_KEY = atob('QVEuQWI4Uk42SkRIa1E3WTJjcEhIUGt0Y3pEdHdpY2RJaHFLZjBDUEZCMFRCMnZtNEtzNnc=');

  const AI_CONFIG = {
    provider: localStorage.getItem('ttt_ai_provider') || 'deepseek',
    deepseekKey: localStorage.getItem('ttt_deepseek_key') || DEFAULT_DEEPSEEK_KEY,
    geminiKey: localStorage.getItem('ttt_gemini_key') || DEFAULT_GEMINI_KEY,
    geminiModel: 'gemini-3.8-flash',
    deepseekModel: 'deepseek-chat',
    maxHistory: 10
  };

  const SYSTEM_KNOWLEDGE = `
Bạn là "Trợ lý AI của Doanh nhân Nguyễn Anh Tuấn (Tuấn Tử Tế • Từ Tâm)" - đại diện số thông minh, thanh lịch, uyên bác và giàu lòng nhân ái trên website tuantute.life.

THÔNG TIN CHÍNH THỨC VỀ DOANH NHÂN NGUYỄN ANH TUẤN:
- Họ và tên: NGUYỄN ANH TUẤN (Thương hiệu cá nhân: Tuấn Tử Tế • Từ Tâm).
- Trang Facebook chính thức: https://www.facebook.com/TuanTuTeTT (5.5K+ Followers).
- Kênh YouTube: @TuấnTửTếTừTâm (https://www.youtube.com/@Tu%E1%BA%A5nT%E1%BB%ADT%E1%BA%BFT%E1%BB%ABT%C3%A2m).
- Email liên hệ: tuan@media-gto.com.
- Website cá nhân: https://tuantute.life/
- Ngày sinh: 02 / 01 / 1977 (Tuổi Bính Thìn).
- Hậu phương gia đình: MỘT vợ + HAI con gái. Kỷ niệm ngày cưới: 19 / 12 / 2005.

MỤC TIÊU KẾT NỐI CHÍNH • CỘNG ĐỒNG ZALO xAI:
- Nhóm Zalo chính thức: **Phát Triển Bản Thân - Tâm - Trí xAI** (Link: https://zalo.me/g/irsrqz032).
- Lớp học trực tuyến hàng tuần: **20h00 tối Thứ Tư & Thứ Bảy** trên Zoom (hoàn toàn miễn phí, phụng sự cộng đồng).
- Mục tiêu nhóm: Cùng học tập, rèn luyện Thân - Tâm - Trí, nhận kịch bản ứng dụng AI thực chiến, giao lưu trực tiếp cùng Thầy Nguyễn Anh Tuấn.
- LƯU Ý BẢO MẬT: Tuyệt đối KHÔNG cung cấp bất kỳ số tài khoản ngân hàng nào. Học viên tham gia hoàn toàn qua nhóm Zalo chính thức https://zalo.me/g/irsrqz032.

KIẾN THỨC VỀ CÁC BÀI GIẢNG TRÊN WEBSITE TUANTUTE.LIFE:
1. BÀI GIẢNG "BÁC SĨ GLENN CUNNINGHAM - NGƯỜI CHẠY NHANH NHẤT THẾ GIỚI":
   - Nhân vật: Bác sĩ / Tiến sĩ Glenn Cunningham (1909 - 1988), huyền thoại "Người sắt Kansas".
   - Bi kịch năm 7 tuổi: Vụ nổ lò sưởi thiêu rụi đôi chân, anh trai qua đời, bác sĩ bảo sẽ tàn phế suốt đời.
   - Lời thề với mẹ: "Con không chỉ đi mà con sẽ CHẠY!". Suốt 2 năm nằm liệt, tự xoa bóp, bám cọc rào tập đứng.
   - Phát hiện kỳ diệu: Khi bước đi quá buốt đau, cậu bé phát hiện "Chạy thì ít đau hơn đi bộ" vì chân chạm đất ngắn hơn.
   - Đỉnh cao: Lập Kỷ lục thế giới cự ly 1 dặm (4:06.8) tại Madison Square Garden 1934; Huy chương Bạc Olympic Berlin 1936.
   - Di sản: Lấy bằng Tiến sĩ Giáo dục, mở trang trại Youth Ranch nuôi dạy hơn 9.000 đứa trẻ cơ nhỡ.
   - Ứng dụng cho người trung niên Việt Nam (38 - 59 tuổi): Nỗi sợ tuổi tác hay công nghệ chỉ là ảo ảnh. Kinh nghiệm sống quý báu kết hợp với "đôi chân thần tốc AI" sẽ tạo nên sức mạnh vô song! Rèn luyện 6 thói quen Thân - Tâm - Trí mỗi ngày.

2. BÀI GIẢNG "BÍ MẬT CỦA MAY MẮN THẬT SỰ" (KTCSxAI):
   - Châm ngôn: "May mắn là khi sự chuẩn bị gặp gỡ cơ hội" (Seneca).
   - 12 bài học tự tạo may mắn: Tự tạo may mắn, theo đuổi đến cùng, dám đổi môi trường, biết cho đi, không trì hoãn, chú ý chi tiết nhỏ, tin vào điều đã xây, may mắn không mua được, kiên trì, cơ hội đến với tất cả, cội nguồn ở chính bạn, không bao giờ quá trễ.
   - Mô phỏng Cây Bốn Lá: Cơ hội như mưa hạt giống rơi xuống mọi người, chỉ mảnh đất chuẩn bị 7 đức tính (Biết ơn, Yêu thương, Phát triển bản thân, Rèn luyện Thân Tâm Trí, Thực hành, Kiên trì, Tin tưởng) mới nảy mầm Cây Bốn Lá.
   - Bánh xe cuộc đời 6 múi: Thể lực, Vận động, Bình an, Kết nối, Học tập, Dùng AI (cần to và tròn đều để lăn xa).
   - Công thức Lệnh Vàng AI 4 bước: VAI TRÒ + VIỆC CẦN LÀM + BỐI CẢNH + ĐỊNH DẠNG.

3. BÀI GIẢNG "CHỈ HUY TÂM THỨC SIÊU CHUYÊN CƠ A388":
   - Tháp 6 tầng nhận thức (Logical Levels): Môi trường -> Hành vi -> Năng lực -> Niềm tin/Giá trị -> Nhân dạng -> Sứ mệnh.
   - Tháp nhu cầu Maslow 5 tầng: Sinh lý -> An toàn -> Xã hội -> Tôn trọng -> Tự thể hiện đỉnh cao.
   - Tư duy Cơ trưởng: Bạn là người cầm lái cỗ máy cuộc đời mình, không để thời tiết hay hoàn cảnh bên ngoài quyết định đích đến.

4. ỨNG DỤNG NOTEBOOKLM & TỰ ĐỘNG HÓA 24/7:
   - Biến tài liệu thành trợ lý thông minh trò chuyện 24/7.
   - Tạo website cá nhân bằng giọng nói thông qua Gemini & GitHub Pages.
   - Kết nối tự động hóa Website + Google Sheets + Telegram Bot chăm sóc học viên tự động.

VĂN PHONG GIAO TIẾP:
- Xưng hô: "Chào bạn! Tôi là Trợ lý AI của Anh Tuấn Tử Tế".
- Giọng điệu ấm áp, hào sảng, trí tuệ, luôn khích lệ tinh thần và kết thúc bằng lời mời tham gia nhóm Zalo https://zalo.me/g/irsrqz032 để nhận trọn bộ tài liệu và lịch học Zoom!
`;

  let chatHistory = [
    {
      role: 'assistant',
      content: 'Chào bạn! Tôi là **Trợ lý AI của Anh Nguyễn Anh Tuấn (Tuấn Tử Tế • Từ Tâm)**. Rất vui được đón tiếp bạn ghé thăm tuantute.life! Bạn cần tìm hiểu thông tin về triết lý sống tử tế, cơ hội hợp tác cùng **GTO Media**, ứng dụng **Kỷ nguyên AI**, hay kết nối cá nhân cùng Anh Tuấn hôm nay ạ?'
    }
  ];

  function formatMarkdown(text) {
    if (!text) return '';
    let html = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/(?:^|\n)[*-]\s+(.+)/g, '\n<li>$1</li>');
    html = html.replace(/(<li>.*?<\/li>)/gs, '<ul>$1</ul>');
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" style="color:#fde047; text-decoration:underline;">$1</a>');
    html = html.replace(/\n\n+/g, '<br><br>').replace(/\n/g, '<br>');
    return html;
  }

  function getSmartFallbackReply(question) {
    const q = question.toLowerCase();

    if (q.includes('zalo') || q.includes('nhóm') || q.includes('cộng đồng') || q.includes('tham gia') || q.includes('đăng ký') || q.includes('lớp') || q.includes('zoom') || q.includes('học')) {
      return `🤝 <strong>Cộng Đồng: Phát Triển Bản Thân - Tâm - Trí xAI:</strong><br><br>` +
        `Mời bạn tham gia ngay nhóm Zalo chính thức của Thầy Nguyễn Anh Tuấn để cùng rèn luyện và nhận tài liệu thực chiến:<br><br>` +
        `👉 <strong>Link tham gia nhóm Zalo:</strong> <a href="https://zalo.me/g/irsrqz032" target="_blank" rel="noopener noreferrer" style="color:#fde047; font-weight:800; text-decoration:underline;">https://zalo.me/g/irsrqz032</a><br><br>` +
        `• <strong>Lịch học trực tuyến:</strong> 20h00 tối Thứ 4 & Thứ 7 hàng tuần trên Zoom (hoàn toàn miễn phí, phụng sự cộng đồng).<br>` +
        `• <strong>Nội dung:</strong> Rèn luyện Thân - Tâm - Trí, ứng dụng Trí tuệ AI thực chiến cho người trung niên và doanh nghiệp!`;
    }

    if (q.includes('cunningham') || q.includes('chạy') || q.includes('người chạy') || q.includes('điền kinh') || q.includes('kỷ lục') || q.includes('bác sĩ')) {
      return `🏃‍♂️ <strong>Huyền Thoại Bác Sĩ Glenn Cunningham – Người Chạy Nhanh Nhất Thế Giới:</strong><br><br>` +
        `• <strong>Ý chí phi thường:</strong> 7 tuổi bị bỏng nặng đôi chân, bác sĩ bảo tàn phế. Nhưng cậu bé thề với mẹ: <em>"Con không chỉ đi mà con sẽ CHẠY!"</em>.<br>` +
        `• <strong>Kỷ lục thế giới:</strong> Năm 1934, ông lập Kỷ lục thế giới chạy 1 dặm (4:06.8) tại Madison Square Garden và đoạt Huy chương Bạc Olympic 1936.<br>` +
        `• <strong>Di sản:</strong> Lấy bằng Tiến sĩ Giáo dục, cưu mang hơn 9.000 đứa trẻ khó khăn.<br>` +
        `• <strong>Bài học cho người trung niên thời AI:</strong> Đừng bao giờ tự ti về tuổi tác hay công nghệ. Hãy coi AI là "đôi chân thần tốc mới" kết hợp cùng vốn sống quý báu của bạn để bứt phá!<br><br>` +
        `👉 Mời bạn vào nhóm Zalo để nhận bài giảng chi tiết: <a href="https://zalo.me/g/irsrqz032" target="_blank" rel="noopener noreferrer">https://zalo.me/g/irsrqz032</a>`;
    }

    if (q.includes('may mắn') || q.includes('12 bài') || q.includes('cây bốn lá') || q.includes('seneca')) {
      return `🍀 <strong>Bí Mật Của May Mắn Thật Sự:</strong><br><br>` +
        `<blockquote><em>“May mắn là khi sự chuẩn bị gặp gỡ cơ hội.” (Seneca)</em></blockquote><br>` +
        `• Cơ hội như mưa hạt giống rơi đều xuống tất cả mọi người, nhưng chỉ mảnh đất chuẩn bị <strong>7 đức tính</strong> (Biết ơn, Yêu thương, Phát triển bản thân, Rèn Thân-Tâm-Trí, Thực hành, Kiên trì, Tin tưởng) mới nảy mầm Cây Bốn Lá.<br>` +
        `• <strong>Nguyên tắc vàng:</strong> Bạn là Kiến trúc sư thiết kế, bạn là Chủ công trình quyết định, AI là Đội thợ giỏi thi công!<br><br>` +
        `👉 Tham gia nhóm Zalo học viên: <a href="https://zalo.me/g/irsrqz032" target="_blank" rel="noopener noreferrer">https://zalo.me/g/irsrqz032</a>`;
    }

    if (q.includes('a388') || q.includes('chuyên cơ') || q.includes('6 tầng') || q.includes('nhận thức') || q.includes('maslow')) {
      return `✈️ <strong>Chỉ Huy Tâm Thức Siêu Chuyên Cơ A388:</strong><br><br>` +
        `• <strong>Tháp 6 tầng nhận thức:</strong> Môi trường → Hành vi → Năng lực → Niềm tin/Giá trị → Nhân dạng → Sứ mệnh.<br>` +
        `• <strong>Tư duy Cơ trưởng:</strong> Khi xác định rõ Sứ mệnh phụng sự và Nhân dạng lãnh đạo tử tế, bạn sẽ vượt qua mọi giông bão cuộc đời để hạ cánh an toàn và hạnh phúc!<br><br>` +
        `👉 Nhận tài liệu A388 tại nhóm Zalo: <a href="https://zalo.me/g/irsrqz032" target="_blank" rel="noopener noreferrer">https://zalo.me/g/irsrqz032</a>`;
    }

    if (q.includes('lệnh vàng') || q.includes('prompt') || q.includes('công thức')) {
      return `🤖 <strong>Công Thức "Lệnh Vàng" AI Trong 4 Bước:</strong><br><br>` +
        `<strong>VAI TRÒ + VIỆC CẦN LÀM + BỐI CẢNH + ĐỊNH DẠNG</strong><br><br>` +
        `Ví dụ: <em>"Hãy đóng vai Thư ký riêng. Việc cần làm: Soạn tin nhắn cảm ơn đối tác sau sự kiện. Bối cảnh: Tôi 48 tuổi, kinh doanh du lịch Nha Trang. Định dạng: 3 gạch đầu dòng ngắn gọn, chân thành."</em><br><br>` +
        `👉 Cùng thực hành tại nhóm Zalo: <a href="https://zalo.me/g/irsrqz032" target="_blank" rel="noopener noreferrer">https://zalo.me/g/irsrqz032</a>`;
    }


    if (q.includes('rộng lượng') || q.includes('châm ngôn') || q.includes('triết lý') || q.includes('tử tế')) {
      return `✨ <strong>Triết lý sống của Anh Tuấn Tử Tế:</strong><br><br>` +
        `<blockquote><em>“Sự rộng lượng là thước đo trình độ sống.”<br>(Generosity is a measure of life's level)</em></blockquote><br>` +
        `Đối với Anh Tuấn, sống tử tế không phải là điều gì to tát, mà là sự chân thành trong từng ánh mắt, nụ cười, cách đối xử trân trọng với gia đình, bạn bè, đối tác và luôn sẵn sàng cho đi (Givers Gain) để cùng nhau tạo dựng một cuộc sống tốt đẹp hơn!`;
    }

    if (q.includes('gto') || q.includes('media') || q.includes('sự kiện') || q.includes('mice')) {
      return `🏢 <strong>GTO Media Corporation (Since 2009):</strong><br><br>` +
        `• <strong>Chủ tịch HĐQT:</strong> Doanh nhân Nguyễn Anh Tuấn.<br>` +
        `• <strong>Lĩnh vực thế mạnh:</strong> Tổ chức lễ hội quy mô quốc gia (Festival Biển Nha Trang), sự kiện văn hóa, du lịch, hội nghị quốc tế MICE và chiến lược truyền thông.<br>` +
        `• <strong>Trụ sở:</strong> Biệt thự C10 - C11 KĐT Hưng Phú, TP. Nha Trang, Khánh Hòa.<br>` +
        `• <strong>Website:</strong> <a href="https://gto.vn" target="_blank">gto.vn</a> &bull; <a href="http://gtomedia.vn" target="_blank">gtomedia.vn</a>.`;
    }

    if (q.includes('hội doanh nhân trẻ') || q.includes('kết nối') || q.includes('mạng lưới') || q.includes('doanh nhân') || q.includes('hợp tác')) {
      return `🤝 <strong>Hội Doanh Nhân Trẻ Khánh Hòa & Mạng Lưới Doanh Nhân:</strong><br><br>` +
        `• Anh Tuấn giữ vị trí <strong>Phó Chủ tịch Hội Doanh Nhân Trẻ Khánh Hòa</strong>, luôn tích cực phụng sự, đồng hành cùng các thế hệ khởi nghiệp, chia sẻ kinh nghiệm quản trị và chuyển đổi số.<br>` +
        `• <strong>Kiến tạo cuộc sống Kỷ nguyên AI:</strong> Giúp học viên và doanh nghiệp ứng dụng AI thực chiến, tự động hóa 24/7 để vừa thành công trong sự nghiệp vừa thảnh thơi sống an lạc.`;
    }

    if (q.includes('gia đình') || q.includes('vợ') || q.includes('con') || q.includes('sinh nhật') || q.includes('ngày cưới')) {
      return `👨‍👩‍👧‍👧 <strong>Tổ ấm gia đình - Điểm tựa vững chắc nhất của Anh Tuấn:</strong><br><br>` +
        `• Hậu phương thiêng liêng: <strong>MỘT vợ + HAI con gái</strong> ngoan ngoãn, đáng yêu.<br>` +
        `• <strong>Kỷ niệm ngày cưới:</strong> 19 / 12 / 2005.<br>` +
        `• <strong>Ngày sinh:</strong> 02 / 01 / 1977 (Tuổi Bính Thìn).<br><br>` +
        `Gia đình chính là nguồn động lực lớn nhất để Anh Tuấn không ngừng phụng sự xã hội và lan tỏa năng lượng tử tế mỗi ngày!`;
    }

    if (q.includes('facebook') || q.includes('fb') || q.includes('liên hệ') || q.includes('email') || q.includes('gặp')) {
      return `📞 <strong>Kênh kết nối chính thức cùng Anh Tuấn:</strong><br><br>` +
        `• <strong>Facebook cá nhân:</strong> <a href="https://www.facebook.com/TuanTuTeTT" target="_blank">facebook.com/TuanTuTeTT</a> (5.5K+ Followers).<br>` +
        `• <strong>Kênh YouTube:</strong> <a href="https://www.youtube.com/@Tu%E1%BA%A5nT%E1%BB%ADT%E1%BA%BFT%E1%BB%ABT%C3%A2m" target="_blank">@TuấnTửTếTừTâm</a>.<br>` +
        `• <strong>Email công việc:</strong> <a href="mailto:tuan@media-gto.com">tuan@media-gto.com</a>.<br>` +
        `• <strong>Địa chỉ:</strong> Biệt thự C10 - C11 KĐT Hưng Phú, TP. Nha Trang, Khánh Hòa.`;
    }

    return `Doanh nhân Nguyễn Anh Tuấn (Tuấn Tử Tế Từ Tâm) luôn trân trọng mọi cơ hội kết nối, hợp tác và lan tỏa giá trị tốt đẹp đến cộng đồng. Bạn có thể kết nối trực tiếp qua trang Facebook chính thức: <strong><a href="https://www.facebook.com/TuanTuTeTT" target="_blank">fb.com/TuanTuTeTT</a></strong> hoặc email: <strong>tuan@media-gto.com</strong> bạn nhé!`;
  }

  async function callDeepSeekAPI(messages) {
    const formattedMessages = [
      { role: 'system', content: SYSTEM_KNOWLEDGE },
      ...messages.slice(-AI_CONFIG.maxHistory)
    ];

    const response = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${AI_CONFIG.deepseekKey}`
      },
      body: JSON.stringify({
        model: AI_CONFIG.deepseekModel,
        messages: formattedMessages,
        temperature: 0.7,
        max_tokens: 650
      })
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`DeepSeek error (${response.status}): ${err}`);
    }

    const data = await response.json();
    return data.choices?.[0]?.message?.content || '';
  }

  async function callGeminiAPI(messages) {
    const contents = messages.slice(-AI_CONFIG.maxHistory).map(m => ({
      role: m.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: m.content }]
    }));

    const url = `https://generativelanguage.googleapis.com/v1beta/models/${AI_CONFIG.geminiModel}:generateContent?key=${AI_CONFIG.geminiKey}`;

    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: contents,
        systemInstruction: {
          parts: [{ text: SYSTEM_KNOWLEDGE }]
        },
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 650
        }
      })
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`Gemini error (${response.status}): ${err}`);
    }

    const data = await response.json();
    return data.candidates?.[0]?.content?.parts?.[0]?.text || '';
  }

  async function requestAIResponse(userText) {
    chatHistory.push({ role: 'user', content: userText });

    const primary = AI_CONFIG.provider;
    const backup = primary === 'deepseek' ? 'gemini' : 'deepseek';

    try {
      if (primary === 'deepseek') {
        const reply = await callDeepSeekAPI(chatHistory);
        if (reply) return { reply, provider: 'DeepSeek AI' };
      } else {
        const reply = await callGeminiAPI(chatHistory);
        if (reply) return { reply, provider: 'Gemini AI' };
      }
    } catch (e1) {
      console.warn(`[Tuấn Tử Tế AI] ${primary} failed, trying ${backup}:`, e1.message);
      try {
        if (backup === 'deepseek') {
          const reply = await callDeepSeekAPI(chatHistory);
          if (reply) return { reply, provider: 'DeepSeek AI (Backup)' };
        } else {
          const reply = await callGeminiAPI(chatHistory);
          if (reply) return { reply, provider: 'Gemini AI (Backup)' };
        }
      } catch (e2) {
        console.warn(`[Tuấn Tử Tế AI] Both APIs failed, fallback to local knowledge:`, e2.message);
      }
    }

    const fallback = getSmartFallbackReply(userText);
    return { reply: fallback, provider: 'Trợ lý Tuấn Tử Tế' };
  }

  function renderAIAssistant() {
    const fab = document.createElement('div');
    fab.className = 'ai-fab-launcher';
    fab.id = 'aiFabLauncher';
    fab.setAttribute('role', 'button');
    fab.setAttribute('aria-label', 'Mở trợ lý AI Tuấn Tử Tế');
    fab.innerHTML = `
      <div class="ai-fab-icon-box">
        <span class="ai-fab-pulse-ring"></span>
        <span>✨</span>
      </div>
      <div class="ai-fab-text">
        <span class="ai-fab-title">Hỏi Tuấn Tử Tế</span>
        <span class="ai-fab-sub">Tư vấn tử tế, truyền cảm hứng 24/7</span>
      </div>
      <span class="ai-fab-badge">&#10084;</span>
    `;

    const chatWin = document.createElement('div');
    chatWin.className = 'ai-chat-window';
    chatWin.id = 'aiChatWindow';
    chatWin.setAttribute('role', 'dialog');
    chatWin.setAttribute('aria-label', 'Cửa sổ trò chuyện Trợ lý AI Tuấn Tử Tế');
    chatWin.innerHTML = `
      <!-- Header -->
      <div class="ai-chat-header">
        <div class="ai-chat-profile">
          <div class="ai-avatar">
            <img src="avatar.jpg" alt="Tuấn Tử Tế">
            <span class="ai-online-dot"></span>
          </div>
          <div class="ai-profile-meta">
            <div class="ai-title">
              <span>Tuấn Tử Tế</span>
              
            </div>
            <span class="ai-status-text">Doanh nhân truyền cảm hứng • Kỷ Nguyên AI</span>
          </div>
        </div>
        <div class="ai-header-actions">
          <button class="ai-icon-btn" id="btnAiSettings" style="display:none;" aria-label="Cài đặt">⚙️</button>
          <button class="ai-icon-btn" id="btnAiClear" title="Xóa lịch sử chat" aria-label="Xóa chat">🗑️</button>
          <button class="ai-icon-btn" id="btnAiClose" title="Thu nhỏ" aria-label="Đóng">&times;</button>
        </div>
      </div>

      <!-- Quick Suggestion Chips -->
      <div class="ai-chips-bar" id="aiChipsBar">
        <button class="ai-chip" data-q="Triết lý sống 'Sự rộng lượng là thước đo trình độ sống' của Anh Tuấn là gì?">✨ Triết lý sự rộng lượng?</button>
        <button class="ai-chip" data-q="Giới thiệu về hệ sinh thái GTO Media và ứng dụng Kỷ nguyên AI?">🏢 GTO Media & Kỷ Nguyên AI?</button>
        <button class="ai-chip" data-q="Chia sẻ về hậu phương gia đình thiêng liêng của Anh Tuấn?">👨‍👩‍👧‍👧 Hạnh phúc gia đình?</button>
        <button class="ai-chip" data-q="Làm thế nào để kết nối Facebook và liên hệ hợp tác cùng Anh Tuấn?">📞 Kết nối Facebook & Hợp tác?</button>
        <button class="ai-chip" data-q="Anh Tuấn có những hoạt động chia sẻ kỹ năng và ứng dụng AI nào?">🤖 Đào tạo & Ứng dụng AI?</button>
      </div>

      <!-- Chat Messages Body -->
      <div class="ai-chat-body" id="aiChatBody">
        <div class="ai-msg bot">
          <div class="ai-msg-avatar"><img src="avatar.jpg" alt="Tuấn Tử Tế"></div>
          <div class="ai-msg-bubble">
            ${formatMarkdown(chatHistory[0].content)}
          </div>
        </div>
      </div>

      <!-- Input Form Footer -->
      <div class="ai-chat-footer">
        <form class="ai-input-form" id="aiChatForm">
          <textarea 
            class="ai-input-field" 
            id="aiInputField" 
            rows="1" 
            placeholder="Hỏi về triết lý sống tử tế, GTO Media, Kỷ nguyên AI, hợp tác..."
            aria-label="Nhập câu hỏi"
          ></textarea>
          <button type="submit" class="ai-send-btn" id="aiSendBtn" aria-label="Gửi tin nhắn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M22 2L11 13M22 2L15 22L11 13L2 9L22 2Z"></path>
            </svg>
          </button>
        </form>
        <div class="ai-footer-note">Tuấn Tử Tế • Phụng sự từ tâm 24/7 • Sống tử tế & Tự do</div>
      </div>

      <!-- Settings Overlay Modal -->
      <div class="ai-settings-overlay" id="aiSettingsOverlay">
        <div class="ai-settings-header">
          <h4>⚙️ Cài Đặt Trợ Lý AI Tuấn Tử Tế</h4>
          <button class="ai-icon-btn" id="btnCloseAiSettings">&times;</button>
        </div>
        <div class="ai-settings-body">
          <div class="ai-setting-group">
            <label for="selectAiProvider">Mô hình AI ưu tiên:</label>
            <select class="ai-setting-select" id="selectAiProvider">
              <option value="deepseek">DeepSeek AI (Khuyên dùng - Nhanh, chuẩn tiếng Việt, tinh tế)</option>
              <option value="gemini">Google Gemini AI (Mạnh mẽ & Đầy đủ)</option>
            </select>
            <span class="ai-setting-help">Tự động chuyển mô hình còn lại nếu hệ thống chính phản hồi chậm.</span>
          </div>

          <div class="ai-setting-group">
            <label for="inputDeepseekKey">DeepSeek API Key (Tùy chọn):</label>
            <input type="password" class="ai-setting-input" id="inputDeepseekKey" placeholder="Để trống nếu dùng key mặc định">
          </div>

          <div class="ai-setting-group">
            <label for="inputGeminiKey">Google Gemini API Key (Tùy chọn):</label>
            <input type="password" class="ai-setting-input" id="inputGeminiKey" placeholder="Để trống nếu dùng key mặc định">
          </div>
        </div>
        <div class="ai-settings-footer">
          <button class="ai-btn-reset" id="btnResetAiDefault">Khôi phục mặc định</button>
          <button class="ai-btn-save" id="btnSaveAiSettings">Lưu Cài Đặt</button>
        </div>
      </div>
    `;

    document.body.appendChild(fab);
    document.body.appendChild(chatWin);

    attachAIEvents(fab, chatWin);
  }

  function attachAIEvents(fab, chatWin) {
    const chatBody = document.getElementById('aiChatBody');
    const chatForm = document.getElementById('aiChatForm');
    const inputField = document.getElementById('aiInputField');
    const sendBtn = document.getElementById('aiSendBtn');
    const chipsBar = document.getElementById('aiChipsBar');
    const btnClose = document.getElementById('btnAiClose');
    const btnClear = document.getElementById('btnAiClear');
    const btnSettings = document.getElementById('btnAiSettings');
    const settingsOverlay = document.getElementById('aiSettingsOverlay');
    const btnCloseSettings = document.getElementById('btnCloseAiSettings');
    const btnSaveSettings = document.getElementById('btnSaveAiSettings');
    const btnResetDefault = document.getElementById('btnResetAiDefault');
    const providerBadge = document.getElementById('aiProviderBadge');
    const selectProvider = document.getElementById('selectAiProvider');
    const inputDeepseek = document.getElementById('inputDeepseekKey');
    const inputGemini = document.getElementById('inputGeminiKey');

    function toggleChat(open) {
      const isOpen = open !== undefined ? open : !chatWin.classList.contains('open');
      if (isOpen) {
        chatWin.classList.add('open');
        inputField.focus();
        scrollToBottom();
      } else {
        chatWin.classList.remove('open');
        settingsOverlay.classList.remove('open');
      }
    }

    fab.addEventListener('click', () => toggleChat());
    btnClose.addEventListener('click', () => toggleChat(false));

    function scrollToBottom() {
      setTimeout(() => {
        chatBody.scrollTop = chatBody.scrollHeight;
      }, 50);
    }

    function appendMessage(role, text, sourceLabel) {
      const msgDiv = document.createElement('div');
      msgDiv.className = `ai-msg ${role === 'user' ? 'user' : 'bot'}`;

      if (role === 'assistant') {
        msgDiv.innerHTML = `
          <div class="ai-msg-avatar"><img src="avatar.jpg" alt="Tuấn Tử Tế"></div>
          <div class="ai-msg-bubble">
            ${formatMarkdown(text)}
            
          </div>
        `;
      } else {
        msgDiv.innerHTML = `
          <div class="ai-msg-bubble">
            ${formatMarkdown(text)}
          </div>
        `;
      }

      chatBody.appendChild(msgDiv);
      scrollToBottom();
    }

    let typingElement = null;
    function showTyping() {
      if (typingElement) return;
      typingElement = document.createElement('div');
      typingElement.className = 'ai-typing-indicator';
      typingElement.innerHTML = `
        <span class="ai-typing-dot"></span>
        <span class="ai-typing-dot"></span>
        <span class="ai-typing-dot"></span>
      `;
      chatBody.appendChild(typingElement);
      scrollToBottom();
    }

    function hideTyping() {
      if (typingElement) {
        typingElement.remove();
        typingElement = null;
      }
    }

    async function handleUserSubmit(text) {
      const cleanText = text.trim();
      if (!cleanText) return;

      inputField.value = '';
      inputField.style.height = 'auto';
      sendBtn.disabled = true;

      appendMessage('user', cleanText);
      showTyping();

      try {
        const { reply, provider } = await requestAIResponse(cleanText);
        hideTyping();
        chatHistory.push({ role: 'assistant', content: reply });
        appendMessage('assistant', reply);
      } catch (err) {
        hideTyping();
        appendMessage('assistant', getSmartFallbackReply(cleanText), 'Trợ lý Tuấn Tử Tế');
      } finally {
        sendBtn.disabled = false;
        inputField.focus();
      }
    }

    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleUserSubmit(inputField.value);
    });

    inputField.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleUserSubmit(inputField.value);
      }
    });

    inputField.addEventListener('input', () => {
      inputField.style.height = 'auto';
      inputField.style.height = Math.min(inputField.scrollHeight, 80) + 'px';
    });

    chipsBar.addEventListener('click', (e) => {
      const chip = e.target.closest('.ai-chip');
      if (chip && chip.dataset.q) {
        handleUserSubmit(chip.dataset.q);
      }
    });

    btnClear.addEventListener('click', () => {
      if (confirm('Quý khách có muốn làm mới cuộc trò chuyện không?')) {
        chatHistory = [chatHistory[0]];
        chatBody.innerHTML = `
          <div class="ai-msg bot">
            <div class="ai-msg-avatar"><img src="avatar.jpg" alt="Tuấn Tử Tế"></div>
            <div class="ai-msg-bubble">
              ${formatMarkdown(chatHistory[0].content)}
            </div>
          </div>
        `;
      }
    });

    btnSettings.addEventListener('click', () => {
      selectProvider.value = AI_CONFIG.provider;
      inputDeepseek.value = localStorage.getItem('ttt_deepseek_key') || '';
      inputGemini.value = localStorage.getItem('ttt_gemini_key') || '';
      settingsOverlay.classList.add('open');
    });

    btnCloseSettings.addEventListener('click', () => {
      settingsOverlay.classList.remove('open');
    });

    btnSaveSettings.addEventListener('click', () => {
      AI_CONFIG.provider = selectProvider.value;
      localStorage.setItem('ttt_ai_provider', AI_CONFIG.provider);
      providerBadge.textContent = AI_CONFIG.provider === 'deepseek' ? 'DeepSeek' : 'Gemini';

      if (inputDeepseek.value.trim()) {
        AI_CONFIG.deepseekKey = inputDeepseek.value.trim();
        localStorage.setItem('ttt_deepseek_key', AI_CONFIG.deepseekKey);
      } else {
        localStorage.removeItem('ttt_deepseek_key');
        AI_CONFIG.deepseekKey = DEFAULT_DEEPSEEK_KEY;
      }

      if (inputGemini.value.trim()) {
        AI_CONFIG.geminiKey = inputGemini.value.trim();
        localStorage.setItem('ttt_gemini_key', AI_CONFIG.geminiKey);
      } else {
        localStorage.removeItem('ttt_gemini_key');
        AI_CONFIG.geminiKey = DEFAULT_GEMINI_KEY;
      }

      settingsOverlay.classList.remove('open');
      appendMessage('assistant', `✅ Đã lưu cấu hình AI! Hiện đang ưu tiên mô hình **${AI_CONFIG.provider === 'deepseek' ? 'DeepSeek AI' : 'Google Gemini AI'}**.`);
    });

    btnResetDefault.addEventListener('click', () => {
      localStorage.removeItem('ttt_ai_provider');
      localStorage.removeItem('ttt_deepseek_key');
      localStorage.removeItem('ttt_gemini_key');
      AI_CONFIG.provider = 'deepseek';
      AI_CONFIG.deepseekKey = DEFAULT_DEEPSEEK_KEY;
      AI_CONFIG.geminiKey = DEFAULT_GEMINI_KEY;
      selectProvider.value = 'deepseek';
      inputDeepseek.value = '';
      inputGemini.value = '';
      providerBadge.textContent = 'DeepSeek';
      settingsOverlay.classList.remove('open');
      appendMessage('assistant', '🔄 Đã khôi phục cài đặt mặc định của hệ thống.');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderAIAssistant);
  } else {
    renderAIAssistant();
  }
})();
