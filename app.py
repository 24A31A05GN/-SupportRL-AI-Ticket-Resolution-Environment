from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

tasks = [
    {"id": 1, "issue": "wrong item received", "priority": "medium", "sentiment": "neutral", "correct_action": "replace"},
    {"id": 2, "issue": "payment failed", "priority": "high", "sentiment": "angry", "correct_action": "refund"},
    {"id": 3, "issue": "delivery delayed", "priority": "low", "sentiment": "neutral", "correct_action": "apologize"},
]

env_state = {
    "reward": 0.0,
    "step": 0,
    "task_index": 0,
    **tasks[0]
}

class StepRequest(BaseModel):
    action: str
    reasoning: str

@app.get("/")
def home():
    return {"message": "API working"}

@app.post("/reset")
def reset():
    global env_state
    env_state = {
        "reward": 0.0,
        "step": 0,
        "task_index": 0,
        **tasks[0]
    }
    return {"message": "Environment reset successful", "state": env_state}

@app.post("/step")
def step(request: StepRequest):
    global env_state

    correct = tasks[env_state["task_index"]]["correct_action"]

    if request.action.lower() == correct:
        reward = 0.8
    else:
        reward = 0.2

    env_state["reward"] = reward
    env_state["step"] += 1

    task_index = env_state["task_index"] + 1
    done = task_index >= len(tasks)

    if not done:
        env_state["task_index"] = task_index
        env_state.update(tasks[task_index])

    return {
        "reward": reward,
        "observation": f"Step {env_state['step']} done. Action: {request.action}",
        "done": done
    }

@app.get("/state")
def state():
    return env_state

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
