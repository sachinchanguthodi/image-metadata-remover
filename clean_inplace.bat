@echo off
cd /d "%~dp0"
if "%~1"=="" (
    echo Drag one or more image files or folders onto this .bat file.
    pause
    exit /b
)
for %%F in (%*) do (
    echo Cleaning: %%~F
    python remove_metadata.py "%%~F"
)
echo.
echo Done. Metadata removed in place.
pause
