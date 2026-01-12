import feedparser
import time
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
RSS_URL = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/rss/garnet.xml"

last_entry = ""

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    
while True:
    feed = feedparser.parse(RSS_URL)

    if feed.entries:
        entry = feed.entries[0]
        latest = entry.get("id") or entry.get("link") or entry.get("title")

        if latest != last_entry:
            last_entry = latest
            send_message(
                f"🚀 HyperOS Update Detected!\n{entry.title}"
            )

    time.sleep(3600)

