@echo off
echo Stopping development environment...

:: 关闭Chrome开发实例
taskkill /F /IM chrome.exe

:: 关闭Flask服务器
taskkill /F /IM python.exe

echo Development environment stopped!
pause 