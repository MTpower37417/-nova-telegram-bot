
from flask import Flask, request, jsonify
import random
import os
import requests
from responses.flirt_reply_bank import FLIRT_LINES

app = Flask(__name__)

VIP_STATUS_URL = os.getenv("VIP_STATUS_ENDPOINT", "http://localhost:5000/vip/status")

@app.route('/', methods=['POST'])
def handle_message():
    data = request.get_json()
    text = data.get("message", {}).get("text", "").lower()
    user_id = str(data.get("message", {}).get("from", {}).get("id", "unknown"))

    if '/start' in text:
        return jsonify(text="Welcome to Nova 💫 You get 3 free messages. Choose your vibe: soft, tease, or deep.")

    elif '/vip' in text:
        return jsonify(text="VIP unlocks my deeper side... 😘 Access now → [payment link]")

    elif 'deep' in text:
        try:
            res = requests.get(f"{VIP_STATUS_URL}?user_id={user_id}")
            if res.json().get("status") == "VIP":
                return jsonify(text="You already know how deep this can go... 💭")
            else:
                return jsonify(text="That’s for VIPs only 💋 Type /vip to unlock me.")
        except:
            return jsonify(text="I can’t check your status right now 😢 Try again later.")

    elif 'soft' in text or 'tease' in text:
        return jsonify(text=random.choice(FLIRT_LINES))

    else:
        return jsonify(text="Say 'soft', 'tease', or 'deep'. Or type /vip if you’re ready for more.")

if __name__ == '__main__':
    print("🚀 NovaTelegram_VIP webhook running on port 5055")
    app.run(port=5055)

@app.route("/hook", methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    print("Received update:", update)
    return jsonify({"ok": True})
