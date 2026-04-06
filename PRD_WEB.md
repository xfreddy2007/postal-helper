# Project Requirement Document

Use the current code structure to generate a web version of this postal helper application.

# Requirement for backend service

Use Flask framework for its backend API service

# Requirement for frontend service

Use plain HTML, CSS, and Javascript to (No pre-built Javascript framework).

# Implementation

## File Structure

```
postal-helper/
├── postal_helper.py          ← existing CLI core (unchanged)
├── app.py                    ← Flask backend
├── requirements.txt          ← Python dependencies
├── templates/
│   └── index.html            ← Single-page UI (Traditional Chinese)
└── static/
    ├── style.css             ← Styles
    └── script.js             ← Fetch-based lookup logic
```

## Backend (`app.py`)

- Imports `lookup_postal_code` directly from `postal_helper.py` — no duplication
- Routes:
  - `GET /` → serves `index.html`
  - `POST /api/lookup` → accepts `{"address": "..."}`, returns `{"zipcode6", "zipcode", "detail_url"}`
- HTTP 400 on missing address, HTTP 502 on upstream API failure

## Frontend

- Plain HTML/CSS/JS — no framework
- Address input + submit button
- Displays 6-digit code (preferred) or 5-digit fallback, plus optional detail link
- Loading state while request is in flight; error card on failure

## Setup & Run

```bash
pip install -r requirements.txt
python3 app.py
# Open http://127.0.0.1:5000
```

## API Test

```bash
curl -X POST http://127.0.0.1:5000/api/lookup \
  -H "Content-Type: application/json" \
  -d '{"address":"台北市杭州南路一段23號"}'
```
