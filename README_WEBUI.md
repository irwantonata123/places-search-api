# Places API Tool untuk Open WebUI

## 🎯 Simple Setup:

Ada **3 versi tool** yang bisa Anda coba:

1. **`places_webui_tool.py`** - Versi lengkap dengan formatting
2. **`simple_places_tool.py`** - Versi sederhana
3. **`explicit_places_tool.py`** - Versi eksplisit dengan link yang jelas ⭐ **RECOMMENDED**

## 🚀 Cara Import ke Open WebUI:

1. **Copy isi salah satu file tool**
2. Buka Open WebUI → **Settings** → **Tools**
3. Klik **"Create Tool"**
4. Paste code dan save dengan nama **"Places Search"**
5. **PENTING: Toggle ON tool** - Lihat di sidebar kiri ada switch/toggle untuk enable tool
6. Done! ✅

## 🔧 Cara Toggle ON Tool:

### Method 1: Di Settings

1. **Settings** → **Tools**
2. Cari tool "Places Search" yang sudah dibuat
3. Klik **toggle/switch** di sebelah nama tool (warna hijau = ON)

### Method 2: Di Chat Interface

1. Saat mulai chat baru
2. Di sidebar kiri atau bawah ada **Tools** section
3. Centang/toggle tool "Places Search"
4. Tool akan aktif untuk chat session tersebut## 🔥 Tips Agar LLM Pakai Tool:

Contoh prompt :

- ✅ "cari restaurant di jakarta"
- ✅ "cari hotel bali"
- ✅ "\*cafe bandung"

## ✅ Prerequisites:

1. **Server running**: `D:/Projects/PlacesApi/.venv/Scripts/python.exe -m uvicorn main:app --reload --port 9022`
2. **API Key**: File `.env` berisi `GOOGLE_MAPS_API_KEY`
3. **Network**: Open WebUI bisa akses `localhost:9022`

## 🧪 Test Commands:

## 🔧 Troubleshooting:

**LLM tidak pakai tool?**

1. **Cek tool sudah ON**:

   - Settings → Tools → cari "Places Search" → pastikan toggle hijau/ON
   - ATAU di chat interface, sidebar ada Tools section → centang "Places Search"

2. **Restart chat session** kalau perlu

**Tool error?**

```bash
# Cek API masih hidup
curl http://127.0.0.1:9022/places?query=test
```

## 🔗 Fix Link Google Maps Tidak Muncul:

**Problem**: Tool jalan tapi link Google Maps tidak terlihat di output

**Solution**:

1. Gunakan **`explicit_places_tool.py`** (versi terbaru)
2. Tool ini format link dengan lebih jelas:
   - `🔗 **GOOGLE MAPS LINK:** https://...`
   - `🌐 **[CLICK HERE FOR GOOGLE MAPS](...)**`

**Test**: Copy `explicit_places_tool.py` → import ke Open WebUI → coba lagi

## 📸 Visual Guide Toggle:

```
Settings → Tools:
┌─────────────────────────────┐
│ Places Search               │
│ ○ ← Toggle ini (ON = hijau) │
└─────────────────────────────┘

Chat Interface:
┌─── Sidebar ────┐
│ 🔧 Tools       │
│ ☑ Places Search│ ← Centang ini
│ ☐ Other Tool   │
└────────────────┘
```
