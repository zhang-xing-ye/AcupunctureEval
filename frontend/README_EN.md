# AcupunctureEval Frontend

[中文](README.md) | [English](README_EN.md)

This directory contains the frontend site (Vue 3 + Vite). It mainly provides:

- Home / dataset introduction page
- Leaderboard page (fetching data from backend APIs)

---

## Quick Start (Windows)

Open a terminal in this directory (`frontend/`):

```powershell
npm install
npm run dev
```

Then open the URL shown in the terminal output (typically `http://127.0.0.1:5173/`).

---

## Backend Integration Notes

By default, the frontend requests `http://<host>:8000` on the same machine (see `src/utils/request.js`).

Backend APIs:

- `GET /qa/data?skip=0&limit=20`
- `GET /vqa/data?skip=0&limit=20`

---

## Data Shape (for leaderboard tables)

The backend returns a list of records. Each record contains:

- Model info: `llm_name`, `llm_org`
- Scores:
  - QA: `a1_score`, `a2_score`, `a3_score`, `a4_score`, `b_score`, `x_score`, `avg_score`
  - VQA: `type_one_single_score`, `type_one_multi_score`, `type_two_score`, `type_three_score`, `avg_score`
- Time fields (if present): `created_at` / `created_time` (depending on the actual API response)

On the frontend, it is recommended to add a small mapping layer (e.g. map `avg_score` to the UI field `score`).

---

## Dataset Notes

- The QA/VQA JSON files included in this repo are for demo and integration.
- If you have your own full question bank / reference answers, you can replace the files under `datasets/` and `backend/datasets/`, then submit predictions in the same format for evaluation.
