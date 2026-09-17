# Employee list maintenance

Local Flask API and Vite React page for maintaining one organization-wide employee list. This foundation runbook covers install and start commands only.

Requires **Python 3.14.7** and **Node.js 22 LTS**.

## Install

```bash
python3.14 -m venv backend/.venv
source backend/.venv/bin/activate
pip install -r backend/requirements.txt
cd frontend && npm install
```

On Windows, activate with `backend\.venv\Scripts\activate`.

## Run Flask

```bash
source backend/.venv/bin/activate
python backend/app.py
```

API: `http://127.0.0.1:5000` (health: `GET /health`). CORS allows the Vite origin `http://localhost:5173`.

## Run Vite

```bash
cd frontend
npm run dev
```

App: `http://localhost:5173`.

## Run pytest

```bash
source backend/.venv/bin/activate
cd backend
pytest
```
