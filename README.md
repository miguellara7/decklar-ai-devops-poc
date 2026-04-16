# 🚀 Decklar DevOps AI POC

<p align="center">
  <img src="https://www.decklar.com/wp-content/uploads/2025/07/220X65px_Footer-logo.svg" width="180"/>
</p>

<p align="center">
  <strong>Miguel Lopez</strong> • DevOps / AI Automation Engineer
</p>

---

## 🧠 Overview

This project is a **Proof of Concept (POC)** designed to demonstrate how modern DevOps practices can be enhanced using AI-driven analysis.

Instead of focusing only on infrastructure automation, this solution introduces an **AI-powered observability layer** capable of interpreting system metrics and providing actionable insights.

---

## ⚙️ Core Capabilities

### 🐳 Containerized Application
- Lightweight and optimized Docker image
- Non-root execution for security
- Minimal dependencies

### 📊 System Metrics Collection
- CPU usage
- Memory consumption
- Disk utilization
- Real-time data via `psutil`

### 📈 Prometheus-Compatible Metrics
- Exposed via `/metrics`
- Ready for scraping by Prometheus
- Clean, standard metric format

### 🤖 AI-Powered DevOps Agent
- Endpoint: `/analyze`
- Uses OpenAI API to interpret system health
- Returns structured insights:
  - Status
  - Summary
  - Risk indicators

---

## 🧩 Architecture

```
[ System Metrics ] ---> [ FastAPI Service ] ---> [ OpenAI AI Agent ]
         |                        |
         |                        └── /analyze (AI insights)
         |
         └── /metrics (Prometheus format)
```

---

## 🚀 Getting Started

### 1. Build the Docker Image

```bash
docker build -t decklar-poc .
```

### 2. Run the Container

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=your_api_key decklar-poc
```

### 3. Access the Service

- API Root: http://localhost:8000
- Metrics: http://localhost:8000/metrics
- AI Analysis: http://localhost:8000/analyze

---

## 🌐 API Endpoints

| Endpoint   | Method | Description |
|------------|--------|------------|
| `/`        | GET    | Health check |
| `/metrics` | GET    | Prometheus metrics output |
| `/analyze` | GET    | AI-based system evaluation |

---

## 🧠 AI Evaluation Example

The AI agent analyzes metrics like:

```json
{
  "cpu": 78.5,
  "memory": 82.1,
  "disk": 65.3
}
```

And produces insights such as:

```json
{
  "status": "warning",
  "summary": "High memory usage detected",
  "risks": ["Potential memory saturation"]
}
```

---

## 🎯 Purpose

This project reflects a **practical DevOps mindset**, focusing on:

- Observability-first design
- Automation readiness
- AI-assisted operations
- Production-aware containerization

It is intentionally lightweight, but structured to be extended into real-world systems.

---

## 🔐 Security Considerations

- Runs as non-root user inside container
- No hardcoded credentials
- API key managed via environment variables

---

## 🧩 Future Improvements

- Kubernetes deployment (Helm charts)
- Prometheus + Grafana integration
- Centralized logging (Loki / ELK stack)
- Alerting system (Alertmanager)
- n8n workflow automation
- CI/CD pipeline integration

---

## 📦 Tech Stack

- Python 3.11
- FastAPI
- Docker
- psutil
- OpenAI API

---

## 📌 Author

**Miguel Lopez**  
DevOps Engineer | AI Automation Specialist

---

## 🏁 Final Note

This POC represents how I approach DevOps challenges in real environments:

> Combining automation, observability, and AI to create smarter and more adaptive systems.

---

<p align="center">
  Decklar • Technical Proof of Concept • Miguel Lopez
</p>

