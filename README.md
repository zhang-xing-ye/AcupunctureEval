## AcupunctureEval

一个面向“针灸/中医”题库的轻量评测与展示项目：

- 后端（FastAPI + SQLite）：提供 VQA 评测 API、记录并查询排行榜
- 前端（Vue3 + Vite）：展示首页、数据集介绍、排行榜页面（当前排行榜为 mock 数据，尚未对接后端）

文档分层（方案B）：

- 后端细节见：`backend/README.md`
- 前端细节见：`frontend/README.md`

---

## 你能用它做什么（当前能力）

- 启动后端服务，在 `/docs` 里直接调用接口
- **VQA 评测**：通过 `POST /vqa/evaluate` 上传模型预测文件（4个JSON），得到分数并写入 SQLite；通过 `GET /vqa/data` 分页读取排行榜记录
- **QA 评测**：通过 `POST /qa/evaluate` 上传模型预测文件（6个JSON：A1/A2/A3/A4/B/X），得到分数并写入 SQLite；通过 `GET /qa/data` 分页读取排行榜记录

补充：

- 提供“冒烟预测文件生成脚本”，可从标准答案生成 100% 正确的预测文件，用于快速回归验证（见 `backend/scripts/generate_test_predictions.py`）
- QA 分组题型（A3/A4/B）在评测前会做更严格的结构校验，避免静默错对齐
- 多选题答案支持多种输入格式（"A,C" / "A C" / "AC" / ["A","C"]），后端会统一标准化

---

## 快速开始（Windows，新手推荐）

### 0) 先决条件

- 已安装 Conda（Miniconda/Anaconda 皆可）
- 已安装 Node.js（建议 >= 18）与 npm

### 1) 后端：创建环境、安装依赖、建库、启动

在项目根目录下打开终端，执行：

```powershell
cd e:\科研\中医Benchmark\AcupunctureEval\backend

# 仅首次需要：创建环境
conda create -n acue python=3.12

conda activate acue
pip install -r requirements.txt

# 仅首次需要：初始化 SQLite 表
python init_db.py

# 启动后端（开发模式）
fastapi dev main.py
```

启动成功后：

- 打开 `http://127.0.0.1:8000/docs`
- 你应该能看到：
  - VQA 评测：`POST /vqa/evaluate`、`GET /vqa/data`
  - QA 评测：`POST /qa/evaluate`、`GET /qa/data`

### 2) 后端：验证数据库里是否有记录（可选）

在 `backend/` 目录下：

```powershell
conda activate acue
python test.py
```

### 3) 前端：安装依赖并启动

打开另一个终端，执行：

```powershell
cd e:\科研\中医Benchmark\AcupunctureEval\frontend
npm install
npm run dev
```

然后打开终端输出的地址（通常是 `http://127.0.0.1:5173/`）。

> 说明：当前前端页面不依赖后端也能跑起来（排行榜是 mock 数据）。

---

## 项目“文字版架构图”（读代码必看）

```
┌───────────────┐     (未来：HTTP 调用)     ┌──────────────────────────────┐
│  前端 Vue3/Vite │ ───────────────────────> │   后端 FastAPI（backend/）    │
│  - Home         │                          │  main.py -> router/vqaRouter │
│  - Datasets      │ <────────────────────── │  /vqa/data (排行榜查询)       │
│  - Leaderboard   │     (未来：返回榜单)     │  /vqa/evaluate (上传评测)     │
└───────────────┘                          └───────────────┬──────────────┘
																													 │ Depends(get_db)
																													 ▼
																								┌───────────────────────────┐
																								│  core/database.py          │
																								│  - SQLite engine/session   │
																								│  - get_db 依赖注入          │
																								└───────────────┬───────────┘
																																│ ORM Session
																																▼
																								┌───────────────────────────┐
																								│ dao/*  <-> model/*         │
																								│ - 写入/查询排行榜记录        │
																								└───────────────┬───────────┘
																																│ 读取标准答案
																																▼
																								┌───────────────────────────┐
																								│ backend/datasets/vqa/*     │
																								│ - VQA 标准答案（ground truth）│
																								└───────────────────────────┘
```

---

## 目录结构（从哪里开始读）

建议按这个顺序阅读：

1) 后端入口：`backend/main.py`
2) 业务主链路：`backend/router/vqaRouter.py`
3) 数据库基础设施：`backend/core/database.py`
4) 数据访问层：`backend/dao/*.py`
5) 表结构：`backend/model/*.py`
6) 前端入口：`frontend/src/main.js` 与 `frontend/src/router/index.js`

---

## 接口说明（后端）

### VQA 评测

#### 1) `POST /vqa/evaluate`

用途：上传预测结果文件，按标准答案计算四类题型得分并写入排行榜。

请求（multipart/form-data）：
- 表单字段：`llm_name`、`llm_org`
- 文件字段：4 个 JSON（对应单选/多选/定位/操作题）

返回：四类分数 + `average_score` 等。

#### 2) `GET /vqa/data`

用途：分页查询VQA排行榜（按 `avg_score` 降序）。

参数：`skip`、`limit`

### QA 评测

#### 1) `POST /qa/evaluate`

用途：上传6个JSON文件（A1/A2/A3/A4/B/X题型），按标准答案计算各题型得分并写入排行榜。

请求（multipart/form-data）：
- 表单字段：`llm_name`、`llm_org`
- 文件字段：6 个 JSON
  - `file_a1`：A1题型（单选）
  - `file_a2`：A2题型（单选）
  - `file_a3`：A3题型（共享题干+子题）
  - `file_a4`：A4题型（共享题干+子题）
  - `file_b`：B题型（共享选项+子题）
  - `file_x`：X题型（多选）

返回：六个题型分数 + `average_score` 等。

**预测文件格式要求**：
- **扁平题型（A1/A2/X）**：JSON数组，每项包含 `ID` 和 `output`（单选用 `"A"`，多选用 `["A","C"]`）
- **分组题型（A3/A4/B）**：JSON数组，每项包含父题 `ID` 和 `outputs`（按子题顺序的数组；元素可以是 `"A"`，也可以是 `["A"]`，以兼容不同标准答案格式）

**多选题 output 兼容格式**（等价）：

- `["A","C"]`
- `"A,C"`
- `"A C"`
- `"AC"`

#### 2) `GET /qa/data`

用途：分页查询QA排行榜（按 `avg_score` 降序）。

参数：`skip`、`limit`

**最稳妥的调试方式**：打开 `/docs`，在 Swagger UI 里直接上传文件。

---

## 运行与导入约定（重要）

后端约定：把 `backend/` 视为 Python 包根目录。

- 正确做法：进入 `backend/` 再运行（`fastapi dev main.py` 或 `python init_db.py`）
- 避免：在业务代码中使用 `sys.path.append(...)` 这类硬编码路径

更多说明见：`backend/README_IMPORTS.md`

---

## 标准答案数据集位置

- **公开样例（每个 JSON 仅保留前 2 道题目）**

	- root/datasets：
		- QA：`datasets/qa/A1.json` / `A2.json` / `A3.json` / `A4.json` / `B.json` / `X.json`
		- VQA：`datasets/vqa/第一类题型/`、`datasets/vqa/第二类题型/`、`datasets/vqa/第三类题型/`
	- backend/datasets（供后端评测使用）：
		- QA：`backend/datasets/qa/A1.json`…`X.json`
		- VQA：`backend/datasets/vqa/第一类题型/` 等

- **完整备份（保留所有题目，文件名以 `_full.json` 结尾）**
	- QA：`backup/datasets/qa/A1_full.json` … `X_full.json`（后端脚本读取 `backup/backend/datasets/qa/*.json`）
	- VQA：`backup/datasets/vqa/<题型>/<文件名>_full.json`（后端脚本读取 `backup/backend/datasets/vqa/<题型>/<文件名>_full.json`）
	- 说明：`backup/` 默认被 `.gitignore` 忽略，不会提交到仓库

- 使用 `backend/scripts/trim_datasets.py` 可从 `backup/**/_full.json` 重新生成上述“前两题”样例

---

## 现状与后续重构建议（你补写/重构时用）

### 稳定边界（尽量别破坏）

- 后端 API 路径与语义：`/vqa/*`、`/qa/*`
- 数据库会话管理：`core/database.py` 的 `get_db` 使用方式
- 榜单记录的核心字段：模型信息 + 各子分数 + 平均分 + 时间
- 公共评测模块：`core/eval.py` 的函数签名与行为

### 易变部分（推荐优先重构/补齐）

- ~~QA 路由未实现：`backend/router/qaRouter.py` 目前为空~~ ✅ 已完成
- ~~可抽象复用：VQA 路由中"文件预检查/对齐校验/评分计算"的公共逻辑~~ ✅ 已完成
- 前端未对接后端：Leaderboard 目前是 mock，可新增 API client（fetch/axios）对接 `/vqa/data` 和 `/qa/data`

---

## 常见问题（Troubleshooting）

- **导入失败 / ModuleNotFoundError**：请确认当前工作目录是 `backend/`，并遵循 `README_IMPORTS.md` 的导入规范
- **端口占用**：
	- 后端默认 `8000`（换端口可用 `fastapi dev main.py --port 8001` 或按 FastAPI CLI 参数调整）
	- 前端默认 `5173`，端口被占用时 Vite 会自动尝试下一个可用端口
- **找不到数据库文件**：SQLite 文件在 `backend/acue_app.db`

