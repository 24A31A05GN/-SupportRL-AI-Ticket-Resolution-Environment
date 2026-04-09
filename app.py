from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

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
@app.post("/reset")
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
    reward = 0.5
    env_state["reward"] = reward
    done = env_state["step"] >= 5
    return {
        "reward": reward,
        "observation": f"Step {env_state['step']} done. Action: {request.action}",
        "done": done
    }

# ---- State ----
@app.get("/state")
def state():
    return env_state

# ---- Main ----
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
