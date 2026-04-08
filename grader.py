def grade_action(action, task):
    score = 0.0
    breakdown = {}

    if action.action == task["correct_action"]:
        score += 0.6
        breakdown["action_correct"] = 0.6
    else:
        breakdown["action_correct"] = 0.0

    if action.reasoning and len(action.reasoning) > 5:
        score += 0.3
        breakdown["reasoning"] = 0.3
    else:
        breakdown["reasoning"] = 0.0

    if task["priority"] == "high" and action.action == "escalate":
        score += 0.1
        breakdown["priority_bonus"] = 0.1
    else:
        breakdown["priority_bonus"] = 0.0

    return score, breakdown