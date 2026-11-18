@echo off
chcp 65001 >nul
cd /d "%~dp0"
title KTCSxAI - KHỞI ĐỘNG BÀI GIẢNG LOCAL SERVER (PORT 7890)

echo ===============================================================================
echo   KTCSxAI - ĐÀO TẠO GIẢNG VIÊN VƯỢT THỜI GIAN (4D CINEMA)
echo   KHỞI ĐỘNG MÔI TRƯỜNG WEB LOCAL (KHẮC PHỤC 100%% LỖI YOUTUBE 153)
echo ===============================================================================
echo.

:: Mở bài giảng trên trình duyệt Chrome / Trình duyệt mặc định
echo [1/2] Đang mở bài giảng trên trình duyệt: http://localhost:7890/ktcs-thong-diep-gia-tri-di-san-4d.html
start "" "http://localhost:7890/ktcs-thong-diep-gia-tri-di-san-4d.html"

:: Kiểm tra cổng 7890 đã chạy hay chưa
netstat -ano | findstr :7890 >nul
if %errorlevel% equ 0 (
    echo [2/2] Cổng 7890 đã đang hoạt động sẵn sàng!
    echo       Bạn có thể trình chiếu mượt mà không lo lỗi YouTube 153.
    timeout /t 3 >nul
    exit /b 0
)

echo [2/2] Đang khởi chạy máy chủ cục bộ Port 7890...
echo       Giữ cửa sổ này mở trong khi trình chiếu bài giảng.
python -m http.server 7890
pause
