def grade(task, action):
    correct = task.get("correct_action", "")
    if action.lower().strip() == correct.lower().strip():
        return 0.8
    else:
        return 0.2

if __name__ == "__main__":
    from tasks import tasks
    for task in tasks:
        score = grade(task, task["correct_action"])
        print(f"Task {task['id']}: score = {score}")
