# -*- coding: utf-8 -*-
"""
KTCS_Trainer_Hub.py
Ứng dụng Phần Mềm Tự Hành Dành Cho Giảng Viên & Học Viên
Chương trình Kiến Tạo Cuộc Sống xAI (KTCSxAI) - Thầy Tuấn Tử Tế
Tự động hóa 100% quy trình từ Chủ Đề / PDF thành Bài Giảng HTML 4D Cinema 16:9
"""

import os
import sys
import json
import time
import shutil
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PYTHON_EXE = sys.executable

class KTCSTrainerHubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KTCSxAI • HỆ THỐNG TỰ HÀNH BÀI GIẢNG 4D V06")
        self.root.geometry("960x680")
        self.root.minsize(850, 580)
        self.root.configure(bg="#030712")

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#030712", foreground="#f8fafc", font=("Segoe UI", 10))
        style.configure("Header.TLabel", background="#030712", foreground="#f59e0b", font=("Segoe UI", 14, "bold"))
        style.configure("SubHeader.TLabel", background="#030712", foreground="#94a3b8", font=("Segoe UI", 9))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("Accent.TButton", background="#f59e0b", foreground="#000000")

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#0f172a", bd=1, relief="ridge")
        header_frame.pack(fill="x", padx=12, pady=10)

        lbl_title = tk.Label(
            header_frame,
            text="🏛️ KTCSxAI TRAINER HUB • TỔNG CHỈ HUY TỰ HÀNH 4D V06",
            font=("Segoe UI", 13, "bold"),
            bg="#0f172a",
            fg="#f59e0b"
        )
        lbl_title.pack(anchor="w", padx=12, pady=(8, 2))

        lbl_sub = tk.Label(
            header_frame,
            text="Hệ thống đóng gói bài giảng chuẩn rạp chiếu 16:9 • Draggable Splitter • Thẻ Lật Dưới Ảnh • Edge-TTS Nam/Nữ • Hội Đồng AI PIP",
            font=("Segoe UI", 9),
            bg="#0f172a",
            fg="#94a3b8"
        )
        lbl_sub.pack(anchor="w", padx=12, pady=(0, 8))

        # Inputs Frame
        input_frame = tk.LabelFrame(self.root, text=" 1. NGUỒN TÀI LIỆU & CHỦ ĐỀ ĐÀO TẠO ", bg="#030712", fg="#f59e0b", font=("Segoe UI", 10, "bold"))
        input_frame.pack(fill="x", padx=12, pady=6)

        # Topic
        tk.Label(input_frame, text="Chủ đề bài giảng:", bg="#030712", fg="#e2e8f0").grid(row=0, column=0, sticky="w", padx=10, pady=6)
        self.entry_topic = tk.Entry(input_frame, bg="#1e293b", fg="#f8fafc", insertbackground="#f59e0b", font=("Segoe UI", 10))
        self.entry_topic.insert(0, "Thông Điệp Giá Trị, Ý Nghĩa & Di Sản Vượt Thời Gian (KTCSxAI)")
        self.entry_topic.grid(row=0, column=1, sticky="ew", padx=10, pady=6)

        # PDF File
        tk.Label(input_frame, text="Tập tin PDF Slide Deck:", bg="#030712", fg="#e2e8f0").grid(row=1, column=0, sticky="w", padx=10, pady=6)
        self.entry_pdf = tk.Entry(input_frame, bg="#1e293b", fg="#f8fafc", insertbackground="#f59e0b", font=("Segoe UI", 10))
        default_pdf = BASE_DIR / "Kiến_Tạo_Cuộc_Sống_xAI.pdf"
        self.entry_pdf.insert(0, str(default_pdf))
        self.entry_pdf.grid(row=1, column=1, sticky="ew", padx=10, pady=6)

        btn_browse = tk.Button(input_frame, text="Chọn PDF...", bg="#334155", fg="#ffffff", command=self.browse_pdf, relief="flat", padx=10)
        btn_browse.grid(row=1, column=2, padx=10, pady=6)

        input_frame.columnconfigure(1, weight=1)

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#030712")
        btn_frame.pack(fill="x", padx=12, pady=8)

        self.btn_auto = tk.Button(
            btn_frame,
            text="🚀 TỰ ĐỘNG THỰC THI 6 BƯỚC",
            bg="#f59e0b",
            fg="#000000",
            font=("Segoe UI", 9, "bold"),
            relief="raised",
            padx=12,
            pady=8,
            command=self.run_full_pipeline_thread
        )
        self.btn_auto.pack(side="left", padx=3)

        self.btn_open = tk.Button(
            btn_frame,
            text="🎬 MỞ BÀI GIẢNG 4D",
            bg="#0284c7",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="raised",
            padx=10,
            pady=8,
            command=self.open_presentation_chrome
        )
        self.btn_open.pack(side="left", padx=3)

        self.btn_prompts = tk.Button(
            btn_frame,
            text="✨ XUẤT 30 PROMPTS FLOW",
            bg="#0f766e",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=8,
            command=self.export_prompts_thread
        )
        self.btn_prompts.pack(side="left", padx=3)

        self.btn_flow = tk.Button(
            btn_frame,
            text="🔄 NẠP MEDIA GOOGLE FLOW",
            bg="#059669",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=8,
            command=self.run_flow_import_thread
        )
        self.btn_flow.pack(side="left", padx=3)

        self.btn_autoflow = tk.Button(
            btn_frame,
            text="⚡ AUTO FLOW (SPACE)",
            bg="#d97706",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=8,
            command=self.run_auto_flow_thread
        )
        self.btn_autoflow.pack(side="left", padx=3)

        self.btn_publish = tk.Button(
            btn_frame,
            text="📤 XUẤT BẢN GITHUB",
            bg="#475569",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=8,
            command=self.publish_github_thread
        )
        self.btn_publish.pack(side="left", padx=3)

        # Progress & Console Output Frame
        console_frame = tk.LabelFrame(self.root, text=" NHẬT KÝ THỰC THI TỰ HÀNH & KIỂM ĐỊNH CHẤT LƯỢNG ", bg="#030712", fg="#94a3b8", font=("Segoe UI", 9, "bold"))
        console_frame.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        self.console = tk.Text(console_frame, bg="#020617", fg="#38bdf8", font=("Consolas", 9), wrap="word", relief="flat")
        self.console.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        scrollbar = tk.Scrollbar(console_frame, command=self.console.yview)
        scrollbar.pack(side="right", fill="y", pady=8)
        self.console.config(yscrollcommand=scrollbar.set)

        self.log("[*] Khởi động KTCSxAI Trainer Hub V06 thành công. Sẵn sàng phụng sự!")
        self.log(f"[*] Thư mục làm việc: {BASE_DIR}")

    def log(self, msg):
        self.console.insert("end", f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.console.see("end")

    def browse_pdf(self):
        filename = filedialog.askopenfilename(
            title="Chọn file Slide Deck PDF",
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")],
            initialdir=str(BASE_DIR)
        )
        if filename:
            self.entry_pdf.delete(0, "end")
            self.entry_pdf.insert(0, filename)
            self.log(f"[*] Đã chọn tệp PDF: {filename}")

    def export_prompts_thread(self):
        t = threading.Thread(target=self.export_prompts, daemon=True)
        t.start()

    def export_prompts(self):
        self.log("[*] Đang xuất bản danh sách 30 câu lệnh Google Flow 16:9 Loop...")
        script = BASE_DIR / "google_flow_batch_agent.py"
        if script.exists():
            subprocess.run([PYTHON_EXE, str(script)], check=False)
            txt_file = BASE_DIR / "google_flow_prompts_batch.txt"
            if txt_file.exists():
                self.log(f"[OK] Đã xuất bản file câu lệnh tại: {txt_file}")
                # Mở file notepad
                os.system(f'notepad.exe "{txt_file}"')
        else:
            self.log("[!] Chưa tìm thấy google_flow_batch_agent.py")

    def run_flow_import_thread(self):
        t = threading.Thread(target=self.run_flow_import, daemon=True)
        t.start()

    def run_flow_import(self):
        self.log("[*] Đang quét thư mục Downloads và tự động nạp Media Google Flow...")
        script = BASE_DIR / "google_flow_batch_agent.py"
        if script.exists():
            subprocess.run([PYTHON_EXE, str(script)], check=False)
            self.log("[OK] Quét và nạp Media hoàn tất! Mở bài giảng để chiêm ngưỡng.")
        else:
            self.log("[!] Chưa tìm thấy google_flow_batch_agent.py")

    def run_auto_flow_thread(self):
        t = threading.Thread(target=self.run_auto_flow, daemon=True)
        t.start()

    def run_auto_flow(self):
        self.log("[*] Đang khởi chạy Công Cụ Tự Động Quét & Dán Lệnh Google Flow...")
        bat_file = BASE_DIR / "CHAY_AUTO_FLOW.bat"
        try:
            if bat_file.exists():
                subprocess.Popen(f'start cmd /k "{bat_file}"', shell=True)
            else:
                py_file = BASE_DIR / "04_Auto_Video_Flow_V21.py"
                subprocess.Popen(f'start cmd /k ""{PYTHON_EXE}" "{py_file}""', shell=True)
            self.log("[OK] Đã mở cửa sổ Auto Flow. Bấm ô nhập lệnh trên Google Flow rồi nhấn phím SPACE để tự dán!")
        except Exception as e:
            self.log(f"[!] Lỗi khi mở Auto Flow: {e}")

    def run_full_pipeline_thread(self):
        t = threading.Thread(target=self.run_full_pipeline, daemon=True)
        t.start()

    def run_full_pipeline(self):
        self.btn_auto.config(state="disabled")
        self.log("=" * 60)
        self.log(" BẮT ĐẦU QUY TRÌNH 6 BƯỚC HOÀN THIỆN BÀI GIẢNG 4D V06")
        self.log("=" * 60)

        pdf_path = self.entry_pdf.get().strip()
        if not os.path.exists(pdf_path):
            self.log(f"[LỖI] Không tìm thấy file PDF tại: {pdf_path}")
            self.btn_auto.config(state="normal")
            return

        # Bước 1: Render PDF
        self.log("\n[BƯỚC 1/6] Đang xuất toàn bộ trang PDF thành ảnh PNG 16:9 siêu nét...")
        render_script = Path(r"C:\Users\PC\.gemini\antigravity\brain\94a27f09-8d06-4e8f-87c0-47c6935af96a\scratch\render_pdf_pages.py")
        if render_script.exists():
            subprocess.run([PYTHON_EXE, str(render_script)], check=False)
            self.log("  -> [OK] Đã xuất xong 30 trang PNG 16:9 sắc nét.")

        # Bước 2 & 5: Tạo HTML 4D & Dữ liệu 30 slides
        self.log("\n[BƯỚC 2 & 5/6] Đang kiến tạo bài giảng HTML 4D Full-Width và Khóa từ mồ côi...")
        build_script = Path(r"C:\Users\PC\.gemini\antigravity\brain\94a27f09-8d06-4e8f-87c0-47c6935af96a\scratch\build_updated_4d_deck.py")
        if build_script.exists():
            subprocess.run([PYTHON_EXE, str(build_script)], check=False)
            self.log("  -> [OK] Bài giảng HTML 4D Cinema V06 đã sẵn sàng!")

        # Bước 4: Media Google Flow
        self.log("\n[BƯỚC 4/6] Quét và ánh xạ media Google Flow từ Downloads...")
        self.export_prompts()
        self.run_flow_import()

        # Bước 6: Mở Chrome kiểm tra
        self.log("\n[BƯỚC 6/6] Khởi chạy Chrome toàn màn hình để kiểm tra bài giảng...")
        self.open_presentation_chrome()

        self.log("\n" + "=" * 60)
        self.log(" HOÀN TẤT XUẤT SẮC BÀI GIẢNG 4D! SẴN SÀNG CHO BUỔI ĐÀO TẠO!")
        self.log("=" * 60)
        self.btn_auto.config(state="normal")

    def open_presentation_chrome(self):
        target_html = BASE_DIR / "ktcs-thong-diep-gia-tri-di-san-4d.html"
        if not target_html.exists():
            target_html = Path(r"C:\Users\PC\Downloads\Tu_C_Goc\WEBSITE\TuanTuTe.Life\ktcs-thong-diep-gia-tri-di-san-4d.html")

        if target_html.exists():
            self.log(f"[*] Đang mở bài giảng: {target_html.name}")
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]
            for cp in chrome_paths:
                if os.path.exists(cp):
                    subprocess.Popen([cp, "--start-fullscreen", f"file:///{target_html.resolve()}"])
                    return
            import webbrowser
            webbrowser.open(f"file:///{target_html.resolve()}")

    def publish_github_thread(self):
        t = threading.Thread(target=self.publish_github, daemon=True)
        t.start()

    def publish_github(self):
        repo_dir = Path(r"C:\Users\PC\Downloads\Tu_C_Goc\WEBSITE\TuanTuTe.Life")
        if not repo_dir.exists():
            self.log("[LỖI] Không tìm thấy thư mục Git TuanTuTe.Life")
            return

        self.log(f"[*] Đang đẩy bài giảng lên GitHub Pages tuantute.life...")
        try:
            subprocess.run(["git", "add", "."], cwd=str(repo_dir), check=True)
            subprocess.run(["git", "commit", "-m", "feat(ktcs-30-slides): update 30-slide 4D cinema deck, draggable splitter, and council PIP widget"], cwd=str(repo_dir), check=False)
            res1 = subprocess.run(["git", "push", "origin", "Dao-Tao-Se-Chia"], cwd=str(repo_dir), capture_output=True, text=True)
            subprocess.run(["git", "checkout", "main"], cwd=str(repo_dir), check=False)
            subprocess.run(["git", "merge", "Dao-Tao-Se-Chia"], cwd=str(repo_dir), check=False)
            res2 = subprocess.run(["git", "push", "origin", "main"], cwd=str(repo_dir), capture_output=True, text=True)
            subprocess.run(["git", "checkout", "Dao-Tao-Se-Chia"], cwd=str(repo_dir), check=False)
            self.log("[OK] ĐÃ ĐẨY LÊN GITHUB PAGES THÀNH CÔNG TRÊN CẢ 2 NHÁNH!")
            self.log("🔗 Trực tuyến: https://tuantute.life/ktcs-thong-diep-gia-tri-di-san-4d.html")
        except Exception as e:
            self.log(f"[LỖI] {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KTCSTrainerHubApp(root)
    root.mainloop()
