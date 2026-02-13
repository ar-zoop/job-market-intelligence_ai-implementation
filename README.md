# Job Market Intelligence System
A backend system that analyzes multiple job descriptions against a candidate’s resume to determine job fit, skill gaps, and high-ROI learning priorities. This is done using LLM-assisted reasoning and deterministic scoring logic.

## What’s in this repo (current)

### Job description analyzer (LLM → structured JSON)
- **`analyzer.py`**: wraps an LLM call and converts raw job description text into **structured JSON** using a strict schema and a fixed system prompt.
- **Provider details**: configured to use the **DeepSeek** OpenAI-compatible API via `langchain-openai`:
  - model: `deepseek-chat`
  - base URL: `https://api.deepseek.com`
  - API key: `OPENAI_API_KEY` (loaded from environment / `.env`)

### HTTP API (Flask)
- **`app.py`** exposes a small API on port **8000**:
  - **GET `/health`**: basic health check.
  - **POST `/analyze`**: analyzes a job description and returns JSON.

Request body:
```json
{
  "job_description": "raw job description text...",
  "save": false
}
```

Response:
- **Success**: `{ "result": <parsed JSON> }`
- **If the model returns non-JSON**: `{ "result": { "raw": "<model output>" } }`
- **Errors**: `{ "error": "..." }` with an appropriate HTTP status code

Optional persistence:
- If `"save": true`, the server saves the parsed output to **`jds/jd_<timestamp>.json`**.

<img width="3200" height="1904" alt="image" src="https://github.com/user-attachments/assets/777e7118-ac49-445d-86fe-1e42f59a4941" />

### Local script runner (examples)
- **`jd.py`**: sample script that calls `analyze_job_description()` for two in-file job descriptions and writes outputs to:
  - `jds/jd_1.json`
  - `jds/jd_2.json`

## Setup & run

### 1) Install dependencies
```bash
pip install -r requirements.txt
```

### 2) Configure environment
Create a `.env` file (or set environment variables) with:
- **`OPENAI_API_KEY`**: your DeepSeek API key (used by the OpenAI-compatible endpoint).

### 3) Run the API
```bash
python app.py
```

Then call the service, for example:
```bash
curl -X POST http://localhost:8000/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"job_description\":\"Senior backend engineer...\",\"save\":false}"
```
