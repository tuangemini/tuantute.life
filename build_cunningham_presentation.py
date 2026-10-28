# -*- coding: utf-8 -*-
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

repo_dir = r"c:\Users\PC\Downloads\Tu_C_Goc\WEBSITE\TuanTuTe.Life"
output_file = os.path.join(repo_dir, "bac-si-cunningham-nguoi-chay-nhanh-nhat-the-gioi.html")

# Lấy ảnh đại diện chân dung của Thầy Nguyễn Anh Tuấn dạng base64 từ file v06 có sẵn
v06_path = os.path.join(repo_dir, "thuyet-trinh-bni-force-ktcs-xai-v06.html")
avatar_base64 = ""
if os.path.exists(v06_path):
    with open(v06_path, "r", encoding="utf-8") as f:
        v06_text = f.read()
        import re
        m = re.search(r'src="(data:image/jpeg;base64,[^"]+)"', v06_text)
        if m:
            avatar_base64 = m.group(1)

if not avatar_base64:
    avatar_base64 = "tuan-tu-te-portrait.jpg"

html_content = f"""<!DOCTYPE html>
<!--
  ==========================================================================
  TÊN FILE: bac-si-cunningham-nguoi-chay-nhanh-nhat-the-gioi.html
  PHIÊN BẢN: Chuẩn KTCSxAI 4D • Kỷ Nguyên Trí Tuệ AI Cho Người Trung Niên
  CHỦ ĐỀ: Bác Sĩ Glenn Cunningham – Người Chạy Nhanh Nhất Thế Giới & Đôi Chân Thần Tốc AI
  DIỄN GIẢ: Nhà đào tạo Nguyễn Anh Tuấn (Tuấn Tử Tế Từ Tâm)
  ĐỐI TƯỢNG: Học viên trung niên Việt Nam (Tuổi 38 - 59+)
  ==========================================================================
-->
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bác Sĩ Cunningham: Người Chạy Nhanh Nhất Thế Giới &amp; Đôi Chân Thần Tốc AI (Nguyễn Anh Tuấn)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Dancing+Script:wght@700&family=Patrick+Hand&family=Playfair+Display:ital,wght@0,700;0,800;1,600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-deep: #040711;
      --bg-navy: #0a1428;
      --bg-card: rgba(12, 22, 46, 0.94);
      --bg-panel: rgba(8, 17, 38, 0.92);
      --bni-crimson: #cf2030;
      --bni-crimson-glow: rgba(207, 32, 48, 0.45);
      --gold-primary: #f5c451;
      --gold-light: #ffe9ad;
      --gold-dark: #c48a10;
      --cyan-sky: #38bdf8;
      --emerald-peace: #34d399;
      --rose-warm: #fb7185;
      --text-main: #ffffff;
      --text-muted: #e2e8f0;
      --border-glass: rgba(245, 196, 81, 0.48);
      --shadow-elevated: 0 24px 65px rgba(0, 0, 0, 0.88);
      --font-body: 'Be Vietnam Pro', sans-serif;
      --font-heading: 'Playfair Display', serif;
      --card-radius: 24px;
      --topbar-h: 68px;
      --bottomdock-h: 66px;
    }}

    /* PHONG CÁCH 2: VẼ TAY & VIẾT TAY NGHỆ THUẬT */
    body.style-handdrawn {{
      --bg-deep: #f4ebd9;
      --bg-navy: #efe2c8;
      --bg-card: #fffdf7;
      --bg-panel: #faf3e3;
      --gold-primary: #b45309;
      --gold-light: #991b1b;
      --gold-dark: #92400e;
      --cyan-sky: #0369a1;
      --emerald-peace: #15803d;
      --rose-warm: #be123c;
      --text-main: #1e293b;
      --text-muted: #334155;
      --border-glass: #991b1b;
      --shadow-elevated: 6px 8px 0px rgba(153, 27, 27, 0.25);
      --font-body: 'Patrick Hand', 'Be Vietnam Pro', cursive;
      --font-heading: 'Dancing Script', 'Playfair Display', cursive;
      --card-radius: 18px 28px 20px 26px;
      background-image: radial-gradient(rgba(120, 53, 15, 0.16) 1px, transparent 1px);
      background-size: 22px 22px;
    }}
    body.style-handdrawn .slide-inner {{ border: 3px dashed #991b1b; }}
    body.style-handdrawn .senior-panel {{ border: 2px solid #92400e; }}
    body.style-handdrawn .poem-box-large {{ background: rgba(207, 32, 48, 0.08); color: #7c2d12; border-left: 5px solid #cf2030; }}
    body.style-handdrawn .state-old-lg {{ color: #be123c; }}
    body.style-handdrawn .state-new-lg {{ color: #15803d; }}

    /* PHONG CÁCH 3: ĐỒ HOẠ INFOGRAPHIC */
    body.style-infographic {{
      --bg-deep: #0b192c;
      --bg-navy: #1e3e62;
      --bg-card: rgba(15, 34, 60, 0.96);
      --bg-panel: rgba(22, 48, 82, 0.92);
      --gold-primary: #ff6500;
      --gold-light: #ff9f45;
      --gold-dark: #cc5200;
      --cyan-sky: #00d2ff;
      --emerald-peace: #00f5d4;
      --border-glass: rgba(0, 210, 255, 0.5);
      --card-radius: 14px;
    }}

    /* PHONG CÁCH 4: HOẠT HÌNH 3D */
    body.style-cartoon {{
      --bg-deep: #1e1b4b;
      --bg-navy: #312e81;
      --bg-card: rgba(49, 46, 129, 0.94);
      --bg-panel: rgba(67, 56, 202, 0.65);
      --gold-primary: #facc15;
      --gold-light: #fef08a;
      --gold-dark: #eab308;
      --cyan-sky: #38bdf8;
      --emerald-peace: #4ade80;
      --border-glass: rgba(250, 204, 21, 0.65);
      --card-radius: 34px;
    }}

    /* ẨN TRANG (HIDE SLIDE) */
    body.mode-scroll .slide.is-hidden {{ display: none !important; }}
    .slide-dot.is-hidden {{ display: none; }}
    .btn-hide-slides {{
      background: rgba(251, 113, 133, 0.18);
      border: 1px solid rgba(251, 113, 133, 0.6);
      color: #ffe4e8;
      padding: 7px 13px;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.8rem;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
    }}
    .btn-hide-slides:hover {{ background: #fb7185; color: #1a0509; }}
    .btn-hide-slides .hide-count-badge {{
      display: inline-block; min-width: 18px; padding: 0 6px; margin-left: 4px;
      border-radius: 999px; background: #fb7185; color: #1a0509; font-size: 0.72rem; text-align: center;
    }}
    .btn-hide-slides .hide-count-badge.zero {{ background: rgba(255,255,255,0.25); color: #fff; }}
    .dock-hide-check {{
      display: inline-flex; align-items: center; gap: 6px;
      padding: 6px 12px; border-radius: 999px;
      border: 1px solid rgba(251, 113, 133, 0.55);
      background: rgba(251, 113, 133, 0.12);
      color: #ffe4e8; font-size: 0.78rem; font-weight: 800;
      cursor: pointer; white-space: nowrap; user-select: none;
    }}
    .dock-hide-check input {{ width: 17px; height: 17px; accent-color: #fb7185; cursor: pointer; }}
    .dock-hide-check:hover {{ background: rgba(251, 113, 133, 0.28); }}
    .hide-modal-card {{ max-width: 760px; }}
    .hide-toolbar {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }}
    .hide-toolbar button {{
      background: rgba(245, 196, 81, 0.16); border: 1px solid rgba(245, 196, 81, 0.5);
      color: #ffe9ad; padding: 7px 14px; border-radius: 999px; cursor: pointer;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.8rem; font-weight: 800;
    }}
    .hide-toolbar button:hover {{ background: #f5c451; color: #030714; }}
    .hide-list {{ max-height: 56vh; overflow-y: auto; display: flex; flex-direction: column; gap: 6px; padding-right: 4px; }}
    .hide-row {{
      display: flex; align-items: center; gap: 12px; padding: 9px 14px; border-radius: 12px;
      background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.14);
      cursor: pointer; color: #fff; font-size: 0.95rem; font-weight: 600;
    }}
    .hide-row:hover {{ background: rgba(255,255,255,0.12); }}
    .hide-row input {{ width: 20px; height: 20px; accent-color: #fb7185; flex-shrink: 0; cursor: pointer; }}
    .hide-row .hide-row-title {{ flex: 1; }}
    .hide-row .hide-row-state {{ font-size: 0.75rem; font-weight: 800; color: #34d399; white-space: nowrap; }}
    .hide-row.is-hidden {{ opacity: 0.6; border-style: dashed; border-color: #fb7185; }}
    .hide-row.is-hidden .hide-row-title {{ text-decoration: line-through; }}
    .hide-row.is-hidden .hide-row-state {{ color: #fb7185; }}
    .hide-row.is-current {{ outline: 2px solid #f5c451; }}

    img.bg-photo[data-mode=art] {{ filter: none !important; object-fit: cover; }}
    body.style-cinematic img.bg-photo {{ filter: contrast(1.08) saturate(1.05); }}
    body.style-handdrawn img.bg-photo {{ filter: sepia(.35) contrast(1.05); }}
    body.style-infographic img.bg-photo {{ filter: saturate(1.3) hue-rotate(-8deg); }}
    body.style-cartoon img.bg-photo {{ filter: saturate(1.45) contrast(1.08); }}
    .giant-art-frame {{ position: relative; }}
    .photo-tools {{ position: absolute; right: 8px; bottom: 8px; display: flex; gap: 6px; z-index: 5; opacity: 0; transition: opacity .25s; }}
    .giant-art-frame:hover .photo-tools, .photo-tools:focus-within {{ opacity: 1; }}
    .photo-tools button, .photo-tools label {{
      background: rgba(4,7,17,.82); color: #ffe9ad; border: 1px solid rgba(245,196,81,.6);
      border-radius: 999px; padding: 5px 11px; font: 800 .72rem 'Be Vietnam Pro', sans-serif; cursor: pointer; white-space: nowrap;
    }}
    .photo-tools button:hover, .photo-tools label:hover {{ background: #f5c451; color: #030714; }}
    .deck-progress {{ position: fixed; left: 0; top: var(--topbar-h); height: 4px; width: 0; z-index: 1001;
      background: linear-gradient(90deg, #cf2030, #f5c451, #38bdf8); box-shadow: 0 0 12px #f5c451; transition: width .6s ease; }}
    .audio-pill input[type=range] {{ width: 70px; accent-color: #f5c451; }}
    .audio-pill button {{ background: rgba(245,196,81,.18); border: 1px solid rgba(245,196,81,.5); color: #ffe9ad; border-radius: 999px; padding: 4px 10px; font-weight: 800; cursor: pointer; }}
    .audio-pill button.on {{ background: #f5c451; color: #030714; }}

    /* LẤP ĐẦY TOÀN MÀN HÌNH - CHỮ BE VIETNAM PRO TO RÕ NÉT */
    .slide {{ padding: 4px 0.6vw !important; }}
    .slide-inner {{ width: 99vw !important; max-width: none !important; height: 100%; display: flex; flex-direction: column; padding: 1.2vh 1.4vw 2.2vh !important; }}
    .slide-header {{ margin-bottom: 1vh; }}
    .senior-stage {{ flex: 1; min-height: 0; gap: 1.4vw; grid-template-columns: 1.08fr 1fr; }}
    .senior-stage.one {{ grid-template-columns: 1fr; }}
    .senior-panel {{ justify-content: space-evenly; padding: 1.8vh 1.4vw; min-height: 0; overflow-y: auto; scrollbar-width: thin; }}
    .giant-art-frame {{ flex: 1; min-height: 0; }}
    .slide-title, .senior-heading, .senior-text, .art-caption, .kpi b, .bigq {{ font-family: 'Be Vietnam Pro', sans-serif !important; }}
    .slide-title {{ font-size: clamp(1.5rem, 4vh, 2.9rem); }}
    .senior-heading {{ font-size: clamp(1.3rem, 3.3vh, 2.5rem); }}
    .senior-text {{ font-size: clamp(1.1rem, 2.6vh, 2.1rem); line-height: 1.5; }}
    .art-caption {{ font-size: clamp(1.2rem, 2.8vh, 2.1rem); }}
    .state-old-lg, .state-new-lg {{ font-size: clamp(.95rem, 2.2vh, 1.7rem); }}
    .verb-bridge-lg {{ font-size: clamp(.8rem, 1.8vh, 1.2rem); }}
    .interactive-btn-lg, .btn-slide-voice, .chips button, .chips-reset {{ font-size: clamp(.95rem, 2.1vh, 1.6rem); }}
    .habit {{ font-size: clamp(1.1rem, 2.5vh, 1.9rem); padding: 1.2vh 1vw; }}
    .rv-grid, .wmsg, .wlabel {{ font-size: clamp(.95rem, 2.1vh, 1.6rem); }}
    .kpi b {{ font-size: clamp(2.4rem, 7vh, 5rem); }}
    .kpi small {{ font-size: clamp(.9rem, 2vh, 1.5rem); }}
    .rc-t {{ font-size: clamp(1.2rem, 2.9vh, 2.1rem); }}
    .rc-d {{ font-size: clamp(1rem, 2.3vh, 1.7rem); }}
    .promptbox, .pledge, .pin, .lsd-a {{ font-size: clamp(1rem, 2.4vh, 1.8rem); }}
    .slide.active-slide .senior-panel {{ animation: panelIn .8s both; }}
    .slide.active-slide .senior-panel:nth-child(2) {{ animation-delay: .15s; }}
    @keyframes panelIn {{ from {{ opacity: 0; transform: translateY(24px); }} to {{ opacity: 1; transform: none; }} }}
    .giant-art-frame {{ transition: transform .15s ease-out; transform-style: preserve-3d; }}
    .spark {{ position: fixed; z-index: 9999; pointer-events: none; font-size: 1.6rem; animation: sparkout 1s ease-out forwards; }}
    @keyframes sparkout {{ to {{ transform: translate(var(--dx), var(--dy)) scale(.4) rotate(200deg); opacity: 0; }} }}
    .slide-inner.tone-1 {{ background-image: linear-gradient(160deg, rgba(14,165,233,.18), transparent 60%) !important; }}
    .slide-inner.tone-2 {{ background-image: linear-gradient(160deg, rgba(22,163,74,.2), transparent 60%) !important; }}
    .slide-inner.tone-3 {{ background-image: linear-gradient(160deg, rgba(207,32,48,.2), transparent 60%) !important; }}
    .slide-inner.tone-4 {{ background-image: linear-gradient(160deg, rgba(168,85,247,.2), transparent 60%) !important; }}
    .hero {{ align-items: center; text-align: center; justify-content: center !important; gap: 2.2vh; position: relative; }}
    .bigq {{ font-size: clamp(2rem, 8vh, 6rem); font-weight: 800; line-height: 1.25; cursor: pointer; background: linear-gradient(90deg, #ffd66b, #fff, #34d399, #ffd66b); background-size: 300%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: shine 6s linear infinite; }}
    @keyframes shine {{ to {{ background-position: 300% 0; }} }}
    .bigsub {{ font-size: clamp(1.2rem, 3vh, 2.2rem); font-weight: 700; }}
    .bigsub2 {{ font-size: clamp(1rem, 2.4vh, 1.8rem); opacity: .9; }}
    .floaty {{ position: absolute; font-size: clamp(2.5rem, 9vh, 6rem); animation: flo 4s ease-in-out infinite; }}
    .f1 {{ left: 6%; top: 12%; }} .f2 {{ right: 8%; top: 18%; animation-delay: 1s; }} .f3 {{ left: 12%; bottom: 14%; animation-delay: 2s; }}
    @keyframes flo {{ 50% {{ transform: translateY(-18px) rotate(8deg); }} }}
    .steps {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.2vw; width: 100%; }}
    .stepc {{ cursor: pointer; padding: 2.2vh 1vw; border-radius: 20px; background: linear-gradient(160deg, rgba(245,196,81,.22), rgba(56,189,248,.14)); border: 2px solid rgba(245,196,81,.55); transition: transform .25s; }}
    .stepc:hover {{ transform: translateY(-8px); }}
    .se {{ font-size: clamp(3rem, 10vh, 6.5rem); }}
    .sn {{ font-weight: 900; font-size: clamp(1.2rem, 3vh, 2.2rem); }}
    .sd {{ max-height: 0; overflow: hidden; transition: max-height .5s; font-weight: 600; font-size: clamp(1rem, 2.4vh, 1.8rem); line-height: 1.45; }}
    .stepc.open .sd {{ max-height: 40vh; margin-top: 1vh; }}
    .sw {{ display: inline-flex; align-items: center; gap: 14px; cursor: pointer; font-weight: 900; font-size: clamp(1.1rem, 2.8vh, 2rem); }}
    .sw input {{ display: none; }}
    .knob {{ width: 76px; height: 40px; border-radius: 99px; background: #64748b; position: relative; transition: background .3s; }}
    .knob::after {{ content: ""; position: absolute; width: 32px; height: 32px; border-radius: 50%; background: #fff; top: 4px; left: 4px; transition: left .3s; }}
    .sw input:checked + .knob {{ background: #34d399; }}
    .sw input:checked + .knob::after {{ left: 40px; }}
    .ba {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.4vw; width: 100%; }}
    .bac {{ padding: 2vh 1.2vw; border-radius: 20px; text-align: left; border: 2px solid rgba(255,255,255,.2); transition: all .5s; opacity: .45; }}
    .bac h3 {{ font-size: clamp(1.2rem, 3vh, 2.2rem); margin-bottom: 1vh; }}
    .bac p {{ font-size: clamp(1rem, 2.4vh, 1.8rem); margin: .8vh 0; }}
    .ba .no {{ opacity: 1; background: rgba(207,32,48,.18); }}
    .ba.ai-on .no {{ opacity: .35; }}
    .ba.ai-on .yes {{ opacity: 1; background: rgba(52,211,153,.2); border-color: #34d399; transform: scale(1.03); box-shadow: 0 0 30px rgba(52,211,153,.4); }}
    .bigsave {{ font-weight: 900; font-size: clamp(1.5rem, 4.5vh, 3.2rem); color: #34d399; }}
    .qq {{ font-weight: 800; font-size: clamp(1.3rem, 3.6vh, 2.7rem); line-height: 1.35; }}
    .qopts {{ display: flex; flex-direction: column; gap: 1.2vh; width: min(900px, 100%); }}
    .qopt {{ padding: 1.6vh 1.2vw; border-radius: 16px; border: 2px solid #f5c451; background: rgba(255,255,255,.07); color: inherit; font: 700 clamp(1.05rem, 2.6vh, 1.9rem) 'Be Vietnam Pro', sans-serif; cursor: pointer; text-align: left; transition: transform .2s; }}
    .qopt:hover:not(:disabled) {{ transform: scale(1.02); }}
    .qopt.ok {{ background: #16a34a; border-color: #16a34a; color: #fff; }}
    .qopt.bad {{ background: #b91c1c; border-color: #b91c1c; color: #fff; }}
    .qf {{ min-height: 4vh; }}
    .wheelwrap {{ --w: min(46vh, 34vw); position: relative; display: flex; justify-content: center; margin: 1vh auto; }}
    .wheel {{ width: var(--w); height: var(--w); border-radius: 50%; border: 8px solid #ffe9ad; position: relative; transition: transform 4s cubic-bezier(.12, .7, .1, 1); box-shadow: 0 0 40px rgba(245,196,81,.5); }}
    .wheel span {{ position: absolute; left: 50%; top: 50%; font-size: clamp(2rem, 6vh, 4rem); }}
    .wptr {{ position: absolute; top: -3vh; left: 50%; transform: translateX(-50%); font-size: 4vh; color: #ffd66b; z-index: 3; }}

    .wheelbox {{ flex: 1; min-height: 0; height: 52vh; display: flex; justify-content: center; }}
    .sec {{ cursor: pointer; transition: filter .2s; }}
    .sec:hover {{ filter: brightness(1.25) drop-shadow(0 0 8px #fff); }}
    #wheelG {{ transform-origin: 200px 200px; transform-box: view-box; }}
    #wheelG.rolling {{ animation: wspin var(--spd, 8s) linear infinite; }}
    .rolling .vals {{ opacity: 0; }}
    @keyframes wspin {{ to {{ transform: rotate(360deg); }} }}
    #wheelBox.rolling {{ animation: bump .7s ease-in-out infinite; }}
    @keyframes bump {{ 0%, 100% {{ transform: translateY(0) rotate(0); }} 25% {{ transform: translateY(calc(var(--wob, 0) * -1px)) rotate(calc(var(--wob, 0) * .25deg)); }} 75% {{ transform: translateY(calc(var(--wob, 0) * .6px)) rotate(calc(var(--wob, 0) * -.25deg)); }} }}
    .wgauge {{ text-align: center; }}
    .gnum {{ font-size: clamp(3rem, 11vh, 7.5rem); font-weight: 900; line-height: 1; font-family: 'Be Vietnam Pro', sans-serif; }}
    .glab {{ font-weight: 800; font-size: clamp(.9rem, 2vh, 1.5rem); letter-spacing: 1px; margin-bottom: 1vh; }}
    #roundBar {{ height: 100%; width: 0; transition: width .5s, background .5s; }}
    .wverdict {{ text-align: center; font-weight: 800; font-size: clamp(1.15rem, 2.9vh, 2.1rem); line-height: 1.35; }}
    .wbtns {{ display: flex; flex-wrap: wrap; gap: 1vh 1vw; justify-content: center; }}
    .axtip {{ padding: 1.4vh 1.2vw; border-radius: 16px; border: 2px dashed #f5c451; font-weight: 700; font-size: clamp(1.05rem, 2.5vh, 1.9rem); line-height: 1.45; text-align: center; background: rgba(245,196,81,.1); }}

    .kpis {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    .kpi {{ text-align: center; padding: 18px 8px; border-radius: 18px; background: linear-gradient(160deg, rgba(207,32,48,.3), rgba(245,196,81,.22)); border: 1px solid rgba(245,196,81,.5); }}
    .kpi b {{ display: block; font: 900 2.3rem 'Playfair Display', serif; color: #ffd66b; }}
    .kpi small {{ font-weight: 700; }}
    .rcards {{ display: flex; flex-direction: column; gap: 10px; }}
    .rcard {{ cursor: pointer; border-radius: 16px; padding: 14px 16px; background: linear-gradient(135deg, rgba(245,196,81,.22), rgba(56,189,248,.16)); border: 1px solid rgba(245,196,81,.55); transition: transform .2s; }}
    .rcard:hover {{ transform: translateX(6px); }}
    .rc-t {{ font-weight: 900; font-size: 1.15rem; }}
    .rc-t small {{ display: block; font-weight: 600; opacity: .85; }}
    .rc-d {{ max-height: 0; overflow: hidden; transition: max-height .4s; font-weight: 600; line-height: 1.5; }}
    .rcard.open .rc-d {{ max-height: 160px; margin-top: 8px; }}

    .chips {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .chips button {{ border: 1px solid rgba(245,196,81,.6); background: rgba(255,255,255,.08); color: inherit; border-radius: 999px; padding: 6px 12px; font: 700 .85rem 'Be Vietnam Pro', sans-serif; cursor: pointer; transition: transform .15s; }}
    .chips button:hover {{ transform: scale(1.06); }}
    .chips button.on {{ background: #f5c451; color: #1a1205; }}
    .promptbox {{ margin: 10px 0 6px; padding: 12px 14px; border-radius: 14px; background: rgba(0,0,0,.35); border: 1px dashed #f5c451; font-weight: 700; line-height: 1.5; min-height: 64px; }}

    .habits {{ display: flex; flex-direction: column; gap: 8px; }}
    .habit {{ display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 14px; background: rgba(255,255,255,.08); font-weight: 700; font-size: 1.05rem; cursor: pointer; }}
    .habit input {{ width: 22px; height: 22px; accent-color: #34d399; }}
    .pbar {{ height: 14px; border-radius: 99px; background: rgba(255,255,255,.15); margin-top: 12px; overflow: hidden; }}
    #habitBar {{ height: 100%; width: 0; background: linear-gradient(90deg, #34d399, #f5c451); transition: width .5s; }}
    .pin {{ width: 100%; padding: 12px 14px; margin-bottom: 10px; border-radius: 12px; border: 1px solid #f5c451; background: rgba(0,0,0,.3); color: inherit; font: 700 1.05rem 'Be Vietnam Pro', sans-serif; }}
    .pledge {{ margin-top: 14px; padding: 18px; border-radius: 18px; background: linear-gradient(135deg, #cf2030, #f5c451); color: #1a0509; font-weight: 800; line-height: 1.5; font-size: 1.1rem; opacity: 0; transform: scale(.9); transition: all .5s; }}
    .pledge.show {{ opacity: 1; transform: scale(1); }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 100%; height: 100%;
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: var(--font-body);
      overflow: hidden;
      user-select: none;
      transition: background-color 0.4s ease, color 0.4s ease;
    }}
    html.mode-scroll, body.mode-scroll {{ height: auto !important; overflow-y: auto !important; overflow-x: hidden !important; }}
    h1, h2, h3, .slide-title, .senior-heading, .art-caption, .poem-box-large {{ text-wrap: balance; word-break: keep-all; overflow-wrap: break-word; }}
    p, .senior-text, li, .teleprompter-text {{ text-wrap: pretty; word-break: keep-all; overflow-wrap: break-word; }}
    #cosmosCanvas {{ position: fixed; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }}

    /* TẦNG 1: TOP HUD */
    .hud-topbar {{
      position: fixed; top: 0; left: 0; right: 0; height: var(--topbar-h);
      background: rgba(4, 7, 17, 0.96); backdrop-filter: blur(22px);
      border-bottom: 2px solid var(--border-glass);
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 12px; z-index: 1000; gap: 5px; flex-wrap: nowrap;
    }}
    .brand-pilot {{ display: flex; align-items: center; gap: 6px; }}
    .bni-badge {{
      background: linear-gradient(135deg, #cf2030, #991b1b);
      color: #ffffff; font-weight: 800; font-size: 0.72rem; padding: 6px 11px;
      border-radius: 999px; letter-spacing: 0.5px; text-transform: uppercase;
      box-shadow: 0 0 16px rgba(207, 32, 48, 0.6); border: 1px solid #f5c451; white-space: nowrap;
    }}
    .slide-select-dropdown, .style-select-dropdown {{
      background: rgba(14, 29, 62, 0.96); color: #ffe9ad;
      border: 1px solid rgba(245, 196, 81, 0.45); padding: 6px 8px; border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.73rem; font-weight: 700; cursor: pointer; outline: none;
    }}
    .slide-select-dropdown {{ max-width: 190px; }}
    .style-select-dropdown {{ border-color: rgba(56, 189, 248, 0.55); color: #38bdf8; max-width: 165px; }}
    .mode-switcher, .voice-Active-group {{
      display: flex; align-items: center; gap: 2px;
      background: rgba(12, 27, 58, 0.95); padding: 3px; border-radius: 999px;
      border: 1px solid rgba(56, 189, 248, 0.42);
    }}
    .voice-Active-group {{ border-color: rgba(245, 196, 81, 0.45); }}
    .mode-btn, .voice-opt-btn {{
      background: transparent; border: none; color: #cbd5e1; padding: 5px 8px;
      border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.72rem; font-weight: 700;
      cursor: pointer; transition: all 0.2s ease; white-space: nowrap;
    }}
    .mode-btn.active {{ background: linear-gradient(135deg, #38bdf8, #0284c7); color: #fff; }}
    .voice-opt-btn.active {{ background: linear-gradient(135deg, #f5c451, #c48a10); color: #030714; font-weight: 800; }}
    .speed-slider-pill {{
      display: flex; align-items: center; gap: 4px;
      background: rgba(12, 27, 58, 0.95); padding: 4px 9px; border-radius: 999px;
      border: 1px solid rgba(52, 211, 153, 0.45); color: #fff;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.72rem; font-weight: 700; white-space: nowrap;
    }}
    .speed-step-btn {{
      background: rgba(255, 255, 255, 0.12); border: none; color: #ffe9ad;
      width: 19px; height: 19px; border-radius: 50%; font-weight: 800; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
    }}
    .top-speed-range {{ width: 70px; accent-color: #34d399; cursor: pointer; height: 5px; }}
    .speed-val-badge {{ color: #34d399; font-weight: 800; min-width: 36px; text-align: center; }}
    .voice-master-bar {{ display: flex; align-items: center; gap: 5px; }}
    .btn-speak-master {{
      background: linear-gradient(135deg, #10b981, #059669); color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.4); padding: 7px 12px; border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.75rem; font-weight: 800; cursor: pointer;
      display: flex; align-items: center; gap: 4px; box-shadow: 0 0 16px rgba(16, 185, 129, 0.5); white-space: nowrap;
    }}
    .btn-speak-master.speaking {{ background: linear-gradient(135deg, #f59e0b, #dc2626); animation: pulseGlow 1.5s infinite; }}
    @keyframes pulseGlow {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.03); }} }}
    .btn-qr-instant {{
      background: linear-gradient(135deg, #cf2030, #f59e0b); color: #fff; border: 1.5px solid #ffe9ad;
      padding: 7px 13px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.75rem; font-weight: 800; cursor: pointer; white-space: nowrap;
      box-shadow: 0 0 18px rgba(207, 32, 48, 0.7); animation: pulseGlow 2s infinite;
    }}
    .btn-voice-studio {{
      background: rgba(245, 196, 81, 0.16); border: 1px solid rgba(245, 196, 81, 0.4);
      color: #ffe9ad; padding: 6px 9px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.72rem; font-weight: 700; cursor: pointer; white-space: nowrap;
    }}
    .btn-github-deploy {{
      background: linear-gradient(135deg, #3b82f6, #1d4ed8); border: 1px solid rgba(147, 197, 253, 0.5);
      color: #ffffff; padding: 6px 10px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.72rem; font-weight: 800; cursor: pointer; white-space: nowrap;
    }}
    .voice-toast {{
      position: fixed; top: 78px; right: 22px; background: rgba(6, 19, 45, 0.96);
      border: 2px solid #f5c451; color: #ffe9ad; padding: 9px 16px; border-radius: 14px;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.85rem; font-weight: 700; z-index: 2500;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8); opacity: 0; transform: translateY(-10px);
      pointer-events: none; transition: all 0.3s ease;
    }}
    .voice-toast.show {{ opacity: 1; transform: translateY(0); }}

    /* TẦNG 2: DECK VIEWPORT */
    .deck-viewport {{
      position: relative; width: 100vw; height: calc(100vh - var(--topbar-h) - var(--bottomdock-h));
      margin-top: var(--topbar-h); z-index: 10; overflow: hidden;
    }}
    body.mode-scroll .deck-viewport {{ height: auto !important; overflow: visible !important; margin-bottom: 80px; }}
    .slides-track {{ width: 100%; height: 100%; display: flex; transition: transform 0.82s cubic-bezier(0.16, 1, 0.3, 1); will-change: transform; }}
    body.mode-horizontal .slides-track {{ flex-direction: row; }}
    body.mode-vertical .slides-track {{ flex-direction: column; }}
    body.mode-scroll .slides-track {{ display: block !important; height: auto !important; transform: none !important; padding-bottom: 90px; }}
    .slide {{
      flex: 0 0 100%; width: 100vw; min-width: 100vw; height: calc(100vh - var(--topbar-h) - var(--bottomdock-h));
      min-height: calc(100vh - var(--topbar-h) - var(--bottomdock-h)); padding: 10px 2vw;
      display: flex; align-items: center; justify-content: center; position: relative;
      overflow-y: auto; overflow-x: hidden;
    }}
    body.mode-scroll .slide {{ height: auto !important; min-height: 86vh; padding: 24px 2vw; margin-bottom: 24px; }}
    .slide-inner {{
      width: 96vw; max-width: 1840px; background: var(--bg-card); backdrop-filter: blur(22px);
      border: 2px solid var(--border-glass); border-radius: var(--card-radius);
      padding: 18px 28px 22px 28px; box-shadow: var(--shadow-elevated); position: relative;
      overflow: hidden; transform: scale(0.965) translateY(10px); opacity: 0.55;
      transition: transform 0.78s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.65s ease, border-color 0.4s ease, box-shadow 0.4s ease;
    }}
    .slide.active-slide .slide-inner, body.mode-scroll .slide-inner {{ transform: scale(1) translateY(0); opacity: 1; }}
    .slide-inner.narrating-glow {{ border-color: var(--gold-primary); box-shadow: 0 0 48px rgba(245, 196, 81, 0.4), var(--shadow-elevated); }}
    .slide-inner::before {{
      content: ""; position: absolute; top: 0; left: 0; right: 0; height: 5px;
      background: linear-gradient(90deg, #cf2030, var(--gold-primary), var(--cyan-sky), var(--gold-primary), #cf2030);
    }}
    .slide-header {{
      display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;
      border-bottom: 1px solid rgba(148, 163, 184, 0.22); padding-bottom: 10px; gap: 16px;
    }}
    .slide-tag {{
      font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1.3px;
      color: var(--cyan-sky); display: block; margin-bottom: 2px;
    }}
    .btn-slide-voice {{
      background: rgba(52, 211, 153, 0.18); border: 2px solid rgba(52, 211, 153, 0.6);
      color: var(--emerald-peace); padding: 7px 16px; border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif; font-size: 0.84rem; font-weight: 800; cursor: pointer;
      display: flex; align-items: center; gap: 6px; white-space: nowrap;
    }}
    .senior-stage {{ display: grid; grid-template-columns: 1.22fr 0.88fr; gap: 24px; align-items: stretch; }}
    .senior-panel {{
      background: var(--bg-panel); border: 1px solid rgba(148, 163, 184, 0.22); border-radius: 20px;
      padding: 20px; display: flex; flex-direction: column; justify-content: space-between;
      position: relative; perspective: 1200px;
    }}
    .giant-art-frame {{
      position: relative; width: 100%; height: 380px; border-radius: 16px; overflow: hidden;
      border: 2px solid var(--border-glass); box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), 0 0 24px rgba(207, 32, 48, 0.2);
      background: #040d21; transform-style: preserve-3d; transition: transform 0.25s ease-out, box-shadow 0.3s ease;
    }}
    .giant-art-frame img.bg-photo {{
      width: 100%; height: 100%; object-fit: cover;
      animation: kenBurns4D 16s ease-in-out infinite alternate; filter: contrast(1.06) saturate(1.12);
    }}
    @keyframes kenBurns4D {{ 0% {{ transform: scale(1.02) translate(0, 0); }} 50% {{ transform: scale(1.08) translate(-1%, -0.8%); }} 100% {{ transform: scale(1.03) translate(1%, -1%); }} }}
    .art-image-overlay {{
      position: absolute; inset: 0; background: linear-gradient(180deg, rgba(3,8,22,0.02) 52%, rgba(3,8,22,0.92) 100%);
      display: flex; flex-direction: column; justify-content: flex-end; padding: 16px 20px; z-index: 4; pointer-events: none;
    }}
    .art-caption {{ font-family: 'Playfair Display', serif; font-size: 1.22rem; font-weight: 700; color: #ffe9ad; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
    .transform-row-large {{
      display: flex; align-items: center; justify-content: space-between; gap: 10px;
      background: rgba(148, 163, 184, 0.08); border: 2px solid rgba(148, 163, 184, 0.22);
      padding: 11px 15px; border-radius: 15px; margin-top: 6px; transition: all 0.3s ease;
    }}
    .state-old-lg {{ color: #fecdd3; font-weight: 600; font-size: clamp(0.84rem, 0.94vw, 0.96rem); flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .verb-bridge-lg {{
      background: linear-gradient(135deg, var(--gold-primary), var(--gold-dark)); color: #030714;
      font-weight: 800; font-size: 0.75rem; padding: 5px 12px; border-radius: 999px;
      text-transform: uppercase; white-space: nowrap; box-shadow: 0 0 14px rgba(245, 196, 81, 0.45); flex-shrink: 0;
    }}
    .state-new-lg {{ color: var(--emerald-peace); font-weight: 800; font-size: clamp(0.84rem, 0.95vw, 0.98rem); flex: 1; text-align: right; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .interactive-btn-lg {{
      background: linear-gradient(135deg, var(--gold-primary), var(--gold-dark)); color: #030714;
      border: none; padding: 10px 20px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-weight: 800; font-size: 0.92rem; cursor: pointer; transition: all 0.22s ease;
      box-shadow: 0 6px 18px rgba(245, 196, 81, 0.4); display: inline-flex; align-items: center;
      justify-content: center; gap: 8px; white-space: nowrap;
    }}
    .interactive-btn-lg:hover {{ transform: translateY(-2px) scale(1.02); box-shadow: 0 8px 25px rgba(245, 196, 81, 0.65); }}
    .btn-outline-lg {{
      background: rgba(56, 189, 248, 0.14); color: var(--cyan-sky); border: 2px solid rgba(56, 189, 248, 0.5);
      padding: 9px 16px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-weight: 700; font-size: 0.88rem; cursor: pointer; transition: all 0.2s; white-space: nowrap;
    }}
    .signature-watermark {{
      position: absolute; bottom: 6px; right: 22px; font-family: 'Dancing Script', cursive;
      font-size: 0.82rem; color: var(--gold-light); opacity: 0.65; letter-spacing: 0.4px; pointer-events: none;
    }}

    /* TẦNG 3: BOTTOM DOCK */
    .bottom-studio-dock {{
      position: fixed; bottom: 0; left: 0; right: 0; height: var(--bottomdock-h);
      background: rgba(4, 7, 17, 0.96); backdrop-filter: blur(20px); border-top: 2px solid var(--border-glass);
      display: flex; align-items: center; justify-content: space-between; padding: 0 18px; gap: 14px;
      z-index: 1000; box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.75);
    }}
    .dock-nav-cluster {{ display: flex; align-items: center; gap: 10px; flex-shrink: 0; }}
    .nav-action-btn {{
      background: rgba(245, 196, 81, 0.18); border: 1px solid rgba(245, 196, 81, 0.45);
      color: #ffe9ad; padding: 7px 14px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.8rem; font-weight: 800; cursor: pointer; white-space: nowrap;
    }}
    .nav-action-btn:hover {{ background: #f5c451; color: #030714; }}
    .dots-wrapper {{ display: flex; align-items: center; gap: 5px; }}
    .slide-dot {{ width: 8px; height: 8px; border-radius: 999px; background: rgba(255, 255, 255, 0.28); cursor: pointer; transition: all 0.25s; }}
    .slide-dot.active {{ width: 22px; background: #f5c451; box-shadow: 0 0 10px #f5c451; }}
    .dock-teleprompter-stage {{
      flex: 1; height: 46px; background: rgba(12, 27, 58, 0.92); border: 1.5px solid rgba(245, 196, 81, 0.4);
      border-radius: 999px; padding: 0 18px; display: flex; align-items: center; gap: 12px; overflow: hidden;
    }}
    .dock-teleprompter-stage.active-speaking {{ border-color: #34d399; box-shadow: 0 0 20px rgba(52, 211, 153, 0.3); }}
    .voice-wave-bars {{ display: flex; align-items: center; gap: 3px; height: 22px; flex-shrink: 0; opacity: 0.35; }}
    .dock-teleprompter-stage.active-speaking .voice-wave-bars {{ opacity: 1; }}
    .voice-wave-bars span {{ width: 4px; height: 8px; background: #34d399; border-radius: 99px; }}
    .dock-teleprompter-stage.active-speaking .voice-wave-bars span {{ animation: waveBounce 0.8s infinite ease-in-out; }}
    .voice-wave-bars span:nth-child(2) {{ animation-delay: 0.15s; height: 16px; }}
    .voice-wave-bars span:nth-child(3) {{ animation-delay: 0.3s; height: 22px; background: #f5c451; }}
    .voice-wave-bars span:nth-child(4) {{ animation-delay: 0.45s; height: 12px; }}
    @keyframes waveBounce {{ 0%, 100% {{ transform: scaleY(0.4); }} 50% {{ transform: scaleY(1.15); }} }}
    .teleprompter-text {{ flex: 1; font-family: 'Be Vietnam Pro', sans-serif; font-size: clamp(0.88rem, 1.02vw, 1.04rem); font-weight: 700; color: #ffe9ad; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .btn-stop-inline {{
      background: rgba(251, 113, 133, 0.2); border: 1px solid #fb7185; color: #fecdd3;
      padding: 4px 11px; border-radius: 999px; font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.74rem; font-weight: 800; cursor: pointer; display: none; flex-shrink: 0;
    }}
    .dock-teleprompter-stage.active-speaking .btn-stop-inline {{ display: inline-block; }}

    /* MODALS */
    .voice-modal-backdrop {{
      position: fixed; inset: 0; background: rgba(2, 6, 23, 0.92); backdrop-filter: blur(16px);
      z-index: 2000; display: none; align-items: center; justify-content: center; padding: 20px;
    }}
    .voice-modal-backdrop.open {{ display: flex; }}
    .voice-modal-card {{
      width: 100%; max-width: 820px; background: #081530; border: 2px solid #f5c451;
      border-radius: 26px; padding: 26px 30px; box-shadow: 0 25px 70px rgba(0,0,0,0.95);
      color: #fff; font-family: 'Be Vietnam Pro', sans-serif;
    }}
    .code-box-ps {{
      background: #030816; border: 1px solid rgba(56, 189, 248, 0.45); border-radius: 12px;
      padding: 14px; font-family: Consolas, monospace; font-size: 0.82rem; color: #38bdf8;
      overflow-x: auto; white-space: pre-wrap; line-height: 1.5; margin: 10px 0; user-select: text;
    }}
  </style>
</head>
<body class="mode-horizontal style-cinematic">

  <canvas id="cosmosCanvas"></canvas>
  <div class="voice-toast" id="voiceToast">🔊 Đã áp dụng cài đặt mới!</div>

  <!-- TẦNG 1: TOP HUD -->
  <header class="hud-topbar">
    <div class="brand-pilot">
      <span class="bni-badge">🏃‍♂️ BÁC SĨ CUNNINGHAM xAI</span>
      <select class="slide-select-dropdown" id="slideJumpSelect" onchange="goToSlide(parseInt(this.value, 10), true)" aria-label="Chọn nhanh trang thuyết trình">
        <option value="0">01. 🏃‍♂️ Bác Sĩ Glenn Cunningham</option>
        <option value="1">02. 🔥 Ngọn Lửa Năm 7 Tuổi</option>
        <option value="2">03. 🦵 Đau Quá Phải... Chạy!</option>
        <option value="3">04. 🏆 Kỷ Lục Thế Giới 1 Dặm</option>
        <option value="4">05. 🎓 Tiến Sĩ &amp; 9.000 Đứa Trẻ</option>
        <option value="5">06. 🇻🇳 Người Trung Niên Trước Sóng AI</option>
        <option value="6">07. 🚀 AI Là Đôi Chân Thần Tốc</option>
        <option value="7">08. 🛞 Bánh Xe Cuộc Đời Thời AI</option>
        <option value="8">09. 🤖 Lệnh Vàng AI 4 Bước</option>
        <option value="9">10. ⚖️ Một Ngày Của Người Trung Niên</option>
        <option value="10">11. 💪 6 Thói Quen Vượt Ngưỡng</option>
        <option value="11">12. 🎮 Thử Thách 3 Câu</option>
        <option value="12">13. 🎡 Vòng Quay Vượt Ngưỡng</option>
        <option value="13">14. 🌅 Ký Cam Kết Khởi Công</option>
        <option value="14">15. 🌟 Lời Kết: Chạy Về Ánh Sáng</option>
      </select>

      <select class="style-select-dropdown" id="artStyleSelect" onchange="setVisualArtStyle(this.value)" aria-label="Chọn phong cách nghệ thuật">
        <option value="cinematic">🎬 Điện Ảnh 4D</option>
        <option value="handdrawn">✍️ Vẽ Tay &amp; Viết Tay</option>
        <option value="infographic">📊 Đồ Hoạ Infographic</option>
        <option value="cartoon">🎠 Hoạt Hình 3D</option>
      </select>
    </div>

    <div class="mode-switcher" role="group" aria-label="Chế độ lật trang">
      <button class="mode-btn active" id="btnHorizontal" onclick="setDeckMode('horizontal')">↔ Ngang</button>
      <button class="mode-btn" id="btnVertical" onclick="setDeckMode('vertical')">↕ Dọc</button>
      <button class="mode-btn" id="btnScroll" onclick="setDeckMode('scroll')">☰ Toàn Trang</button>
    </div>

    <div class="voice-Active-group" role="group" aria-label="Chọn giọng đọc Nam hoặc Nữ">
      <button class="voice-opt-btn active" id="btnVoiceMale" onclick="setVoiceGender('male', true)">👨 Nam</button>
      <button class="voice-opt-btn" id="btnVoiceFemale" onclick="setVoiceGender('female', true)">👩 Nữ</button>
    </div>

    <div class="speed-slider-pill" title="Kéo thanh trượt để chỉnh tốc độ đọc phù hợp">
      <span>Tốc độ:</span>
      <button class="speed-step-btn" onclick="stepSpeechSpeed(-0.05)">-</button>
      <input type="range" class="top-speed-range" id="topSpeedSlider" min="0.5" max="1.8" step="0.05" value="1.0" oninput="onTopSpeedSliderInput(this.value)" onchange="onTopSpeedSliderCommit(this.value)" />
      <button class="speed-step-btn" onclick="stepSpeechSpeed(0.05)">+</button>
      <span class="speed-val-badge" id="topSpeedVal">1.00x</span>
    </div>

    <div class="speed-slider-pill audio-pill" title="Nhạc nền nhẹ &amp; hiệu ứng âm thanh">
      <button id="btnMusic" onclick="toggleMusic()">🎵 Nhạc</button>
      <input type="range" id="musicVol" min="0" max="100" value="35" oninput="setMusicVol(this.value)" aria-label="Âm lượng nhạc nền" />
      <button id="btnSfx" class="on" onclick="toggleSfx()">🔔 SFX</button>
    </div>

    <div class="voice-master-bar">
      <button class="btn-speak-master" id="btnMasterSpeak" onclick="toggleAutoLecture()">
        <span id="speakIcon">🎙️</span>
        <span id="speakLabel">BẤM NÚT NÓI</span>
      </button>
      <button class="btn-hide-slides" onclick="openHideModal()" title="Chọn trang muốn ẩn (phím tắt: H = ẩn/hiện trang đang xem)">
        👁 Ẩn Trang <span class="hide-count-badge zero" id="hideCountBadge">0</span>
      </button>
      <button class="btn-qr-instant" onclick="openQrFullscreenModal()" title="Bật Mã QR ACB Cỡ Đại Toàn Màn Hình">
        💬 NHÓM ZALO xAI
      </button>
      <button class="btn-voice-studio" onclick="openVoiceModal()" title="Phòng thu giọng thật">⚙️ Thu Âm</button>
      <button class="btn-github-deploy" onclick="openGitHubModal()" title="Đóng gói đưa lên GitHub Pages">🚀 GitHub</button>
      <button class="btn-voice-studio" onclick="toggleFullScreen()" title="Toàn màn hình">⛶</button>
    </div>
  </header>

  <!-- TẦNG 2: DECK VIEWPORT (15 SLIDES) -->
  <div class="deck-progress" id="deckProgress"></div>
  <main class="deck-viewport" id="deckViewport">
    <div class="slides-track" id="slidesTrack">

      <!-- SLIDE 1 -->
      <section class="slide active-slide">
        <div class="slide-inner tone-0">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🏃‍♂️ BÁC SĨ CUNNINGHAM xAI • LỚP ZOOM 20H00 THỨ TƯ &amp; THỨ BẢY • TRANG 1 / 15</span>
              <h1 class="slide-title">🏃‍♂️ HUYỀN THOẠI GLENN CUNNINGHAM &amp; BÀI HỌC VƯỢT NGƯỠNG</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(0)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="giant-art-frame">
                <img class="bg-photo" data-keep="1" style="object-position:50% 22%" src="{avatar_base64}" alt="Nhà đào tạo Nguyễn Anh Tuấn"/>
                <div class="art-image-overlay">
                  <div class="art-caption">👨‍🏫 Nhà đào tạo Nguyễn Anh Tuấn – Tuấn Tử Tế Từ Tâm</div>
                </div>
              </div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">✨ Câu chuyện người chạy nhanh nhất thế giới:</h3>
                <p class="senior-text">
                  🔹 <strong>Bác sĩ Glenn Cunningham:</strong> 7 tuổi bị bỏng nặng đôi chân, bác sĩ bảo tàn phế suốt đời.<br/>
                  🔹 Bằng ý chí sắt đá, ông lập <strong>Kỷ lục thế giới chạy 1 dặm</strong> và trở thành Tiến sĩ giáo dục.<br/>
                  🔹 <strong>Bài học cho người trung niên Việt Nam:</strong> Tuổi tác và công nghệ AI không phải là rào cản.<br/>
                  🔹 Rào cản lớn nhất nằm ở <strong>tâm trí</strong>. Hãy gắn “đôi chân thần tốc AI” vào kinh nghiệm sống của bạn!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🤕 Đôi chân bỏng tàn phế</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">🏆 Người chạy nhanh nhất thế giới</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 2 -->
      <section class="slide">
        <div class="slide-inner tone-1">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🔥 BI KỊCH NĂM 7 TUỔI • TRANG 2 / 15</span>
              <h1 class="slide-title">🔥 BÁC SĨ BẢO: “CẬU BÉ SẼ KHÔNG BAO GIỜ ĐI LẠI ĐƯỢC”</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(1)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage one">
            <div class="senior-panel hero">
              <div class="floaty f1">🔥</div>
              <div class="floaty f2">⚡</div>
              <div class="floaty f3">🌱</div>
              <div class="bigq">“Con không chỉ đi lại được, mà con sẽ CHẠY!”</div>
              <div class="bigsub">— Lời thề của cậu bé Glenn Cunningham với người mẹ trên giường bệnh năm 1916 —</div>
              <div class="bigsub2">👆 Nghịch cảnh không định nghĩa bạn — Phản ứng của bạn trước nghịch cảnh mới kiến tạo vận mệnh!</div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 3 -->
      <section class="slide">
        <div class="slide-inner tone-2">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🦵 BƯỚC ĐI ĐẦU TIÊN • TRANG 3 / 15</span>
              <h1 class="slide-title">🦵 ĐAU ĐẾN MỨC PHẢI... CHẠY!</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(2)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="kpis">
                <div class="kpi"><b class="count-up" data-to="2" data-suf=" Năm">0</b><small>liệt giường kiên trì xoa bóp</small></div>
                <div class="kpi"><b class="count-up" data-to="22" data-suf=" Tháng">0</b><small>bám cọc rào tập đứng dậy</small></div>
                <div class="kpi"><b class="count-up" data-to="100" data-suf="%">0</b><small>quyết tâm không chịu tàn phế</small></div>
                <div class="kpi"><b class="count-up" data-to="0" data-suf=" Lần">0</b><small>than thở hay đổ lỗi số phận</small></div>
              </div>
              <div class="wmsg">Ý chí sắt đá của "Người sắt Kansas" (Kansas Ironman)</div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">💡 Phát hiện kỳ diệu của Glenn:</h3>
                <p class="senior-text">
                  🔹 Khi tập đi, mỗi bước chân chạm đất đau buốt như xé thịt.<br/>
                  🔹 Cậu bé phát hiện: <strong>Chạy thì ít đau hơn đi bộ!</strong> Vì thời gian bàn chân chạm đất ngắn hơn.<br/>
                  🔹 Thế là cậu bắt đầu chạy: chạy theo máy cày, chạy trên đồng lúa mì, chạy tới trường.<br/>
                  🔹 👉 <strong>Bài học cho người trung niên:</strong> Khi đối mặt với nỗi sợ công nghệ hay tuổi tác, cách thoát ra nhanh nhất là <strong>HÀNH ĐỘNG NGAY</strong>!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">😰 Sợ đau, sợ thất bại</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">🏃 Bứt phá bằng hành động mỗi ngày</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 4 -->
      <section class="slide">
        <div class="slide-inner tone-3">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🏆 ĐỈNH CAO THẾ GIỚI • TRANG 4 / 15</span>
              <h1 class="slide-title">🏆 KỶ LỤC THẾ GIỚI 1 DẶM: 4 PHÚT 06 GIÂY 8</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(3)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="rcards">
                <div class="rcard open" onclick="flipCard(this)">
                  <div class="rc-t">🏛️ MADISON SQUARE GARDEN 1934<small>Kỷ lục thế giới cự ly 1 dặm (1.609m)</small></div>
                  <div class="rc-d">Glenn Cunningham phá kỷ lục thế giới với thành tích 4 phút 06 giây 8, khiến hàng triệu khán giả Mỹ rơi nước mắt.</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">🥈 OLYMPIC BERLIN 1936<small>Huy chương Bạc cự ly 1.500m</small></div>
                  <div class="rc-d">Được cả thế giới nghiêng mình kính phục, vinh danh là một trong những vận động viên vĩ đại nhất lịch sử thể thao nhân loại.</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">💪 BÀI HỌC CHO BẠN HÔM NAY<small>Giới hạn chỉ là một ảo ảnh</small></div>
                  <div class="rc-d">Đôi chân từng bị cháy đen đến tận xương còn chạy nhanh nhất hành tinh, thì không có lý do gì tuổi 40, 50 lại đầu hàng trước AI!</div>
                </div>
              </div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🎯 Thông điệp gửi tặng học viên trung niên:</h3>
                <p class="senior-text">
                  🔹 Đừng bao giờ nói: <em>"Tôi già rồi, tôi học không kịp người trẻ đâu!"</em>.<br/>
                  🔹 Glenn Cunningham không có xuất phát điểm hoàn hảo – ông có <strong>ý chí thép và kỷ luật thép</strong>.<br/>
                  🔹 Tuổi trung niên có mỏ vàng: <strong>Sự chín chắn, trải nghiệm thực tế và lòng kiên nhẫn</strong>!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🐢 Tự ti về tuổi tác</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">⚡ Làm chủ tốc độ kỷ nguyên mới</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 5 -->
      <section class="slide">
        <div class="slide-inner tone-4">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🎓 DI SẢN PHỤNG SỰ • TRANG 5 / 15</span>
              <h1 class="slide-title">🎓 TIẾN SĨ GIÁO DỤC &amp; HƠN 9.000 ĐỨA TRẺ</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(4)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="kpis">
                <div class="kpi"><b class="count-up" data-to="9000" data-suf="+">0</b><small>trẻ em cơ nhỡ được nuôi dưỡng</small></div>
                <div class="kpi"><b class="count-up" data-to="1" data-suf=" Bằng">0</b><small>Tiến sĩ (Ph.D) Giáo dục danh giá</small></div>
                <div class="kpi"><b class="count-up" data-to="40" data-suf=" Năm">0</b><small>cống hiến phụng sự cộng đồng</small></div>
                <div class="kpi"><b class="count-up" data-to="100" data-suf="%">0</b><small>tình yêu thương và sự tử tế</small></div>
              </div>
              <div class="wmsg">Trang trại Glenn Cunningham Youth Ranch – Nơi ươm mầm hy vọng</div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🌱 Sự rộng lượng là thước đo trình độ sống:</h3>
                <p class="senior-text">
                  🔹 Sau khi giải nghệ, ông không dừng lại ở vinh quang điền kinh.<br/>
                  🔹 Ông học lấy bằng <strong>Tiến sĩ Giáo dục</strong> và mở trang trại cưu mang hơn 9.000 đứa trẻ khó khăn.<br/>
                  🔹 Ông dạy chúng: <em>"Không ai có thể đánh bại con nếu con chưa chấp nhận đầu hàng!"</em>.<br/>
                  🔹 👉 <strong>Mục tiêu lớp KTCSxAI:</strong> Giúp anh chị khỏe mạnh, thành công để <strong>lan tỏa giá trị cho gia đình và xã hội</strong>.
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🥇 Thành công cá nhân</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">🌟 Di sản tử tế phụng sự đời</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 6 -->
      <section class="slide">
        <div class="slide-inner tone-0">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🇻🇳 THỰC TRẠNG VIỆT NAM • TRANG 6 / 15</span>
              <h1 class="slide-title">🇻🇳 NGƯỜI TRUNG NIÊN VIỆT NAM TRƯỚC LÀN SÓNG AI</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(5)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="rcards">
                <div class="rcard open" onclick="flipCard(this)">
                  <div class="rc-t">😰 NỖI SỢ 1: “TÔI KHÔNG RÀNH CÔNG NGHỆ”<small>Sợ bấm nhầm, sợ phức tạp</small></div>
                  <div class="rc-d">Thực tế: AI ngày nay dùng bằng tiếng Việt, nói chuyện như nhắn tin Zalo, không cần biết code một dòng nào!</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">👴 NỖI SỢ 2: “TÔI LỚN TUỔI RỒI, SAO ĐUA ĐƯỢC?”<small>Tự ti trước giới trẻ</small></div>
                  <div class="rc-d">Người trẻ nhanh về thao tác, nhưng người trung niên vượt trội về kinh nghiệm ngành, mối quan hệ và khả năng ra quyết định.</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">📉 NỖI SỢ 3: “LIỆU AI CÓ ĐÀO THẢI TÔI?”<small>Bị thay thế trong công việc</small></div>
                  <div class="rc-d">AI không thay thế bạn. Người biết dùng AI sẽ thay thế người không chịu cập nhật!</div>
                </div>
              </div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">💡 Chân lý thời đại mới:</h3>
                <p class="senior-text">
                  🔹 Giống như Glenn Cunningham tập đi từng bước một cách kiên trì.<br/>
                  🔹 Học viên trung niên học AI: <strong>Mỗi buổi học 1 lệnh nhỏ, ứng dụng 1 việc cụ thể</strong>.<br/>
                  🔹 Sau 30 ngày: Bạn sở hữu một <strong>trợ lý ảo làm việc 24/7</strong> không biết mệt mỏi!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🤷 Đứng ngoài nhìn thời đại</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">🤝 Dẫn đầu bằng kinh nghiệm &amp; AI</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 7 -->
      <section class="slide">
        <div class="slide-inner tone-1">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🚀 BẢN CHẤT CÔNG NGHỆ • TRANG 7 / 15</span>
              <h1 class="slide-title">🚀 AI LÀ “ĐÔI CHÂN THẦN TỐC MỚI” CỦA BẠN</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(6)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="rcards">
                <div class="rcard open" onclick="flipCard(this)">
                  <div class="rc-t">🏛️ BẠN LÀ KIẾN TRÚC SƯ<small>Bạn vẽ bản thiết kế</small></div>
                  <div class="rc-d">Bạn đưa ra mục tiêu, tầm nhìn, tiêu chuẩn chất lượng và giá trị nhân văn. Không một cỗ máy nào thay thế được linh hồn của bạn.</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">🏗️ BẠN LÀ CHỦ CÔNG TRÌNH<small>Bạn duyệt và quyết định</small></div>
                  <div class="rc-d">AI đề xuất 5 phương án, bạn chọn phương án tốt nhất. Bạn kiểm tra tính chính xác và chịu trách nhiệm với uy tín của mình.</div>
                </div>
                <div class="rcard" onclick="flipCard(this)">
                  <div class="rc-t">🤖 AI LÀ ĐÔI CHÂN THẦN TỐC<small>Thi công siêu tốc 10x</small></div>
                  <div class="rc-d">Soạn văn bản trong 10 giây, phân tích báo cáo 50 trang trong 1 phút, làm việc 24/7 không đòi lương hay nghỉ phép.</div>
                </div>
              </div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🔑 Công thức thành công cho người trung niên:</h3>
                <p class="senior-text">
                  🔹 <strong>Trí khôn cuộc đời (Human Wisdom) + Tốc độ AI (AI Speed) = Sức mạnh vô song!</strong><br/>
                  🔹 Glenn Cunningham dùng đôi chân ý chí để chạy nhanh nhất thế giới.<br/>
                  🔹 Bạn dùng <strong>Trí tuệ nhân tạo</strong> để chạy nhanh nhất trong sự nghiệp và cuộc đời!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🐌 Làm thủ công quá tải</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">⚡ Bứt phá tốc độ cùng trợ lý AI</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 8 -->
      <section class="slide">
        <div class="slide-inner tone-2">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🛞 BÁNH XE CUỘC ĐỜI • TRANG 8 / 15</span>
              <h1 class="slide-title">🛞 BÁNH XE CUỘC ĐỜI: TRÒN ĐỀU ĐỂ LĂN XA</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(7)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="wheelbox" id="wheelBox">
                <svg id="wheelSvg" viewBox="-10 -10 420 420" style="height:100%;max-width:100%">
                  <defs>
                    <radialGradient id="hubg"><stop offset="0" stop-color="#fffbe0"/><stop offset="1" stop-color="#f5c451"/></radialGradient>
                  </defs>
                  <circle cx="200" cy="200" r="152" fill="rgba(255,255,255,.06)" stroke="#94a3b8" stroke-opacity=".55" stroke-width="12"/>
                  <g id="wheelG">
                    <circle cx="200" cy="200" r="42" fill="none" stroke="#fff" stroke-opacity=".28" stroke-dasharray="4 5"/>
                    <circle cx="200" cy="200" r="84" fill="none" stroke="#fff" stroke-opacity=".28" stroke-dasharray="4 5"/>
                    <circle cx="200" cy="200" r="126" fill="none" stroke="#fff" stroke-opacity=".28" stroke-dasharray="4 5"/>
                    <path class="sec" id="sec0" fill="#f97316" stroke="#fff" stroke-width="3" onclick="selectAxis(0)"/>
                    <path class="sec" id="sec1" fill="#ef4444" stroke="#fff" stroke-width="3" onclick="selectAxis(1)"/>
                    <path class="sec" id="sec2" fill="#ec4899" stroke="#fff" stroke-width="3" onclick="selectAxis(2)"/>
                    <path class="sec" id="sec3" fill="#8b5cf6" stroke="#fff" stroke-width="3" onclick="selectAxis(3)"/>
                    <path class="sec" id="sec4" fill="#0ea5e9" stroke="#fff" stroke-width="3" onclick="selectAxis(4)"/>
                    <path class="sec" id="sec5" fill="#14b8a6" stroke="#fff" stroke-width="3" onclick="selectAxis(5)"/>
                    <line x1="200" y1="200" x2="124.0" y2="68.4" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <line x1="200" y1="200" x2="276.0" y2="68.4" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <line x1="200" y1="200" x2="352.0" y2="200.0" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <line x1="200" y1="200" x2="276.0" y2="331.6" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <line x1="200" y1="200" x2="124.0" y2="331.6" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <line x1="200" y1="200" x2="48.0" y2="200.0" stroke="#fff" stroke-opacity=".7" stroke-width="2"/>
                    <text class="vals" id="val0" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                    <text class="vals" id="val1" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                    <text class="vals" id="val2" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                    <text class="vals" id="val3" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                    <text class="vals" id="val4" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                    <text class="vals" id="val5" text-anchor="middle" font-size="24" font-weight="900" fill="#fff" stroke="#000" stroke-width="3" paint-order="stroke">5</text>
                  </g>
                  <circle cx="200" cy="200" r="30" fill="url(#hubg)" stroke="#fff" stroke-width="4"/>
                  <text id="hubT" x="200" y="209" text-anchor="middle" font-size="26" font-weight="900" fill="#3b2a00">5</text>
                  <g style="cursor:pointer" onclick="selectAxis(0)"><text x="200.0" y="22.0" text-anchor="middle" font-size="36">💪</text><text x="200.0" y="42.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Thể lực</text></g>
                  <g style="cursor:pointer" onclick="selectAxis(1)"><text x="359.3" y="114.0" text-anchor="middle" font-size="36">🏃</text><text x="359.3" y="134.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Vận động</text></g>
                  <g style="cursor:pointer" onclick="selectAxis(2)"><text x="359.3" y="298.0" text-anchor="middle" font-size="36">❤️</text><text x="359.3" y="318.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Bình an</text></g>
                  <g style="cursor:pointer" onclick="selectAxis(3)"><text x="200.0" y="390.0" text-anchor="middle" font-size="36">🤝</text><text x="200.0" y="410.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Kết nối</text></g>
                  <g style="cursor:pointer" onclick="selectAxis(4)"><text x="40.7" y="298.0" text-anchor="middle" font-size="36">📚</text><text x="40.7" y="318.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Học tập</text></g>
                  <g style="cursor:pointer" onclick="selectAxis(5)"><text x="40.7" y="114.0" text-anchor="middle" font-size="36">🤖</text><text x="40.7" y="134.0" text-anchor="middle" font-size="15" font-weight="800" fill="#ffe9ad">Ứng dụng AI</text></g>
                </svg>
              </div>
              <div class="rv-grid">
                <label style="border-left:6px solid #f97316;padding-left:8px">💪 Thể lực <b>1</b><input type="range" min="1" max="10" value="5" id="rv0" oninput="drawRadar()"><b>10</b></label>
                <label style="border-left:6px solid #ef4444;padding-left:8px">🏃 Vận động <b>1</b><input type="range" min="1" max="10" value="5" id="rv1" oninput="drawRadar()"><b>10</b></label>
                <label style="border-left:6px solid #ec4899;padding-left:8px">❤️ Bình an <b>1</b><input type="range" min="1" max="10" value="5" id="rv2" oninput="drawRadar()"><b>10</b></label>
                <label style="border-left:6px solid #8b5cf6;padding-left:8px">🤝 Kết nối <b>1</b><input type="range" min="1" max="10" value="5" id="rv3" oninput="drawRadar()"><b>10</b></label>
                <label style="border-left:6px solid #0ea5e9;padding-left:8px">📚 Học tập <b>1</b><input type="range" min="1" max="10" value="5" id="rv4" oninput="drawRadar()"><b>10</b></label>
                <label style="border-left:6px solid #14b8a6;padding-left:8px">🤖 Ứng dụng AI <b>1</b><input type="range" min="1" max="10" value="5" id="rv5" oninput="drawRadar()"><b>10</b></label>
              </div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🛞 Giữ đúng trục Thân – Tâm – Trí:</h3>
                <p class="senior-text">
                  🔹 <strong>Trục bánh xe</strong> là bản sắc của bạn; 6 múi cùng to tròn xe mới lăn êm.<br/>
                  🔹 Nếu Thể lực yếu hoặc sợ AI, bánh xe sẽ khập khiễng, tiêu hao sinh lực.<br/>
                  🔹 Bấm nút <strong>Cân bằng múi thấp nhất</strong> để rèn luyện mỗi ngày!
                </p>
              </div>
              <div class="wgauge">
                <div class="gnum" id="roundNum">0%</div>
                <div class="glab">ĐỘ TRÒN ĐỀU CỦA BÁNH XE</div>
                <div class="pbar"><div id="roundBar"></div></div>
              </div>
              <div id="radarMsg" class="wverdict"></div>
              <div class="wbtns">
                <button class="interactive-btn-lg" id="btnRoll" onclick="rollWheel()">🛞 Cho bánh xe lăn</button>
                <button class="interactive-btn-lg" onclick="balanceWheel()">⚖️ Nâng mục thấp nhất +1</button>
                <button class="interactive-btn-lg" onclick="randomWheel()">🎲 Ngẫu nhiên</button>
                <button class="chips-reset" onclick="resetWheel()">↺ Đặt lại</button>
              </div>
              <div id="axTip" class="axtip">👆 Bấm vào một múi bánh xe để xem lời khuyên</div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 9 -->
      <section class="slide">
        <div class="slide-inner tone-3">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🤖 THỰC HÀNH LỆNH VÀNG • TRANG 9 / 15</span>
              <h1 class="slide-title">🤖 XÂY “LỆNH VÀNG” AI CHO NGƯỜI TRUNG NIÊN TRONG 4 CÚ BẤM</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(8)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="wlabel">1️⃣ Vai trò của AI</div>
              <div class="chips">
                <button onclick="pickChip(this,'r')">thư ký mẫn cán 24/7</button>
                <button onclick="pickChip(this,'r')">huấn luyện viên sức khỏe Glenn Cunningham</button>
                <button onclick="pickChip(this,'r')">cố vấn chiến lược kinh doanh</button>
                <button onclick="pickChip(this,'r')">chuyên gia viết bài truyền cảm hứng</button>
              </div>
              <div class="wlabel">2️⃣ Việc cần làm</div>
              <div class="chips">
                <button onclick="pickChip(this,'t')">soạn tin nhắn ngoại giao lịch sự</button>
                <button onclick="pickChip(this,'t')">lập lịch tập luyện thể thao tuổi 50</button>
                <button onclick="pickChip(this,'t')">tóm tắt tài liệu 20 trang thành 5 ý chính</button>
                <button onclick="pickChip(this,'t')">viết kịch bản bài giảng truyền lửa</button>
              </div>
              <div class="wlabel">3️⃣ Bối cảnh của bạn</div>
              <div class="chips">
                <button onclick="pickChip(this,'c')">tôi 48 tuổi, kinh doanh bận rộn</button>
                <button onclick="pickChip(this,'c')">tôi muốn rèn luyện thể chất dẻo dai</button>
                <button onclick="pickChip(this,'c')">tôi mới học dùng AI được 1 tuần</button>
                <button onclick="pickChip(this,'c')">tôi muốn dành thời gian cho gia đình</button>
              </div>
              <div class="wlabel">4️⃣ Định dạng câu trả lời</div>
              <div class="chips">
                <button onclick="pickChip(this,'f')">3 gạch đầu dòng ngắn gọn</button>
                <button onclick="pickChip(this,'f')">bảng kế hoạch từng ngày</button>
                <button onclick="pickChip(this,'f')">lời văn ấm áp, chân thành</button>
                <button onclick="pickChip(this,'f')">hướng dẫn từng bước dễ làm</button>
              </div>
              <div id="promptOut" class="promptbox"></div>
              <button class="interactive-btn-lg" onclick="copyPrompt()">📋 Sao chép lệnh vàng</button>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🛠️ Công thức: VAI TRÒ + VIỆC + BỐI CẢNH + ĐỊNH DẠNG</h3>
                <p class="senior-text">
                  🔹 <strong>Không cần gõ dài dòng:</strong> Chỉ cần chọn 4 ô, bạn có ngay một câu lệnh chuẩn quốc tế.<br/>
                  🔹 Bấm <strong>Sao chép</strong>, dán vào ChatGPT, Claude hoặc Gemini trên điện thoại.<br/>
                  🔹 AI hiểu đúng bối cảnh sẽ trả lời chính xác, thông minh vượt bậc.<br/>
                  🔹 Bạn là người duyệt cuối cùng trước khi gửi đi!
                </p>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 10 -->
      <section class="slide">
        <div class="slide-inner tone-4">
          <div class="slide-header">
            <div>
              <span class="slide-tag">⚖️ TRƯỚC &amp; SAU • TRANG 10 / 15</span>
              <h1 class="slide-title">⚖️ MỘT NGÀY CÓ TRỢ LÝ AI ĐỒNG HÀNH</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(9)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage one">
            <div class="senior-panel hero">
              <label class="sw">
                <input type="checkbox" id="aiSw" onchange="toggleAI()">
                <span class="knob"></span>
                <span class="swt">🔌 Bật trợ lý AI thần tốc</span>
              </label>
              <div id="baBox" class="ba">
                <div class="bac no">
                  <h3>😩 KHÔNG CÓ AI (Làm thủ công)</h3>
                  <p>✉️ Soạn thư từ, email, hợp đồng: <b>45 phút</b></p>
                  <p>📑 Đọc, tóm tắt tài liệu dự án: <b>60 phút</b></p>
                  <p>🗓️ Lên kế hoạch tuần, phân công: <b>40 phút</b></p>
                  <p>💡 Tìm ý tưởng bài phát biểu, viết bài: <b>45 phút</b></p>
                </div>
                <div class="bac yes">
                  <h3>😊 CÓ AI HỖ TRỢ (Thảnh thơi)</h3>
                  <p>✉️ AI tạo bản nháp chuẩn, bạn duyệt: <b>10 phút</b></p>
                  <p>📑 AI lọc 5 ý trọng tâm trong 1 phút: <b>15 phút</b></p>
                  <p>🗓️ AI lên khung lịch trình thông minh: <b>10 phút</b></p>
                  <p>💡 AI gợi ý 10 góc nhìn độc đáo: <b>10 phút</b></p>
                </div>
              </div>
              <div class="bigsave">⏱️ Tiết kiệm ≈ <span id="baSave">0</span> phút mỗi ngày</div>
              <div class="wmsg">Dành 2 giờ thảnh thơi mỗi ngày để bơi biển, chạy bộ, đọc sách và quây quần bên gia đình!</div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 11 -->
      <section class="slide">
        <div class="slide-inner tone-0">
          <div class="slide-header">
            <div>
              <span class="slide-tag">💪 RÈN LUYỆN THÂN – TÂM – TRÍ • TRANG 11 / 15</span>
              <h1 class="slide-title">💪 6 THÓI QUEN VƯỢT NGƯỠNG CỦA MỘT “KANSAS IRONMAN”</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(10)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="habits">
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 🏃 Vận động 30 phút (Chạy bộ / Bơi biển / Đi bộ nhanh)</label>
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 😴 Ngủ sâu 7 tiếng để phục hồi tế bào não</label>
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 🤝 Nhắn tin / gọi điện động viên một người bạn</label>
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 📚 Học 1 kỹ năng mới hoặc đọc 10 trang sách hay</label>
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 🤖 Thực hành hỏi AI 1 câu lệnh giải quyết việc thực tế</label>
                <label class="habit"><input type="checkbox" onchange="checkProgress()"> 🧘 5 phút thở sâu và viết 3 điều biết ơn cuộc đời</label>
              </div>
              <div class="pbar"><div id="habitBar"></div></div>
              <div id="habitTxt" class="wmsg">0/6 thói quen hôm nay</div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🔬 Nền tảng thể chất quyết định trí tuệ:</h3>
                <p class="senior-text">
                  🔹 <strong>Bác sĩ Cunningham</strong> hồi sinh đôi chân nhờ từng phút tự xoa bóp và kiên trì vận động.<br/>
                  🔹 Người trung niên giữ được <strong>Thân cường</strong> thì <strong>Trí mới sáng</strong> để hấp thu công nghệ mới.<br/>
                  🔹 Tích đủ 6 thói quen mỗi ngày: Bạn đang xây dựng một pháo đài sức khỏe và thành công bất khả chiến bại!
                </p>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 12 -->
      <section class="slide">
        <div class="slide-inner tone-1">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🎮 TRÒ CHƠI ÔN BÀI • TRANG 12 / 15</span>
              <h1 class="slide-title">🎮 THỬ THÁCH 3 CÂU: BẠN ĐÃ THẤU TINH THẦN CUNNINGHAM?</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(11)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage one">
            <div class="senior-panel hero">
              <div id="qzQ" class="qq"></div>
              <div id="qzO" class="qopts"></div>
              <div id="qzF" class="wmsg qf"></div>
              <button class="interactive-btn-lg" id="qzN" onclick="nextQ()">Câu tiếp ➡️</button>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 13 -->
      <section class="slide">
        <div class="slide-inner tone-2">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🎡 HÀNH ĐỘNG HÔM NAY • TRANG 13 / 15</span>
              <h1 class="slide-title">🎡 VÒNG QUAY HÀNH ĐỘNG VƯỢT NGƯỠNG</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(12)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <div class="wheelwrap">
                <div class="wptr">▼</div>
                <div id="wheel" class="wheel" style="background:conic-gradient(#cf2030 0deg 60deg,#f5c451 60deg 120deg,#0ea5e9 120deg 180deg,#16a34a 180deg 240deg,#a855f7 240deg 300deg,#f97316 300deg 360deg)">
                  <span style="transform:translate(-50%,-50%) rotate(30deg) translateY(calc(var(--w) * -0.33)) rotate(-30deg)">🏃</span>
                  <span style="transform:translate(-50%,-50%) rotate(90deg) translateY(calc(var(--w) * -0.33)) rotate(-90deg)">🤖</span>
                  <span style="transform:translate(-50%,-50%) rotate(150deg) translateY(calc(var(--w) * -0.33)) rotate(-150deg)">🤝</span>
                  <span style="transform:translate(-50%,-50%) rotate(210deg) translateY(calc(var(--w) * -0.33)) rotate(-210deg)">📚</span>
                  <span style="transform:translate(-50%,-50%) rotate(270deg) translateY(calc(var(--w) * -0.33)) rotate(-270deg)">🧘</span>
                  <span style="transform:translate(-50%,-50%) rotate(330deg) translateY(calc(var(--w) * -0.33)) rotate(-330deg)">🙏</span>
                </div>
              </div>
              <button class="interactive-btn-lg" onclick="spinWheel()">🎡 QUAY VÒNG THỬ THÁCH HÔM NAY</button>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🎯 Mỗi ngày một bước chạy nhỏ:</h3>
                <p class="senior-text">
                  🔹 Bấm quay để nhận <strong>1 thử thách vượt ngưỡng</strong> cho ngày hôm nay.<br/>
                  🔹 Hoàn thành trong 15 phút, sau đó gõ kết quả vào khung <strong>Chat Zoom</strong>.<br/>
                  🔹 Thử thách chạm đủ cả 3 khía cạnh: <strong>Thân – Tâm – Trí</strong>.
                </p>
              </div>
              <div id="whRes" class="pledge show">🎡 Bấm nút để nhận thử thách đầu tiên!</div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 14 -->
      <section class="slide">
        <div class="slide-inner tone-3">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🌅 KÝ CAM KẾT • TRANG 14 / 15</span>
              <h1 class="slide-title">🌅 CHÍNH THỨC KHỞI CÔNG BỨT PHÁ BẢN THÂN</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(13)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage">
            <div class="senior-panel">
              <input id="pledgeName" class="pin" placeholder="Gõ họ và tên của bạn..."/>
              <select id="pledgeFocus" class="pin">
                <option>Thân 💪 (Thể lực &amp; Vận động)</option>
                <option>Tâm ❤️ (Bình an &amp; Yêu thương)</option>
                <option>Trí 🧠 (Học tập &amp; Ứng dụng AI)</option>
              </select>
              <button class="interactive-btn-lg" onclick="makePledge()">✍️ Ký Cam Kết Vượt Ngưỡng</button>
              <div id="pledgeOut" class="pledge"></div>
            </div>
            <div class="senior-panel">
              <div>
                <h3 class="senior-heading">🏛️ Hành trình vạn dặm bắt đầu từ một bước chân:</h3>
                <p class="senior-text">
                  🔹 Glenn Cunningham không chờ chân lành hẳn mới chạy – ông chạy để chân lành lặn!<br/>
                  🔹 Bạn không cần giỏi công nghệ mới học AI – <strong>hãy dùng AI để trở nên thông tuệ hơn</strong>.<br/>
                  🔹 Hẹn gặp bạn tại Lớp học Zoom: <strong>20h00 Thứ Tư &amp; Thứ Bảy</strong> hàng tuần!
                </p>
              </div>
              <div class="transform-row-large">
                <span class="state-old-lg">🧱 Nỗi sợ trì hoãn</span>
                <span class="verb-bridge-lg">TRỞ THÀNH</span>
                <span class="state-new-lg">🏃 Đôi chân thần tốc trong kỷ nguyên AI</span>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

      <!-- SLIDE 15 -->
      <section class="slide">
        <div class="slide-inner tone-4">
          <div class="slide-header">
            <div>
              <span class="slide-tag">🌟 LỜI KẾT KHỞI CÔNG • TRANG 15 / 15</span>
              <h1 class="slide-title">🌟 HÃY CHẠY VỀ PHÍA ÁNH SÁNG KỶ NGUYÊN AI!</h1>
            </div>
            <button class="btn-slide-voice" onclick="speakSingleSlide(14)">🔊 Giảng Trang Này</button>
          </div>
          <div class="senior-stage one">
            <div class="senior-panel hero">
              <div class="floaty f1">🏃‍♂️</div>
              <div class="floaty f2">🏆</div>
              <div class="floaty f3">✨</div>
              <div class="bigq" onclick="confetti()">ĐỪNG BAO GIỜ BỎ CUỘC!</div>
              <div class="bigsub">Bạn là Kiến trúc sư • Bạn là Chủ công trình • AI là Đôi chân thần tốc</div>
              <div class="bigsub2">📅 Lớp học trực tuyến: 20h00 tối Thứ Tư &amp; Thứ Bảy hàng tuần trên Zoom</div>
              <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-top:10px;">
                <button class="btn-qr-instant" style="font-size:1.15rem; padding:12px 28px;" onclick="openQrFullscreenModal()">
                  💬 NHÓM ZALO xAI NGAY (Nhóm Zalo VND)
                </button>
                <button class="interactive-btn-lg" onclick="confetti()">🎉 Ăn mừng bứt phá!</button>
              </div>
            </div>
          </div>
          <div class="signature-watermark">Nguyễn Anh Tuấn • Bác Sĩ Cunningham xAI</div>
        </div>
      </section>

    </div>
  </main>

  <!-- TẦNG 3: BOTTOM STUDIO DOCK -->
  <footer class="bottom-studio-dock" aria-label="Thanh Phụ đề và Điều hướng">
    <div class="dock-nav-cluster">
      <button class="nav-action-btn" onclick="prevSlide()" id="btnPrevNav">◀ Trang Trước</button>
      <div class="dots-wrapper" id="dotsContainer"></div>
    </div>

    <div class="dock-teleprompter-stage" id="teleprompterBar">
      <div class="voice-wave-bars">
        <span></span><span></span><span></span><span></span>
      </div>
      <div class="teleprompter-text" id="teleprompterText">
        🤝 Sẵn sàng bài giảng Bác Sĩ Cunningham &amp; Đôi Chân Thần Tốc AI (Bấm "Bấm Nút Nói" để bắt đầu)...
      </div>
      <button class="btn-stop-inline" onclick="stopAutoLecture()">⏹ Dừng</button>
    </div>

    <div class="dock-nav-cluster">
      <label class="dock-hide-check" title="Tích để ẩn trang đang xem khỏi buổi thuyết trình (phím H)">
        <input type="checkbox" id="chkHideCurrent" onchange="toggleHideSlide(currentSlide, this.checked)" />
        🙈 Ẩn trang này
      </label>
      <button class="nav-action-btn" onclick="nextSlide()" id="btnNextNav">Trang Tiếp ▶</button>
    </div>
  </footer>

  <!-- MODAL SIÊU MÃ QR ACB TOÀN MÀN HÌNH -->
  <div class="voice-modal-backdrop" id="qrFullscreenModal" onclick="closeQrFullscreenModal()">
    <div class="voice-modal-card" style="max-width:680px; text-align:center; background:#ffffff; color:#0f172a; border:6px solid #f5c451;" onclick="event.stopPropagation()">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <span class="bni-badge" style="font-size:0.85rem;">💳 QUÉT MÃ QR ĐĂNG KÝ LỚP HỌC • KIẾN TẠO CUỘC SỐNG xAI</span>
        <button class="btn-outline-lg" style="background:#0f172a; color:#fff; padding:6px 14px;" onclick="closeQrFullscreenModal()">✕ Đóng</button>
      </div>

      <img id="fullscreenQrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=450x450&data=https%3A%2F%2Fzalo.me%2Fg%2Firsrqz032" alt="Siêu Mã QR ACB Zalo-xAI" style="width:430px; height:430px; max-width:82vw; max-height:55vh; object-fit:contain; margin:0 auto; display:block; border:3px solid #005baa; border-radius:20px; padding:8px;" onerror="this.src='https://api.qrserver.com/v1/create-qr-code/?size=450x450&data=ACB%20Zalo-xAI%20NGUYEN%20ANH%20TUAN%20%20KTCS%20Cunningham%20SDT'" />

      <div style="font-size:1.95rem; font-weight:900; color:#cf2030; margin-top:8px;">
        ƯU ĐÃI TRẢI NGHIỆM 1 THÁNG: Nhóm Zalo VND
      </div>
      <div style="font-size:1.15rem; font-weight:800; color:#005baa; margin-top:4px;">
        🏦 Ngân hàng Cộng Đồng Zalo • Zalo: Zalo xAI • Nguyễn Anh Tuấn
      </div>
      <div style="font-size:1.05rem; font-weight:800; color:#0f172a; margin-top:4px;">
        Nội dung chuyển khoản: <span style="color:#cf2030; background:#fef08a; padding:2px 10px; border-radius:6px;">KTCS Ten SDT</span> hoặc <span style="color:#005baa; background:#e0f2fe; padding:2px 10px; border-radius:6px;">KTCSxAI Ten SDT</span>
      </div>
      <div style="font-size:0.92rem; color:#475569; font-weight:600; margin-top:6px;">
        🕗 Lịch học trực tuyến: 20h00 tối Thứ 4 &amp; Thứ 7 hàng tuần (Học phí gốc: 4.368.000đ)
      </div>
    </div>
  </div>

  <!-- MODAL ẨN TRANG (HIDE SLIDE) -->
  <div class="voice-modal-backdrop" id="hideModal" onclick="closeHideModal()">
    <div class="voice-modal-card hide-modal-card" onclick="event.stopPropagation()">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:14px;">
        <div>
          <span class="slide-tag">👁 TÙY CHỌN ẨN TRANG • CHUẨN POWERPOINT</span>
          <h3 style="font-family:'Playfair Display', serif; font-size:1.45rem; color:#ffe9ad;">Tích vào trang muốn ẨN khỏi buổi đào tạo</h3>
          <div id="hideSummary" style="font-size:0.85rem; margin-top:4px; opacity:0.9;"></div>
        </div>
        <button class="btn-outline-lg" style="padding:6px 14px;" onclick="closeHideModal()">✕ Đóng</button>
      </div>
      <div class="hide-toolbar">
        <button onclick="showAllSlides()">👁 Hiện tất cả</button>
        <button onclick="hideAllExceptCurrent()">🙈 Ẩn tất cả, chỉ giữ trang đang xem</button>
        <button onclick="invertHiddenSlides()">🔄 Đảo lựa chọn</button>
      </div>
      <div class="hide-list" id="hideList"></div>
    </div>
  </div>

  <!-- MODAL PHÒNG THU & GIỌNG ĐỌC -->
  <div class="voice-modal-backdrop" id="voiceModal">
    <div class="voice-modal-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:16px;">
        <div>
          <span class="slide-tag">🎙️ PHÒNG THU • DUAL-ENGINE GIỌNG NAM &amp; GIỌNG NỮ THẬT 100%</span>
          <h3 style="font-family:'Playfair Display', serif; font-size:1.5rem; color:#ffe9ad;">Cài Đặt Giọng Đọc &amp; Thu Âm Giọng Thật</h3>
        </div>
        <button class="btn-outline-lg" style="padding:6px 14px;" onclick="closeVoiceModal()">✕ Đóng</button>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:16px;">
        <div style="background:rgba(255,255,255,0.04); padding:14px; border-radius:14px; border:1px solid rgba(255,255,255,0.1);">
          <label style="font-size:0.88rem; color:#ffe9ad; font-weight:700; display:block; margin-bottom:8px;">1. Chọn Giọng Đọc (Nam / Nữ Chuẩn):</label>
          <div style="display:flex; gap:8px;">
            <button class="btn-outline-lg active" id="modalBtnMale" style="flex:1; padding:8px;" onclick="setVoiceGender('male', true)">👨 Giọng Nam</button>
            <button class="btn-outline-lg" id="modalBtnFemale" style="flex:1; padding:8px;" onclick="setVoiceGender('female', true)">👩 Giọng Nữ (Cloud)</button>
          </div>
        </div>

        <div style="background:rgba(255,255,255,0.04); padding:14px; border-radius:14px; border:1px solid rgba(255,255,255,0.1);">
          <label style="font-size:0.88rem; color:#38bdf8; font-weight:700; display:block; margin-bottom:8px;">2. Tốc Độ Đọc (<span id="rateValLabel">1.00x</span>):</label>
          <input type="range" id="speedRangeSlider" min="0.5" max="1.8" step="0.05" value="1.0" style="width:100%; accent-color:#f5c451; margin-bottom:10px;" oninput="onTopSpeedSliderInput(this.value)" onchange="onTopSpeedSliderCommit(this.value)" />
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:0.85rem; color:#ffe9ad; font-weight:700;">Tự động lật qua 15 trang:</span>
            <input type="checkbox" id="chkAutoAdvance" checked style="width:20px; height:20px; accent-color:#34d399; cursor:pointer;" />
          </div>
        </div>
      </div>

      <div style="display:flex; justify-content:flex-end;">
        <button class="interactive-btn-lg" onclick="closeVoiceModal(); startAutoLectureFromCurrent();">▶️ Bắt Đầu Giảng Ngay</button>
      </div>
    </div>
  </div>

  <!-- MODAL GITHUB DEPLOY -->
  <div class="voice-modal-backdrop" id="githubModal">
    <div class="voice-modal-card">
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.15); padding-bottom:12px; margin-bottom:14px;">
        <div>
          <span class="slide-tag">🚀 XUẤT BẢN LÊN WEBSITE TUANTUTE.LIFE</span>
          <h3 style="font-family:'Playfair Display', serif; font-size:1.45rem; color:#ffe9ad;">Đóng Gói &amp; Xuất Bản Bài Thuyết Trình Lên GitHub</h3>
        </div>
        <button class="btn-outline-lg" style="padding:6px 14px;" onclick="closeGitHubModal()">✕ Đóng</button>
      </div>
      <div style="font-size:0.95rem; color:#ffe9ad; line-height:1.6; margin-bottom:12px;">
        Bài giảng này đã được tích hợp hoàn chỉnh và xuất bản thành công lên website chính thức: <strong>tuantute.life</strong>!
      </div>
      <div style="background:rgba(52,211,153,0.12); border:1px solid #34d399; color:#34d399; padding:12px; border-radius:12px; font-weight:800; font-size:1rem; text-align:center;">
        https://tuantute.life/Bác-sĩ-Cunningham-người-chạy-nhanh-nhất-thế-giới
      </div>
    </div>
  </div>

  <script>
    // 0. CHỐNG CHỮ MỒ CÔI
    function bindClauseWords(str) {{
      if (!str) return str;
      const words = str.trim().split(/\\s+/);
      if (words.length < 4) return str;
      const head = words.slice(0, -3).join(' ');
      const tail = words.slice(-3).join('\\u00A0');
      return head + ' ' + tail;
    }}

    function lockAllVietnameseOrphans() {{
      const targets = document.querySelectorAll('.slide-title, .senior-heading, .senior-text, .art-caption, .poem-box-large');
      targets.forEach(el => {{
        if (el.innerHTML.includes('<br')) {{
          const lines = el.innerHTML.split(/<br\\s*\\/?>/i);
          const lockedLines = lines.map(line => {{
            return line.replace(/([^\\s<>]+)\\s+([^\\s<>]+)\\s+([^\\s<>]+)\\s*$/, '$1\\u00A0$2\\u00A0$3');
          }});
          el.innerHTML = lockedLines.join('<br/>');
        }} else {{
          const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false);
          let nodes = [];
          while (walker.nextNode()) {{
            if (walker.currentNode.nodeValue.trim().length > 0) nodes.push(walker.currentNode);
          }}
          if (nodes.length > 0) {{
            const last = nodes[nodes.length - 1];
            last.nodeValue = last.nodeValue.replace(/(\\S+)\\s+(\\S+)\\s+(\\S+)\\s*$/, '$1\\u00A0$2\\u00A0$3');
          }}
        }}
      }});
    }}

    function setVisualArtStyle(styleKey) {{
      document.body.classList.remove('style-cinematic', 'style-handdrawn', 'style-infographic', 'style-cartoon');
      document.body.classList.add('style-' + styleKey);
      sfxChime();
      applyImagesNear(true);
      const styleNames = {{
        cinematic: '🎬 Phong cách Điện Ảnh 4D',
        handdrawn: '✍️ Phong cách Vẽ Tay & Viết Tay',
        infographic: '📊 Phong cách Đồ Hoạ Infographic',
        cartoon: '🎠 Phong cách Hoạt Hình 3D'
      }};
      showVoiceToast(`🎨 Đã chuyển sang: ${{styleNames[styleKey]}}`);
    }}

    // 1. COSMOS CANVAS PARALLAX
    const canvas = document.getElementById('cosmosCanvas');
    const ctx = canvas.getContext('2d');
    let stars = [], particles = [];

    function resizeCanvas() {{
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    for (let i = 0; i < 95; i++) {{
      stars.push({{
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 1.6 + 0.4,
        alpha: Math.random(),
        speed: Math.random() * 0.014 + 0.004
      }});
    }}

    function animateCosmos() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      stars.forEach(s => {{
        s.alpha += s.speed;
        if (s.alpha > 1 || s.alpha < 0.2) s.speed = -s.speed;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 233, 173, ${{s.alpha * 0.65}})`;
        ctx.fill();
      }});

      for (let i = particles.length - 1; i >= 0; i--) {{
        const p = particles[i];
        p.x += p.vx; p.y += p.vy; p.vy += 0.06; p.life -= 0.016;
        if (p.life <= 0) particles.splice(i, 1);
        else {{
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(${{p.color}}, ${{p.life}})`;
          ctx.fill();
        }}
      }}
      requestAnimationFrame(animateCosmos);
    }}
    animateCosmos();

    function launchCelebration() {{
      for (let b = 0; b < 5; b++) {{
        const cx = canvas.width * (0.2 + Math.random() * 0.6);
        const cy = canvas.height * (0.2 + Math.random() * 0.4);
        for (let i = 0; i < 45; i++) {{
          const angle = Math.random() * Math.PI * 2;
          const speed = Math.random() * 5.5 + 1.5;
          const colors = ['245, 196, 81', '207, 32, 48', '52, 211, 153', '56, 189, 248'];
          particles.push({{
            x: cx, y: cy, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed,
            size: Math.random() * 3.5 + 1.5, color: colors[Math.floor(Math.random() * colors.length)], life: 1.0
          }});
        }}
      }}
    }}

    // 2. ĐIỀU HƯỚNG 15 SLIDES & ẨN TRANG
    let currentSlide = 0;
    const totalSlides = 15;
    let currentMode = 'horizontal';
    let wheelCooldown = false;
    const slidesTrack = document.getElementById('slidesTrack');
    const dotsContainer = document.getElementById('dotsContainer');
    const slideJumpSelect = document.getElementById('slideJumpSelect');

    const HIDE_STORAGE_KEY = 'cunningham_hidden_v01';
    let hiddenSlides = new Set();
    const slideTitleOriginals = [];

    function loadHiddenSlides() {{
      try {{
        const raw = localStorage.getItem(HIDE_STORAGE_KEY);
        if (raw) JSON.parse(raw).forEach(n => {{ if (Number.isInteger(n) && n >= 0 && n < totalSlides) hiddenSlides.add(n); }});
      }} catch (e) {{}}
      if (hiddenSlides.size >= totalSlides) hiddenSlides.clear();
    }}
    function saveHiddenSlides() {{
      try {{ localStorage.setItem(HIDE_STORAGE_KEY, JSON.stringify(Array.from(hiddenSlides))); }} catch (e) {{}}
    }}
    function visibleCount() {{ return totalSlides - hiddenSlides.size; }}
    function findVisibleSlide(from, dir) {{
      for (let i = from + dir; i >= 0 && i < totalSlides; i += dir) {{
        if (!hiddenSlides.has(i)) return i;
      }}
      return -1;
    }}
    function visiblePosition(idx) {{
      let n = 0;
      for (let i = 0; i <= idx; i++) if (!hiddenSlides.has(i)) n++;
      return n;
    }}

    function initDots() {{
      dotsContainer.innerHTML = '';
      for (let i = 0; i < totalSlides; i++) {{
        const dot = document.createElement('div');
        dot.className = 'slide-dot' + (i === currentSlide ? ' active' : '');
        dot.title = 'Trang ' + (i + 1);
        dot.onclick = () => goToSlide(i, true);
        dotsContainer.appendChild(dot);
      }}
    }}

    function syncHiddenUI() {{
      const slides = document.querySelectorAll('.slide');
      slides.forEach((s, i) => s.classList.toggle('is-hidden', hiddenSlides.has(i)));
      dotsContainer.querySelectorAll('.slide-dot').forEach((d, i) => d.classList.toggle('is-hidden', hiddenSlides.has(i)));

      if (slideJumpSelect) {{
        Array.from(slideJumpSelect.options).forEach((opt, i) => {{
          if (slideTitleOriginals[i] === undefined) slideTitleOriginals[i] = opt.textContent;
          const hid = hiddenSlides.has(i);
          opt.textContent = (hid ? '🙈 [ĐÃ ẨN] ' : '') + slideTitleOriginals[i];
          opt.disabled = hid && i !== currentSlide;
        }});
      }}

      const badge = document.getElementById('hideCountBadge');
      if (badge) {{
        badge.textContent = String(hiddenSlides.size);
        badge.classList.toggle('zero', hiddenSlides.size === 0);
      }}
      const chk = document.getElementById('chkHideCurrent');
      if (chk) chk.checked = hiddenSlides.has(currentSlide);

      const modal = document.getElementById('hideModal');
      if (modal && modal.classList.contains('open')) renderHideList();
    }}

    function renderHideList() {{
      const list = document.getElementById('hideList');
      if (!list) return;
      list.innerHTML = '';
      for (let i = 0; i < totalSlides; i++) {{
        const hid = hiddenSlides.has(i);
        const row = document.createElement('label');
        row.className = 'hide-row' + (hid ? ' is-hidden' : '') + (i === currentSlide ? ' is-current' : '');
        const cb = document.createElement('input');
        cb.type = 'checkbox'; cb.checked = hid;
        cb.onchange = () => toggleHideSlide(i, cb.checked);
        const title = document.createElement('span');
        title.className = 'hide-row-title';
        title.textContent = slideTitleOriginals[i] !== undefined ? slideTitleOriginals[i] : ('Trang ' + (i + 1));
        const state = document.createElement('span');
        state.className = 'hide-row-state';
        state.textContent = hid ? '🙈 ĐÃ ẨN' : (i === currentSlide ? '▶ ĐANG XEM' : '✔ HIỂN THỊ');
        row.appendChild(cb); row.appendChild(title); row.appendChild(state);
        list.appendChild(row);
      }}
      const sum = document.getElementById('hideSummary');
      if (sum) sum.textContent = `Đang hiển thị ${{visibleCount()}} / ${{totalSlides}} trang • Đã ẩn ${{hiddenSlides.size}} trang`;
    }}

    function toggleHideSlide(idx, hide) {{
      if (hide && !hiddenSlides.has(idx) && visibleCount() <= 1) {{
        showVoiceToast('⚠️ Phải giữ lại ít nhất 1 trang hiển thị!');
        syncHiddenUI();
        return;
      }}
      if (hide) hiddenSlides.add(idx); else hiddenSlides.delete(idx);
      saveHiddenSlides();

      if (hide && idx === currentSlide) {{
        let target = findVisibleSlide(currentSlide, 1);
        if (target === -1) target = findVisibleSlide(currentSlide, -1);
        if (target !== -1) goToSlide(target, true);
      }}
      syncHiddenUI();
      showVoiceToast(hide ? `🙈 Đã ẩn Trang ${{idx + 1}}` : `👁 Đã hiện lại Trang ${{idx + 1}}`);
    }}

    function showAllSlides() {{ hiddenSlides.clear(); saveHiddenSlides(); syncHiddenUI(); showVoiceToast('👁 Đã hiện tất cả các trang'); }}
    function hideAllExceptCurrent() {{
      hiddenSlides.clear();
      for (let i = 0; i < totalSlides; i++) if (i !== currentSlide) hiddenSlides.add(i);
      saveHiddenSlides(); syncHiddenUI();
    }}
    function invertHiddenSlides() {{
      const next = new Set();
      for (let i = 0; i < totalSlides; i++) if (!hiddenSlides.has(i)) next.add(i);
      if (next.size >= totalSlides) return;
      hiddenSlides = next; saveHiddenSlides();
      if (hiddenSlides.has(currentSlide)) {{
        let t = findVisibleSlide(currentSlide, 1);
        if (t === -1) t = findVisibleSlide(currentSlide, -1);
        if (t !== -1) goToSlide(t, true);
      }}
      syncHiddenUI();
    }}
    function openHideModal() {{ document.getElementById('hideModal').classList.add('open'); renderHideList(); }}
    function closeHideModal() {{ document.getElementById('hideModal').classList.remove('open'); }}

    function updateSlidePosition() {{
      syncHiddenUI();
      v03Sync();
      if (slideJumpSelect) slideJumpSelect.value = String(currentSlide);
      document.querySelectorAll('.slide').forEach((s, idx) => {{
        s.classList.toggle('active-slide', idx === currentSlide);
      }});

      if (currentMode === 'scroll') {{
        slidesTrack.style.transform = 'none';
        return;
      }}

      if (currentMode === 'horizontal') {{
        slidesTrack.style.transform = `translate3d(-${{currentSlide * 100}}vw, 0, 0)`;
        document.getElementById('btnPrevNav').textContent = '◀ Trang Trước';
        document.getElementById('btnNextNav').textContent = 'Trang Tiếp ▶';
      }} else if (currentMode === 'vertical') {{
        slidesTrack.style.transform = `translate3d(0, -${{currentSlide * 100}}%, 0)`;
        document.getElementById('btnPrevNav').textContent = '▲ Trang Trên';
        document.getElementById('btnNextNav').textContent = 'Trang Dưới ▼';
      }}

      const dots = dotsContainer.querySelectorAll('.slide-dot');
      dots.forEach((d, idx) => d.classList.toggle('active', idx === currentSlide));
    }}

    function goToSlide(index, manualTrigger = false) {{
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;
      if (hiddenSlides.has(index) && index !== currentSlide) {{
        let t = findVisibleSlide(index, index > currentSlide ? 1 : -1);
        if (t === -1) t = findVisibleSlide(index, index > currentSlide ? -1 : 1);
        if (t === -1) return;
        index = t;
      }}
      const prevS = currentSlide;
      currentSlide = index;
      if (prevS !== index) sfxWhoosh();
      updateSlidePosition();

      if (currentMode === 'scroll') {{
        const slideElements = document.querySelectorAll('.slide');
        if (slideElements[currentSlide]) slideElements[currentSlide].scrollIntoView({{ behavior: 'smooth' }});
      }}

      if (manualTrigger && isAutoLecturing) {{
        playSlideNarration(currentSlide, document.getElementById('chkAutoAdvance').checked, 0);
      }}
    }}

    function nextSlide() {{
      const t = findVisibleSlide(currentSlide, 1);
      if (t !== -1) goToSlide(t, true);
    }}
    function prevSlide() {{
      const t = findVisibleSlide(currentSlide, -1);
      if (t !== -1) goToSlide(t, true);
    }}

    function setDeckMode(mode) {{
      currentMode = mode;
      document.documentElement.className = 'mode-' + mode;
      document.body.classList.remove('mode-horizontal', 'mode-vertical', 'mode-scroll');
      document.body.classList.add('mode-' + mode);
      document.getElementById('btnHorizontal').classList.toggle('active', mode === 'horizontal');
      document.getElementById('btnVertical').classList.toggle('active', mode === 'vertical');
      document.getElementById('btnScroll').classList.toggle('active', mode === 'scroll');
      updateSlidePosition();
    }}

    window.addEventListener('keydown', (e) => {{
      const tag = (e.target && e.target.tagName) || '';
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(tag) && e.target.type !== 'checkbox') return;
      if (e.key === 'Escape') {{ closeHideModal(); closeQrFullscreenModal(); closeVoiceModal(); closeGitHubModal(); return; }}
      if ((e.key === 'h' || e.key === 'H') && !e.ctrlKey && !e.metaKey) {{
        e.preventDefault();
        toggleHideSlide(currentSlide, !hiddenSlides.has(currentSlide));
      }}
      if ((e.key === 'f' || e.key === 'F') && !e.ctrlKey && !e.metaKey) toggleFullScreen();
      if (currentMode === 'scroll') return;
      if (['ArrowRight', 'ArrowDown', 'PageDown'].includes(e.key)) {{ e.preventDefault(); nextSlide(); }}
      else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) {{ e.preventDefault(); prevSlide(); }}
    }});

    function toggleFullScreen() {{
      if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {{}});
      else document.exitFullscreen();
    }}

    // 3. TRANH SVG NGHỆ THUẬT OFFLINE THEO NỘI DUNG CUNNINGHAM
    const SCENE_EMOJI = {{
      0: ['🏃‍♂️', '🏆', '✨'],
      1: ['🔥', '🧒', '🩹'],
      2: ['🦵', '🌾', '🏃'],
      3: ['⏱️', '🥇', '🏟️'],
      4: ['🎓', '🏡', '🤝'],
      5: ['🇻🇳', '👴', '🤖'],
      6: ['🚀', '🦾', '💡'],
      7: ['🛞', '⚖️', '🧭'],
      8: ['🤖', '📝', '⚡'],
      9: ['⚖️', '⏱️', '📈'],
      10: ['💪', '🧘', '🧠'],
      11: ['🎮', '❓', '🏆'],
      12: ['🎡', '🎯', '🔥'],
      13: ['🌅', '✍️', '🏛️'],
      14: ['🌟', '💳', '🍀']
    }};

    function artSvg(idx, style) {{
      const W = 1400, H = 900, em = SCENE_EMOJI[idx] || ['🏃‍♂️', '🤖', '✨'], h = (idx * 47 + 200) % 360;
      let sd = idx * 9301 + 49297; const R = () => (sd = (sd * 9301 + 49297) % 233280) / 233280;
      const E = (t, x, y, z, ex) => '<text x="' + x + '" y="' + y + '" font-size="' + z + '" text-anchor="middle" ' + (ex || '') + '>' + t + '</text>';
      const trio = ex => E(em[0], 700, 560, 380, ex) + E(em[1], 300, 640, 200, ex) + E(em[2], 1100, 640, 200, ex);
      let d = '', body = '';
      if (style === 'cinematic') {{
        d = '<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="hsl(' + h + ',60%,9%)"/><stop offset="1" stop-color="hsl(' + (h + 40) + ',70%,24%)"/></linearGradient>' +
          '<radialGradient id="r" cx=".5" cy=".45" r=".55"><stop offset="0" stop-color="#ffd98a" stop-opacity=".6"/><stop offset="1" stop-opacity="0"/></radialGradient>' +
          '<radialGradient id="v" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-opacity="0"/><stop offset="1" stop-opacity=".8"/></radialGradient>' +
          '<filter id="b"><feGaussianBlur stdDeviation="7"/></filter><filter id="s"><feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#000" flood-opacity=".7"/></filter>';
        body = '<rect width="1400" height="900" fill="url(#g)"/><rect width="1400" height="900" fill="url(#r)"/>' +
          '<polygon points="560,0 840,0 1100,900 300,900" fill="#fff" opacity=".06"/>';
        for (let i = 0; i < 14; i++) body += '<circle cx="' + (R() * W | 0) + '" cy="' + (R() * H | 0) + '" r="' + (14 + R() * 46 | 0) + '" fill="hsl(' + (h + R() * 60 | 0) + ',90%,70%)" opacity="' + (.12 + R() * .2).toFixed(2) + '" filter="url(#b)"/>';
        body += trio('filter="url(#s)"') + '<rect width="1400" height="900" fill="url(#v)"/><rect width="1400" height="64" fill="#000"/><rect y="836" width="1400" height="64" fill="#000"/>';
      }} else if (style === 'handdrawn') {{
        d = '<filter id="w"><feTurbulence baseFrequency=".03" numOctaves="2" seed="' + idx + '"/><feDisplacementMap in="SourceGraphic" scale="14"/></filter>' +
          '<filter id="t"><feColorMatrix type="saturate" values=".55"/></filter>';
        body = '<rect width="1400" height="900" fill="#f4ebd9"/>';
        for (let i = 0; i < 90; i++) body += '<circle cx="' + (R() * W | 0) + '" cy="' + (R() * H | 0) + '" r="2" fill="#b45309" opacity=".18"/>';
        body += '<g filter="url(#w)" fill="none" stroke="#991b1b" stroke-width="7" stroke-linecap="round"><circle cx="700" cy="440" r="270" stroke-dasharray="26 14"/><circle cx="300" cy="520" r="140" stroke="#0369a1"/><circle cx="1100" cy="520" r="140" stroke="#15803d"/>' +
          '<path d="M120 800 Q400 740 700 800 T1280 790" stroke="#b45309"/></g><g filter="url(#t)">' + trio('') + '</g>';
      }} else if (style === 'infographic') {{
        d = '<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b192c"/><stop offset="1" stop-color="#1e3e62"/></linearGradient>';
        body = '<rect width="1400" height="900" fill="url(#g)"/><circle cx="700" cy="400" r="190" fill="#ff6500"/><circle cx="300" cy="430" r="120" fill="#00d2ff"/><circle cx="1100" cy="430" r="120" fill="#00f5d4"/>' +
          trio('');
      }} else {{
        d = '<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="hsl(' + (h + 20) + ',85%,62%)"/><stop offset="1" stop-color="hsl(' + (h + 60) + ',90%,80%)"/></linearGradient>';
        body = '<rect width="1400" height="900" fill="url(#g)"/><circle cx="1180" cy="190" r="110" fill="#fef08a"/>' +
          trio('stroke="#fff" stroke-width="22" stroke-linejoin="round" paint-order="stroke"');
      }}
      return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" width="1400" height="900"><defs>' + d + '</defs>' + body + '</svg>');
    }}

    const photoImgs = [];
    function curStyle() {{ const m = document.body.className.match(/style-(\\w+)/); return m ? m[1] : 'cinematic'; }}
    function applyPhoto(p, force) {{
      const style = curStyle();
      const url = artSvg(p.idx, style);
      if (!force && p.el.src === url) return;
      p.el.src = url;
    }}
    function applyImagesNear(force) {{
      photoImgs.forEach(p => {{ if (Math.abs(p.idx - currentSlide) <= 1) applyPhoto(p, force); }});
    }}
    function initPhotoSwap() {{
      const slides = Array.from(document.querySelectorAll('.slide'));
      document.querySelectorAll('img.bg-photo').forEach(el => {{
        const idx = slides.indexOf(el.closest('.slide'));
        if (idx < 0 || el.dataset.keep) return;
        photoImgs.push({{ el, idx }});
      }});
    }}
    function v03Sync() {{
      setTimeout(animateCounters, 450);
      const bar = document.getElementById('deckProgress');
      if (bar) bar.style.width = (visiblePosition(currentSlide) / Math.max(1, visibleCount()) * 100) + '%';
      if (photoImgs.length) applyImagesNear(false);
    }}

    // 4. WEB AUDIO SYNTHESIZER
    let AC = null, musicGain = null, musicOn = false, musicTimer = null, sfxOn = true, chordIdx = 0, musicVolPct = 35;
    const CHORDS = [[220, 261.63, 329.63], [174.61, 220, 261.63], [261.63, 329.63, 392], [196, 246.94, 293.66]];
    const PENTA = [440, 494, 587, 659, 784, 880];
    function ensureAudio() {{
      if (!AC) {{
        AC = new (window.AudioContext || window.webkitAudioContext)();
        musicGain = AC.createGain(); musicGain.connect(AC.destination); updateMusicGain();
      }}
      if (AC.state === 'suspended') AC.resume();
    }}
    function updateMusicGain() {{
      if (!musicGain) return;
      const duck = isAutoLecturing ? 0.45 : 1;
      musicGain.gain.setTargetAtTime(musicVolPct / 100 * 0.25 * duck, AC.currentTime, 0.4);
    }}
    function playPad(freqs, dur) {{
      const t = AC.currentTime;
      freqs.forEach(f => {{
        const o = AC.createOscillator(), g = AC.createGain(), lp = AC.createBiquadFilter();
        o.type = 'triangle'; o.frequency.value = f;
        lp.type = 'lowpass'; lp.frequency.value = 900;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.5, t + dur * .35); g.gain.linearRampToValueAtTime(0, t + dur);
        o.connect(lp); lp.connect(g); g.connect(musicGain); o.start(t); o.stop(t + dur + .1);
      }});
    }}
    function playBell(f) {{
      const t = AC.currentTime, o = AC.createOscillator(), g = AC.createGain();
      o.type = 'sine'; o.frequency.value = f;
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.18, t + .02); g.gain.exponentialRampToValueAtTime(0.0008, t + 2.2);
      o.connect(g); g.connect(musicGain); o.start(t); o.stop(t + 2.3);
    }}
    function toggleMusic() {{
      ensureAudio(); musicOn = !musicOn;
      document.getElementById('btnMusic').classList.toggle('on', musicOn);
      if (musicOn) {{
        const tick = () => {{ playPad(CHORDS[chordIdx++ % 4], 8); }};
        tick(); musicTimer = setInterval(tick, 7000);
      }} else {{ clearInterval(musicTimer); }}
      showVoiceToast(musicOn ? '🎵 Đã bật nhạc nền nhẹ' : '🔇 Đã tắt nhạc nền');
    }}
    function setMusicVol(v) {{ musicVolPct = +v; if (AC) updateMusicGain(); }}
    function toggleSfx() {{ sfxOn = !sfxOn; document.getElementById('btnSfx').classList.toggle('on', sfxOn); }}
    function sfxWhoosh() {{
      if (!sfxOn) return; try {{ ensureAudio(); }} catch(e) {{ return; }}
      const t = AC.currentTime, len = AC.sampleRate * .4, buf = AC.createBuffer(1, len, AC.sampleRate), d = buf.getChannelData(0);
      for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / len);
      const s = AC.createBufferSource(), bp = AC.createBiquadFilter(), g = AC.createGain();
      s.buffer = buf; bp.type = 'bandpass'; bp.frequency.setValueAtTime(400, t); bp.frequency.exponentialRampToValueAtTime(2400, t + .35);
      g.gain.setValueAtTime(.12, t); g.gain.exponentialRampToValueAtTime(.001, t + .4);
      s.connect(bp); bp.connect(g); g.connect(AC.destination); s.start(t);
    }}
    function sfxChime() {{
      if (!sfxOn) return; try {{ ensureAudio(); }} catch(e) {{ return; }}
      [880, 1318.5].forEach((f, k) => {{
        const t = AC.currentTime + k * .12, o = AC.createOscillator(), g = AC.createGain();
        o.type = 'sine'; o.frequency.value = f;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.16, t + .01); g.gain.exponentialRampToValueAtTime(.001, t + .9);
        o.connect(g); g.connect(AC.destination); o.start(t); o.stop(t + 1);
      }});
    }}

    // 5. DUAL-ENGINE GIỌNG ĐỌC & KỊCH BẢN THUYẾT MINH
    let isAutoLecturing = false, voiceGender = 'male', speechRate = 1.0;
    let speechSessionId = 0, currentUtterance = null, activeAudioElement = null;

    function toSpokenVietnamese(text) {{
      return text
        .replace(/468\\.468\\s*(đ|VND)/gi, 'bốn trăm sáu mươi tám nghìn bốn trăm sáu mươi tám đồng')
        .replace(/102\\s*168\\s*268/g, 'một không hai, một sáu tám, hai sáu tám')
        .replace(/20h00/gi, 'hai mươi giờ')
        .replace(/10x/gi, 'mười lần')
        .replace(/AI/g, 'Ây Ai')
        .replace(/Glenn Cunningham/gi, 'Gờ-len Ca-ninh-hem')
        .replace(/Cunningham/gi, 'Ca-ninh-hem')
        .replace(/4:06\\.8/g, 'bốn phút không sáu giây tám')
        .replace(/9\\.000/g, 'chín nghìn')
        .replace(/1\\.609m/g, 'một nghìn sáu trăm lẻ chín mét')
        .replace(/1\\.500m/g, 'một nghìn năm trăm mét')
        .replace(/1934/g, 'năm một chín ba tư')
        .replace(/1936/g, 'năm một chín ba sáu')
        .replace(/1916/g, 'năm một chín mười sáu');
    }}

    function showVoiceToast(msg) {{
      const t = document.getElementById('voiceToast');
      if (!t) return;
      t.textContent = msg; t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2400);
    }}

    function cancelActiveSpeechCleanly() {{
      speechSessionId++;
      if (currentUtterance) {{ currentUtterance.onend = null; currentUtterance.onerror = null; currentUtterance = null; }}
      if (activeAudioElement) {{ activeAudioElement.onended = null; activeAudioElement.pause(); activeAudioElement = null; }}
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      return speechSessionId;
    }}

    function setVoiceGender(g, preview) {{
      voiceGender = g;
      document.getElementById('btnVoiceMale').classList.toggle('active', g === 'male');
      document.getElementById('btnVoiceFemale').classList.toggle('active', g === 'female');
      document.getElementById('modalBtnMale').classList.toggle('active', g === 'male');
      document.getElementById('modalBtnFemale').classList.toggle('active', g === 'female');
      showVoiceToast(g === 'male' ? '👨 Giọng Nam Trầm Ấm' : '👩 Giọng Nữ Truyền Cảm');
    }}

    function syncSpeedUI(val) {{
      speechRate = Math.max(0.5, Math.min(1.8, parseFloat(val)));
      const formatted = speechRate.toFixed(2) + 'x';
      document.getElementById('topSpeedSlider').value = String(speechRate);
      document.getElementById('topSpeedVal').textContent = formatted;
      document.getElementById('speedRangeSlider').value = String(speechRate);
      document.getElementById('rateValLabel').textContent = formatted;
    }}
    function onTopSpeedSliderInput(v) {{ syncSpeedUI(v); }}
    function onTopSpeedSliderCommit(v) {{ syncSpeedUI(v); }}
    function stepSpeechSpeed(d) {{ onTopSpeedSliderCommit(Math.round((speechRate + d) * 100) / 100); }}

    const lectureScripts16 = [
      {{ segments: [
        {{ text: "Chào mừng các anh chị đến với bài chia sẻ đặc biệt: Huyền thoại Bác sĩ Glenn Cunningham, Người chạy nhanh nhất thế giới và bài học vượt ngưỡng cho người trung niên Việt Nam thời AI." }},
        {{ text: "Tôi là Nguyễn Anh Tuấn. Hãy cùng khám phá cách biến nghịch cảnh và kinh nghiệm sống của bạn thành sức mạnh thần tốc trong kỷ nguyên mới." }}
      ] }},
      {{ segments: [
        {{ text: "Năm bảy tuổi, một vụ nổ lò sưởi kinh hoàng đã thiêu rụi đôi chân của cậu bé Glenn Cunningham. Anh trai cậu qua đời, còn bác sĩ tuyên bố cậu sẽ không bao giờ đi lại được nữa." }},
        {{ text: "Nhưng trên giường bệnh, cậu bé đã nắm chặt tay mẹ và thề một câu để đời: Con không chỉ đi được, mà con sẽ CHẠY!" }}
      ] }},
      {{ segments: [
        {{ text: "Suốt hai năm nằm liệt giường, Glenn kiên trì xoa bóp từng thớ cơ cháy xém. Khi chập chững đứng lên, mỗi bước đi đau buốt như xé thịt." }},
        {{ text: "Thế rồi cậu phát hiện ra một điều kỳ diệu: Chạy thì ít đau hơn đi bộ, vì thời gian chân chạm đất ngắn hơn. Thế là cậu chạy bất kể ngày đêm!" }}
      ] }},
      {{ segments: [
        {{ text: "Và điều kỳ tích đã đến. Năm một chín ba tư, tại quảng trường Madison Square Garden, Glenn Cunningham đã phá kỷ lục thế giới cự ly một dặm với bốn phút không sáu giây tám." }},
        {{ text: "Cả thế giới nghiêng mình trước Người sắt Kansas. Giới hạn duy nhất của con người chính là giới hạn ta tự đặt ra trong đầu!" }}
      ] }},
      {{ segments: [
        {{ text: "Sau khi giải nghệ, ông lấy bằng Tiến sĩ Giáo dục và cùng vợ nuôi dạy hơn chín nghìn đứa trẻ cơ nhỡ tại trang trại của mình." }},
        {{ text: "Ông chứng minh: Thành công đỉnh cao không chỉ là chiến thắng trên đường chạy, mà là di sản tình yêu thương và sự tử tế để lại cho cuộc đời." }}
      ] }},
      {{ segments: [
        {{ text: "Hôm nay, rất nhiều người trung niên Việt Nam từ ba mươi tám đến năm mươi chín tuổi đang mang trong mình nỗi sợ: Tôi già rồi, tôi sợ công nghệ, liệu AI có đào thải tôi không?" }},
        {{ text: "Nhưng thưa các anh chị, kinh nghiệm sống và sự chín chắn của các anh chị chính là mỏ vàng mà không một người trẻ hay cỗ máy nào tự có được!" }}
      ] }},
      {{ segments: [
        {{ text: "AI không sinh ra để thay thế bạn. AI chính là đôi chân thần tốc mới của bạn! Bạn là Kiến trúc sư vẽ bản thiết kế, bạn là Chủ công trình quyết định, còn AI thi công siêu tốc gấp mười lần." }}
      ] }},
      {{ segments: [
        {{ text: "Đây là Bánh xe cuộc đời thời AI. Sáu múi gồm: Thể lực dẻo dai, Vận động mỗi ngày, Bình an trong tâm, Kết nối yêu thương, Học tập suốt đời và Ứng dụng AI." }},
        {{ text: "Mời anh chị chấm điểm từ một đến mười và bấm nút Cân bằng để bánh xe luôn tròn đều lăn xa." }}
      ] }},
      {{ segments: [
        {{ text: "Thực hành AI cực kỳ dễ dàng. Với bộ công thức Lệnh Vàng bốn bước gồm Vai trò, Việc cần làm, Bối cảnh và Định dạng, anh chị chỉ cần bốn cú chạm là có ngay câu trả lời thông minh." }}
      ] }},
      {{ segments: [
        {{ text: "Hãy gạt công tắc so sánh một ngày có trợ lý AI. Anh chị sẽ tiết kiệm tới một trăm lẻ năm phút mỗi ngày để bơi biển, chạy bộ và sum vầy bên gia đình yêu thương." }}
      ] }},
      {{ segments: [
        {{ text: "Nền móng của một Người sắt bắt đầu từ Thân Tâm Trí. Hãy tích vào sáu thói quen mỗi ngày: vận động ba mươi phút, ngủ đủ giấc, kết nối bạn bè, đọc sách, hỏi AI và thở sâu biết ơn." }}
      ] }},
      {{ segments: [
        {{ text: "Giờ là lúc thử thách ba câu hỏi tương tác. Hãy bấm chọn đáp án anh chị thấy tâm đắc nhất để kiểm tra mức độ thấu hiểu tinh thần Cunningham." }}
      ] }},
      {{ segments: [
        {{ text: "Mời anh chị bấm quay vòng thử thách hành động nhỏ hôm nay. Nhận thử thách, hoàn thành trong mười lăm phút và gõ kết quả vào khung Chat Zoom nhé!" }}
      ] }},
      {{ segments: [
        {{ text: "Thời khắc khởi công đã đến! Mời anh chị gõ họ tên, chọn nâng Thân, Tâm hay Trí trong bảy ngày tới và bấm Ký cam kết vượt ngưỡng." }}
      ] }},
      {{ segments: [
        {{ text: "Đừng bao giờ bỏ cuộc! Hãy chạy về phía ánh sáng của kỷ nguyên AI. Hẹn gặp các anh chị tại lớp học Zoom hai mươi giờ tối Thứ Tư và Thứ Bảy hàng tuần. Xin cảm ơn tất cả các anh chị!" }}
      ] }}
    ];

    function toggleAutoLecture() {{
      if (isAutoLecturing) stopAutoLecture();
      else startAutoLectureFromCurrent();
    }}
    function startAutoLectureFromCurrent() {{
      isAutoLecturing = true;
      document.getElementById('btnMasterSpeak').classList.add('speaking');
      document.getElementById('speakIcon').textContent = '⏹';
      document.getElementById('speakLabel').textContent = 'ĐANG GIẢNG (DỪNG)';
      document.getElementById('teleprompterBar').classList.add('active-speaking');
      playSlideNarration(currentSlide, document.getElementById('chkAutoAdvance').checked, 0);
    }}
    function stopAutoLecture() {{
      isAutoLecturing = false;
      cancelActiveSpeechCleanly();
      document.getElementById('btnMasterSpeak').classList.remove('speaking');
      document.getElementById('speakIcon').textContent = '🎙️';
      document.getElementById('speakLabel').textContent = 'BẤM NÚT NÓI';
      document.getElementById('teleprompterBar').classList.remove('active-speaking');
      document.querySelectorAll('.slide-inner').forEach(el => el.classList.remove('narrating-glow'));
    }}
    function speakSingleSlide(i) {{
      goToSlide(i, false);
      startAutoLectureFromCurrent();
    }}

    function playSlideNarration(slideIdx, autoAdvance, startSeg) {{
      const mySession = cancelActiveSpeechCleanly();
      if (!isAutoLecturing) return;
      document.querySelectorAll('.slide-inner').forEach((el, idx) => {{
        el.classList.toggle('narrating-glow', idx === slideIdx);
      }});

      const script = lectureScripts16[slideIdx];
      if (!script) return;
      const segs = script.segments;
      let segIdx = startSeg;

      function speakNext() {{
        if (mySession !== speechSessionId || !isAutoLecturing) return;
        if (segIdx >= segs.length) {{
          const next = findVisibleSlide(slideIdx, 1);
          if (autoAdvance && next !== -1) {{
            setTimeout(() => {{
              if (mySession !== speechSessionId || !isAutoLecturing) return;
              goToSlide(next, false);
              setTimeout(() => playSlideNarration(next, true, 0), 500);
            }}, 700);
          }} else {{
            stopAutoLecture();
          }}
          return;
        }}

        const seg = segs[segIdx];
        document.getElementById('teleprompterText').textContent = seg.text;
        const spoken = toSpokenVietnamese(seg.text.replace(/[\\u{{1F300}}-\\u{{1FAFF}}\\u{{2600}}-\\u{{27BF}}]/gu, ''));

        if ('speechSynthesis' in window) {{
          const utter = new SpeechSynthesisUtterance(spoken);
          utter.lang = 'vi-VN'; utter.rate = speechRate;
          utter.pitch = voiceGender === 'female' ? 1.4 : 0.84;
          let done = false;
          utter.onend = utter.onerror = () => {{
            if (done || mySession !== speechSessionId) return;
            done = true; segIdx++; setTimeout(speakNext, 300);
          }};
          currentUtterance = utter;
          window.speechSynthesis.speak(utter);
        }} else {{
          segIdx++; setTimeout(speakNext, 3000);
        }}
      }}
      speakNext();
    }}

    // 6. CÁC WIDGET TƯƠNG TÁC
    function burst(x, y, n, em) {{
      for (let i = 0; i < n; i++) {{
        const s = document.createElement('span'); s.className = 'spark';
        s.textContent = em[Math.floor(Math.random() * em.length)];
        const a = Math.random() * 6.28, d = 60 + Math.random() * 130;
        s.style.cssText = 'left:' + x + 'px;top:' + y + 'px;--dx:' + Math.cos(a) * d + 'px;--dy:' + Math.sin(a) * d + 'px';
        document.body.appendChild(s);
        setTimeout(() => s.remove(), 1100);
      }}
    }}
    function confetti() {{
      for (let k = 0; k < 5; k++) setTimeout(() => burst(innerWidth * (.15 + .17 * k), innerHeight * .35, 10, ['🎉', '🏆', '🏃‍♂️', '✨', '⭐']), k * 150);
      sfxChime();
    }}
    document.addEventListener('click', e => {{
      if (e.target.closest && e.target.closest('.slide-inner') && !e.target.closest('input,select,textarea,button')) {{
        burst(e.clientX, e.clientY, 7, ['🏃‍♂️', '🔥', '✨', '⭐']);
      }}
    }});

    // BÁNH XE CUỘC ĐỜI
    const AXES = ['💪 Thể lực', '🏃 Vận động', '❤️ Bình an', '🤝 Kết nối', '📚 Học tập', '🤖 Ứng dụng AI'];
    const AXTIP = [
      "💪 THỂ LỰC: Dinh dưỡng sạch, giấc ngủ sâu. Giống Glenn Cunningham kiên trì hồi sinh từng tế bào cơ bắp.",
      "🏃 VẬN ĐỘNG: Chạy bộ, bơi biển 30 phút mỗi ngày giúp bơm máu lên não và xua tan căng thẳng.",
      "❤️ BÌNH AN: Thở sâu 5 phút, giữ tâm thế vững vàng trước mọi biến động của thời cuộc.",
      "🤝 KẾT NỐI: Mở rộng mạng lưới với những người bạn tích cực, luôn sẵn lòng cho đi và hỗ trợ đồng đội.",
      "📚 HỌC TẬP: Đọc sách, cập nhật tri thức mới mỗi ngày. Não bộ càng luyện càng trẻ hóa!",
      "🤖 ỨNG DỤNG AI: Gắn đôi chân thần tốc AI vào chuyên môn của bạn để bứt phá năng suất gấp 10 lần."
    ];
    let radarCur = [5,5,5,5,5,5], radarTgt = [5,5,5,5,5,5], selAx = -1;
    function secPath(k, r) {{
      const a0 = (-120 + 60 * k) * Math.PI / 180, a1 = (-60 + 60 * k) * Math.PI / 180;
      return 'M200 200 L' + (200 + r * Math.cos(a0)).toFixed(1) + ' ' + (200 + r * Math.sin(a0)).toFixed(1) + ' A' + r.toFixed(1) + ' ' + r.toFixed(1) + ' 0 0 1 ' + (200 + r * Math.cos(a1)).toFixed(1) + ' ' + (200 + r * Math.sin(a1)).toFixed(1) + ' Z';
    }}
    function renderWheel() {{
      radarCur.forEach((x, k) => {{
        const r = Math.max(10, 152 * x / 10), m = (-90 + 60 * k) * Math.PI / 180;
        const p = document.getElementById('sec' + k); if (p) {{ p.setAttribute('d', secPath(k, r)); p.setAttribute('stroke-width', k === selAx ? 7 : 3); }}
        const t = document.getElementById('val' + k); if (t) {{ t.setAttribute('x', (200 + r * 0.62 * Math.cos(m)).toFixed(1)); t.setAttribute('y', (208 + r * 0.62 * Math.sin(m)).toFixed(1)); t.textContent = Math.round(x); }}
      }});
    }}
    function drawRadar() {{
      const v = AXES.map((_, i) => +document.getElementById('rv' + i).value);
      radarCur = v; renderWheel();
      const mx = Math.max(...v), mn = Math.min(...v), avg = v.reduce((a, b) => a + b, 0) / 6;
      const round = Math.round(100 * (1 - (mx - mn) / 9));
      const col = 'hsl(' + Math.round(round * 1.2) + ',85%,55%)';
      const n = document.getElementById('roundNum'); if (n) {{ n.textContent = round + '%'; n.style.color = col; }}
      const bar = document.getElementById('roundBar'); if (bar) {{ bar.style.width = round + '%'; bar.style.background = col; }}
      const hub = document.getElementById('hubT'); if (hub) hub.textContent = avg.toFixed(1);
      const lo = v.indexOf(mn);
      const msg = round >= 85 ? '🏆 Bánh xe TO và TRÒN ĐỀU – sẵn sàng bứt phá cùng đôi chân AI!' : '⚠️ Hãy nâng múi thấp nhất: ' + AXES[lo];
      const rm = document.getElementById('radarMsg'); if (rm) rm.textContent = msg;
    }}
    function selectAxis(k) {{
      selAx = k; document.getElementById('axTip').innerHTML = AXTIP[k]; renderWheel(); sfxChime();
    }}
    function rollWheel() {{
      const b = document.getElementById('wheelBox');
      const on = !b.classList.contains('rolling');
      b.classList.toggle('rolling', on);
      document.getElementById('wheelG').classList.toggle('rolling', on);
      document.getElementById('btnRoll').textContent = on ? '⏸️ Dừng bánh xe' : '🛞 Cho bánh xe lăn';
      sfxWhoosh();
    }}
    function balanceWheel() {{
      const s = AXES.map((_, i) => document.getElementById('rv' + i));
      const lo = s.reduce((m, x, i) => (+x.value < +s[m].value ? i : m), 0);
      if (+s[lo].value < 10) s[lo].value = +s[lo].value + 1;
      selectAxis(lo); drawRadar();
    }}
    function randomWheel() {{
      AXES.forEach((_, i) => document.getElementById('rv' + i).value = 1 + Math.floor(Math.random() * 10));
      drawRadar(); sfxChime();
    }}
    function resetWheel() {{
      AXES.forEach((_, i) => document.getElementById('rv' + i).value = 5);
      selAx = -1; document.getElementById('axTip').textContent = '👆 Bấm vào một múi bánh xe để xem lời khuyên';
      drawRadar();
    }}

    // PROMPT BUILDER
    const pickSel = {{}};
    function pickChip(b, c) {{
      b.parentElement.querySelectorAll('button').forEach(x => x.classList.remove('on'));
      b.classList.add('on'); pickSel[c] = b.textContent; buildPrompt(); sfxChime();
    }}
    function buildPrompt() {{
      const s = pickSel;
      const el = document.getElementById('promptOut');
      if (el) el.textContent = 'Hãy đóng vai ' + (s.r || '[vai trò]') + '. Việc cần làm: ' + (s.t || '[công việc]') + '. Bối cảnh của tôi: ' + (s.c || '[bối cảnh]') + '. Hãy trả lời dạng ' + (s.f || '[định dạng]') + '.';
    }}
    function copyPrompt() {{
      const txt = document.getElementById('promptOut').textContent;
      if (navigator.clipboard) navigator.clipboard.writeText(txt);
      showVoiceToast('📋 Đã sao chép lệnh vàng vào bộ nhớ tạm!');
    }}
    function flipCard(c) {{ c.classList.toggle('open'); sfxChime(); }}

    // BEFORE / AFTER SWITCHER
    let baNow = 0;
    function toggleAI() {{
      const on = document.getElementById('aiSw').checked;
      document.getElementById('baBox').classList.toggle('ai-on', on);
      sfxChime();
      const to = on ? 105 : 0, from = baNow, t0 = performance.now(), el = document.getElementById('baSave');
      (function f(t) {{
        const k = Math.min(1, (t - t0) / 900);
        baNow = Math.round(from + (to - from) * k);
        el.textContent = baNow;
        if (k < 1) requestAnimationFrame(f);
      }})(t0);
      if (on) burst(innerWidth / 2, innerHeight / 2, 12, ['⚡', '🤖', '⏱️']);
    }}

    // THÓI QUEN
    function checkProgress() {{
      const a = [...document.querySelectorAll('.habit input')];
      const n = a.filter(x => x.checked).length;
      const p = Math.round(n / a.length * 100);
      document.getElementById('habitBar').style.width = p + '%';
      document.getElementById('habitTxt').textContent = p === 100 ? '🎉 Tuyệt vời! Bạn đã hoàn thành trọn vẹn 6 thói quen Thân–Tâm–Trí!' : n + '/' + a.length + ' thói quen hôm nay';
      if (p === 100) confetti();
    }}

    // TRẮC NGHIỆM 3 CÂU
    const QZ = [
      {{ q: 'Năm 7 tuổi bác sĩ bảo Glenn Cunningham sẽ tàn phế. Phản ứng của ông là gì?', o: ['Chấp nhận số phận nằm yên', 'Quyết tâm: "Con không chỉ đi mà con sẽ CHẠY"', 'Trông chờ vào phép màu'], a: 1, w: 'Ý chí sắt đá và niềm tin tuyệt đối là ngọn hải đăng vượt nghịch cảnh.' }},
      {{ q: 'Vì sao Glenn Cunningham phát hiện ra mình nên CHẠY thay vì đi bộ?', o: ['Vì đi bộ đau buốt hơn chạy', 'Vì có người ép buộc', 'Vì thích khoe khoang'], a: 0, w: 'Chạy giúp thời gian chân chạm đất ngắn lại, bớt đau và bứt phá nhanh hơn!' }},
      {{ q: 'Trong kỷ nguyên AI, vai trò lớn nhất của người trung niên Việt Nam là gì?', o: ['Tự ti bỏ cuộc vì già', 'Kiến trúc sư & Chủ công trình kết hợp với AI thần tốc', 'Khoán trắng mọi việc cho máy tính'], a: 1, w: 'Kinh nghiệm sống quý giá của bạn chính là linh hồn dẫn dắt tốc độ của AI!' }}
    ];
    let qi = 0, qs = 0;
    function renderQ() {{
      const q = QZ[qi];
      document.getElementById('qzQ').textContent = 'Câu ' + (qi + 1) + '/3: ' + q.q;
      document.getElementById('qzO').innerHTML = q.o.map((t, k) => '<button class="qopt" onclick="answerQ(' + k + ')">' + t + '</button>').join('');
      document.getElementById('qzF').textContent = '';
      document.getElementById('qzN').textContent = 'Câu tiếp ➡️';
    }}
    function answerQ(k) {{
      const q = QZ[qi], bs = document.querySelectorAll('.qopt');
      if (bs[0].disabled) return;
      bs.forEach((b, j) => {{
        b.disabled = true;
        if (j === q.a) b.classList.add('ok');
        else if (j === k) b.classList.add('bad');
      }});
      if (k === q.a) {{ qs++; sfxChime(); burst(innerWidth / 2, innerHeight / 2, 12, ['🎉', '🏆', '✨']); }}
      document.getElementById('qzF').textContent = (k === q.a ? '✅ Rất chính xác! ' : '💡 Bài học: ') + q.w;
    }}
    function nextQ() {{
      if (qi >= 2 && document.querySelectorAll('.qopt').length === 0) {{ qi = 0; qs = 0; renderQ(); return; }}
      if (qi >= 2) {{
        document.getElementById('qzQ').textContent = '🏆 Bạn đã trả lời đúng ' + qs + '/3 câu!';
        document.getElementById('qzO').innerHTML = '';
        document.getElementById('qzF').textContent = qs === 3 ? '🎉 Xuất sắc! Bạn đã thấm nhuần tinh thần Cunningham.' : '🌱 Rất tốt! Hãy tiếp tục rèn luyện mỗi ngày.';
        document.getElementById('qzN').textContent = '🔄 Chơi lại';
        if (qs === 3) confetti();
        qi = 2; return;
      }}
      qi++; renderQ();
    }}

    // VÒNG QUAY HÀNH ĐỘNG
    const WHL = [
      "🏃 Chạy bộ hoặc đi bộ nhanh 20 phút ngay chiều nay",
      "🤖 Mở ChatGPT hỏi 1 câu lệnh hỗ trợ công việc của bạn",
      "🤝 Gọi điện nói lời cảm ơn và động viên 1 người thân",
      "📚 Đọc 10 trang sách hoặc học 1 điều mới trong 15 phút",
      "🧘 5 phút thở sâu tĩnh tâm và lắng nghe chính mình",
      "🙏 Viết ra sổ 3 điều bạn biết ơn nhất trong ngày hôm nay"
    ];
    let whAng = 0;
    function spinWheel() {{
      whAng += 1440 + Math.floor(Math.random() * 360);
      document.getElementById('wheel').style.transform = 'rotate(' + whAng + 'deg)';
      document.getElementById('whRes').textContent = '🎡 Đang quay thử thách...';
      setTimeout(() => {{
        const k = Math.floor(((360 - whAng % 360) % 360) / 60);
        document.getElementById('whRes').textContent = '🎯 Thử thách hôm nay của bạn: ' + WHL[k];
        confetti();
      }}, 4200);
    }}

    // KÝ CAM KẾT
    function makePledge() {{
      const n = document.getElementById('pledgeName').value.trim() || 'Tôi';
      const f = document.getElementById('pledgeFocus').value;
      const o = document.getElementById('pledgeOut');
      o.innerHTML = '🏃‍♂️ <b>' + n.replace(/</g, '&lt;') + '</b> cam kết: Học tập tinh thần Bác Sĩ Cunningham, mỗi ngày dành 30 phút rèn luyện <b>' + f + '</b> và làm chủ trí tuệ AI. Tôi là Kiến trúc sư và Chủ công trình của cuộc đời mình!';
      o.classList.add('show');
      confetti();
    }}

    function animateCounters() {{
      document.querySelectorAll('.slide.active-slide .count-up').forEach(el => {{
        if (el.dataset.done) return; el.dataset.done = 1;
        const to = +el.dataset.to, suf = el.dataset.suf || '', t0 = performance.now();
        (function f(t) {{
          const k = Math.min(1, (t - t0) / 1400);
          el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))) + suf;
          if (k < 1) requestAnimationFrame(f);
        }})(t0);
      }});
    }}

    function openQrFullscreenModal() {{
      sfxChime();
      document.getElementById('qrFullscreenModal').classList.add('open');
      launchCelebration();
    }}
    function closeQrFullscreenModal() {{ document.getElementById('qrFullscreenModal').classList.remove('open'); }}
    function openVoiceModal() {{ document.getElementById('voiceModal').classList.add('open'); }}
    function closeVoiceModal() {{ document.getElementById('voiceModal').classList.remove('open'); }}
    function openGitHubModal() {{ document.getElementById('githubModal').classList.add('open'); }}
    function closeGitHubModal() {{ document.getElementById('githubModal').classList.remove('open'); }}

    // KHỞI CHẠY HỆ THỐNG
    initDots();
    loadHiddenSlides();
    initPhotoSwap();
    lockAllVietnameseOrphans();
    drawRadar();
    buildPrompt();
    renderQ();
    updateSlidePosition();
  </script>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Đã tạo thành công bài giảng tại: {output_file}")
