"""
title: Google Places Search
author: Local Developer
version: 1.0.0
description: Search for real places using Google Maps Places API
"""

import json
import requests

class Tools:
    def __init__(self):
        pass

    def get_places(self, query: str = "") -> str:
        """
        Get real places from Google Maps based on search query.
        This tool searches for actual places and returns real location data.
        
        Args:
            query (str): What places to search for (e.g. "restaurant jakarta", "hotel bali")
            
        Returns:
            str: List of real places with addresses and Google Maps links
        """
        if not query:
            return "❌ Please provide a search query (e.g., 'restaurant jakarta')"
            
        try:
            # Call the Places API
            url = "http://127.0.0.1:9022/places"
            response = requests.get(url, params={"query": query}, timeout=15)
            
            if response.status_code != 200:
                return f"⚠️ API Error: {response.status_code}"
            
            data = response.json()
            
            if "error" in data:
                return f"❌ {data['error']}"
            
            places = data.get("places", [])
            if not places:
                return f"No places found for '{query}'"
            
            # Format the results
            output = f"📍 **{len(places)} places found for '{query}':**\n\n"
            
            for i, place in enumerate(places, 1):
                output += f"**{i}. {place['name']}**\n"
                output += f"📍 Address: {place['address']}\n"
                output += f"🔗 Google Maps: {place['maps_link']}\n"
                output += f"🗺️ [Click here to view on Google Maps]({place['maps_link']})\n\n"
            
            return output
            
        except requests.exceptions.ConnectionError:
            return "🔌 Cannot connect to Places API. Make sure server is running at http://127.0.0.1:9022"
        except Exception as e:
            return f"❌ Error: {str(e)}"
