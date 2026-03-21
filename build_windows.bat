@echo off
echo ============================================
echo  RamaPlot - Build Script
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Install Python 3.10+ from python.org
    pause & exit /b 1
)

echo Detected:
python --version
echo.

echo [1/5] Installing dependencies...
python -m pip install --upgrade pip -q
python -m pip install flask biopython matplotlib numpy scipy requests reportlab pillow pyinstaller --upgrade -q

echo [2/5] Generating self-contained app...
python generate_embedded.py
if errorlevel 1 (
    echo ERROR: Failed to generate app_embedded.py
    pause & exit /b 1
)

echo [3/5] Stopping any running RamaPlot instance...
taskkill /f /im RamaPlot.exe >nul 2>&1
timeout /t 2 /nobreak >nul

echo [4/5] Cleaning previous build...
if exist build rmdir /s /q build
if exist dist  rmdir /s /q dist

echo [5/5] Building executable...
python -m PyInstaller ramaplot.spec --clean --noconfirm
if errorlevel 1 (
    echo.
    echo ERROR: Build failed. Common fixes:
    echo   1. Run as Administrator
    echo   2. Temporarily disable antivirus
    pause & exit /b 1
)

echo.
echo ============================================
echo  dist\RamaPlot.exe is ready!
echo  Double-click it to launch RamaPlot.
echo ============================================
echo.
pause
