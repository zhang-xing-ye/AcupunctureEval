# AcupunctureEval Frontend

本目录为前端站点（Vue 3 + Vite）。目前主要提供：

- 首页/数据集介绍页面
- 排行榜页面 UI（**当前数据为 mock，尚未对接后端接口**）

---

## 快速开始（Windows）

在本目录（frontend/）打开终端：

```powershell
npm install
npm run dev
```

然后打开终端输出的地址（通常为 `http://127.0.0.1:5173/`）。

---

## 最小对接说明（计划近期对接）

目标：让排行榜页面从后端读取数据。

后端接口（默认 `http://127.0.0.1:8000`）：

- `GET /qa/data?skip=0&limit=20`
- `GET /vqa/data?skip=0&limit=20`

### 方式 1：Vite dev server 代理（推荐）

在 `vite.config.js` 配置 `server.proxy`，例如把 `/api` 代理到后端：

- 前端请求：`/api/qa/data?skip=0&limit=20`
- 代理到：`http://127.0.0.1:8000/qa/data?skip=0&limit=20`

（Vite 官方配置项：`server.proxy`，详见 Vite 文档。）

### 方式 2：直接请求后端（不走代理）

直接请求 `http://127.0.0.1:8000/qa/data` / `http://127.0.0.1:8000/vqa/data`。

注意：后端当前已开启 CORS（允许任意来源），本地开发一般可直接调用。

---

## 数据结构（对接排行榜表格需要）

后端返回是记录列表，每条记录包含：

- 模型信息：`llm_name`、`llm_org`
- 分数：
	- QA：`a1_score`、`a2_score`、`a3_score`、`a4_score`、`b_score`、`x_score`、`avg_score`
	- VQA：`type_one_single_score`、`type_one_multi_score`、`type_two_score`、`type_three_score`、`avg_score`
- 时间字段（如果存在）：`created_at`/`created_time`（以实际接口返回为准）

前端对接时，建议做一次字段映射层（例如把 `avg_score` 映射为 UI 的 `score`）。

---

## 数据集说明

- 当前公开的 QA/VQA JSON（位于 `datasets/qa` 与 `datasets/vqa`）仅保留每个文件的前 2 道题目，作为轻量示例。
- 需要完整题库时，请使用 `backup/` 下的 `*_full.json`（例如 `backup/datasets/qa/A1_full.json` 或 `backup/datasets/vqa/第一类题型/单选题_324题_full.json`）。
- 你可以通过 `backend/scripts/trim_datasets.py` 从 `backup/**/_full.json` 重新生成 trimmed 样例。
- 说明：`backup/` 默认被 `.gitignore` 忽略，不会提交到仓库。
