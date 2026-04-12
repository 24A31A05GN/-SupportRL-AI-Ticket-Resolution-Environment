from grader import grade

tasks = [
    {
        "id": 1,
        "issue": "wrong item received",
        "priority": "medium",
        "sentiment": "neutral",
        "correct_action": "respond",
        "grader": grade
    },
    {
        "id": 2,
        "issue": "payment failed",
        "priority": "high",
        "sentiment": "angry",
        "correct_action": "escalate",
        "grader": grade
    },
    {
        "id": 3,
        "issue": "delivery delayed",
        "priority": "low",
        "sentiment": "neutral",
        "correct_action": "investigate",
        "grader": grade
    },
    {
        "id": 4,
        "issue": "product damaged on arrival",
        "priority": "high",
        "sentiment": "angry",
        "correct_action": "escalate",
        "grader": grade
    },
    {
        "id": 5,
        "issue": "refund not received after 7 days",
        "priority": "medium",
        "sentiment": "angry",
        "correct_action": "investigate",
        "grader": grade
    },
    {
        "id": 6,
        "issue": "tracking number not working",
        "priority": "low",
        "sentiment": "neutral",
        "correct_action": "respond",
        "grader": grade
    }
]