# -*- coding: utf-8 -*-
import os, json, urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OVERRIDES_FILE = os.path.join(BASE_DIR, "user_media_overrides.json")
CUSTOM_MEDIA_DIR = os.path.join(BASE_DIR, "media", "custom")
os.makedirs(CUSTOM_MEDIA_DIR, exist_ok=True)

class KTCSHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/api/load-user-overrides"):
            data = {}
            if os.path.exists(OVERRIDES_FILE):
                try:
                    with open(OVERRIDES_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception:
                    data = {}
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length > 0 else b""
        if self.path.startswith("/api/save-user-overrides"):
            try:
                data = json.loads(raw.decode("utf-8"))
                with open(OVERRIDES_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                resp = json.dumps({"ok": True}).encode("utf-8")
                self.send_response(200)
            except Exception as e:
                resp = json.dumps({"ok": False, "error": str(e)}).encode("utf-8")
                self.send_response(400)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(resp)))
            self.end_headers()
            self.wfile.write(resp)
            return
        if self.path.startswith("/api/upload-custom-media"):
            parsed = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(parsed.query)
            fname = os.path.basename(qs.get("filename", ["custom_media.bin"])[0])
            dest = os.path.join(CUSTOM_MEDIA_DIR, fname)
            with open(dest, "wb") as f:
                f.write(raw)
            resp = json.dumps({"ok": True, "rel_path": f"media/custom/{fname}"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(resp)))
            self.end_headers()
            self.wfile.write(resp)
            return
        self.send_response(404)
        self.end_headers()

if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 7890), KTCSHandler)
    print("KTCSxAI Server running at http://localhost:7890")
    srv.serve_forever()
