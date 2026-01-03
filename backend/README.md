
# AcupunctureEval Backend

[中文](README.md) | [English](README_EN.md)

本目录为后端服务（FastAPI + SQLite）。后端负责：

- 读取标准答案数据集（`backend/datasets/`，为公开样例）
- 接收模型预测文件（JSON），计算分数
- 将评测结果写入 SQLite（acue_app.db）
- 提供排行榜查询接口

## 快速开始（Windows）

在本目录（backend/）打开终端：

```powershell
conda create -n acue python=3.12
conda activate acue
pip install -r requirements.txt

# 初始化数据库（仅首次需要）
python init_db.py

# 启动服务
fastapi dev main.py
```

启动后访问：

- Swagger UI：`http://127.0.0.1:8000/docs`

## 接口概览

### VQA

- `POST /vqa/evaluate`：上传 4 个 JSON 预测文件，计算各题型分数并写入排行榜
- `GET /vqa/data?skip=0&limit=10`：分页读取 VQA 排行榜（按 avg_score 降序）

### QA

- `POST /qa/evaluate`：上传 6 个 JSON 预测文件（A1/A2/A3/A4/B/X），计算分数并写入排行榜
- `GET /qa/data?skip=0&limit=10`：分页读取 QA 排行榜（按 avg_score 降序）

## 预测文件格式（关键）

### 扁平题型（VQA/QA 的单选、多选）

JSON 数组，每个元素至少包含：

- `ID`（或 `id`）：题目唯一标识
- `output`（或 `Output`）：预测结果

单选示例：

```json
[
	{"ID": "1", "output": "A"}
]
```

多选支持以下输入形式（会统一标准化）：

- 列表：`["A", "C"]`
- 逗号分隔字符串：`"A,C"`
- 空格分隔字符串：`"A C"`
- 连写字符串：`"AC"`

### 分组题型（A3/A4/B）

JSON 数组，每个元素是“父题”，至少包含：

- `ID`（或 `id`）：父题 ID
- `outputs`（或 `Outputs`）：按子题顺序排列的预测数组

示例（`outputs` 为“子题答案序列”，每个元素对应一个子题）：

```json
[
	{"ID": "A3-001", "outputs": ["A", "C"]}
]
```

如果你的数据里子题答案本身是列表（例如 `"answer": ["A"]`），也允许：

```json
[
	{"ID": "A3-001", "outputs": [["A"], ["C"]]}
]
```

后端会对 A3/A4/B 做更严格的结构校验（父题 ID、outputs 类型、子题数量一致性）。

## 示例预测生成（可选）

用于快速验证“上传→评分→入库”的最小闭环：

```powershell
conda activate acue
python scripts/generate_test_predictions.py
```

生成目录：`backend/scripts/test_predictions/`（本地运行时生成，默认已被仓库的 `.gitignore` 忽略）。

## 标准答案数据集路径

- VQA：`backend/datasets/vqa/` 下的各题型 JSON
- QA：`backend/datasets/qa/A1.json` / `A2.json` / `A3.json` / `A4.json` / `B.json` / `X.json`

## 代码入口（读代码顺序）

1. main.py：FastAPI 应用入口与路由挂载
2. router/vqaRouter.py、router/qaRouter.py：接口与业务流程
3. core/eval.py：公共评测逻辑（解析/校验/对齐/计分）
4. dao/* + model/*：排行榜数据入库与查询


