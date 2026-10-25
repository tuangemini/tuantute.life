/**
 * TUẤN TỬ TẾ - EXECUTIVE DIGITAL HUB & SMART vCARD
 * Tương tác ứng dụng, tạo danh thiếp số vCard, mã QR SVG, hiệu ứng thả tim & lưu trữ
 */

document.addEventListener('DOMContentLoaded', () => {
  // Application State
  const state = {
    theme: localStorage.getItem('ttt_theme') || 'dark',
    heartCount: parseInt(localStorage.getItem('ttt_hearts') || '1879', 10),
    messages: JSON.parse(localStorage.getItem('ttt_messages') || 'null') || [
      {
        name: "Lê Minh Trí (Hội Doanh Nhân Trẻ)",
        time: "Vừa xong",
        text: "Chúc anh Tuấn luôn tràn đầy năng lượng và lan tỏa triết lý 'Sự rộng lượng là thước đo trình độ sống' đến cộng đồng doanh nhân!"
      },
      {
        name: "Trần Mai Anh (Đối tác GTO Media)",
        time: "Hôm qua",
        text: "Sự kiện Festival biển do GTO Media tổ chức quá đẳng cấp. Cảm ơn sự tận tâm và tử tế của anh Tuấn cùng đội ngũ."
      },
      {
        name: "Hoàng Nhật Nam",
        time: "2 ngày trước",
        text: "Người anh luôn trân quý sự tử tế trong từng hành động và lời nói. Tự hào được đồng hành cùng anh!"
      }
    ]
  };

  // DOM Elements
  const el = {
    html: document.documentElement,
    liveClock: document.getElementById('liveClock'),
    themeBtns: document.querySelectorAll('.theme-btn'),
    btnDownloadVCard: document.getElementById('btnDownloadVCard'),
    btnDownloadVCardDirect: document.getElementById('btnDownloadVCardDirect'),
    btnCopyContact: document.getElementById('btnCopyContact'),
    btnShareModal: document.getElementById('btnShareModal'),
    btnCloseShareModal: document.getElementById('btnCloseShareModal'),
    shareModalOverlay: document.getElementById('shareModalOverlay'),
    btnCopyShareUrl: document.getElementById('btnCopyShareUrl'),
    shareUrlInput: document.getElementById('shareUrlInput'),
    btnShareFB: document.getElementById('btnShareFB'),
    btnShareZalo: document.getElementById('btnShareZalo'),
    btnNativeShare: document.getElementById('btnNativeShare'),
    btnTriggerQRCard: document.getElementById('btnTriggerQRCard'),
    
    // Heart and Kindness Wall
    btnHeartTap: document.getElementById('btnHeartTap'),
    heartCountNumber: document.getElementById('heartCountNumber'),
    kindnessForm: document.getElementById('kindnessForm'),
    guestName: document.getElementById('guestName'),
    guestMessage: document.getElementById('guestMessage'),
    kindnessStream: document.getElementById('kindnessStream'),
    heartsCanvas: document.getElementById('heartsCanvas'),
    
    // QR Code Frame
    vcardQrFrame: document.getElementById('vcardQrFrame'),
    toastWrapper: document.getElementById('toastWrapper'),
    skypeCard: document.getElementById('skypeCard')
  };

  // -------------------------------------------------------------
  // INITIALIZATION
  // -------------------------------------------------------------
  function init() {
    initTheme();
    startClock();
    renderHeartsCount();
    renderKindnessStream();
    generateQrSvg();
    attachListeners();
  }

  // -------------------------------------------------------------
  // THEME MANAGEMENT
  // -------------------------------------------------------------
  function initTheme() {
    setTheme(state.theme);
  }

  function setTheme(themeName) {
    state.theme = themeName;
    el.html.setAttribute('data-theme', themeName);
    localStorage.setItem('ttt_theme', themeName);

    el.themeBtns.forEach(btn => {
      if (btn.getAttribute('data-theme') === themeName) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // -------------------------------------------------------------
  // CLOCK
  // -------------------------------------------------------------
  function startClock() {
    function update() {
      const now = new Date();
      // Format Vietnam time
      const h = String(now.getHours()).padStart(2, '0');
      const m = String(now.getMinutes()).padStart(2, '0');
      const s = String(now.getSeconds()).padStart(2, '0');
      if (el.liveClock) {
        el.liveClock.textContent = `${h}:${m}:${s}`;
      }
    }
    update();
    setInterval(update, 1000);
  }

  // -------------------------------------------------------------
  // vCARD (.vcf) FILE GENERATOR
  // -------------------------------------------------------------
  function downloadVCard() {
    const vCardData = [
      'BEGIN:VCARD',
      'VERSION:3.0',
      'N:Tuấn;Nguyễn;Anh;;',
      'FN:Nguyễn Anh Tuấn (Tuấn Tử Tế Từ Tâm)',
      'ORG:GTO Media Corporation;Hội Doanh Nhân Trẻ Khánh Hòa;Tuấn Tử Tế Từ Tâm',
      'TITLE:Chủ tịch HĐQT GTO Media & Doanh Nhân Truyền Cảm Hứng',
      'EMAIL;TYPE=INTERNET,PREF:tuan@media-gto.com',
      'URL:https://www.facebook.com/TuanTuTeTT',
      'URL:https://www.youtube.com/@Tu%E1%BA%A5nT%E1%BB%ADT%E1%BA%BFT%E1%BB%ABT%C3%A2m',
      'URL:https://tuantute.life',
      'URL:https://gto.vn',
      'URL:http://gtomedia.vn',
      'ADR;TYPE=WORK:;;Biệt thự C10-C11 KĐT Hưng Phú;Nha Trang;Khánh Hòa;;Vietnam',
      'NOTE:Doanh nhân truyền cảm hứng & Tạo dựng cuộc sống tốt đẹp! Triết lý: Sự rộng lượng là thước đo trình độ sống. Trân quý sự tử tế.',
      'REV:2026-10-18T12:00:00Z',
      'END:VCARD'
    ].join('\r\n');

    const blob = new Blob([vCardData], { type: 'text/vcard;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'Nguyen_Anh_Tuan_Tuan_Tu_Te.vcf');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    showToast('Đã tải file danh thiếp số (.vcf)! Bấm mở để lưu vào danh bạ điện thoại.');
    spawnFloatingHeart(window.innerWidth / 2, window.innerHeight / 2);
  }

  // -------------------------------------------------------------
  // QR CODE SVG ENGINE (PURE JAVASCRIPT STANDALONE)
  // -------------------------------------------------------------
  function generateQrSvg() {
    // Generate an authentic high-resolution SVG QR code (Error Correction Level H) for https://tuantute.life/
    const matrix = [
      "11111110110110011010001111111",
      "10000010010001011100001000001",
      "10111010011001101001001011101",
      "10111010101100110010001011101",
      "10111010011011101011001011101",
      "10000010000011100101101000001",
      "11111110101010101010101111111",
      "00000000001100101111100000000",
      "00101110111001001010110001001",
      "10101101011011001111011000001",
      "11100111000100100110000011111",
      "10001101001110110110111010010",
      "00000111100000100111001101000",
      "11000001011101100000111100001",
      "10001111100011101010100100111",
      "11100101011000000111100100010",
      "10000011001111101110111001011",
      "01000000010001000100011000011",
      "10010110111110101000010000111",
      "01111101010111111011101010011",
      "10111010001000001010111110011",
      "00000000110000110110100010001",
      "11111110011100000011101010111",
      "10000010110111010110100010011",
      "10111010111010001010111111010",
      "10111010011110110010110010000",
      "10111010110011001111000111101",
      "10000010000011011101100101010",
      "11111110011101100101100010011"
    ];

    const cellSize = 5;
    const padding = 10;
    const matrixLen = matrix.length;
    const totalDim = matrixLen * cellSize + padding * 2;

    let paths = '';
    for (let r = 0; r < matrix.length; r++) {
      for (let c = 0; c < matrix[r].length; c++) {
        if (matrix[r][c] === '1') {
          const x = padding + c * cellSize;
          const y = padding + r * cellSize;
          paths += `<rect x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" fill="#0f172a" rx="1" />`;
        }
      }
    }

    const centerPos = totalDim / 2;
    const svg = `
      <svg viewBox="0 0 ${totalDim} ${totalDim}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="QR Code Tuấn Tử Tế">
        <rect width="${totalDim}" height="${totalDim}" fill="#ffffff" rx="10" />
        ${paths}
        <!-- Decorative golden center logo icon -->
        <circle cx="${centerPos}" cy="${centerPos}" r="14" fill="#ffffff" />
        <circle cx="${centerPos}" cy="${centerPos}" r="11" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
        <text x="${centerPos}" y="${centerPos + 4}" font-family="sans-serif" font-size="11" font-weight="900" fill="#000000" text-anchor="middle">T</text>
      </svg>
    `;

    if (el.vcardQrFrame) {
      el.vcardQrFrame.innerHTML = svg;
    }
  }

  // -------------------------------------------------------------
  // KINDNESS WALL & FLOATING HEARTS
  // -------------------------------------------------------------
  function renderHeartsCount() {
    if (el.heartCountNumber) {
      el.heartCountNumber.textContent = state.heartCount.toLocaleString('vi-VN');
    }
  }

  function spawnFloatingHeart(x, y) {
    const heart = document.createElement('div');
    heart.className = 'flying-heart';
    heart.innerHTML = '&#10084;&#65039;';

    // Random trajectory
    const randX = (Math.random() - 0.5) * 160 + 'px';
    const randRot = (Math.random() - 0.5) * 60 + 'deg';
    const randSize = Math.floor(Math.random() * 18 + 20) + 'px';

    heart.style.left = (x || (window.innerWidth / 2)) + 'px';
    heart.style.top = (y || (window.innerHeight - 100)) + 'px';
    heart.style.fontSize = randSize;
    heart.style.setProperty('--rand-x', randX);
    heart.style.setProperty('--rand-rot', randRot);

    el.heartsCanvas.appendChild(heart);

    setTimeout(() => {
      heart.remove();
    }, 1800);
  }

  function handleHeartTap(e) {
    state.heartCount += 1;
    localStorage.setItem('ttt_hearts', state.heartCount);
    renderHeartsCount();

    const rect = el.btnHeartTap.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top;

    // Burst 3 hearts
    for (let i = 0; i < 3; i++) {
      setTimeout(() => {
        spawnFloatingHeart(x + (Math.random() - 0.5) * 40, y);
      }, i * 100);
    }

    showToast('Cảm ơn bạn đã gửi trao sự tử tế! ❤️');
  }

  function renderKindnessStream() {
    if (!el.kindnessStream) return;
    el.kindnessStream.innerHTML = state.messages.map(item => `
      <div class="stream-card">
        <div class="stream-top">
          <span class="stream-author">${escapeHtml(item.name)}</span>
          <span class="stream-time">${item.time}</span>
        </div>
        <p class="stream-msg">${escapeHtml(item.text)}</p>
      </div>
    `).join('');
  }

  function handleKindnessSubmit(e) {
    e.preventDefault();
    const name = el.guestName.value.trim();
    const message = el.guestMessage.value.trim();

    if (!name || !message) {
      showToast('Vui lòng điền đầy đủ tên và lời nhắn!');
      return;
    }

    const newMessage = {
      name: name,
      time: 'Vừa xong',
      text: message
    };

    state.messages.unshift(newMessage);
    if (state.messages.length > 25) {
      state.messages.pop();
    }

    localStorage.setItem('ttt_messages', JSON.stringify(state.messages));
    renderKindnessStream();

    // Trigger hearts burst
    for (let i = 0; i < 6; i++) {
      setTimeout(() => {
        spawnFloatingHeart(window.innerWidth / 2 + (Math.random() - 0.5) * 120, window.innerHeight * 0.7);
      }, i * 80);
    }

    el.kindnessForm.reset();
    showToast(`Lời chúc của bạn đã được lưu lên Bức Tường Tử Tế!`);
  }

  // -------------------------------------------------------------
  // TOAST NOTIFICATION UTILITY
  // -------------------------------------------------------------
  function showToast(msg) {
    const toast = document.createElement('div');
    toast.className = 'toast-msg';
    toast.innerHTML = `
      <span style="color:#f59e0b;font-size:1.1rem;">&#10004;</span>
      <span>${msg}</span>
    `;

    el.toastWrapper.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(16px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  function escapeHtml(text) {
    const map = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
  }

  // -------------------------------------------------------------
  // EVENT LISTENERS
  // -------------------------------------------------------------
  function attachListeners() {
    // Theme buttons
    el.themeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const theme = btn.getAttribute('data-theme');
        setTheme(theme);
        showToast(`Đã chuyển sang giao diện: ${theme === 'dark' ? 'Đen Sang Trọng' : theme === 'amber' ? 'Ấm Áp Tử Tế' : 'Tươi Sáng'}`);
      });
    });

    // vCard downloads
    if (el.btnDownloadVCard) el.btnDownloadVCard.addEventListener('click', downloadVCard);
    if (el.btnDownloadVCardDirect) el.btnDownloadVCardDirect.addEventListener('click', downloadVCard);

    // Copy Email contact
    if (el.btnCopyContact) {
      el.btnCopyContact.addEventListener('click', () => {
        navigator.clipboard.writeText('tuan@media-gto.com').then(() => {
          showToast('Đã sao chép email: tuan@media-gto.com');
        }).catch(() => {
          showToast('Không thể sao chép email');
        });
      });
    }

    // Scroll to QR on card click
    if (el.btnTriggerQRCard) {
      el.btnTriggerQRCard.addEventListener('click', () => {
        const qrCard = document.querySelector('.card-vcard');
        if (qrCard) {
          qrCard.scrollIntoView({ behavior: 'smooth' });
          qrCard.style.boxShadow = '0 0 35px rgba(245, 158, 11, 0.4)';
          setTimeout(() => {
            qrCard.style.boxShadow = '';
          }, 1500);
        }
      });
    }

    // Share Modal
    if (el.btnShareModal) {
      el.btnShareModal.addEventListener('click', () => {
        el.shareModalOverlay.classList.add('active');
        el.shareModalOverlay.setAttribute('aria-hidden', 'false');
      });
    }

    if (el.btnCloseShareModal) {
      el.btnCloseShareModal.addEventListener('click', () => {
        el.shareModalOverlay.classList.remove('active');
        el.shareModalOverlay.setAttribute('aria-hidden', 'true');
      });
    }

    if (el.shareModalOverlay) {
      el.shareModalOverlay.addEventListener('click', (e) => {
        if (e.target === el.shareModalOverlay) {
          el.shareModalOverlay.classList.remove('active');
          el.shareModalOverlay.setAttribute('aria-hidden', 'true');
        }
      });
    }

    // Copy Share URL
    if (el.btnCopyShareUrl) {
      el.btnCopyShareUrl.addEventListener('click', () => {
        el.shareUrlInput.select();
        navigator.clipboard.writeText(el.shareUrlInput.value).then(() => {
          showToast('Đã sao chép liên kết trang web!');
        });
      });
    }

    // Social Sharing
    if (el.btnShareFB) {
      el.btnShareFB.addEventListener('click', () => {
        window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent('https://tuantute.life/'), '_blank');
      });
    }

    if (el.btnShareZalo) {
      el.btnShareZalo.addEventListener('click', () => {
        window.open('https://sp.zalo.me/share_inline?link=' + encodeURIComponent('https://tuantute.life/'), '_blank');
      });
    }

    if (el.btnNativeShare) {
      el.btnNativeShare.addEventListener('click', () => {
        if (navigator.share) {
          navigator.share({
            title: 'Tuấn Tử Tế (Từ Tâm) | Nguyễn Anh Tuấn - Kiến Tạo Cuộc Sống Kỷ Nguyên Trí Tuệ AI',
            text: 'Doanh nhân truyền cảm hứng & Tạo dựng cuộc sống tốt đẹp! Sự rộng lượng là thước đo trình độ sống.',
            url: 'https://tuantute.life/'
          }).catch(() => {});
        } else {
          navigator.clipboard.writeText('https://tuantute.life/').then(() => {
            showToast('Đã sao chép liên kết để chia sẻ: https://tuantute.life/');
          });
        }
      });
    }

    // Heart tap
    if (el.btnHeartTap) {
      el.btnHeartTap.addEventListener('click', handleHeartTap);
    }

    // Kindness form
    if (el.kindnessForm) {
      el.kindnessForm.addEventListener('submit', handleKindnessSubmit);
    }

    // Skype card click
    if (el.skypeCard) {
      el.skypeCard.addEventListener('click', () => {
        window.location.href = 'skype:gto.media?chat';
      });
    }

    // Keyboard ESC to close modal
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && el.shareModalOverlay.classList.contains('active')) {
        el.shareModalOverlay.classList.remove('active');
        el.shareModalOverlay.setAttribute('aria-hidden', 'true');
      }
    });
  }

  // Run on start
  init();
});
