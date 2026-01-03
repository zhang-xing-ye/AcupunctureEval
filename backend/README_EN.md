# AcupunctureEval Backend

[中文](README.md) | [English](README_EN.md)

This directory contains the backend service (FastAPI + SQLite). The backend is responsible for:

- Loading the reference dataset (`backend/datasets/`, public demo samples)
- Receiving model prediction files (JSON) and computing scores
- Writing evaluation results into SQLite (`acue_app.db`)
- Providing leaderboard query APIs

## Quick Start (Windows)

Open a terminal in this directory (`backend/`):

```powershell
conda create -n acue python=3.12
conda activate acue
pip install -r requirements.txt

# Initialize database (only needed once)
python init_db.py

# Start the service (development)
fastapi dev main.py
```

After it starts:

- Swagger UI: `http://127.0.0.1:8000/docs`

## API Overview

### VQA

- `POST /vqa/evaluate`: upload 4 JSON prediction files, compute scores per question type, and write to the leaderboard
- `GET /vqa/data?skip=0&limit=10`: paginate VQA leaderboard (sorted by `avg_score` descending)

### QA

- `POST /qa/evaluate`: upload 6 JSON prediction files (A1/A2/A3/A4/B/X), compute scores, and write to the leaderboard
- `GET /qa/data?skip=0&limit=10`: paginate QA leaderboard (sorted by `avg_score` descending)

## Prediction File Format (Important)

### Flat question types (single-choice / multi-choice in VQA & QA)

A JSON array. Each element must contain at least:

- `ID` (or `id`): unique question identifier
- `output` (or `Output`): model prediction

Single-choice example:

```json
[
  {"ID": "1", "output": "A"}
]
```

For multi-choice, the backend accepts these input forms (and normalizes them):

- Array: `["A", "C"]`
- Comma-separated string: `"A,C"`
- Space-separated string: `"A C"`
- Concatenated string: `"AC"`

### Grouped question types (A3/A4/B)

A JSON array. Each element is a “parent question” and must contain at least:

- `ID` (or `id`): parent question ID
- `outputs` (or `Outputs`): an array of predictions in the sub-question order

Example (`outputs` is the “sub-answer sequence”; each element corresponds to one sub-question):

```json
[
  {"ID": "A3-001", "outputs": ["A", "C"]}
]
```

If your sub-question answer itself is a list (e.g. `"answer": ["A"]`), this is also supported:

```json
[
  {"ID": "A3-001", "outputs": [["A"], ["C"]]}
]
```

The backend applies stricter structural validation for A3/A4/B (parent ID, `outputs` type, consistency of sub-question count).

## Generate Example Predictions (Optional)

For quickly validating the minimal loop of “upload → score → write to DB”:

```powershell
conda activate acue
python scripts/generate_test_predictions.py
```

Output directory: `backend/scripts/test_predictions/` (generated locally; ignored by the repo’s `.gitignore` by default).

## Reference Dataset Paths

- VQA: JSON files under `backend/datasets/vqa/`
- QA: `backend/datasets/qa/A1.json` / `A2.json` / `A3.json` / `A4.json` / `B.json` / `X.json`

## Code Entry Points (Suggested reading order)

1. `main.py`: FastAPI app entry and router mounting
2. `router/vqaRouter.py`, `router/qaRouter.py`: endpoints and evaluation workflow
3. `core/eval.py`: shared evaluation logic (parse/validate/align/score)
4. `dao/*` + `model/*`: leaderboard persistence and queries
