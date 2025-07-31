import os

API_ID    = os.environ.get("API_ID", "6024888")
API_HASH  = os.environ.get("API_HASH", "c78489a1b52a6dac192f2c1b6eb30435")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8387436765:AAHSjwCK1LAXlYM5f9IYfQ7Q-jf4zoAVkSU") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
