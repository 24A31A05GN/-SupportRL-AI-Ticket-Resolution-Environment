def grade(task, action):
    correct = task.get("correct_action", "")
    priority = task.get("priority", "medium")
    sentiment = task.get("sentiment", "neutral")

    if action.lower().strip() == correct.lower().strip():
        # bonus reward for high priority correct action
        if priority == "high":
            return 0.9
        elif priority == "medium":
            return 0.7
        else:
            return 0.6
    else:
        # penalty based on sentiment
        if sentiment == "angry":
            return 0.1
        else:
            return 0.3
