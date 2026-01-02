# 冒烟测试预测文件

此目录包含从标准答案自动生成的预测文件，用于快速验证评测逻辑。

## 文件说明

### VQA预测文件（vqa/）
- `single_choice.json`: 第一类题型-单选题（324题）
- `multi_choice.json`: 第一类题型-多选题（600题）
- `location.json`: 第二类题型-定位题（37题）
- `operation.json`: 第三类题型-针灸操作题（35题）

### QA预测文件（qa/）
- `a1_predictions.json`: A1题型（单选）
- `a2_predictions.json`: A2题型（单选）
- `a3_predictions.json`: A3题型（共享题干+子题）
- `a4_predictions.json`: A4题型（共享题干+子题）
- `b_predictions.json`: B题型（共享选项+子题）
- `x_predictions.json`: X题型（多选）

## 使用方式

1. 运行脚本生成预测文件（建议在 backend/ 目录执行）：
   ```powershell
   cd e:\科研\中医Benchmark\AcupunctureEval\backend
   conda activate acue
   python scripts/generate_test_predictions.py
   ```

2. 在 `/docs` 页面使用生成的文件进行评测测试

3. **预期结果**：所有题型的准确率应为 1.0（100%）

## 重新生成

如果标准答案文件有更新，重新运行脚本即可：
```powershell
python scripts/generate_test_predictions.py
```

## 说明

- 此脚本读取 `backup/backend/datasets/qa/*_full.json` 与 `backup/backend/datasets/vqa/*_full.json`，以确保冒烟预测覆盖完整题库。
- 如果你只希望对外展示前 2 道题，可通过 `backend/scripts/trim_datasets.py` 从 `backup/**/_full.json` 重新生成 trimmed 样例 `backend/datasets/qa/*.json` 与 `backend/datasets/vqa/**/*.json`。
