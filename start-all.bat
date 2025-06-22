@echo off
REM This script will start the Python backend and React frontend in two separate windows

REM Start the Python backend
start cmd /k "cd /d %~dp0 && python server.py"

REM Start the React frontend
start cmd /k "cd /d %~dp0my-app && npm run dev"
