@echo off
echo Starting SSD dev server on http://localhost:8080
echo Phone (USB): adb reverse tcp:8080 tcp:8080  then open http://localhost:8080 in Chrome
cd /d "%~dp0www"
py -m http.server 8080
