@echo off
cd /d "%~dp0"
if "%~1"=="" (
    echo Drag one or more image files or folders onto this .bat file.
    pause
    exit /b
)
for %%F in (%*) do (
    echo Cleaning: %%~F
    python remove_metadata.py "%%~F" -o "%%~dpF%%~nF_clean%%~xF"
)
echo.
echo Done. Cleaned copies saved next to the originals with a _clean suffix.
pause
