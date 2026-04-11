def grade(task, action):
    correct = task.get("correct_action", "")
    if action.lower() == correct.lower():
        return 0.8  # strictly between 0 and 1
    else:
        return 0.2  # strictly between 0 and 1

tasks = [
    {"id": 1, "issue": "wrong item received", "priority": "medium", "sentiment": "neutral", "correct_action": "replace"},
    {"id": 2, "issue": "payment failed", "priority": "high", "sentiment": "angry", "correct_action": "refund"},
    {"id": 3, "issue": "delivery delayed", "priority": "low", "sentiment": "neutral", "correct_action": "apologize"},
]

if __name__ == "__main__":
    for task in tasks:
        score = grade(task, task["correct_action"])
        print(f"Task {task['id']}: score = {score}")
