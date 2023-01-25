@echo off
set SELF_PATH=%~dp0
cd /d %SELF_PATH%

set pyver=""

py --version 2> nul
if not %errorlevel% == 0 (
  echo ƒGƒ‰[
) else (
  for /f "usebackq delims=" %%A in (`py --version`) do set pyver=%%A
  REM echo %pyver%
)

cd test 2> nul

if %errorlevel% neq 0 (
  echo ‚¨‚Í‚æ‚¤¢ŠE
)

pause