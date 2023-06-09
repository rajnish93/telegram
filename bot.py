import requests
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

resp = requests.get("https://api.telegram.org/bot"+bot_token+"/getUpdates")
print(resp.text)