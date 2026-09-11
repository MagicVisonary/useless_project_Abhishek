@echo off
title Mango Pari - Game Server
echo Starting Mango Pari Multiplayer Server...
cd /d "%~dp0"
py server.py || python server.py
pause
