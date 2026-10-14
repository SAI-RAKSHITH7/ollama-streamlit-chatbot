@echo off
title Local AI Chatbot (Ollama + Streamlit)
echo ========================================================
echo   Starting Ollama and Streamlit Local AI Chatbot...
echo ========================================================

:: Check if Ollama is running, if not start it
tasklist /FI "IMAGENAME eq ollama.exe" 2>NUL | find /I /N "ollama.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo Starting Ollama in background...
    start "" "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" serve
    timeout /t 3 /nobreak >nul
) else (
    echo Ollama is already running.
)

:: Run Streamlit app
echo Opening Streamlit in your default browser...
python -m streamlit run app.py
pause
