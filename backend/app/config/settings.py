import os
from pathlib import Path
from dotenv import load_dotenv

# Project root (backend/)
BASE_DIR = Path(__file__).resolve().parents[3]

# Load .env
load_dotenv(BASE_DIR / ".env")
print("BASE_DIR:", BASE_DIR)
print(".env exists:", (BASE_DIR / ".env").exists())
# ==========================
# Application
# ==========================
APP_NAME = "Atlas AI"
APP_VERSION = "1.0.0"
DEBUG = True

# ==========================
# Development
# ==========================
DEV_TELEGRAM_USER_ID = 123456789

# ==========================
# Gemini
# ==========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.5-flash-lite"

# ==========================
# Telegram
# ==========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ==========================
# Supabase
# ==========================
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")

# ==========================
# Financial APIs
# ==========================
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ==========================
# Memory
# ==========================
MAX_HISTORY = 10

# ==========================
# AI
# ==========================
SYSTEM_TEMPERATURE = 0.3
MAX_OUTPUT_TOKENS = 2048