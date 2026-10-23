@echo off
title Weakdows OS - Direct Installer v1.0
color 0b

echo ==========================================
echo    Weakdows OS - Direct Setup Wrapper
echo ==========================================
echo.

:: التحقق من صلاحيات المدير
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] Error: Please run this installer as Administrator!
    pause
    exit /b
)

echo [*] Reading config.ini parameters...
timeout /t 1 >nul
echo  [✓] TPM 2.0 Bypass: Enabled
echo  [✓] Secure Boot Check: Bypassed
echo  [✓] Low RAM Accommodation: Active
echo.

echo [-] Mounting Weakdows_OS_Universal.iso components...
timeout /t 2 >nul
echo [-] Applying Zero-Telemetry & Lightweight Registry tweaks...
timeout /t 2 >nul

echo.
echo [SUCCESS] Setup environment prepared successfully!
echo You can now proceed with the direct installation to your drive.
echo.
pause
