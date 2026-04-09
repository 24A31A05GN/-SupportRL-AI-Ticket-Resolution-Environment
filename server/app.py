import requests
import os

BASE_URL = "http://127.0.0.1:7860"

print("[START]")

# Reset environment
try:
    requests.post(f"{BASE_URL}/reset", timeout=10)
    print("[RESET] Done")
except Exception as e:
    print(f"[RESET ERROR] {e}")

done = False
step_count = 0

while not done and step_count < 5:
    try:
        state = requests.get(f"{BASE_URL}/state", timeout=10).json()

        # LLM call
        api_base = os.environ.get("API_BASE_URL", "")
        api_key = os.environ.get("API_KEY", "dummy")

        action = "replace"  # default fallback

        if api_base:
            try:
                llm_resp = requests.post(
                    f"{api_base}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a customer support AI. Choose one action: replace, refund, escalate, or apologize. Reply with just one word."
                            },
                            {
                                "role": "user",
                                "content": f"Issue: {state.get('issue', 'unknown')}. Priority: {state.get('priority', 'medium')}. Sentiment: {state.get('sentiment', 'neutral')}. What action?"
                            }
                        ],
                        "max_tokens": 10
                    },
                    timeout=30
                ).json()

                action = llm_resp["choices"][0]["message"]["content"].strip().lower()
                print(f"[LLM] Action: {action}")

            except Exception as e:
                print(f"[LLM ERROR] {e}")
                action = "replace"

        # Step in environment
        step_response = requests.post(
            f"{BASE_URL}/step",
            json={"action": action, "reasoning": f"LLM decided to {action}"},
            timeout=10
        ).json()

        reward = step_response["reward"]
        done = step_response["done"]
        step_count += 1
        print(f"[STEP {step_count}] Action: {action}, Reward: {reward}, Done: {done}")

    except Exception as e:
        print(f"[ERROR] {e}")
        break

print("[END]")
