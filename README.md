# 🗺️ Places Search API

A secure FastAPI-based service for searching places using Google Maps Places API, with Open WebUI integration.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![Google Maps](https://img.shields.io/badge/Google%20Maps-4285F4?style=for-the-badge&logo=google-maps)](https://developers.google.com/maps)

## ✨ Features

- 🔍 **Real-time place search** using Google Maps Places API
- 🔗 **Direct Google Maps links** for easy navigation
- 🌐 **Open WebUI integration** with clickable links
- 🔒 **Security-focused** with proper error handling
- 📱 **Multiple link formats** for maximum compatibility
- 🚀 **Fast setup** with automated scripts
- 📱 **Multiple link formats** for maximum compatibility
- ⚡ **Fast and lightweight** with automatic reloading

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Maps API Key ([Get one here](https://developers.google.com/maps/documentation/places/web-service/get-api-key))

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/places-search-api.git
cd places-search-api
```

### 2. Setup Environment

#### Using the automated setup script:

**Windows:**

```bash
setup_new_location.bat
```

**Linux/macOS:**

```bash
chmod +x setup_new_location.sh
./setup_new_location.sh
```

#### Manual setup:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_MAPS_API_KEY=your_api_key_here" > .env
```

### 3. Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

### 4. Run the Server

```bash
python -m uvicorn main:app --reload --port 9022
```

Server will start at: `http://127.0.0.1:9022`

## 📖 API Documentation

### Search Places Endpoint

**GET** `/places?query={search_term}`

**Parameters:**

- `query` (required): Search term for places

**Example Request:**

```bash
curl "http://127.0.0.1:9022/places?query=restaurant+jakarta"
```

**Example Response:**

```json
{
  "places": [
    {
      "name": "Restaurant Name",
      "address": "Full Address",
      "maps_link": "https://www.google.com/maps/search/?api=1&query=lat,lng",
      "embed_link": "https://maps.google.com/maps?q=lat,lng&z=15&output=embed"
    }
  ]
}
```

### API Documentation (Interactive)

Visit `http://127.0.0.1:9022/docs` for interactive API documentation with Swagger UI.

## 🛠️ Open WebUI Integration

This project includes custom tools for Open WebUI integration:

### Available Tools:

1. **`places_webui_tool.py`** - Standard version with multiple link formats
2. **`places_webui_tool_v2.py`** - Enhanced version with better formatting

### How to Use:

1. Copy one of the tool files
2. Upload to your Open WebUI instance
3. Use the `search_places` function with any query

**Example queries:**

- `restaurant jakarta`
- `hotel bali`
- `coffee shop bandung`
- `tourist attractions yogyakarta`

## 🧪 Testing

### Test API Endpoint:

```bash
# Test basic functionality
curl "http://127.0.0.1:9022/places?query=test"

# Test with real query
curl "http://127.0.0.1:9022/places?query=restaurant+jakarta"
```

### Test in Browser:

Visit: `http://127.0.0.1:9022/places?query=restaurant+jakarta`

## 📁 Project Structure

```
places-search-api/
├── main.py                     # Main FastAPI application
├── places_webui_tool.py        # Open WebUI tool (standard)
├── places_webui_tool_v2.py     # Open WebUI tool (enhanced)
├── requirements.txt            # Python dependencies
├── setup_new_location.bat      # Windows setup script
├── setup_new_location.sh       # Linux/macOS setup script
├── .env.example               # Environment variables template
├── README.md                  # This file
└── TESTING_GUIDE.md          # Detailed testing instructions
```

## ⚙️ Configuration

### Environment Variables

| Variable              | Description              | Required |
| --------------------- | ------------------------ | -------- |
| `GOOGLE_MAPS_API_KEY` | Your Google Maps API key | Yes      |

### API Settings

- **Default Port:** 9022
- **CORS:** Enabled for all origins (configure for production)
- **Timeout:** 10 seconds for external API calls

## 🔧 Development

### Running in Development Mode

```bash
python -m uvicorn main:app --reload --port 9022
```

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🐛 Troubleshooting

### Common Issues:

1. **Server won't start:**

   - Check if port 9022 is available
   - Verify virtual environment is activated
   - Ensure all dependencies are installed

2. **API returns no results:**

   - Verify Google Maps API key is valid
   - Check API key has Places API enabled
   - Try different search queries

3. **Links not clickable in Open WebUI:**
   - Use the enhanced tool version (`places_webui_tool_v2.py`)
   - Copy the plain text link manually
   - Update Open WebUI to latest version

### Error Messages:

- `Google Maps API key not configured` → Add API key to `.env` file
- `Connection Error` → Start the API server first
- `Timeout` → Check internet connection and API limits

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [TESTING_GUIDE.md](TESTING_GUIDE.md) for detailed instructions
2. Create an issue on GitHub
3. Make sure to include error messages and steps to reproduce

## 🙏 Acknowledgments

- Google Maps Places API for location data
- FastAPI for the excellent web framework
- Open WebUI community for integration inspiration

---

⭐ **Star this repo if you find it helpful!**
