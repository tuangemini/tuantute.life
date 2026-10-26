@echo off
chcp 65001 > nul
title ĐĂNG BÀI ĐÀO TẠO NOTEBOOKLM LÊN TUANTUTE.LIFE
cls
echo =====================================================================
echo    🌟 TUẤN TỬ TẾ - TỰ ĐỘNG ĐĂNG BÀI NOTEBOOKLM LÊN GITHUB PAGES 🌟
echo =====================================================================
echo.
cd /d "%~dp0"
python publish_notebooklm_post.py
echo.
echo =====================================================================
pause
