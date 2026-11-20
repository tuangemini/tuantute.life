@echo off
chcp 65001 >nul
cd /d "%~dp0"
title KTCSxAI - KHAI PHÓNG NGƯỜI THẦY BÊN TRONG (PORT 7890)
start "" "http://localhost:7890/ktcs-khai-phong-nguoi-thay-22-trang-4d.html"
netstat -ano | findstr :7890 >nul
if %errorlevel% equ 0 (
    timeout /t 2 >nul
    exit /b 0
)
python "%~dp0server_7890.py"
pause
