import requests

BASE_URL = "http://127.0.0.1:8000"

print("[START]")

requests.get(f"{BASE_URL}/reset")

done = False

while not done:
    response = requests.post(
        f"{BASE_URL}/step",
        json={
            "action": "test",
            "reasoning": "auto agent running"
        }
    ).json()

    action = "test"
    reward = response["reward"]

    print(f"[STEP] Action: {action}, Reward: {reward}")

    done = response["done"]

print("[END]")
