import os
import time
import re
import json
import traceback
import sys
import unicodedata
import threading
import tempfile

# FIX TRIỆT ĐỂ LỖI WIN 11: Chuyển thư mục cache comtypes sang %TEMP% để tránh [Errno 13] Permission denied trong Program Files
_cache_dir = os.path.join(tempfile.gettempdir(), "comtypes_gen")
os.makedirs(_cache_dir, exist_ok=True)
sys.path.insert(0, _cache_dir)
os.environ["COMTYPES_PATH"] = _cache_dir
try:
    import comtypes
    import comtypes.client
    comtypes.client.gen_dir = _cache_dir
    import comtypes.gen
    if _cache_dir not in comtypes.gen.__path__:
        comtypes.gen.__path__.insert(0, _cache_dir)
except Exception:
    pass

try:
    import pyperclip
    import pyautogui
    import keyboard
    try:
        import uiautomation as auto
    except Exception:
        auto = None
except ImportError as e:
    print("❌ LỖI: BẠN CHƯA CÀI ĐẶT ĐỦ THƯ VIỆN!")
    print("👉 Hãy mở CMD và gõ lệnh sau rồi Enter:")
    print("pip install pyautogui pyperclip keyboard uiautomation")
    input("\nNhấn Enter để thoát...")
    sys.exit()

# Chuột được trả hoàn toàn cho người dùng -> tắt cơ chế "góc màn hình" của pyautogui
# (nếu không, rê chuột vào góc sẽ làm tool văng lỗi)
pyautogui.FAILSAFE = False

# Đặt False trên Windows 11 để người dùng tự do bấm SPACE là dán ngay, không bị chặn bởi uiautomation
REQUIRE_INPUT_FOCUS = False

# Sau khi bấm Enter gửi lệnh, chờ tối đa bao lâu (giây) để ô nhập lấy lại focus
FOCUS_GRACE_SECONDS = 3.0

# Thời gian nghỉ giữa 2 câu lệnh (giây)
GAP_BETWEEN_PROMPTS = 1.5


def clean_vietnamese(text):
    text = text.replace('Đ', 'D').replace('đ', 'd')
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = re.sub(r'[^A-Z0-9]', '_', text.upper())
    text = re.sub(r'_+', '_', text).strip('_')
    return text

def slugify_name(text):
    """Chuyển tiếng Việt có dấu -> chữ thường không dấu, nối bằng dấu gạch ngang"""
    text = text.replace('Đ', 'D').replace('đ', 'd')
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return text

def get_png_label(item, idx):
    """Giữ NGUYÊN tên ảnh gốc trong file dữ liệu (VD: 01_nguoi-xua-dan-giu-loc.png).
    Nếu file không có sẵn tên thì tự tạo theo cùng cấu trúc từ title."""
    out_name = item.get('out') or item.get('ten_file') or item.get('filename')
    if out_name:
        name = os.path.basename(str(out_name).strip())
        name = re.sub(r'\.(png|mp4|jpg|jpeg)$', '', name, flags=re.IGNORECASE)
        return f"{name}.png"
    title = item.get('title')
    if title:
        title_str = " ".join(title) if isinstance(title, list) else str(title)
        slug = slugify_name(title_str)
        if slug:
            return f"{idx:02d}_{slug}.png"
    return None

def build_prompt(item, idx):
    prompt_text = item.get('video_prompt') or item.get('prompt')
    if not prompt_text:
        return None
    label = get_png_label(item, idx)
    return f"[{label}] {prompt_text}" if label else prompt_text

def scan_and_load_prompts(target_files):
    prompts_dict = {}
    current_idx = 1
    found_files = []

    for filename in target_files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            file_has_prompts = False
            match = re.search(r'\[\s*\{[\s\S]*\}\s*\]', content)

            if match:
                try:
                    data = json.loads(match.group(0))
                    if isinstance(data, list):
                        for item in data:
                            final_prompt = build_prompt(item, current_idx)
                            if final_prompt:
                                prompts_dict[current_idx] = final_prompt
                                current_idx += 1
                                file_has_prompts = True
                except json.JSONDecodeError:
                    pass

            if not file_has_prompts:
                objects = re.findall(r'\{[^{}]*(?:"video_prompt"|"prompt")[^{}]*\}', content)
                for obj_str in objects:
                    try:
                        item = json.loads(obj_str)
                        final_prompt = build_prompt(item, current_idx)
                        if final_prompt:
                            prompts_dict[current_idx] = final_prompt
                            current_idx += 1
                            file_has_prompts = True
                    except:
                        pass

            if file_has_prompts:
                found_files.append(filename)

        except Exception as e:
            print(f"⚠️ Bỏ qua file '{filename}' do lỗi đọc: {e}")

    return prompts_dict, found_files

def get_files_to_run():
    current_script = os.path.basename(__file__)
    valid_exts = ('.html', '.txt', '.json', '.md', '.js')
    all_files = [f for f in os.listdir('.') if f.lower().endswith(valid_exts) and f != current_script]

    if not all_files:
        return []
    if len(all_files) == 1:
        return all_files

    print("\n" + "="*55)
    print("📂 PHÁT HIỆN NHIỀU FILE DỮ LIỆU. BẠN MUỐN CHẠY FILE NÀO?")
    for i, f in enumerate(all_files, 1):
        print(f"  {i}. {f}")

    option_all = len(all_files) + 1
    print(f"  {option_all}. 🌟 Gộp TẤT CẢ các file lại thành 1 danh sách")

    while True:
        try:
            choice = input(f"\n👉 Mời chọn số (Từ 1 -> {option_all}): ").strip()
            choice_idx = int(choice)
            if 1 <= choice_idx <= len(all_files):
                print(f"✅ Đã chọn: {all_files[choice_idx-1]}")
                return [all_files[choice_idx-1]]
            elif choice_idx == option_all:
                print("✅ Đã chọn: Gộp toàn bộ file.")
                return all_files
            else:
                print("❌ Lỗi: Số chọn không có trong danh sách.")
        except ValueError:
            print("❌ Lỗi: Vui lòng chỉ nhập số.")


# ----------------------------------------------------------------------
# KIỂM TRA "ĐANG Ở Ô NHẬP LIỆU" (dùng Windows UI Automation)
# ----------------------------------------------------------------------
def describe_focus():
    """Mô tả ngắn phần tử đang giữ focus (để báo cho người dùng khi bị từ chối)."""
    try:
        if not auto:
            return "Chrome / Flow (Chế độ tự do)"
        c = auto.GetFocusedControl()
        if c:
            name = (c.Name or "").strip()[:40]
            return f"{c.ControlTypeName}" + (f" '{name}'" if name else "")
        top = auto.GetForegroundControl()
        if top:
            return f"Cửa sổ '{top.Name[:30]}'"
        return "không xác định"
    except Exception:
        return "không xác định"

def is_input_focused():
    """True nếu phần tử đang giữ focus là ô nhập chữ hoặc đang ở trong trình duyệt Chrome / Google Flow."""
    if not REQUIRE_INPUT_FOCUS:
        return True
    try:
        c = auto.GetFocusedControl()
        top = auto.GetForegroundControl()

        # Nhận diện nếu đang ở trong cửa sổ trình duyệt (Chrome, Edge, Brave...)
        top_name = (top.Name or "").lower() if top else ""
        top_class = (top.ClassName or "").lower() if top else ""
        is_browser = any(b in top_class or b in top_name for b in ["chrome", "edge", "brave", "flow", "google"])

        if not c:
            # Nếu không bắt được element con nhưng đang active cửa sổ Chrome -> Cho phép dán!
            return is_browser

        # 1. Ô nhập chuẩn Windows (textbox, textarea, input...)
        if c.ControlType == auto.ControlType.EditControl:
            try:
                vp = c.GetPattern(auto.PatternId.ValuePattern)
                if vp is not None and vp.IsReadOnly:
                    return False
            except Exception:
                pass
            return True

        # 2. Ô nhập dạng rich-text / contenteditable: nhận diện qua role TEXT (0x2A), không READONLY (0x40)
        try:
            lp = c.GetLegacyIAccessiblePattern()
            if lp is not None and lp.Role == 0x2A and not (lp.State & 0x40):
                return True
        except Exception:
            pass

        # 3. Phù hợp tuyệt đối với Chrome / Google Flow trên Win 11:
        # Trong Chrome, các ô nhập thường là DocumentControl, PaneControl, GroupControl
        c_class = (c.ClassName or "").lower()
        if is_browser or "chrome" in c_class or c.ControlType in (auto.ControlType.PaneControl, auto.ControlType.DocumentControl, auto.ControlType.GroupControl):
            return True

        return False
    except Exception:
        # Nếu có lỗi khi kiểm tra focus, mặc định cho phép dán theo lệnh SPACE của người dùng
        return True

def wait_until_input_focused(timeout):
    """Chờ tối đa `timeout` giây cho đến khi con trỏ nằm trong ô nhập. Trả về True/False."""
    end = time.time() + timeout
    while True:
        if is_input_focused():
            return True
        if time.time() >= end:
            return False
        time.sleep(0.25)


# ----------------------------------------------------------------------
# PHÍM SPACE / ESC
# ----------------------------------------------------------------------
def wait_for_space_or_esc():
    """Chờ SPACE (bắt đầu/tiếp tục) hoặc ESC (hủy đợt chạy).
    Chỉ chặn đúng phím Space trong lúc chờ (để dấu cách không lọt vào ô nhập);
    các phím khác và chuột hoạt động bình thường. Bấm xong là gỡ chặn ngay."""
    done = threading.Event()
    result = {}

    def on_space():
        result['key'] = 'space'
        done.set()

    def on_esc():
        result['key'] = 'esc'
        done.set()

    h_space = keyboard.add_hotkey('space', on_space, suppress=True)
    h_esc = keyboard.add_hotkey('esc', on_esc, suppress=True)
    try:
        while not done.wait(0.1):
            pass
    finally:
        for h in (h_space, h_esc):
            try:
                keyboard.remove_hotkey(h)
            except Exception:
                pass
    return result.get('key', 'esc')

def parse_range_input(range_input, total_prompts):
    """Enter (để trống) = chạy từ 1 đến hết. Trả về (danh_sách_hợp_lệ, thông_báo_lỗi)."""
    if range_input == '':
        return list(range(1, total_prompts + 1)), None

    target_indices = set()
    try:
        parts = range_input.split(',')
        for part in parts:
            part = part.strip()
            if not part:
                continue
            if '-' in part:
                sub_parts = part.split('-')
                if len(sub_parts) == 2:
                    s = int(sub_parts[0].strip())
                    e = int(sub_parts[1].strip())
                    target_indices.update(range(s, e + 1))
            else:
                target_indices.add(int(part))
    except ValueError:
        return [], "❌ Lỗi: Vui lòng nhập đúng định dạng (VD: 5, 8, 12 hoặc 2-12)."

    valid = [i for i in sorted(target_indices) if 1 <= i <= total_prompts]
    if not valid:
        return [], "❌ Lỗi: Các số bạn nhập không hợp lệ hoặc vượt quá giới hạn."
    return valid, None


def run_batch(valid_indices, prompts_dict):
    """Chạy một đợt. Trả về số câu lệnh đã đẩy thành công."""
    success_count = 0
    idx_pointer = 0

    while idx_pointer < len(valid_indices):
        current_idx = valid_indices[idx_pointer]

        print(f"\n⏳ Đang chờ... Bấm vào ô nhập lệnh của Google Flow (chuột tự do), rồi BẤM SPACE để nạp câu số {current_idx}.")
        print("   (Bấm ESC lúc này để HỦY cả đợt chạy.)")
        pressed = wait_for_space_or_esc()

        if pressed == 'esc':
            print("⏹ ĐÃ HỦY ĐỢT CHẠY NÀY.")
            break

        # Bắt buộc con trỏ đang nằm trong ô nhập mới được chạy
        if not is_input_focused():
            print(f"🚫 CHƯA DÁN: con trỏ đang ở '{describe_focus()}', không phải ô nhập lệnh.")
            print("   👉 Hãy click vào ô nhập lệnh của Flow rồi bấm SPACE lại.")
            continue

        print("▶ Bắt đầu dán liên tục. Chuột và bàn phím là của bạn - bấm ESC để TẠM DỪNG.")

        paused = threading.Event()
        h_esc = keyboard.add_hotkey('esc', paused.set, suppress=True)

        try:
            while idx_pointer < len(valid_indices):
                inner_idx = valid_indices[idx_pointer]

                if paused.is_set():
                    break

                # Chỉ dán khi còn đang ở ô nhập (cho ô nhập một khoảng ngắn để lấy lại focus sau khi gửi)
                if not wait_until_input_focused(FOCUS_GRACE_SECONDS):
                    print(f"\n🚫 TỰ ĐỘNG DỪNG: con trỏ không còn ở ô nhập lệnh (đang ở '{describe_focus()}').")
                    print(f"   Chưa dán câu {inner_idx}. Hãy click lại vào ô nhập rồi bấm SPACE để tiếp tục.")
                    break

                if paused.is_set():
                    break

                print(f"▶ Đang xử lý câu lệnh {inner_idx}...")
                pyperclip.copy(prompts_dict[inner_idx])
                time.sleep(0.1)

                # Kiểm tra lần cuối ngay trước khi dán (người dùng có thể vừa click đi nơi khác)
                if not is_input_focused() or paused.is_set():
                    print(f"⏸ Chưa dán câu {inner_idx} vì bạn vừa rời khỏi ô nhập hoặc bấm ESC.")
                    break

                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.5)
                pyautogui.press('enter')

                success_count += 1
                idx_pointer += 1

                if idx_pointer >= len(valid_indices):
                    break

                # Nghỉ giữa các câu, vẫn lắng nghe ESC
                end_sleep = time.time() + GAP_BETWEEN_PROMPTS
                while time.time() < end_sleep and not paused.is_set():
                    time.sleep(0.05)

            if paused.is_set() and idx_pointer < len(valid_indices):
                print("\n⏸ ĐÃ TẠM DỪNG do bạn bấm ESC!")
                print(f"   Câu tiếp theo sẽ là câu số {valid_indices[idx_pointer]}.")
        finally:
            try:
                keyboard.remove_hotkey(h_esc)
            except Exception:
                pass

    return success_count


def main():
    print("\n" + "="*55)
    print("🤖 TOOL GOOGLE FLOW (V20 - CHUỘT TỰ DO, ESC TẠM DỪNG, CHỈ DÁN VÀO Ô NHẬP)")

    target_files = get_files_to_run()
    if not target_files:
        print("\n⚠️ Không tìm thấy file dữ liệu nào trong thư mục này!")
        input("\nNhấn Enter để thoát...")
        return

    print("🔍 Đang quét và bóc tách tiêu đề...")
    prompts_dict, found_files = scan_and_load_prompts(target_files)
    total_prompts = len(prompts_dict)

    if not prompts_dict:
        print("\n⚠️ File bạn chọn không chứa cấu trúc JSON câu lệnh nào hợp lệ!")
        input("\nNhấn Enter để thoát...")
        return

    print(f"\n✅ TỔNG CỘNG THU THẬP ĐƯỢC: {total_prompts} câu lệnh.")
    print("-" * 55)

    while True:
        print("\n👉 NHẬP SỐ THỨ TỰ CẦN LÀM (VD: 2-12, hoặc 5, 8, 12, 27):")
        print(f"👉 Chỉ bấm ENTER = chạy TẤT CẢ từ câu 1 đến câu {total_prompts}.")
        range_input = input("👉 Mời bạn nhập (Gõ '0' để chọn lại file hoặc thoát): ").strip()

        if range_input == '0':
            print("👋 Đã dừng lệnh hiện tại.")
            break

        valid_indices, err = parse_range_input(range_input, total_prompts)
        if err:
            print(err)
            continue

        if range_input == '':
            print(f"🎯 Mặc định: chạy TẤT CẢ {len(valid_indices)} câu lệnh (từ 1 đến {total_prompts}).")
        else:
            print(f"🎯 Đã chốt danh sách {len(valid_indices)} video cần làm: {valid_indices}")

        print("\n" + "="*55)
        print("🚀 ĐÃ SẴN SÀNG!")
        print("1. Mở Google Flow, TỰ click chuột vào ô nhập lệnh.")
        print("2. Bấm phím SPACE (Dấu cách) để bắt đầu dán.")
        print("3. Chuột và bàn phím luôn thuộc về bạn. Bấm ESC bất cứ lúc nào để TẠM DỪNG.")
        print("4. Tool chỉ dán khi con trỏ đang nằm trong ô nhập liệu.")
        print("="*55)

        success_count = run_batch(valid_indices, prompts_dict)

        print("\n" + "="*55)
        print(f"🎉 HOÀN TẤT ĐỢT CHẠY! Đã đẩy thành công {success_count} câu lệnh.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n❌ ĐÃ XẢY RA LỖI KHÔNG MONG MUỐN:")
        traceback.print_exc()
    finally:
        input("\nNhấn phím Enter để thoát chương trình...")
