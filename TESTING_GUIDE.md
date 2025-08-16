# 🗺️ Places API - Testing Guide

## Masalah Link Google Maps di Open WebUI

### ✅ Solusi yang Sudah Diterapkan:

1. **File `places_webui_tool.py`** - Updated dengan format link yang lebih kompatibel
2. **File `places_webui_tool_v2.py`** - Versi enhanced dengan multiple format link

### 🔧 Format Link yang Disediakan:

1. **Plain Text Link** - Bisa di-copy manual
2. **Markdown Link** - `[Text](URL)` format
3. **HTML Link** - `<a href='URL'>Text</a>` format

## 🚀 Cara Testing:

### 1. **Pastikan Server Berjalan**

```bash
python -m uvicorn main:app --reload --port 9022
```

### 2. **Test via Browser**

Buka: `http://127.0.0.1:9022/places?query=restaurant+jakarta`

### 3. **Test via Open WebUI**

- Upload file `places_webui_tool.py` atau `places_webui_tool_v2.py`
- Gunakan function `search_places`
- Test dengan query: `restaurant jakarta`, `hotel bali`, dll

### 4. **Test Manual Link**

Contoh response akan berisi:

```
🗺️ Hasil pencarian untuk 'restaurant':

### 1. Nama Restaurant
📍 Alamat: Jl. Example No. 123

🔗 Copy link ini: https://www.google.com/maps/search/?api=1&query=-6.123,106.456
🌐 [🗺️ BUKA DI GOOGLE MAPS](https://www.google.com/maps/search/?api=1&query=-6.123,106.456)
📍 Klik untuk buka Google Maps
```

## 🎯 Troubleshooting:

### Jika link masih tidak bisa diklik:

1. **Copy link manual** dari text yang disediakan
2. **Paste di browser** untuk buka Google Maps
3. **Update Open WebUI** ke versi terbaru yang support HTML links

### Alternative solutions:

1. Gunakan **embed_link** untuk iframe Google Maps
2. Buat **QR Code** untuk link Google Maps
3. Export ke **JSON/CSV** untuk external processing

## 📋 Link Format Examples:

**Original Google Maps Link:**

```
https://www.google.com/maps/search/?api=1&query=-6.2,106.8
```

**Embed Link (untuk iframe):**

```
https://maps.google.com/maps?q=-6.2,106.8&z=15&output=embed
```
