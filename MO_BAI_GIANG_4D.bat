@echo off
cd /d "%~dp0"
chcp 65001 > nul
title MO BAI GIANG 4D CINEMA - THAY TUAN TU TE
echo ========================================================
echo   DANG KHOI DONG BAI GIANG 4D CINEMA 16:9 TRAP CHIEU
echo   Giang vien: Nguyen Anh Tuan (Tuan Tu Te) - KTCSxAI
echo ========================================================
echo.
start "" "chrome.exe" --start-fullscreen "file:///%~dp0ktcs-thong-diep-gia-tri-di-san-4d.html"
exit
