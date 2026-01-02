from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
import logging
from core.database import get_db
from core import eval as eval_utils
from dao import qa_leaderboard_dao
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/qa", tags=["QA Leaderboard"])

# 标准答案路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_BASE_PATH = os.path.join(BASE_DIR, "datasets", "qa")

A1_PATH = os.path.join(DATASET_BASE_PATH, "A1.json")
A2_PATH = os.path.join(DATASET_BASE_PATH, "A2.json")
A3_PATH = os.path.join(DATASET_BASE_PATH, "A3.json")
A4_PATH = os.path.join(DATASET_BASE_PATH, "A4.json")
B_PATH = os.path.join(DATASET_BASE_PATH, "B.json")
X_PATH = os.path.join(DATASET_BASE_PATH, "X.json")


def calculate_grouped_accuracy(
    predictions: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
    dataset_name: str,
) -> float:
    """
    计算分组题型（A3/A4/B）的准确率
    这些题型有父题ID和子题列表，需要按父题对齐后再计算子题准确率

    Args:
        predictions: 预测数据，每项包含父题ID和outputs数组
        ground_truth: 标准答案，每项包含父题ID和questions数组
        dataset_name: 数据集名称

    Returns:
        准确率
    """
    total_count = 0
    correct_count = 0

    # 构建标准答案映射
    gt_map = {}
    for gt_item in ground_truth:
        parent_id = str(gt_item.get('ID'))
        questions = gt_item.get('questions', [])
        # 存储每个子题的答案
        gt_map[parent_id] = [
            eval_utils.normalize_field_name(q, 'answer', ['Answer'])
            for q in questions
        ]
        total_count += len(questions)

    # 构建预测映射
    pred_map = {}
    for pred_item in predictions:
        parent_id = str(pred_item.get('ID') or pred_item.get('id'))
        # 兼容outputs/Outputs
        outputs = eval_utils.normalize_field_name(pred_item, 'outputs', ['Outputs'])
        if outputs and isinstance(outputs, list):
            pred_map[parent_id] = outputs

    # 对齐计分
    for parent_id, gt_answers in gt_map.items():
        pred_outputs = pred_map.get(parent_id)

        if pred_outputs is None:
            logger.warning(f"[{dataset_name}] 父题 {parent_id} 缺少预测结果")
            continue

        # 验证子题数量
        if len(pred_outputs) != len(gt_answers):
            logger.warning(
                f"[{dataset_name}] 父题 {parent_id} 子题数量不匹配: "
                f"预测 {len(pred_outputs)} 题，标准答案 {len(gt_answers)} 题"
            )

        # 按顺序对齐子题
        for i, gt_answer in enumerate(gt_answers):
            if i >= len(pred_outputs):
                break

            pred_output = pred_outputs[i]

            # 使用单选题计分逻辑（因为答案都是数组，取第一个元素比对）
            if eval_utils.score_single_choice(pred_output, gt_answer):
                correct_count += 1

    if total_count == 0:
        return 0.0

    return round(correct_count / total_count, 4)


@router.post("/evaluate", summary="QA选择题评测")
async def upload_and_calculate(
    llm_name: str = Form(..., description="模型名称"),
    llm_org: Optional[str] = Form(None, description="模型所属组织"),
    file_a1: UploadFile = File(..., description="A1题型JSON文件"),
    file_a2: UploadFile = File(..., description="A2题型JSON文件"),
    file_a3: UploadFile = File(..., description="A3题型JSON文件"),
    file_a4: UploadFile = File(..., description="A4题型JSON文件"),
    file_b: UploadFile = File(..., description="B题型JSON文件"),
    file_x: UploadFile = File(..., description="X题型（多选题）JSON文件"),
    db: Session = Depends(get_db)
):
    """
    接收用户上传的六个JSON文件，计算各题型正确率并存入数据库。
    """
    logger.info(f"Received QA evaluation request for {llm_name} from {llm_org}")

    # 1. 加载标准答案
    gt_a1 = eval_utils.load_json_file(A1_PATH)
    gt_a2 = eval_utils.load_json_file(A2_PATH)
    gt_a3 = eval_utils.load_json_file(A3_PATH)
    gt_a4 = eval_utils.load_json_file(A4_PATH)
    gt_b = eval_utils.load_json_file(B_PATH)
    gt_x = eval_utils.load_json_file(X_PATH)
    
    # 2. 读取并解析上传的文件
    pred_a1 = await eval_utils.parse_upload_file(file_a1)
    pred_a2 = await eval_utils.parse_upload_file(file_a2)
    pred_a3 = await eval_utils.parse_upload_file(file_a3)
    pred_a4 = await eval_utils.parse_upload_file(file_a4)
    pred_b = await eval_utils.parse_upload_file(file_b)
    pred_x = await eval_utils.parse_upload_file(file_x)
    
    # 3. 验证扁平题型（A1/A2/X）
    eval_utils.validate_predictions(pred_a1, gt_a1, "A1题型")
    eval_utils.validate_predictions(pred_a2, gt_a2, "A2题型")
    eval_utils.validate_predictions(pred_x, gt_x, "X题型（多选题）")
    
    # 验证分组题型（A3/A4/B）
    eval_utils.validate_grouped_predictions(pred_a3, gt_a3, "A3题型")
    eval_utils.validate_grouped_predictions(pred_a4, gt_a4, "A4题型")
    eval_utils.validate_grouped_predictions(pred_b, gt_b, "B题型")
    
    # 3.5. 数据一致性检查（非严格模式，仅记录警告）
    eval_utils.check_id_consistency(pred_a1, gt_a1, "A1题型", strict=False)
    eval_utils.check_id_consistency(pred_a2, gt_a2, "A2题型", strict=False)
    eval_utils.check_id_consistency(pred_a3, gt_a3, "A3题型", strict=False)
    eval_utils.check_id_consistency(pred_a4, gt_a4, "A4题型", strict=False)
    eval_utils.check_id_consistency(pred_b, gt_b, "B题型", strict=False)
    eval_utils.check_id_consistency(pred_x, gt_x, "X题型", strict=False)
    
    # 4. 计算正确率
    # A1/A2: 单选题
    score_a1 = eval_utils.calculate_accuracy(pred_a1, gt_a1, 'single')
    score_a2 = eval_utils.calculate_accuracy(pred_a2, gt_a2, 'single')
    
    # A3/A4/B: 分组题型（共享题干或选项 + 多个子题）
    score_a3 = calculate_grouped_accuracy(pred_a3, gt_a3, "A3题型")
    score_a4 = calculate_grouped_accuracy(pred_a4, gt_a4, "A4题型")
    score_b = calculate_grouped_accuracy(pred_b, gt_b, "B题型")
    
    # X: 多选题
    score_x = eval_utils.calculate_accuracy(pred_x, gt_x, 'multi')
    
    # 5. 计算平均分
    average_score = round(
        (score_a1 + score_a2 + score_a3 + score_a4 + score_b + score_x) / 6, 
        4
    )
    
    logger.info(
        f"QA Scores: A1={score_a1}, A2={score_a2}, A3={score_a3}, "
        f"A4={score_a4}, B={score_b}, X={score_x}, Avg={average_score}"
    )
    
    # 6. 存入数据库
    record = qa_leaderboard_dao.add_record(
        db,
        llm_name=llm_name,
        llm_org=llm_org or "",
        a1_score=score_a1,
        a2_score=score_a2,
        a3_score=score_a3,
        a4_score=score_a4,
        b_score=score_b,
        x_score=score_x,
        avg_score=average_score
    )
    
    if not record:
        raise HTTPException(status_code=500, detail="数据库保存失败")
    
    return {
        "llm_name": llm_name,
        "llm_org": llm_org,
        "a1_score": score_a1,
        "a2_score": score_a2,
        "a3_score": score_a3,
        "a4_score": score_a4,
        "b_score": score_b,
        "x_score": score_x,
        "average_score": average_score,
        "message": "QA评测完成并已记录"
    }


@router.get("/data", summary="获取QA排行数据")
async def get_all_data(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    获取QA数据表中所有记录，支持分页。
    """
    records = qa_leaderboard_dao.get_all_sorted_by_score(db, skip=skip, limit=limit)
    return records
