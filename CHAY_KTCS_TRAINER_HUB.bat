@echo off
cd /d "%~dp0"
chcp 65001 >nul
title KTCSxAI TRAINER HUB - THẦY TUẤN TỬ TẾ
echo =====================================================================
echo    KHỞI CHẠY HỆ THỐNG ĐÀO TẠO TỰ HÀNH BÀI GIẢNG 4D (KTCSxAI)
echo    Chương trình Kiến Tạo Cuộc Sống xAI • Nguyễn Anh Tuấn
echo =====================================================================
"C:\Program Files\Python312\python.exe" "%~dp0KTCS_Trainer_Hub.py"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [LỖI] Có lỗi khi chạy ứng dụng. Nhấn phím bất kỳ để thoát...
    pause >nul
)
