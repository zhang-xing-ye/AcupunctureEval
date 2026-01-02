from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
import logging
from core.database import get_db
from core import eval as eval_utils
from dao import vqa_leaderboard_dao
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/vqa", tags=["VQA Leaderboard"])

# 标准答案路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_BASE_PATH = os.path.join(BASE_DIR, "datasets", "vqa")

TYPE_ONE_SINGLE_PATH = os.path.join(DATASET_BASE_PATH, "第一类题型", "单选题_324题.json")
TYPE_ONE_MULTI_PATH = os.path.join(DATASET_BASE_PATH, "第一类题型", "多选题_600题.json")
TYPE_TWO_PATH = os.path.join(DATASET_BASE_PATH, "第二类题型", "定位题_37题.json")
TYPE_THREE_PATH = os.path.join(DATASET_BASE_PATH, "第三类题型", "针灸操作题_35题.json")

@router.post("/evaluate", summary="文件上传与正确率计算")
async def upload_and_calculate(
    llm_name: str = Form(..., description="模型名称"),
    llm_org: Optional[str] = Form(None, description="模型所属组织"),
    file_type_one_single: UploadFile = File(..., description="第一类题型-单选题JSON文件"),
    file_type_one_multi: UploadFile = File(..., description="第一类题型-多选题JSON文件"),
    file_type_two: UploadFile = File(..., description="第二类题型-定位题JSON文件"),
    file_type_three: UploadFile = File(..., description="第三类题型-针灸操作题JSON文件"),
    db: Session = Depends(get_db)
):
    """
    接收用户上传的四个JSON文件，计算各题型正确率并存入数据库。
    """
    logger.info(f"Received evaluation request for {llm_name} from {llm_org}")

    # 1. 加载标准答案（使用公共函数）
    gt_one_single = eval_utils.load_json_file(TYPE_ONE_SINGLE_PATH)
    gt_one_multi = eval_utils.load_json_file(TYPE_ONE_MULTI_PATH)
    gt_two = eval_utils.load_json_file(TYPE_TWO_PATH)
    gt_three = eval_utils.load_json_file(TYPE_THREE_PATH)

    # 2. 读取并解析上传的文件（使用公共函数）
    pred_one_single = await eval_utils.parse_upload_file(file_type_one_single)
    pred_one_multi = await eval_utils.parse_upload_file(file_type_one_multi)
    pred_two = await eval_utils.parse_upload_file(file_type_two)
    pred_three = await eval_utils.parse_upload_file(file_type_three)

    # 3. 验证预测数据（使用公共函数）
    eval_utils.validate_predictions(pred_one_single, gt_one_single, "第一类题型-单选题")
    eval_utils.validate_predictions(pred_one_multi, gt_one_multi, "第一类题型-多选题")
    eval_utils.validate_predictions(pred_two, gt_two, "第二类题型-定位题")
    eval_utils.validate_predictions(pred_three, gt_three, "第三类题型-针灸操作题")

    # 3.5. 数据一致性检查（非严格模式，仅记录警告）
    eval_utils.check_id_consistency(pred_one_single, gt_one_single, "第一类题型-单选题", strict=False)
    eval_utils.check_id_consistency(pred_one_multi, gt_one_multi, "第一类题型-多选题", strict=False)
    eval_utils.check_id_consistency(pred_two, gt_two, "第二类题型-定位题", strict=False)
    eval_utils.check_id_consistency(pred_three, gt_three, "第三类题型-针灸操作题", strict=False)

    # 4. 计算正确率（使用公共函数）
    score_single = eval_utils.calculate_accuracy(pred_one_single, gt_one_single, 'single')
    score_multi = eval_utils.calculate_accuracy(pred_one_multi, gt_one_multi, 'multi')
    score_two = eval_utils.calculate_accuracy(pred_two, gt_two, 'single')
    score_three = eval_utils.calculate_accuracy(pred_three, gt_three, 'single')

    # 5. 计算平均分
    average_score = round((score_single + score_multi + score_two + score_three) / 4, 4)

    logger.info(
        f"Scores calculated: S1={score_single}, S2={score_multi}, "
        f"S3={score_two}, S4={score_three}, Avg={average_score}"
    )

    # 6. 存入数据库
    record = vqa_leaderboard_dao.add_record(
        db,
        llm_name=llm_name,
        llm_org=llm_org or "",
        type_one_single_score=score_single,
        type_one_multi_score=score_multi,
        type_two_score=score_two,
        type_three_score=score_three,
        avg_score=average_score
    )

    if not record:
        raise HTTPException(status_code=500, detail="数据库保存失败")

    return {
        "llm_name": llm_name,
        "llm_org": llm_org,
        "type_one_single_score": score_single,
        "type_one_multi_score": score_multi,
        "type_two_score": score_two,
        "type_three_score": score_three,
        "average_score": average_score,
        "message": "评测完成并已记录"
    }

@router.get("/data", summary="获取所有排行数据")
async def get_all_data(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """
    获取qa数据表中所有记录，支持分页。
    """
    records = vqa_leaderboard_dao.get_all_sorted_by_score(db, skip=skip, limit=limit)
    return records
