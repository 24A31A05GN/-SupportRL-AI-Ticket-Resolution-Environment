def grade(task, action):
    correct = task.get("correct_action", "")
    priority = task.get("priority", "medium")
    sentiment = task.get("sentiment", "neutral")

    if action.lower().strip() == correct.lower().strip():
        # bonus reward for high priority correct action
        if priority == "high":
            return 0.92
        elif priority == "medium":
            return 0.75
        else:
            return 0.65
    else:
        # penalty based on sentiment
        if sentiment == "angry":
            return 0.15
        else:
            return 0.35