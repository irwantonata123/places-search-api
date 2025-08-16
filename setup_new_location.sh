#!/bin/bash
# Quick Setup Script untuk PlacesApi di Lokasi Baru

echo "🚀 Setting up PlacesApi in new location..."

# Check if we're in correct directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Make sure you're in PlacesApi directory"
    exit 1
fi

echo "📁 Current directory: $(pwd)"

# Create new virtual environment
echo "🔧 Creating new virtual environment..."
python -m venv .venv-new

# Activate and install dependencies
echo "📦 Installing dependencies..."
.venv-new/Scripts/pip install -r requirements.txt

# Test installation
echo "🧪 Testing installation..."
.venv-new/Scripts/python -c "import fastapi, uvicorn, requests; print('✅ Dependencies installed successfully!')"

# Check .env file
if [ -f ".env" ]; then
    echo "✅ .env file found"
else
    echo "⚠️  Warning: .env file not found. Create one with GOOGLE_MAPS_API_KEY"
fi

echo ""
echo "🎯 Setup complete! To run the server:"
echo "   .venv-new/Scripts/python -m uvicorn main:app --reload --port 9022"
echo ""
echo "🔗 Test API:"
echo "   curl \"http://127.0.0.1:9023/places?query=test\""
