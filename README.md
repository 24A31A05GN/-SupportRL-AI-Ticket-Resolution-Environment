---
title: Customer-Env
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---Sure! Here's your **SupportRL README content** cleaned up with **extra spaces removed**, compact and ready to use exactly as you want:

---

# 🚀 SupportRL: AI Ticket Resolution Environment

## 📌 Overview

**SupportRL** is a mini **reinforcement learning (RL) environment** built using the OpenEnv framework. It simulates real-world customer support systems where an AI agent selects actions such as **respond**, **investigate**, or **escalate**, and receives rewards based on the quality of its decisions.

## 🎯 Objective

To design and evaluate an AI agent that can make effective decisions in customer support scenarios using:

* Task-based environments
* Reward-driven evaluation
* Performance tracking

## 🌐 Live Demo

🔗 [https://huggingface.co/spaces/Revathi-05/customer-env](https://huggingface.co/spaces/Revathi-05/customer-env)

## 🚀 Features

* 📄 Multiple customer support ticket scenarios
* ⚙️ Custom RL environment (state, action, reward)
* 🎯 Reward system (normalized between 0 and 1)
* 🤖 Rule-based intelligent agent
* 📊 Performance tracking (accuracy calculation)
* 🌐 FastAPI backend with REST API endpoints
* ☁️ Deployed on Hugging Face Spaces

## 🧠 Environment Design

### 🔹 State

Each state represents a support ticket containing:

* Issue description
* Priority level (low, medium, high)
* Customer sentiment (neutral, angry, panic)

### 🔹 Actions

The agent can choose one of the following:

* **respond** → handle simple issues
* **investigate** → analyze moderate issues
* **escalate** → handle critical or high-priority issues

### 🔹 Reward Logic

* ✔ Correct action → positive reward
* ❌ Incorrect action → penalty
* ⚠ High-priority issue not escalated → additional penalty
* 🎯 Rewards are normalized in the range **[0, 1]**

## 🔌 API Endpoints

### 1️⃣ Reset Environment

```bash
GET /reset
```

➡ Returns a new support ticket (initial state)

### 2️⃣ Take Action

```bash
POST /step
```

#### Example Request:

```json
{"action":"respond"}
```

#### Response Includes:

* Next state
* Reward
* Done flag

### 3️⃣ Get Current State

```bash
GET /state
```

### 4️⃣ Auto Run Agent

```bash
GET /auto-run
```

➡ Runs the agent automatically through tasks

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd supportrl-project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Server

```bash
uvicorn app:app --reload
```

### 4️⃣ Open API Docs

```bash
http://127.0.0.1:8000/docs
```

## 🧪 Running the Agent

```bash
python inference.py
```

### 📌 Expected Output Format

```text
[START]
[STEP] action 1
[STEP] action 2
[END]
```

## 📊 Performance Evaluation

The agent tracks:

* Total tasks
* Correct decisions
* Accuracy (%)

## ☁️ Deployment

🔗 [https://huggingface.co/spaces/Revathi-05/customer-env](https://huggingface.co/spaces/Revathi-05/customer-env)

## 🔑 Environment Variables

No external API tokens are required.
Example configuration:

```bash
API_BASE_URL=http://127.0.0.1:8000
MODEL_NAME=rule-based-agent
HF_TOKEN=not-required
```

## ⚠️ Important Notes

* Rewards are always between **0 and 1**
* All API endpoints must return valid responses
* Inference output must follow the required format
* Project should pass validation before submission

## 👨‍💻 Team Members

* **K. Mahitha Sri Ishwarya** (Team Lead)
* **Ch. Revathi**

## 📌 Conclusion

SupportRL demonstrates how reinforcement learning concepts can be applied to simulate and evaluate AI decision-making in customer support environments.

---

If you want, I can also **make it even shorter for GitHub README**, keeping it under **1 page** but keeping all key points.

Do you want me to do that?
