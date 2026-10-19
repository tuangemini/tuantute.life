/**
 * AI ASSISTANT CHATBOT (DEEPSEEK & GOOGLE GEMINI) - TUẤN TỬ TẾ (tuantute.life)
 * Tự động giải đáp 24/7 mọi thắc mắc về Anh Nguyễn Anh Tuấn (Tuấn Tử Tế Từ Tâm),
 * triết lý sống tử tế, sự rộng lượng, hệ sinh thái GTO Media, BNI Khánh Hòa,
 * Hội Doanh Nhân Trẻ, kết nối kinh doanh và gia đình.
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
- Họ và tên: NGUYỄN ANH TUẤN (Thương hiệu cá nhân: Tuấn Tử Tế &bull; Từ Tâm).
- Trang Facebook chính thức: https://www.facebook.com/TuanTuTeTT (5.5K+ Followers).
- Kênh YouTube: @TuấnTửTếTừTâm (https://www.youtube.com/@Tu%E1%BA%A5nT%E1%BB%ADT%E1%BA%BFT%E1%BB%ABT%C3%A2m).
- Email liên hệ: tuan@media-gto.com.
- Website cá nhân: https://tuantute.life/
- Ngày sinh: 02 / 01 / 1977 (Tuổi Bính Thìn).
- Hậu phương gia đình thiêng liêng: MỘT vợ + HAI con gái. Kỷ niệm ngày cưới: 19 / 12 / 2005.

SỨ MỆNH & TRIẾT LÝ SỐNG CỐT LÕI:
- Slogan định vị: "Doanh nhân truyền cảm hứng &bull; Tạo dựng cuộc sống tốt đẹp!".
- Thông điệp truyền cảm hứng: "Cherish kindness &bull; Trân quý sự tử tế".
- Châm ngôn sống kinh điển: "Sự rộng lượng là thước đo trình độ sống" (Generosity is a measure of life's level).
- Luôn đặt chữ TÂM và sự TỬ TẾ làm kim chỉ nam trong mọi hoạt động kinh doanh, đối nhân xử thế và gắn kết cộng đồng.

VỊ THẾ DOANH NGHIỆP & CÔNG TÁC XÃ HỘI:
1. Chủ tịch HĐQT GTO Media Corporation (Since 2009):
   - Đơn vị dẫn đầu tại Nha Trang - Khánh Hòa và khu vực miền Trung về tổ chức lễ hội quy mô quốc gia (Festival Biển Nha Trang), sự kiện văn hóa, du lịch, hội nghị cao cấp (MICE) và chiến lược tiếp thị đa phương tiện.
   - Trụ sở: Biệt thự C10 - C11 Khu đô thị Hưng Phú, TP. Nha Trang, Khánh Hòa.
   - Website doanh nghiệp: https://gto.vn / http://gtomedia.vn.

2. Giám đốc BNI Vùng Khánh Hòa:
   - Đại diện tổ chức kết nối thương mại lớn nhất toàn cầu BNI tại Khánh Hòa, gắn kết hàng trăm doanh nhân theo triết lý "Givers Gain - Cho là nhận", giúp các doanh nghiệp mở rộng thị trường và tăng trưởng doanh thu bền vững.
   - Thành tích nổi bật: Đạt giải thưởng quốc gia danh giá BNI Vietnam National Notable Networker Award (Năm 2013).

3. Phó Chủ tịch Hội Doanh Nhân Trẻ Khánh Hòa:
   - Tích cực phụng sự, đồng hành cùng các thế hệ doanh nhân trẻ khởi nghiệp, chia sẻ kinh nghiệm quản trị, ứng dụng trí tuệ nhân tạo (AI), công nghệ số và livestream thực chiến.

4. Diễn giả truyền cảm hứng & Đào tạo phát triển bản thân:
   - Thường xuyên tổ chức các buổi chia sẻ về tư duy tích cực, xây dựng phong cách sống đàng hoàng, tử tế, làm chủ tài chính và kiến tạo hạnh phúc trọn vẹn.

VĂN PHONG GIAO TIẾP CỦA TRỢ LÝ AI:
- Xưng hô: "Chào bạn/Quý đối tác! Tôi là Trợ lý AI của Anh Tuấn Tử Tế".
- Giọng điệu hào sảng, ấm áp, văn minh, lịch lãm, truyền cảm hứng tích cực, luôn hướng đến sự hợp tác chân thành và giá trị bền lâu.
- Luôn khích lệ tinh thần tử tế, rộng lượng và chia sẻ thông tin liên lạc chính thức (Facebook fb.com/TuanTuTeTT, email tuan@media-gto.com).
`;

  let chatHistory = [
    {
      role: 'assistant',
      content: 'Chào bạn! Tôi là **Trợ lý AI của Anh Nguyễn Anh Tuấn (Tuấn Tử Tế • Từ Tâm)**. Rất vui được đón tiếp bạn ghé thăm tuantute.life! Bạn cần tìm hiểu thông tin về triết lý sống tử tế, cơ hội hợp tác cùng **GTO Media**, mạng lưới **BNI Khánh Hòa**, hay kết nối cá nhân cùng Anh Tuấn hôm nay ạ?'
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

    if (q.includes('bni') || q.includes('kết nối') || q.includes('mạng lưới') || q.includes('doanh nhân')) {
      return `🤝 <strong>BNI Vùng Khánh Hòa & Hội Doanh Nhân Trẻ:</strong><br><br>` +
        `• Anh Tuấn đảm nhiệm vai trò <strong>Giám đốc BNI Vùng Khánh Hòa</strong>, kết nối hàng trăm chủ doanh nghiệp địa phương giao thương theo triết lý "Cho là nhận".<br>` +
        `• <strong>Giải thưởng quốc gia:</strong> BNI Vietnam National Notable Networker Award 2013.<br>` +
        `• Đồng thời giữ vị trí <strong>Phó Chủ tịch Hội Doanh Nhân Trẻ Khánh Hòa</strong>, luôn tiếp sức cho thế hệ khởi nghiệp công nghệ và chuyển đổi số.`;
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
        <span class="ai-fab-title">Trợ Lý AI Anh Tuấn</span>
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
              <span>Trợ Lý AI Tuấn Tử Tế</span>
              <span class="ai-provider-pill" id="aiProviderBadge">${AI_CONFIG.provider === 'deepseek' ? 'DeepSeek' : 'Gemini'}</span>
            </div>
            <span class="ai-status-text">Doanh nhân truyền cảm hứng • GTO & BNI</span>
          </div>
        </div>
        <div class="ai-header-actions">
          <button class="ai-icon-btn" id="btnAiSettings" title="Cài đặt mô hình AI" aria-label="Cài đặt">⚙️</button>
          <button class="ai-icon-btn" id="btnAiClear" title="Xóa lịch sử chat" aria-label="Xóa chat">🗑️</button>
          <button class="ai-icon-btn" id="btnAiClose" title="Thu nhỏ" aria-label="Đóng">&times;</button>
        </div>
      </div>

      <!-- Quick Suggestion Chips -->
      <div class="ai-chips-bar" id="aiChipsBar">
        <button class="ai-chip" data-q="Triết lý sống 'Sự rộng lượng là thước đo trình độ sống' của Anh Tuấn là gì?">✨ Triết lý sự rộng lượng?</button>
        <button class="ai-chip" data-q="Giới thiệu về hệ sinh thái GTO Media và BNI Khánh Hòa?">🏢 GTO Media & BNI?</button>
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
            placeholder="Hỏi về triết lý sống tử tế, GTO Media, BNI, hợp tác..."
            aria-label="Nhập câu hỏi"
          ></textarea>
          <button type="submit" class="ai-send-btn" id="aiSendBtn" aria-label="Gửi tin nhắn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M22 2L11 13M22 2L15 22L11 13L2 9L22 2Z"></path>
            </svg>
          </button>
        </form>
        <div class="ai-footer-note">Hỗ trợ bởi DeepSeek & Google Gemini AI • Phụng sự từ tâm 24/7</div>
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
            ${sourceLabel ? `<div style="font-size:0.64rem; opacity:0.6; margin-top:5px; text-align:right;">⚡ ${sourceLabel}</div>` : ''}
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
        appendMessage('assistant', reply, provider);
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
