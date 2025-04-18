
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
invite_log = []

@app.route('/payment/mock', methods=['POST'])
def payment_handler():
    data = request.get_json()
    user = data.get('user_id', 'unknown')
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    invite_log.append({'user': user, 'ts': timestamp})

    return jsonify({
        "status": "logged",
        "msg": f"{user} registered for VIP at {timestamp}"
    })

@app.route('/invite/log', methods=['GET'])
def show_invite():
    return jsonify(invite_log)

if __name__ == '__main__':
    print("💰 Mock Payment Tracker running on port 5059")
    app.run(port=5059)
