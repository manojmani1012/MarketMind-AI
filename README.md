# MarketMind AI

Autonomous Market Research Platform built using:

- React (Frontend)
- FastAPI (Backend)
- LangGraph (Agent Orchestration)
- LangChain
- OpenAI / Ollama
- Tavily Search

MarketMind AI performs:

- Market Research
- Competitor Analysis
- SWOT Analysis
- Trend Discovery
- Executive Report Generation

---

# Architecture

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph Workflow
 │
 ├── Planner Agent
 │
 ├── Research Agent
 │
 ├── Competitor Agent
 │
 ├── SWOT Agent
 │
 └── Report Agent
 │
 ▼
Executive Report
```

---

# Current Version

Current MVP includes:

✅ Planner Agent

✅ Research Agent

✅ Competitor Analysis Agent

✅ SWOT Agent

✅ Executive Report Agent

✅ React Dashboard

✅ FastAPI Backend

✅ LangGraph Workflow

✅ OpenAI Support

✅ Ollama Support

---

# Project Structure

```text
MarketMind-AI/

├── Backend/
│
│   ├── app/
│   │
│   ├── agents/
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── competitor.py
│   │   ├── swot.py
│   │   ├── reporter.py
│   │   └── llm.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   ├── models/
│   │   └── state.py
│   │
│   └── main.py
│
│   ├── requirements.txt
│   └── .env
│
└── Frontend/
    │
    ├── src/
    │
    ├── pages/
    │   └── Dashboard.jsx
    │
    ├── services/
    │   └── api.js
    │
    ├── App.jsx
    └── App.css
```

---

# Prerequisites

Install:

- Python 3.11+
- Node.js 20+
- npm
- Git

---

# Clone Repository

```bash
git clone <repo-url>

cd MarketMind-AI
```

---

# Backend Setup

Navigate:

```bash
cd Backend
```

Create Virtual Environment:

```bash
python -m venv market_venv
```

Activate:

Windows

```bash
market_venv\Scripts\activate
```

Linux / Mac

```bash
source market_venv/bin/activate
```

---

# Install Backend Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install \
fastapi \
uvicorn \
langgraph \
langchain \
langchain-openai \
langchain-community \
tavily-python \
python-dotenv \
python-certifi-win32
```

---

# Environment Variables

Create:

```text
Backend/.env
```

---

# OpenAI Configuration

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxx
```

---

# Tavily API Key

Create free account:

https://app.tavily.com

Generate API Key.

Add:

```env
TAVILY_API_KEY=tvly-xxxxxxxx
```

---

# OpenAI SSL Issue (Corporate Network)

If receiving:

```text
SSL: CERTIFICATE_VERIFY_FAILED
```

Install:

```bash
pip install python-certifi-win32
```

This allows Python to use Windows trusted certificates.

---

# Run Backend

```bash
cd Backend

uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate:

```bash
cd Frontend
```

Install:

```bash
npm install
```

Install Axios:

```bash
npm install axios
```

Run:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5174
```

---

# Testing

Open:

```text
http://localhost:8000/docs
```

POST:

```json
{
  "query": "AI Coding Assistants Market 2026"
}
```

Expected:

```json
{
  "query": "...",
  "plan": "...",
  "research": "...",
  "competitors": "...",
  "swot": "...",
  "report": "..."
}
```

---

# Using OpenAI

Current OpenAI file:

```text
Backend/app/agents/llm.py
```

Example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

Requirements:

```env
OPENAI_API_KEY=
```

---

# Using Ollama (Recommended)

No OpenAI credits required.

---

# Install Ollama

Download:

https://ollama.com

---

# Pull Model

```bash
ollama pull llama3.1:8b
```

or

```bash
ollama pull qwen3:8b
```

---

# Verify

```bash
ollama run llama3.1:8b
```

---

# Update llm.py

Replace:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)
```

with:

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)
```

No API key required.

---

# Current Workflow

```text
Planner
   ↓
Research
   ↓
Competitor
   ↓
SWOT
   ↓
Executive Report
```

---

# Agent Responsibilities

## Planner Agent

Creates research plan.

Output:

```text
Research Objectives
Research Steps
Analysis Plan
```

---

## Research Agent

Collects market intelligence.

Output:

```text
Market Size
Growth
Trends
Target Audience
```

---

## Competitor Agent

Analyzes competitors.

Output:

```text
Pricing
Strengths
Weaknesses
Market Position
```

---

## SWOT Agent

Generates SWOT.

Output:

```text
Strengths
Weaknesses
Opportunities
Threats
```

---

## Report Agent

Generates executive report.

Output:

```text
Executive Summary
Recommendations
Market Attractiveness
```

---

# Current Limitations

Current version uses:

- Mock Research Data
- Mock Competitor Data
- Mock SWOT Data

No real web search yet.

---

# Roadmap

## Phase 2

Real Market Research

Integrate:

- Tavily Search
- News Sources
- Industry Reports

Add:

```text
Trend Detection Agent
```

---

## Phase 3

Competitor Intelligence

Add:

```text
Pricing Analysis Agent
```

Capabilities:

- Pricing Tables
- Feature Comparison
- Market Positioning

---

## Phase 4

Sentiment Analysis

Add:

```text
Sentiment Agent
```

Sources:

- Reddit
- Twitter/X
- Product Reviews
- Community Forums

---

## Phase 5

Human Review

Add:

```text
Human Approval Node
```

Workflow:

```text
Agents
 ↓
Human Review
 ↓
Final Report
```

---

## Phase 6

PDF Export

Generate:

- PDF Reports
- PowerPoint Reports
- Excel Market Sheets

---

## Phase 7

Multi-Agent Collaboration

Upgrade:

```text
Planner
   ↓
Research Team
   ├── Trend Agent
   ├── Pricing Agent
   ├── Sentiment Agent
   └── Competitor Agent
   ↓
Reviewer Agent
   ↓
Report Agent
```

---

## Phase 8

Persistent Memory

Add:

- PostgreSQL
- Vector Database

Options:

- pgvector
- Chroma
- Qdrant

Capabilities:

- Historical Research
- Competitive Tracking
- Knowledge Base

---

# Future Enterprise Features

- Multi Tenant Support
- Authentication
- RBAC
- Research History
- Report Library
- Scheduled Research
- Email Reports
- Executive Dashboards
- Team Collaboration

---

# Tech Stack

Frontend

- React
- Axios

Backend

- FastAPI
- LangGraph
- LangChain

LLM

- OpenAI
- Ollama

Search

- Tavily

Deployment

- Docker
- Azure App Service
- Azure Container Apps
- Kubernetes

---

# License

MIT License