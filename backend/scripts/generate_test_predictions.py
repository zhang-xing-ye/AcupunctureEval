"""
生成冒烟测试用的预测文件
从标准答案自动生成100%正确的预测文件，用于快速验证评测逻辑
"""
import json
import os
from pathlib import Path
from typing import Dict, Any, List

BASE_DIR = Path(__file__).parent.parent
REPO_ROOT = BASE_DIR.parent
BACKUP_DIR = REPO_ROOT / "backup" / "backend" / "datasets"
OUTPUT_DIR = BASE_DIR / "scripts" / "test_predictions"


def generate_vqa_predictions():
    """生成VQA预测文件（从标准答案转换）"""
    print("生成VQA预测文件...")

    vqa_dir = BACKUP_DIR / "vqa"
    output_vqa_dir = OUTPUT_DIR / "vqa"
    output_vqa_dir.mkdir(parents=True, exist_ok=True)

    # VQA四个题型
    vqa_files = {
        "第一类题型/单选题_324题_full.json": "single_choice.json",
        "第一类题型/多选题_600题_full.json": "multi_choice.json",
        "第二类题型/定位题_37题_full.json": "location.json",
        "第三类题型/针灸操作题_35题_full.json": "operation.json"
    }

    for src_path, dst_name in vqa_files.items():
        src_file = vqa_dir / src_path
        if not src_file.exists():
            print(f"  ⚠️  标准答案文件不存在: {src_file}")
            continue

        with open(src_file, 'r', encoding='utf-8') as f:
            gt_data = json.load(f)

        # 转换为预测格式：answer -> output
        predictions = []
        for item in gt_data:
            pred_item = {
                "ID": item.get("ID"),
                "output": item.get("Answer")  # 使用标准答案作为预测输出
            }
            predictions.append(pred_item)

        output_file = output_vqa_dir / dst_name
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(predictions, f, ensure_ascii=False, indent=2)

        print(f"  ✓ 生成 {dst_name}: {len(predictions)} 题")


def generate_qa_flat_predictions():
    """生成QA扁平题型预测文件（A1/A2/X）"""
    print("\n生成QA扁平题型预测文件...")

    qa_dir = BACKUP_DIR / "qa"
    output_qa_dir = OUTPUT_DIR / "qa"
    output_qa_dir.mkdir(parents=True, exist_ok=True)

    # 扁平题型
    flat_types = {
        "A1_full.json": "a1_predictions.json",
        "A2_full.json": "a2_predictions.json",
        "X_full.json": "x_predictions.json"
    }

    for src_name, dst_name in flat_types.items():
        src_file = qa_dir / src_name
        if not src_file.exists():
            print(f"  ⚠️  标准答案文件不存在: {src_file}")
            continue

        with open(src_file, 'r', encoding='utf-8') as f:
            gt_data = json.load(f)

        # 转换为预测格式：answer -> output
        predictions = []
        for item in gt_data:
            pred_item = {
                "ID": item.get("ID"),
                "output": item.get("answer")  # QA使用小写answer
            }
            predictions.append(pred_item)

        output_file = output_qa_dir / dst_name
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(predictions, f, ensure_ascii=False, indent=2)

        print(f"  ✓ 生成 {dst_name}: {len(predictions)} 题")


def generate_qa_grouped_predictions():
    """生成QA分组题型预测文件（A3/A4/B）"""
    print("\n生成QA分组题型预测文件...")

    qa_dir = BACKUP_DIR / "qa"
    output_qa_dir = OUTPUT_DIR / "qa"
    output_qa_dir.mkdir(parents=True, exist_ok=True)

    # 分组题型
    grouped_types = {
        "A3_full.json": "a3_predictions.json",
        "A4_full.json": "a4_predictions.json",
        "B_full.json": "b_predictions.json"
    }

    for src_name, dst_name in grouped_types.items():
        src_file = qa_dir / src_name
        if not src_file.exists():
            print(f"  ⚠️  标准答案文件不存在: {src_file}")
            continue

        with open(src_file, 'r', encoding='utf-8') as f:
            gt_data = json.load(f)

        # 转换为预测格式：questions[*].answer -> outputs
        predictions = []
        for item in gt_data:
            # 提取所有子题的答案
            questions = item.get("questions", [])
            outputs = []
            for q in questions:
                answer = q.get("answer")
                outputs.append(answer)
            
            pred_item = {
                "ID": item.get("ID"),
                "outputs": outputs  # 按子题顺序排列的答案数组
            }
            predictions.append(pred_item)
        
        output_file = output_qa_dir / dst_name
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(predictions, f, ensure_ascii=False, indent=2)
        
        total_questions = sum(len(p["outputs"]) for p in predictions)
        print(f"  ✓ 生成 {dst_name}: {len(predictions)} 个父题，{total_questions} 个子题")


def generate_readme():
    """生成说明文档"""
    readme_content = """# 冒烟测试预测文件

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

1. 运行脚本生成预测文件：
   ```bash
   python scripts/generate_test_predictions.py
   ```

2. 在 `/docs` 页面使用生成的文件进行评测测试

3. **预期结果**：所有题型的准确率应为 1.0（100%）

## 重新生成

如果标准答案文件有更新，重新运行脚本即可：
```bash
python scripts/generate_test_predictions.py
```
"""
    
    readme_file = OUTPUT_DIR / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✓ 生成说明文档: {readme_file}")


def main():
    """主函数"""
    print("=" * 60)
    print("开始生成冒烟测试预测文件")
    print("=" * 60)
    
    # 创建输出目录
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 生成各类预测文件
    generate_vqa_predictions()
    generate_qa_flat_predictions()
    generate_qa_grouped_predictions()
    generate_readme()
    
    print("\n" + "=" * 60)
    print("✓ 完成！所有预测文件已生成到:")
    print(f"  {OUTPUT_DIR}")
    print("\n使用方法:")
    print("  1. 启动后端: fastapi dev main.py")
    print("  2. 访问 http://127.0.0.1:8000/docs")
    print("  3. 使用生成的预测文件测试评测接口")
    print("  4. 预期所有准确率为 1.0 (100%)")
    print("=" * 60)


if __name__ == "__main__":
    main()
