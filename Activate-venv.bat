@echo off
chcp 65001 > NUL
call %~dp0venv\Scripts\activate.bat
cmd /k
