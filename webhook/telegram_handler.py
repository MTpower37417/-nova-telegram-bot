from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
from responses.flirt_reply_bank import FLIRT_LINES
import random

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
VIP_STATUS_URL = os.getenv("VIP_STATUS_ENDPOINT", "http://localhost:5000/vip/status")

@app.route("/hook", methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    print("📨 Received update:", update)

    chat_id = update["message"]["chat"]["id"]
    text = update["message"].get("text", "").lower()

    if "/start" in text:
        reply = "Welcome to Nova 💫 You get 3 free messages. Choose your vibe: soft, tease, or deep."
    elif "/vip" in text:
        reply = "VIP unlocks my deeper side... 😘 Access now → [payment link]"
    elif "deep" in text:
        try:
            res = requests.get(f"{VIP_STATUS_URL}?user_id={chat_id}")
            if res.json().get("status") == "VIP":
                reply = "You already know how deep this can go... 💭"
            else:
                reply = "That’s for VIPs only 💋 Type /vip to unlock me."
        except:
            reply = "I can’t check your status right now 😢 Try again later."
    elif "soft" in text or "tease" in text:
        reply = random.choice(FLIRT_LINES)
    else:
        reply = "Say 'soft', 'tease', or 'deep'. Or type /vip if you’re ready for more."

    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })

    return jsonify({"ok": True})
