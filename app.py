# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---- Global environment state ----
env_state = {
    "reward": 0.0,
    "step": 0,
    "id": 1,
    "issue": "wrong item received",
    "priority": "medium",
    "sentiment": "neutral",
    "correct_action": "replace"
}

# ---- Request model ----
class StepRequest(BaseModel):
    action: str
    reasoning: str

# ---- Home ----
@app.get("/")
def home():
    return {"message": "API working"}

# ---- Reset ----
@app.get("/reset")
def reset():
    global env_state
    env_state["reward"] = 0.0
    env_state["step"] = 0
    return {
        "message": "Environment reset successful",
        "state": env_state
    }

# ---- Step ----
@app.post("/step")
def step(request: StepRequest):
    global env_state

    env_state["step"] += 1

    # ✅ Reward logic (0.0 to 1.0)
    reward = 0.5
    env_state["reward"] = reward

    # ✅ IMPORTANT: Done becomes True after 5 steps
    done = False
    if env_state["step"] >= 5:
        done = True

    return {
        "reward": reward,
        "observation": f"Step {env_state['step']} done. Action: {request.action}",
        "done": done
    }

# ---- State ----
@app.get("/state")
def state():
    return env_state

# ---- Auto-run ----
@app.get("/auto-run")
def auto_run():
    global env_state

    logs = []

    # simulate 5 steps
    for i in range(5):
        env_state["step"] += 1
        env_state["reward"] = 0.5

        logs.append({
            "step": env_state["step"],
            "reward": env_state["reward"]
        })

    return {
        "logs": logs,
        "final_state": env_state
    }