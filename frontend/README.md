# AcupunctureEval Frontend

[中文](README.md) | [English](README_EN.md)

本目录为前端站点（Vue 3 + Vite）。目前主要提供：

- 首页/数据集介绍页面
- 排行榜页面（从后端接口读取数据）

---

## 快速开始（Windows）

在本目录（frontend/）打开终端：

```powershell
npm install
npm run dev
```

然后打开终端输出的地址（通常为 `http://127.0.0.1:5173/`）。

---

## 与后端联调说明

默认情况下，前端会请求同一台机器上的 `http://<host>:8000`（见 `src/utils/request.js`）。

后端接口：

- `GET /qa/data?skip=0&limit=20`
- `GET /vqa/data?skip=0&limit=20`

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

- 仓库内提供的 QA/VQA JSON 用于演示与联调。
- 如果你有自己的完整题库/标准答案，可替换 `datasets/` 与 `backend/datasets/` 下的文件，再按相同格式提交预测进行评测。

