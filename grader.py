def grade(task, action):
    correct = task.get("correct_action", "")
    if action.lower().strip() == correct.lower().strip():
        return 0.8
    else:
        return 0.2
