# main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import requests
import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Places Search API",
    description="A secure API for searching places using Google Maps",
    version="1.0.0"
)

# Security: Trusted hosts
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["localhost", "127.0.0.1", "*.localhost"]
)

# CORS - Configure for production
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # Specify allowed origins instead of "*"
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET methods for this API
    allow_headers=["*"],
)

# Ambil dari .env atau system env var
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if not GOOGLE_MAPS_API_KEY or GOOGLE_MAPS_API_KEY == "YOUR_GOOGLE_MAPS_API_KEY_HERE":
    logger.error("Google Maps API key not configured properly")

@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Places Search API is running"}

@app.get("/places", tags=["Search"])
def search_places(query: str = Query(..., min_length=1, max_length=100, description="Search query for places")):
    """
    Search for places using Google Maps Places API
    
    Args:
        query: Search query (e.g., 'restaurant jakarta', 'hotel bali')
    
    Returns:
        JSON response with places data including names, addresses, and Google Maps links
    """
    if not GOOGLE_MAPS_API_KEY or GOOGLE_MAPS_API_KEY == "YOUR_GOOGLE_MAPS_API_KEY_HERE":
        raise HTTPException(
            status_code=500, 
            detail="Google Maps API key not configured. Please set GOOGLE_MAPS_API_KEY in .env file"
        )
    
    # Input validation and sanitization
    query = query.strip()
    if len(query) < 1:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": GOOGLE_MAPS_API_KEY,
        "fields": "name,formatted_address,geometry",  # Limit fields for efficiency
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Enhanced logging and error handling
        api_status = data.get('status')
        logger.info(f"Google API Status: {api_status} for query: {query}")
        
        if api_status not in ['OK', 'ZERO_RESULTS']:
            logger.error(f"Google API Error: {api_status} - {data}")
            raise HTTPException(
                status_code=502, 
                detail=f"Google Maps API Error: {api_status}"
            )
        
        if api_status == 'ZERO_RESULTS':
            return {"places": [], "message": f"No places found for '{query}'"}
        
        results = []
        for place in data.get("results", [])[:5]:  # Limit to 5 results
            try:
                name = place.get("name", "Unknown")
                address = place.get("formatted_address", "Address not available")
                geometry = place.get("geometry", {}).get("location", {})
                lat = geometry.get("lat")
                lng = geometry.get("lng")
                
                if lat is None or lng is None:
                    continue
                    
                maps_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
                embed_link = f"https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed"
                
                results.append({
                    "name": name,
                    "address": address,
                    "maps_link": maps_link,
                    "embed_link": embed_link,
                    "coordinates": {"lat": lat, "lng": lng}
                })
            except Exception as e:
                logger.warning(f"Error processing place data: {e}")
                continue

        return {"places": results, "total": len(results)}
    
    except requests.exceptions.Timeout:
        logger.error("Google Maps API timeout")
        raise HTTPException(status_code=504, detail="Request timeout to Google Maps API")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        raise HTTPException(status_code=502, detail="Failed to connect to Google Maps API")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
