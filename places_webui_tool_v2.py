"""
title: Places Search Tool v2 (Enhanced Links)
author: Local Developer  
version: 2.0.0
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
        Search for places using Google Maps Places API. Returns real-time location data with clickable maps links.
        
        :param query: Search query for places like 'restaurant jakarta', 'hotel bali', 'cafe bandung'
        :return: Formatted places information with addresses and clickable Google Maps links
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
            
            # Create formatted response with clickable links
            result = f"🗺️ **Hasil pencarian untuk '{query}':**\n\n"
            
            for i, place in enumerate(places, 1):
                name = place.get('name', 'Unknown')
                address = place.get('address', 'Address not available')
                maps_link = place.get('maps_link', '')
                
                result += f"### {i}. {name}\n"
                result += f"📍 **Alamat:** {address}\n\n"
                
                if maps_link:
                    # Multiple formats untuk memastikan link bisa diklik
                    result += f"🔗 **Copy link ini:** `{maps_link}`\n\n"
                    result += f"🌐 [🗺️ BUKA DI GOOGLE MAPS]({maps_link})\n\n"
                    result += f"<a href='{maps_link}' target='_blank' style='color: #1a73e8; text-decoration: none; font-weight: bold;'>📍 Klik untuk buka Google Maps</a>\n\n"
                
                if i < len(places):
                    result += "---\n\n"
            
            return result
            
        except requests.exceptions.ConnectionError:
            return f"🔌 **Error:** Places API server tidak berjalan di {self.api_url}\n\nJalankan server dengan:\n```\npython -m uvicorn main:app --reload --port 9022\n```"
        except requests.exceptions.Timeout:
            return "⏱️ **Timeout:** API request terlalu lama"
        except Exception as e:
            return f"❌ **Error:** {str(e)}"
