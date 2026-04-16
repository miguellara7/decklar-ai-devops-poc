
"""
Decklar | Miguel Lopez | DevOps AI POC

Features:
- System metrics collection (CPU, Memory, Disk)
- Prometheus-compatible metrics endpoint
- AI-based evaluation using OpenAI
- FastAPI service (production-style structure)
"""

import psutil
import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from openai import OpenAI

app = FastAPI(title="Decklar DevOps AI Monitoring")

# Initialize OpenAI client (expects OPENAI_API_KEY env var)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Metrics Collection
# -----------------------------
def collect_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }

# -----------------------------
# AI Evaluation
# -----------------------------
def evaluate_metrics_with_ai(metrics):
    """
    Uses OpenAI to interpret system health.
    This simulates an AI-powered observability agent.
    """

    prompt = f"""
    You are a DevOps monitoring agent.
    Analyze these system metrics and return a short status and risks.

    Metrics:
    CPU: {metrics['cpu']}%
    Memory: {metrics['memory']}%
    Disk: {metrics['disk']}%

    Respond in JSON:
    {{
        "status": "...",
        "summary": "...",
        "risks": []
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return {
            "status": "error",
            "summary": str(e),
            "risks": []
        }

# -----------------------------
# API Endpoints
# -----------------------------

@app.get("/")
def root():
    return {"message": "Decklar DevOps AI POC running"}

@app.get("/metrics")
def prometheus_metrics():
    """
    Prometheus-style metrics endpoint
    """

    m = collect_metrics()

    output = f"""
# HELP system_cpu_usage CPU usage percentage
# TYPE system_cpu_usage gauge
system_cpu_usage {m['cpu']}

# HELP system_memory_usage Memory usage percentage
# TYPE system_memory_usage gauge
system_memory_usage {m['memory']}

# HELP system_disk_usage Disk usage percentage
# TYPE system_disk_usage gauge
system_disk_usage {m['disk']}
"""

    return PlainTextResponse(output)

@app.get("/analyze")
def analyze():
    """
    Combines metrics + AI evaluation
    """

    metrics = collect_metrics()
    ai_analysis = evaluate_metrics_with_ai(metrics)

    return {
        "metrics": metrics,
        "ai_analysis": ai_analysis
    }
