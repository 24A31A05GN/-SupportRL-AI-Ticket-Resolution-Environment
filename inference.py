import requests
import os

BASE_URL = "http://127.0.0.1:7860"

# Tasks matching SupportRL environment
TASKS = ["wrong_item", "payment_failed", "delivery_delayed"]

def clamp_score(score):
    """Ensures score stays strictly within (0, 1)"""
    return max(0.01, min(0.99, score))

def grade(task, action):
    correct = task.get("correct_action", "")
    priority = task.get("priority", "medium")
    sentiment = task.get("sentiment", "neutral")

    if action.lower().strip() == correct.lower().strip():
        if priority == "high":
            raw = 0.9
        elif priority == "medium":
            raw = 0.75
        else:
            raw = 0.65
    else:
        if sentiment == "angry":
            raw = 0.15
        else:
            raw = 0.35

    return clamp_score(raw)

def run_task(task_name):
    print(f"[TASK] Starting: {task_name}")

    try:
        requests.post(f"{BASE_URL}/reset", timeout=10)
        print(f"[RESET] Done for task: {task_name}")
    except Exception as e:
        print(f"[RESET ERROR] {e}")
        print("[END]")
        return

    done = False
    step_count = 0

    while not done and step_count < 10:
        try:
            state = requests.get(f"{BASE_URL}/state", timeout=10).json()

            api_base = os.environ.get("API_BASE_URL", "")
            api_key = os.environ.get("API_KEY", "dummy")

            action = "respond"  # default fallback

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
                                    "content": """You are an expert customer support AI agent.
Your job is to analyze support tickets and choose the best action.

Available actions:
- respond: for simple, low priority issues that need a quick reply
- investigate: for medium priority issues that need more analysis
- escalate: for high priority or angry customer issues needing manager attention

Rules:
- If priority is HIGH → escalate
- If sentiment is ANGRY → escalate
- If priority is MEDIUM → investigate
- If priority is LOW → respond

Reply with ONLY one word: respond, investigate, or escalate."""
                                },
                                {
                                    "role": "user",
                                    "content": f"""Ticket details:
Issue: {state.get('issue', 'unknown')}
Priority: {state.get('priority', 'medium')}
Sentiment: {state.get('sentiment', 'neutral')}

What is the best action?"""
                                }
                            ],
                            "max_tokens": 10
                        },
                        timeout=30
                    ).json()

                    action = llm_resp["choices"][0]["message"]["content"].strip().lower()
                    if action not in ["respond", "investigate", "escalate"]:
                        action = "respond"
                    print(f"[LLM] Action: {action}")

                except Exception as e:
                    print(f"[LLM ERROR] {e}")
                    action = "respond"

            # Grade using clamped grader
            score = grade(state, action)
            print(f"[GRADE] Task: {task_name}, Score: {score}")

            step_response = requests.post(
                f"{BASE_URL}/step",
                json={"action": action, "reasoning": f"LLM decided to {action}"},
                timeout=10
            ).json()

            reward = step_response.get("reward", 0.5)
            done = step_response.get("done", False)
            step_count += 1
            print(f"[STEP {step_count}] Task: {task_name}, Action: {action}, Reward: {reward}, Done: {done}")

        except Exception as e:
            print(f"[ERROR] {e}")
            break

    print("[END]")


def main():
    print("[START]")
    try:
        for task_name in TASKS:
            run_task(task_name)
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
        # Emit one [END] per task on fatal failure
        for _ in TASKS:
            print("[END]")


if __name__ == "__main__":
    main()
