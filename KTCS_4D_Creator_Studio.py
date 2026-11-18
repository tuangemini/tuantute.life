# -*- coding: utf-8 -*-
"""
KTCS 4D Creator Studio - Ứng Dụng Phần Mềm Tự Hành (KTCSxAI)
Dành cho Thầy Tuấn Tử Tế và các thế hệ học viên, giảng viên
Chỉ cần nhập chủ đề / nạp file PDF -> Tự động sinh trọn bộ bài giảng 4D Cinema 16:9 hoàn hảo.
"""

import os
import sys
import json
import time
import urllib.parse
import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Add scripts directory to path
BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / ".agents" / "skills" / "ktcs-4d-training" / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from ktcs_universal_engine import build_4d_cinema_lecture, DOMAIN_FRAMEWORKS
except ImportError:
    # Fallback to local import
    import ktcs_universal_engine
    build_4d_cinema_lecture = ktcs_universal_engine.build_4d_cinema_lecture
    DOMAIN_FRAMEWORKS = ktcs_universal_engine.DOMAIN_FRAMEWORKS

PORT = 7890

HTML_UI = """<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KTCSxAI • ỨNG DỤNG KIẾN TẠO BÀI GIẢNG 4D CINEMA 16:9</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #030712; color: #f3f4f6; }
    .font-display { font-family: 'Space Grotesk', sans-serif; }
    .glass-card { background: rgba(17, 24, 39, 0.7); backdrop-filter: blur(16px); border: 1px solid rgba(55, 65, 81, 0.6); }
    .glass-card:hover { border-color: rgba(245, 158, 11, 0.4); }
    .glow-cyan { box-shadow: 0 0 25px -5px rgba(6, 182, 212, 0.3); }
    .glow-amber { box-shadow: 0 0 25px -5px rgba(245, 158, 11, 0.35); }
    input, select, textarea { background-color: rgba(3, 7, 18, 0.8) !important; }
  </style>
</head>
<body class="min-h-screen flex flex-col items-center justify-start p-4 lg:p-8 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-gray-950 to-black">

  <!-- Header Banner -->
  <header class="w-full max-w-4xl text-center mb-8 pt-4">
    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold tracking-wider mb-3">
      <span class="animate-pulse">⚡</span> KTCSxAI • STUDIO TỰ HÀNH BÀI GIẢNG 4D
    </div>
    <h1 class="text-2xl lg:text-4xl font-extrabold font-display text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-amber-400 to-amber-500 mb-2">
      KIẾN TẠO BÀI GIẢNG 4D CINEMA 16:9
    </h1>
    <p class="text-xs lg:text-sm text-slate-400 max-w-2xl mx-auto leading-relaxed">
      Dành cho Thầy Tuấn Tử Tế & Học viên. Chỉ cần nhập chủ đề hoặc nạp file PDF, hệ thống tự động sinh trọn bộ bài giảng HTML 4D Cinema tương tác, khóa từ mồ côi và âm thanh tiếng Việt.
    </p>
  </header>

  <!-- Main Creator Form -->
  <main class="w-full max-w-4xl glass-card rounded-3xl p-6 lg:p-8 shadow-2xl relative overflow-hidden">
    <form id="createForm" onsubmit="handleCreate(event)" class="space-y-6">
      
      <!-- Row 1: Chủ đề & Giảng viên -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
          <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider mb-1.5">
            🎯 Chủ Đề Bài Giảng (Mọi Lĩnh Vực):
          </label>
          <input type="text" id="topicInput" required 
                 placeholder="VD: Bán Hàng Giá Trị Cao Bằng Trí Tuệ Cảm Xúc, Lãnh Đạo Kỷ Nguyên AI..." 
                 class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-400 transition">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
            👤 Tên Giảng Viên:
          </label>
          <input type="text" id="trainerInput" value="Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI" 
                 class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-amber-400 transition">
        </div>
      </div>

      <!-- Row 2: Lĩnh vực & Số Slide -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2">
          <label class="block text-xs font-bold text-cyan-300 uppercase tracking-wider mb-1.5">
            🏛️ Lĩnh Vực Đào Tạo:
          </label>
          <select id="domainSelect" class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-cyan-400 transition">
            <option value="triet_ly_song">🌟 Thân - Tâm - Trí & Di Sản Vượt Thời Gian (KTCSxAI)</option>
            <option value="lanh_dao">👑 Lãnh Đạo Vượt Bão & Quản Trị Đội Ngũ</option>
            <option value="ban_hang">💎 Bán Hàng Giá Trị Cao & Kể Chuyện (Storyselling)</option>
            <option value="cong_nghe_ai">🤖 Kiến Trúc Sư AI & Làm Chủ Kỷ Nguyên Số</option>
            <option value="giao_duc">🎓 Đào Tạo Giảng Viên & Sư Phạm Chuyển Hóa</option>
            <option value="tai_chinh">💰 Tài Chính Cá Nhân Vững Bền & Thịnh Vượng Đích Thực</option>
            <option value="suc_khoe">🌱 Sinh Khí Trẻ Hóa & Sức Khỏe Thân Tâm</option>
            <option value="tong_quat">⚡ Chương Trình Đào Tạo Chuyển Hóa Tổng Quát</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
            📊 Số Trang (Nếu Không Dùng PDF):
          </label>
          <select id="slideCountSelect" class="w-full border border-slate-700 rounded-xl p-3 text-sm text-slate-100 focus:outline-none focus:border-cyan-400 transition">
            <option value="15">15 Trang (Chuẩn Seminar 60 phút)</option>
            <option value="10">10 Trang (Cô đọng 30 phút)</option>
            <option value="20">20 Trang (Chuyên sâu 90 phút)</option>
            <option value="30" selected>30 Trang (Master Class Vượt Thời Gian)</option>
          </select>
        </div>
      </div>

      <!-- Row 3: Nạp Tệp PDF (Tùy chọn) -->
      <div>
        <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1.5">
          📄 Nạp Tệp PDF Slide Deck (Tùy Chọn - NotebookLM, Canva, PowerPoint):
        </label>
        <div class="flex items-center gap-3">
          <input type="text" id="pdfPathInput" placeholder="Đường dẫn file .pdf hoặc bấm nút duyệt bên cạnh..." 
                 class="flex-1 border border-slate-700 rounded-xl p-3 text-sm text-slate-200 font-mono text-xs focus:outline-none focus:border-amber-400 transition">
          <button type="button" onclick="browsePDF()" class="bg-slate-800 hover:bg-slate-700 text-amber-400 border border-slate-700 font-bold text-xs px-4 py-3 rounded-xl transition flex items-center gap-1.5 shrink-0">
            📁 Duyệt File PDF
          </button>
        </div>
        <p class="text-[11px] text-slate-500 mt-1">
          💡 <em>Nếu chọn PDF, hệ thống sẽ tự động đếm đủ N trang và xuất ảnh WebP 16:9 siêu nét, đồng bộ tuyệt đối 1 trang PDF = 1 trang HTML!</em>
        </p>
      </div>

      <!-- Action Button -->
      <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="text-xs text-slate-400 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          Sẵn sàng xuất bản chuẩn 16:9 • Khóa từ mồ côi • 100% Offline
        </div>
        <button type="submit" id="submitBtn" 
                class="w-full sm:w-auto bg-gradient-to-r from-amber-500 via-amber-600 to-amber-500 hover:from-amber-400 hover:to-amber-500 text-black font-extrabold text-sm px-8 py-3.5 rounded-2xl shadow-xl glow-amber flex items-center justify-center gap-2 transition transform hover:scale-105 active:scale-95">
          <span>⚡</span> BẮT ĐẦU KIẾN TẠO BÀI GIẢNG 4D (1-CLICK)
        </button>
      </div>
    </form>

    <!-- Progress & Result Modal -->
    <div id="statusBox" class="hidden mt-6 p-5 rounded-2xl bg-slate-950 border border-cyan-500/40">
      <div class="flex items-center gap-3 mb-3">
        <div id="spinner" class="w-5 h-5 border-2 border-cyan-400 border-t-transparent rounded-full animate-spin"></div>
        <h4 id="statusTitle" class="text-sm font-bold text-cyan-300">Đang khởi tạo hệ thống...</h4>
      </div>
      <div id="statusLogs" class="text-xs font-mono text-slate-400 space-y-1 max-h-40 overflow-y-auto mb-4 p-2 bg-slate-900 rounded-lg">
      </div>
      <div id="resultActions" class="hidden flex items-center gap-3 flex-wrap">
        <a id="openLectureBtn" href="#" target="_blank" 
           class="bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow-lg flex items-center gap-2 hover:from-emerald-400 hover:to-teal-500 transition">
          🎬 Mở Bài Giảng Trực Tiếp (16:9)
        </a>
        <button onclick="copyOutputDir()" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs px-4 py-2.5 rounded-xl transition">
          📂 Chép Đường Dẫn Thư Mục
        </button>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="mt-8 text-center text-xs text-slate-500">
    Hệ thống KTCSxAI Studio • Bản quyền thuộc về Thầy Tuấn Tử Tế (Nguyễn Anh Tuấn)
  </footer>

  <script>
    let currentOutputDir = '';

    async function browsePDF() {
      try {
        const res = await fetch('/api/browse-pdf');
        const data = await res.json();
        if (data.path) {
          document.getElementById('pdfPathInput').value = data.path;
          if (!document.getElementById('topicInput').value) {
            const fileName = data.path.split(/[\\\\/]/).pop().replace('.pdf', '');
            document.getElementById('topicInput').value = fileName;
          }
        }
      } catch (err) {
        alert('Không thể mở cửa sổ duyệt file: ' + err.message);
      }
    }

    async function handleCreate(e) {
      e.preventDefault();
      const topic = document.getElementById('topicInput').value.trim();
      const trainer = document.getElementById('trainerInput').value.trim();
      const domain = document.getElementById('domainSelect').value;
      const slideCount = parseInt(document.getElementById('slideCountSelect').value);
      const pdfPath = document.getElementById('pdfPathInput').value.trim();

      const statusBox = document.getElementById('statusBox');
      const statusTitle = document.getElementById('statusTitle');
      const statusLogs = document.getElementById('statusLogs');
      const resultActions = document.getElementById('resultActions');
      const submitBtn = document.getElementById('submitBtn');

      statusBox.classList.remove('hidden');
      resultActions.classList.add('hidden');
      submitBtn.disabled = true;
      submitBtn.classList.add('opacity-50');

      statusLogs.innerHTML = '';
      const addLog = (msg) => {
        const div = document.createElement('div');
        div.textContent = msg;
        statusLogs.appendChild(div);
        statusLogs.scrollTop = statusLogs.scrollHeight;
      };

      addLog('🚀 Bắt đầu quá trình kiến tạo bài giảng 4D Cinema...');
      addLog(`🎯 Chủ đề: ${topic}`);
      addLog(`🏛️ Lĩnh vực: ${domain}`);
      if (pdfPath) addLog(`📄 PDF đính kèm: ${pdfPath}`);

      try {
        const resp = await fetch('/api/build-lecture', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            topic: topic,
            trainer: trainer,
            domain: domain,
            slideCount: slideCount,
            pdfPath: pdfPath
          })
        });

        const result = await resp.json();
        if (result.success) {
          statusTitle.textContent = `🎉 ĐÃ XUẤT BẢN THÀNH CÔNG (${result.total_slides} TRANG 4D CINEMA)!`;
          statusTitle.className = 'text-sm font-bold text-emerald-400';
          document.getElementById('spinner').classList.add('hidden');
          addLog(`[OK] Thư mục: ${result.output_dir}`);
          addLog(`[OK] Trình chiếu: ${result.html_path}`);
          currentOutputDir = result.output_dir;

          document.getElementById('openLectureBtn').href = 'file:///' + result.html_path.replace(/\\\\/g, '/');
          resultActions.classList.remove('hidden');
        } else {
          statusTitle.textContent = '❌ Có lỗi xảy ra trong quá trình xuất bản!';
          statusTitle.className = 'text-sm font-bold text-red-400';
          addLog(`[LỖI] ${result.error}`);
        }
      } catch (err) {
        statusTitle.textContent = '❌ Lỗi kết nối máy chủ!';
        addLog(`[LỖI] ${err.message}`);
      } finally {
        submitBtn.disabled = false;
        submitBtn.classList.remove('opacity-50');
      }
    }

    function copyOutputDir() {
      if (currentOutputDir) {
        navigator.clipboard.writeText(currentOutputDir).then(() => {
          alert('✓ Đã sao chép đường dẫn thư mục bài giảng!');
        });
      }
    }
  </script>
</body>
</html>
"""

class StudioRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_UI.encode("utf-8"))
        elif parsed.path == "/api/browse-pdf":
            # Call native tkinter file chooser
            chosen_path = ""
            try:
                import tkinter as tk
                from tkinter import filedialog
                root = tk.Tk()
                root.withdraw()
                root.attributes("-topmost", True)
                chosen_path = filedialog.askopenfilename(
                    title="Chọn Tệp PDF Bài Giảng (KTCSxAI)",
                    filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
                )
                root.destroy()
            except Exception as e:
                pass
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"path": chosen_path}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/build-lecture":
            content_len = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_len).decode("utf-8")
            data = json.loads(body)

            topic = data.get("topic", "Bài Giảng 4D").strip()
            trainer = data.get("trainer", "Nguyễn Anh Tuấn (Tuấn Tử Tế) • KTCSxAI").strip()
            domain = data.get("domain", "triet_ly_song")
            slide_count = int(data.get("slideCount", 15))
            pdf_path = data.get("pdfPath", "").strip() or None

            # Generate target directory name with date
            import datetime
            date_prefix = datetime.datetime.now().strftime("%m%d")
            clean_topic = re.sub(r'[^\w\s-]', '', topic).strip()
            folder_name = f"{date_prefix} - {clean_topic}"
            
            output_dir = str(BASE_DIR / folder_name)

            try:
                res = build_4d_cinema_lecture(
                    topic=topic,
                    domain_key=domain,
                    output_dir=output_dir,
                    pdf_path=pdf_path,
                    target_count=slide_count,
                    trainer_name=trainer
                )

                # Automatically open in Chrome
                try:
                    target_html_url = "file:///" + res["html_path"].replace("\\", "/")
                    webbrowser.open(target_html_url)
                except Exception:
                    pass

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "output_dir": res["output_dir"],
                    "html_path": res["html_path"],
                    "total_slides": res["total_slides"]
                }).encode("utf-8"))

            except Exception as e:
                import traceback
                traceback.print_exc()
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": str(e)
                }).encode("utf-8"))

def start_server():
    server = HTTPServer(("127.0.0.1", PORT), StudioRequestHandler)
    print(f"================================================================")
    print(f"  KTCSxAI 4D CREATOR STUDIO - HE THONG TU HANH")
    print(f"  May chu dang chay tai: http://localhost:{PORT}")
    print(f"  Tu dong mo trinh duyet Chrome...")
    print(f"================================================================")
    
    # Open browser
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung may chu.")

if __name__ == "__main__":
    start_server()
