
import requests

def simulate_vip_unlock(user_id="u888"):
    redirect_url = f"http://localhost:5000/vip/redirect?user_id={user_id}"
    print("[🔁] Simulating redirect...")
    r = requests.get(redirect_url)
    print("Redirect Response:", r.json())

    status_url = f"http://localhost:5000/vip/status?user_id={user_id}"
    r = requests.get(status_url)
    print("VIP Status Check:", r.json())

if __name__ == '__main__':
    simulate_vip_unlock()
