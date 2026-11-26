@echo off
cd /d "%~dp0"
python apps\viewer\server.py
if errorlevel 1 pause
