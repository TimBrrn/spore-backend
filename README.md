# BioSamples Back

Backend service built with **FastAPI** (tested on Python 3.13.5; works on 3.10+) and an embedded **SQLite** database stored in `data/`.

---

## Prerequisites

- Python **3.10 or newer**
- `virtualenv` or any tool that can create a local venv
- `pip` 23+

---

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Environment variables (create a .env file at the repo root)
DATABASE_URL="sqlite:///./data/spore.db"

# 4. Start the server (default port: http://127.0.0.1:8000)
uvicorn main:app

```

## Project Layout

```bash
.
├─ data/           # SQLite file lives here
├─ routes/         # FastAPI routers
├─ schemas/        # Pydantic models
├─ services/       # Business logic
├─ main.py         # FastAPI entrypoint
└─ requirements.txt
```
