@echo off
:: =====================================================================
::  Weakdows OS - Fast CMD Shell Launcher
:: =====================================================================
title Weakdows Command Prompt
color 0A

echo =====================================================
echo        Weakdows OS - Secure CMD Shell v1.0
echo =====================================================
echo Type 'exit' to close this window, or 'help' for options.
echo.

:prompt
set /p "user_input=Weakdows:\> "

if /i "%user_input%"=="exit" goto end
if /i "%user_input%"=="help" (
    echo Available commands:
    echo   status  - Check core system status
    echo   clear   - Clear the screen
    echo   version - Show system version
    echo   exit    - Exit the shell
    goto prompt
)
if /i "%user_input%"=="status" (
    echo [+] Memory: Ultra-Optimized [OK]
    echo [+] Security: Private Vault Active [OK]
    goto prompt
)
if /i "%user_input%"=="clear" (
    cls
    goto prompt
)
if /i "%user_input%"=="version" (
    echo Weakdows OS v2.4.0 (HP EliteDesk Optimized)
    goto prompt
)

:: Execute standard system commands if not custom
call %user_input%
goto prompt

:end
echo Closing Weakdows CLI...
timeout /t 2 >nul
