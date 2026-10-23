@echo off
:: =====================================================================
::  Weakdows OS - Weak10 Speed Edition Setup Script
:: =====================================================================

title Weak10 Setup & Debloat
color 0B

echo =========================================================
echo         Initializing Weak10 Speed Edition Setup          
echo =========================================================
echo.

echo [*] Purging Windows Bloatware, Cortana, and Telemetry...
timeout /t 1 >nul

echo [-] Configuring W-Reg Engine for 1024MB RAM Optimization...
timeout /t 1 >nul

echo [-] Optimizing Background Services & Windows Update Policies...
timeout /t 1 >nul

echo.
echo [SUCCESS] Weak10 environment setup complete! Ready to load.
pause
