# -*- coding: utf-8 -*-
"""
KTCS 4D Creator Studio V08 - Ứng Dụng Phần Mềm Tự Hành & Tự Học Hỏi Tiến Hóa (KTCSxAI)
Dành cho Thầy Tuấn Tử Tế và các thế hệ học viên, giảng viên Việt Nam.
- Hỗ trợ mọi đầu vào: Chủ đề bất kỳ, file .PDF, .HTML, .TXT, .MD hoặc dán nội dung trực tiếp.
- Chạy mượt cả khi có AI (Gemini API) lẫn 100% Offline không cần API Key.
- Tích hợp Nhật Ký Học Hỏi & Nâng Cấp Tự Hành + Kho Video YouTube Tiếng Việt đã xác thực.
"""

import os
import re
import sys
import json
import datetime
import mimetypes
import urllib.parse
import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / ".agents" / "skills" / "ktcs-4d-training" / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from ktcs_universal_engine import (
    build_4d_cinema_lecture,
    DOMAIN_FRAMEWORKS,
    load_evolution_log,
    record_lesson_learned,
    verify_and_add_youtube,
    VERIFIED_VN_YOUTUBE_BANK,
)

PORT = 7890

HTML_UI = """<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KTCSxAI V09 • STUDIO KIẾN TẠO BÀI GIẢNG 4D TỰ HỌC HỎI</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #030712; color: #f8fafc; }
    .font-display { font-family: 'Space Grotesk', sans-serif; }
    .glass-card { background: rgba(15, 23, 42, 0.82); backdrop-filter: blur(18px); border: 1px solid rgba(245, 158, 11, 0.25); }
    .glow-amber { box-shadow: 0 0 28px -5px rgba(245, 158, 11, 0.45); }
    input, select, textarea { background-color: rgba(2, 6, 23, 0.9) !important; }
    .tab-btn.active { background: linear-gradient(135deg, #f59e0b, #eab308); color: #020617; font-weight: 800; }
  </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-start p-4 lg:p-7 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-gray-950 to-black">

  <!-- Header Banner -->
  <header class="w-full max-w-5xl text-center mb-6 pt-2">
    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/15 border border-amber-400/40 text-amber-300 text-xs font-bold tracking-wider mb-3">
      <span class="animate-pulse">✨</span> KTCSxAI STUDIO V08 • TỰ HÀNH • TỰ HỌC HỎI • CHẠY MƯỢT CẢ KHI KHÔNG CÓ AI API
    </div>
    <h1 class="text-2xl lg:text-4xl font-extrabold font-display text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-amber-400 to-emerald-300 mb-2">
      KIẾN TẠO BÀI GIẢNG 4D CINEMA 16:9 TRUYỀN CẢM HỨNG
    </h1>
    <p class="text-xs lg:text-sm text-slate-300 max-w-3xl mx-auto leading-relaxed">
      Đưa vào <b>Chủ đề bất kỳ</b> hoặc file <b>.PDF, .HTML, .TXT, .MD</b> — Hệ thống tự động tạo bài giảng HTML/CSS 4D sống động, YouTube Tiếng Việt đã xác thực, Tua chậm Slow-Mo, Toàn màn hình, Thẻ lật 3D &amp; Âm nhạc truyền cảm hứng cho người trung niên Việt Nam.
    </p>

    <!-- Mode Tabs -->
    <div class="inline-flex items-center gap-2 bg-slate-900/90 p-1.5 rounded-2xl border border-slate-700 mt-4">
      <button onclick="switchTab('creator')" id="tabCreator" class="tab-btn active px-4 py-2 rounded-xl text-xs transition">
        ⚡ Kiến Tạo Bài Giảng 4D
      </button>
      <button onclick="switchTab('evolution')" id="tabEvolution" class="tab-btn px-4 py-2 rounded-xl text-xs text-slate-300 hover:text-amber-300 transition">
        🧠 Nhật Ký Học Hỏi &amp; Tiến Hóa (<span id="evoCount">0</span>)
      </button>
      <a href="/ktcs-thong-diep-gia-tri-di-san-4d.html" target="_blank" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600/90 hover:bg-emerald-500 text-white transition">
        🎬 Mở Bài Giảng Mẫu 30 Trang V08
      </a>
    </div>
  </header>

  <!-- TAB 1: CREATOR STUDIO -->
  <main id="panelCreator" class="w-full max-w-5xl glass-card rounded-3xl p-6 lg:p-8 shadow-2xl">
    <form id="createForm" onsubmit="handleCreate(event)" class="space-y-5">

      <!-- Row 1: Topic & Trainer -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
          <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider mb-1.5">
            🎯 Chủ Đề Bài Giảng (Mọi Lĩnh Vực):
          </label>
          <input type="text" id="topicInput" required
                 placeholder="VD: Sống Bình An Tuổi Trung Niên, Làm Chủ AI Thực Chiến, Nghệ Thuật Truyền Cảm Hứng..."
                 class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-400">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
            👤 Tên Giảng Viên:
          </label>
          <input type="text" id="trainerInput" value="Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI"
                 class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-amber-400">
        </div>
      </div>

      <!-- Row 2: Domain & Slide Count -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
          <label class="block text-xs font-bold text-cyan-300 uppercase tracking-wider mb-1.5">
            🏛️ Lĩnh Vực Đào Tạo (Tự Khớp Kho Video YouTube Tiếng Việt):
          </label>
          <select id="domainSelect" class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-cyan-400">
            <option value="auto" selected>✨ Tự Động Nhận Diện Theo Nội Dung &amp; Chủ Đề (Khuyên Dùng)</option>
            <option value="triet_ly_song">🌟 Thân - Tâm - Trí &amp; Di Sản Vượt Thời Gian (KTCSxAI)</option>
            <option value="lanh_dao">👑 Lãnh Đạo Vượt Bão &amp; Quản Trị Đội Ngũ</option>
            <option value="ban_hang">💎 Bán Hàng Giá Trị Cao &amp; Kể Chuyện (Storyselling)</option>
            <option value="cong_nghe_ai">🤖 Kiến Trúc Sư AI &amp; Làm Chủ Kỷ Nguyên Số</option>
            <option value="giao_duc">🎓 Đào Tạo Giảng Viên &amp; Sư Phạm Chuyển Hóa</option>
            <option value="tai_chinh">💰 Tài Chính Cá Nhân Vững Bền &amp; Thịnh Vượng Đích Thực</option>
            <option value="suc_khoe">🌱 Sinh Khí Trẻ Hóa &amp; Sức Khỏe Thân Tâm Tuổi Trung Niên</option>
            <option value="tong_quat">⚡ Chương Trình Đào Tạo Chuyển Hóa Tổng Quát</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
            📊 Số Trang (Nếu Tự Sinh):
          </label>
          <select id="slideCountSelect" class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-cyan-400">
            <option value="10">10 Trang (Cô đọng 30 phút)</option>
            <option value="15" selected>15 Trang (Chuẩn Seminar 60 phút)</option>
            <option value="20">20 Trang (Chuyên sâu 90 phút)</option>
            <option value="30">30 Trang (Master Class Vượt Thời Gian)</option>
          </select>
        </div>
      </div>

      <!-- Row 3: Multi-format File Input (.PDF, .HTML, .TXT, .MD) -->
      <div>
        <label class="block text-xs font-bold text-emerald-300 uppercase tracking-wider mb-1.5">
          📂 Nạp Một Hoặc Nhiều Tệp Tài Liệu Phối Hợp (.PDF, .HTML, .TXT, .MD, .JSON, Ảnh, Video):
        </label>
        <div class="flex items-center gap-3">
          <input type="text" id="sourceFileInput" placeholder="Chọn 1 hoặc nhiều file (.pdf, .html, .txt, .json, ảnh .png/.webp, video .mp4) ngăn cách bởi dấu ; ..."
                 class="flex-1 border border-slate-700 rounded-xl p-3 text-xs font-mono text-slate-200 focus:outline-none focus:border-emerald-400">
          <button type="button" onclick="browseSourceFile()" class="bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/40 font-bold text-xs px-4 py-3 rounded-xl transition shrink-0">
            📁 Chọn Nhiều File (Đa Định Dạng)
          </button>
        </div>
      </div>

      <!-- Row 4: Paste Raw Text / Notes + Optional Gemini API Key -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
            📝 Hoặc Dán Trực Tiếp Nội Dung / Dàn Ý / Văn Bản (Tùy Chọn):
          </label>
          <textarea id="rawTextInput" rows="3" placeholder="Dán dàn ý bài giảng, bài viết hoặc nội dung muốn chuyển thành slide 4D tương tác..."
                    class="w-full border border-slate-700 rounded-xl p-3 text-xs text-slate-200 focus:outline-none focus:border-amber-400"></textarea>
        </div>
        <div>
          <label class="block text-xs font-bold text-purple-300 uppercase tracking-wider mb-1.5">
            🤖 Gemini API Key (Không Bắt Buộc):
          </label>
          <input type="password" id="apiKeyInput" placeholder="Để trống = Chạy Smart Offline 100%"
                 class="w-full border border-slate-700 rounded-xl p-3 text-xs text-slate-200 focus:outline-none focus:border-purple-400 mb-2">
          <p class="text-[11px] text-emerald-400/90 leading-snug">
            ✓ Kể cả <b>không có API Key AI</b>, Smart Offline Engine vẫn xuất file HTML/CSS 4D sống động, YouTube VN xác thực &amp; âm thanh đầy đủ!
          </p>
        </div>
      </div>

      <!-- Action Button -->
      <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="text-xs text-slate-300 flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
          V08 Ready: Preview YouTube VN • Tua Chậm Slow-Mo • Toàn Màn Hình • Kéo Dọc Mở Rộng
        </div>
        <button type="submit" id="submitBtn"
                class="w-full sm:w-auto bg-gradient-to-r from-amber-500 via-yellow-500 to-amber-500 hover:from-amber-400 hover:to-yellow-400 text-black font-extrabold text-sm px-8 py-3.5 rounded-2xl shadow-xl glow-amber flex items-center justify-center gap-2 transition transform hover:scale-105">
          <span>⚡</span> BẮT ĐẦU KIẾN TẠO BÀI GIẢNG 4D V09
        </button>
      </div>
    </form>

    <!-- Progress & Result Box -->
    <div id="statusBox" class="hidden mt-6 p-5 rounded-2xl bg-slate-950 border border-cyan-500/40">
      <div class="flex items-center gap-3 mb-3">
        <div id="spinner" class="w-5 h-5 border-2 border-cyan-400 border-t-transparent rounded-full animate-spin"></div>
        <h4 id="statusTitle" class="text-sm font-bold text-cyan-300">Đang khởi tạo hệ thống...</h4>
      </div>
      <div id="statusLogs" class="text-xs font-mono text-slate-300 space-y-1 max-h-40 overflow-y-auto mb-4 p-2.5 bg-slate-900 rounded-lg"></div>
      <div id="resultActions" class="hidden flex items-center gap-3 flex-wrap">
        <a id="openLectureBtn" href="#" target="_blank"
           class="bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow-lg flex items-center gap-2 hover:from-emerald-400 hover:to-teal-500 transition">
          🎬 Mở Bài Giảng Trực Tiếp (Không Lỗi YouTube 153)
        </a>
        <button onclick="copyOutputDir()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs px-4 py-2.5 rounded-xl transition">
          📂 Chép Đường Dẫn Thư Mục
        </button>
      </div>
    </div>
  </main>

  <!-- TAB 2: SELF-EVOLUTION & LEARNING LOG -->
  <section id="panelEvolution" class="hidden w-full max-w-5xl glass-card rounded-3xl p-6 lg:p-8 shadow-2xl space-y-6">
    <div class="flex items-center justify-between flex-wrap gap-3 border-b border-slate-800 pb-4">
      <div>
        <h2 class="text-lg font-extrabold text-amber-300">🧠 NHẬT KÝ HỌC HỎI &amp; TIẾN HÓA TỰ HÀNH (SELF-EVOLVING ENGINE)</h2>
        <p class="text-xs text-slate-400">Hệ thống ghi nhận mọi bài học tối ưu, lịch sử xuất bản và tự mở rộng kho Video YouTube Tiếng Việt đã xác thực.</p>
      </div>
      <span id="evoVersionBadge" class="text-xs font-bold px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">V09.0 Multi-Modal</span>
    </div>

    <!-- Add Lesson Learned & Verify New Vietnamese YouTube -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <div class="bg-slate-950/70 border border-slate-800 rounded-2xl p-4 space-y-3">
        <h3 class="text-xs font-extrabold text-cyan-300 uppercase">✍️ Ghi Nhật Ký Học Hỏi / Quy Tắc Nâng Cấp Mới</h3>
        <input type="text" id="lessonCatInput" placeholder="Danh mục (VD: Giao Diện, Sư Phạm, Âm Thanh...)" class="w-full border border-slate-700 rounded-lg p-2 text-xs text-slate-100">
        <textarea id="lessonInsightInput" rows="2" placeholder="Bài học kinh nghiệm hoặc yêu cầu tối ưu cần ghi nhớ cho các phiên bản sau..." class="w-full border border-slate-700 rounded-lg p-2 text-xs text-slate-100"></textarea>
        <button onclick="saveNewLesson()" class="bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs px-4 py-2 rounded-lg transition">💾 Lưu Vào Bộ Nhớ Tiến Hóa</button>
      </div>

      <div class="bg-slate-950/70 border border-slate-800 rounded-2xl p-4 space-y-3">
        <h3 class="text-xs font-extrabold text-red-400 uppercase">▶ Dạy Hệ Thống Video YouTube Tiếng Việt Mới (Tự Xác Thực)</h3>
        <input type="text" id="newYtUrlInput" placeholder="Dán link YouTube tiếng Việt (https://www.youtube.com/watch?v=...)" class="w-full border border-slate-700 rounded-lg p-2 text-xs text-slate-100 font-mono">
        <select id="newYtDomainSelect" class="w-full border border-slate-700 rounded-lg p-2 text-xs text-slate-100">
          <option value="triet_ly_song">Thân - Tâm - Trí &amp; Di Sản</option>
          <option value="lanh_dao">Lãnh Đạo &amp; Đội Ngũ</option>
          <option value="ban_hang">Bán Hàng &amp; Kể Chuyện</option>
          <option value="cong_nghe_ai">AI Thực Chiến</option>
          <option value="giao_duc">Đào Tạo Giảng Viên</option>
          <option value="suc_khoe">Sức Khỏe Tuổi Trung Niên</option>
          <option value="tong_quat">Tổng Quát</option>
        </select>
        <button onclick="addVerifiedYouTube()" class="bg-red-600 hover:bg-red-500 text-white font-bold text-xs px-4 py-2 rounded-lg transition">✓ Xác Thực &amp; Thêm Vào Kho Video VN</button>
        <div id="ytAddStatus" class="text-[11px] text-slate-400"></div>
      </div>
    </div>

    <!-- Lists -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <div>
        <h3 class="text-xs font-extrabold text-amber-300 uppercase mb-2">📚 Bài Học Tối Ưu Đã Ghi Nhận</h3>
        <div id="lessonsList" class="space-y-2 max-h-64 overflow-y-auto pr-1"></div>
      </div>
      <div>
        <h3 class="text-xs font-extrabold text-emerald-300 uppercase mb-2">🚀 Lịch Sử Kiến Tạo Bài Giảng 4D</h3>
        <div id="historyList" class="space-y-2 max-h-64 overflow-y-auto pr-1"></div>
      </div>
    </div>
  </section>

  <footer class="mt-6 text-center text-xs text-slate-500">
    KTCSxAI V08 Self-Evolving Studio • Bản quyền thuộc về Thầy Tuấn Tử Tế (Nguyễn Anh Tuấn)
  </footer>

  <script>
    let currentOutputDir = '';

    function switchTab(tab) {
      document.getElementById('panelCreator').classList.toggle('hidden', tab !== 'creator');
      document.getElementById('panelEvolution').classList.toggle('hidden', tab !== 'evolution');
      document.getElementById('tabCreator').classList.toggle('active', tab === 'creator');
      document.getElementById('tabEvolution').classList.toggle('active', tab === 'evolution');
      if (tab === 'evolution') loadEvolutionLog();
    }

    async function browseSourceFile() {
      try {
        const res = await fetch('/api/browse-file');
        const data = await res.json();
        if (data.path) {
          document.getElementById('sourceFileInput').value = data.path;
          if (!document.getElementById('topicInput').value) {
            const fileName = data.path.split(/[\\\\/]/).pop().replace(/\\.(pdf|html|htm|txt|md)$/i, '');
            document.getElementById('topicInput').value = fileName;
          }
        }
      } catch (err) {
        alert('Không thể mở hộp thoại duyệt file: ' + err.message);
      }
    }

    async function handleCreate(e) {
      e.preventDefault();
      const topic = document.getElementById('topicInput').value.trim();
      const trainer = document.getElementById('trainerInput').value.trim();
      const domain = document.getElementById('domainSelect').value;
      const slideCount = parseInt(document.getElementById('slideCountSelect').value);
      const sourceFile = document.getElementById('sourceFileInput').value.trim();
      const rawText = document.getElementById('rawTextInput').value.trim();
      const apiKey = document.getElementById('apiKeyInput').value.trim();

      const statusBox = document.getElementById('statusBox');
      const statusTitle = document.getElementById('statusTitle');
      const statusLogs = document.getElementById('statusLogs');
      const resultActions = document.getElementById('resultActions');
      const submitBtn = document.getElementById('submitBtn');

      statusBox.classList.remove('hidden');
      resultActions.classList.add('hidden');
      document.getElementById('spinner').classList.remove('hidden');
      submitBtn.disabled = true;
      submitBtn.classList.add('opacity-50');
      statusLogs.innerHTML = '';

      const addLog = (msg) => {
        const div = document.createElement('div');
        div.textContent = msg;
        statusLogs.appendChild(div);
        statusLogs.scrollTop = statusLogs.scrollHeight;
      };

      addLog('🚀 Bắt đầu kiến tạo bài giảng 4D Cinema V08...');
      addLog(`🎯 Chủ đề: ${topic} | Lĩnh vực: ${domain}`);
      if (sourceFile) addLog(`📂 Tệp nguồn: ${sourceFile}`);
      if (rawText) addLog(`📝 Văn bản trực tiếp: ${rawText.length} ký tự`);
      addLog(apiKey ? '🤖 Chế độ: Gemini AI + Fallback tự động' : '⚡ Chế độ: Smart Offline Engine (100% không phụ thuộc API Key)');

      try {
        const resp = await fetch('/api/build-lecture', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ topic, trainer, domain, slideCount, sourceFile, rawText, apiKey })
        });
        const result = await resp.json();
        if (result.success) {
          statusTitle.textContent = `🎉 ĐÃ XUẤT BẢN THÀNH CÔNG (${result.total_slides} TRANG 4D V08)!`;
          statusTitle.className = 'text-sm font-bold text-emerald-400';
          document.getElementById('spinner').classList.add('hidden');
          addLog(`[OK] Nguồn: ${result.input_type.toUpperCase()} | Chế độ: ${result.used_ai ? 'Gemini AI' : 'Smart Offline Engine'}`);
          addLog(`[OK] Thư mục: ${result.output_dir}`);
          currentOutputDir = result.output_dir;
          document.getElementById('openLectureBtn').href = result.server_url;
          resultActions.classList.remove('hidden');
          loadEvolutionLog();
        } else {
          statusTitle.textContent = '❌ Có lỗi xảy ra!';
          statusTitle.className = 'text-sm font-bold text-red-400';
          addLog('[LỖI] ' + result.error);
        }
      } catch (err) {
        statusTitle.textContent = '❌ Lỗi kết nối máy chủ!';
        addLog('[LỖI] ' + err.message);
      } finally {
        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-50');
      }
    }

    function copyOutputDir() {
      if (currentOutputDir) {
        navigator.clipboard.writeText(currentOutputDir).then(() => alert('✓ Đã sao chép đường dẫn thư mục!'));
      }
    }

    async function loadEvolutionLog() {
      try {
        const res = await fetch('/api/evolution-log');
        const data = await res.json();
        document.getElementById('evoCount').textContent = (data.lessons_learned || []).length;
        document.getElementById('evoVersionBadge').textContent = `${data.version || 'V08.0'} • ${data.total_verified_yt || 18} Video VN`;

        const lBox = document.getElementById('lessonsList');
        lBox.innerHTML = (data.lessons_learned || []).map(item => `
          <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-xs">
            <div class="flex items-center justify-between mb-1">
              <span class="font-bold text-amber-300">${item.category}</span>
              <span class="text-[10px] text-slate-500">${item.date}</span>
            </div>
            <p class="text-slate-300 leading-relaxed">${item.insight}</p>
          </div>
        `).join('') || '<p class="text-xs text-slate-500">Chưa có bài học nào.</p>';

        const hBox = document.getElementById('historyList');
        hBox.innerHTML = (data.build_history || []).map(h => `
          <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-xs">
            <div class="flex items-center justify-between mb-1">
              <span class="font-bold text-emerald-300">${h.topic}</span>
              <span class="text-[10px] text-slate-400">${h.total_slides} trang • ${h.mode}</span>
            </div>
            <div class="text-[10px] text-slate-500 font-mono truncate">${h.timestamp} • ${h.output_dir}</div>
          </div>
        `).join('') || '<p class="text-xs text-slate-500">Chưa có lịch sử xuất bản.</p>';
      } catch (e) {}
    }

    async function saveNewLesson() {
      const category = document.getElementById('lessonCatInput').value.trim();
      const insight = document.getElementById('lessonInsightInput').value.trim();
      if (!insight) return alert('Vui lòng nhập nội dung bài học!');
      await fetch('/api/evolution-lesson', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ category, insight })
      });
      document.getElementById('lessonCatInput').value = '';
      document.getElementById('lessonInsightInput').value = '';
      loadEvolutionLog();
    }

    async function addVerifiedYouTube() {
      const url = document.getElementById('newYtUrlInput').value.trim();
      const domain = document.getElementById('newYtDomainSelect').value;
      const st = document.getElementById('ytAddStatus');
      st.textContent = '⏳ Đang xác thực link YouTube qua oEmbed...';
      const res = await fetch('/api/evolution-youtube', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, domain })
      });
      const data = await res.json();
      if (data.ok) {
        st.innerHTML = `<span class="text-emerald-400">✓ Đã thêm: ${data.entry.title}</span>`;
        document.getElementById('newYtUrlInput').value = '';
        loadEvolutionLog();
      } else {
        st.innerHTML = `<span class="text-red-400">❌ ${data.error}</span>`;
      }
    }

    loadEvolutionLog();
  </script>
</body>
</html>
"""

class StudioRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ["/", "/index.html"]:
            data = HTML_UI.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if parsed.path in ["/api/browse-pdf", "/api/browse-file"]:
            chosen_path = ""
            try:
                import tkinter as tk
                from tkinter import filedialog
                root = tk.Tk()
                root.withdraw()
                root.attributes("-topmost", True)
                chosen_paths = list(filedialog.askopenfilenames(
                    title="Chọn Một Hoặc Nhiều Tài Liệu (.PDF, .HTML, .TXT, .JSON, Ảnh, Video)",
                    filetypes=[
                        ("Tất cả định dạng hỗ trợ", "*.pdf *.html *.htm *.txt *.md *.json *.png *.jpg *.jpeg *.webp *.svg *.gif *.mp4 *.webm *.mov"),
                        ("Tài liệu (PDF, HTML, TXT, JSON)", "*.pdf *.html *.htm *.txt *.md *.json"),
                        ("Hình ảnh & Video", "*.png *.jpg *.jpeg *.webp *.svg *.mp4 *.webm *.mov"),
                        ("All Files", "*.*"),
                    ],
                ))
                root.destroy()
            except Exception:
                chosen_paths = []
            self._send_json({"path": chosen_paths[0] if chosen_paths else "", "paths": chosen_paths})
            return

        if parsed.path == "/api/load-user-overrides":
            ov_file = BASE_DIR / "user_media_overrides.json"
            if ov_file.exists():
                try:
                    self._send_json(json.loads(ov_file.read_text(encoding="utf-8")))
                    return
                except Exception:
                    pass
            self._send_json({"slides": {}})
            return

        if parsed.path == "/api/evolution-log":
            log = load_evolution_log()
            log["total_verified_yt"] = len(VERIFIED_VN_YOUTUBE_BANK) + len(log.get("learned_youtube_bank", []))
            self._send_json(log)
            return

        # Static file serving with Referrer-Policy (Fixes YouTube Error 153)
        rel_path = urllib.parse.unquote(parsed.path.lstrip("/"))
        target_file = None
        for root_dir in [BASE_DIR, BASE_DIR / "1118 - Thong Diep Y Nghia - Gia Tri", BASE_DIR / "lessons"]:
            candidate = root_dir / rel_path
            if candidate.exists() and candidate.is_file():
                target_file = candidate
                break

        if target_file:
            mime_type, _ = mimetypes.guess_type(str(target_file))
            ext = target_file.suffix.lower()
            if ext == ".html": mime_type = "text/html; charset=utf-8"
            elif ext == ".js": mime_type = "application/javascript; charset=utf-8"
            elif ext == ".css": mime_type = "text/css; charset=utf-8"
            elif ext == ".svg": mime_type = "image/svg+xml"
            elif ext in [".png", ".jpg", ".jpeg", ".webp"]: mime_type = f"image/{ext.lstrip('.')}"
            elif ext == ".mp4": mime_type = "video/mp4"
            elif not mime_type: mime_type = "application/octet-stream"

            try:
                file_size = target_file.stat().st_size
                self.send_response(200)
                self.send_header("Content-Type", mime_type)
                self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(file_size))
                self.end_headers()
                with open(target_file, "rb") as f_in:
                    while chunk := f_in.read(65536):
                        self.wfile.write(chunk)
            except Exception:
                pass
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/upload-custom-media":
            qs = urllib.parse.parse_qs(parsed.query)
            fname = Path(qs.get("filename", ["custom_media.bin"])[0]).name
            custom_dir = BASE_DIR / "media" / "custom"
            custom_dir.mkdir(parents=True, exist_ok=True)
            content_len = int(self.headers.get("Content-Length", 0))
            raw_bytes = self.rfile.read(content_len) if content_len else b""
            target = custom_dir / fname
            target.write_bytes(raw_bytes)
            self._send_json({"ok": True, "rel_path": f"media/custom/{fname}"})
            return

        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
        data = json.loads(body)

        if parsed.path == "/api/save-user-overrides":
            ov_file = BASE_DIR / "user_media_overrides.json"
            ov_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            self._send_json({"ok": True})
            return

        if parsed.path == "/api/evolution-lesson":
            log = record_lesson_learned(data.get("category", ""), data.get("insight", ""))
            self._send_json({"ok": True, "log": log})
            return

        if parsed.path == "/api/evolution-youtube":
            res = verify_and_add_youtube(data.get("url", ""), data.get("domain", "tong_quat"))
            self._send_json(res)
            return

        if parsed.path == "/api/build-lecture":
            topic = data.get("topic", "Bài Giảng 4D").strip()
            trainer = data.get("trainer", "Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI").strip()
            domain = data.get("domain", "triet_ly_song")
            slide_count = int(data.get("slideCount", 15))
            raw_src = (data.get("sourceFile") or data.get("pdfPath") or "").strip()
            source_files = [s.strip() for s in raw_src.split(";") if s.strip()] if raw_src else []
            source_file = source_files[0] if source_files else None
            raw_text = (data.get("rawText") or "").strip() or None
            api_key = (data.get("apiKey") or "").strip() or None

            date_prefix = datetime.datetime.now().strftime("%m%d")
            clean_topic = re.sub(r'[^\w\s-]', '', topic).strip()[:45] or "Bai-Giang-4D"
            folder_name = f"{date_prefix} - {clean_topic}"
            output_dir = str(BASE_DIR / folder_name)

            try:
                res = build_4d_cinema_lecture(
                    topic=topic,
                    domain_key=domain,
                    output_dir=output_dir,
                    source_file=source_file,
                    source_files=source_files,
                    raw_text=raw_text,
                    target_count=slide_count,
                    trainer_name=trainer,
                    api_key=api_key,
                )
                server_url = f"http://localhost:{PORT}/{urllib.parse.quote(folder_name)}/index.html"
                try:
                    webbrowser.open(server_url)
                except Exception:
                    pass

                self._send_json({
                    "success": True,
                    "output_dir": res["output_dir"],
                    "html_path": res["html_path"],
                    "server_url": server_url,
                    "total_slides": res["total_slides"],
                    "used_ai": res["used_ai"],
                    "input_type": res["input_type"],
                })
            except Exception as e:
                import traceback
                traceback.print_exc()
                self._send_json({"success": False, "error": str(e)}, status=500)
            return

        self._send_json({"error": "Unknown endpoint"}, status=404)

def start_server():
    server = HTTPServer(("127.0.0.1", PORT), StudioRequestHandler)
    print("================================================================")
    print("  KTCSxAI 4D CREATOR STUDIO V08 - SELF-EVOLVING ENGINE")
    print(f"  May chu dang chay tai: http://localhost:{PORT}")
    print("================================================================")
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung may chu.")

if __name__ == "__main__":
    start_server()
