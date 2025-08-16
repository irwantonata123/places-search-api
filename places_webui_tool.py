"""
title: Places Search Tool
author: Local Developer  
version: 1.0.0
required_open_webui_version: 0.1.0
"""

import requests

class Tools:
    def __init__(self):
        # Default to localhost, but can be configured via environment
        import os
        api_host = os.getenv("PLACES_API_HOST", "127.0.0.1")
        api_port = os.getenv("PLACES_API_PORT", "9022")
        self.api_url = f"http://{api_host}:{api_port}/places"
        
    def search_places(self, query: str) -> str:
        """
        Search for places using Google Maps Places API. Returns real-time location data from Google Maps.
        
        :param query: Search query for places like 'restaurant jakarta', 'hotel bali', 'cafe bandung'
        :return: Formatted places information with addresses and Google Maps links
        """
        try:
            response = requests.get(self.api_url, params={"query": query}, timeout=10)
            
            if response.status_code != 200:
                return f"⚠️ API returned status {response.status_code}"
                
            data = response.json()
            
            if "error" in data:
                return f"⚠️ API Error: {data['error']}"
            
            places = data.get("places", [])
            if not places:
                return f"❌ No places found for '{query}'. Try different keywords."
            
            # Create formatted response with real data
            result = f"🗺️ **Places found for '{query}':**\n\n"
            
            for i, place in enumerate(places, 1):
                name = place.get('name', 'Unknown')
                address = place.get('address', 'Address not available')
                maps_link = place.get('maps_link', '')
                
                result += f"**{i}. {name}**\n"
                result += f"📍 {address}\n"
                if maps_link:
                    # Format yang lebih kompatibel untuk Open WebUI
                    result += f"🔗 **Link Google Maps:** {maps_link}\n"
                    result += f"🌐 <a href='{maps_link}' target='_blank'>🗺️ Buka di Google Maps</a>\n"
                
                if i < len(places):
                    result += "\n" + "─" * 50 + "\n\n"
            
            return result
            
        except requests.exceptions.ConnectionError:
            return f"🔌 Connection Error: Places API server not running at {self.api_url}"
        except requests.exceptions.Timeout:
            return "⏱️ Timeout: API request took too long"
        except Exception as e:
            return f"❌ Error: {str(e)}"
