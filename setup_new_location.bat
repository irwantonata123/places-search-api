@echo off
REM Quick Setup Script untuk PlacesApi di Lokasi Baru (Windows)

echo 🚀 Setting up PlacesApi in new location...

REM Check if we're in correct directory
if not exist "main.py" (
    echo ❌ Error: main.py not found. Make sure you're in PlacesApi directory
    pause
    exit /b 1
)

echo 📁 Current directory: %cd%

REM Create new virtual environment
echo 🔧 Creating new virtual environment...
python -m venv .venv-new

REM Install dependencies
echo 📦 Installing dependencies...
.venv-new\Scripts\pip install -r requirements.txt

REM Test installation
echo 🧪 Testing installation...
.venv-new\Scripts\python -c "import fastapi, uvicorn, requests; print('✅ Dependencies installed successfully!')"

REM Check .env file
if exist ".env" (
    echo ✅ .env file found
) else (
    echo ⚠️  Warning: .env file not found. Create one with GOOGLE_MAPS_API_KEY
)

echo.
echo 🎯 Setup complete! To run the server:
echo    .venv-new\Scripts\python -m uvicorn main:app --reload --port 9022
echo.
echo 🔗 Test API:
echo    curl "http://127.0.0.1:9023/places?query=test"
pause
