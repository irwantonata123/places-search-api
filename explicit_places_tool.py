"""
title: Places Finder
author: Local Developer
version: 1.0.0
description: Find real places with Google Maps links
"""

import requests

class Tools:
    def __init__(self):
        pass

    def find_places(self, location_query: str = "") -> str:
        """
        Find real places with Google Maps links
        
        Args:
            location_query (str): What to search for (e.g. "restaurant jakarta", "hotel bali")
            
        Returns:
            str: Places with clickable Google Maps links
        """
        if not location_query:
            return "❌ Please specify what places to find (e.g., 'restaurant jakarta')"
            
        try:
            url = "http://127.0.0.1:9022/places"
            response = requests.get(url, params={"query": location_query}, timeout=15)
            
            if response.status_code != 200:
                return f"⚠️ API Error: {response.status_code}"
            
            data = response.json()
            
            if "error" in data:
                return f"❌ {data['error']}"
            
            places = data.get("places", [])
            if not places:
                return f"No places found for '{location_query}'"
            
            # Create very clear output with explicit links
            result = f"🗺️ **{len(places)} REAL PLACES for '{location_query}':**\n\n"
            
            for i, place in enumerate(places, 1):
                name = place.get('name', 'Unknown')
                address = place.get('address', 'Address unavailable')
                maps_url = place.get('maps_link', '')
                
                result += f"**{i}. {name}**\n"
                result += f"📍 **Address:** {address}\n"
                
                if maps_url:
                    result += f"🔗 **GOOGLE MAPS LINK:** {maps_url}\n"
                    result += f"🌐 **[CLICK HERE FOR GOOGLE MAPS]({maps_url})**\n"
                
                result += "\n" + "="*60 + "\n\n"
            
            return result
            
        except requests.exceptions.ConnectionError:
            return "🔌 Cannot connect to Places API. Server not running at http://127.0.0.1:9022"
        except Exception as e:
            return f"❌ Error: {str(e)}"
