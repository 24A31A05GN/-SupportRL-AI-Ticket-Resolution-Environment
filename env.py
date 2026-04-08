from tasks import tasks
import random

class SupportEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(tasks)
        return {
            "ticket_id": self.current_task["ticket_id"],
            "issue_description": self.current_task["issue_description"],
            "priority": self.current_task["priority"],
            "customer_sentiment": self.current_task["customer_sentiment"]
        }

    def step(self, action):
        from grader import grade_action

        task = self.current_task
        score, breakdown = grade_action(action, task)

        observation = {
            "ticket_id": task["ticket_id"],
            "issue_description": task["issue_description"],
            "priority": task["priority"],
            "customer_sentiment": task["customer_sentiment"]
        }

        return {
            "observation": observation,
            "reward": score,
            "done": True,
            "info": {
                "correct_action": task["correct_action"],
                "score_breakdown": breakdown
            }
        }