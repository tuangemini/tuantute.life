@echo off
cd /d "%~dp0"
chcp 65001 > nul
title KTCSxAI 4D CREATOR STUDIO - THAY TUAN TU TE
echo =====================================================================
echo    KHOI DONG KTCS 4D CREATOR STUDIO (KIEN TAO BAI GIANG TU HANH)
echo    Giang vien: Nguyen Anh Tuan (Tuan Tu Te) • Chuong trinh KTCSxAI
echo =====================================================================
echo.
echo [*] Dang khoi chay Studio Web App tai http://localhost:7890...
echo [*] Trinh duyet Chrome se tu dong mo len trong giay lat...
echo.
"C:\Program Files\Python312\python.exe" "%~dp0KTCS_4D_Creator_Studio.py"
pause
