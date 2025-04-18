
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock VIP status DB (temporary, no persistence)
vip_users = set()

@app.route('/vip/redirect', methods=['GET'])
def handle_redirect():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"status": "error", "msg": "missing user_id"}), 400
    vip_users.add(user_id)
    return jsonify({
        "status": "ok",
        "user": user_id,
        "vip": True,
        "msg": "You're now a VIP. Nova is all yours 💖"
    })

@app.route('/vip/status', methods=['GET'])
def check_status():
    user_id = request.args.get("user_id")
    status = "VIP" if user_id in vip_users else "free"
    return jsonify({
        "user": user_id,
        "status": status
    })

if __name__ == '__main__':
    print("🔓 VIP Redirect Server running on port 5000")
    app.run(port=5000)
