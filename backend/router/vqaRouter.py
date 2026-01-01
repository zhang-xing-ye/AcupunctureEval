from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
import json
import logging
from core.database import get_db
from dao import vqa_leaderboard_dao
import os

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/vqa", tags=["VQA Leaderboard"])

# 标准答案路径配置
# 假设 backend 为当前工作目录或父目录的一部分
# 使用 __file__ 定位更准确
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_BASE_PATH = os.path.join(BASE_DIR, "datasets", "vqa")

TYPE_ONE_SINGLE_PATH = os.path.join(DATASET_BASE_PATH, "第一类题型", "单选题_324题.json")
TYPE_ONE_MULTI_PATH = os.path.join(DATASET_BASE_PATH, "第一类题型", "多选题_600题.json")
TYPE_TWO_PATH = os.path.join(DATASET_BASE_PATH, "第二类题型", "定位题_37题.json")
TYPE_THREE_PATH = os.path.join(DATASET_BASE_PATH, "第三类题型", "针灸操作题_35题.json")

def load_json(path: str) -> List[Dict[str, Any]]:
    """加载JSON文件"""
    if not os.path.exists(path):
        logger.error(f"Dataset file not found: {path}")
        raise HTTPException(status_code=500, detail=f"Standard dataset file not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load dataset from {path}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to load standard dataset")

def validate_and_preprocess(predictions: List[Dict[str, Any]], ground_truth: List[Dict[str, Any]], dataset_name: str) -> List[Dict[str, Any]]:
    """
    验证并预处理预测数据
    1. 检查题目数量一致性
    2. 检查 output 字段完整性
    3. 将 output 中的 None 转换为 ""
    """
    expected_count = len(ground_truth)
    actual_count = len(predictions)
    
    if actual_count != expected_count:
        logger.error(f"[{dataset_name}] Count mismatch: expected {expected_count}, got {actual_count}")
        raise HTTPException(
            status_code=400, 
            detail=f"{dataset_name}: 题目数量与标准答案不匹配，请确保上传文件包含 {expected_count} 道题目 (实际: {actual_count})"
        )

    missing_output_ids = []
    
    for item in predictions:
        # 获取 ID，如果没有 ID 则尝试获取 id，否则标记为 Unknown
        item_id = str(item.get('ID') or item.get('id') or 'Unknown')
        
        # 检查是否存在 output 或 Output
        has_output = 'output' in item
        has_Output = 'Output' in item
        
        if not has_output and not has_Output:
            missing_output_ids.append(item_id)
            continue
            
        # Null 值处理
        target_keys = []
        if has_output: target_keys.append('output')
        if has_Output: target_keys.append('Output')
        
        for key in target_keys:
            if item[key] is None:
                logger.warning(f"[{dataset_name}] ID {item_id}: Null value found in '{key}', converting to empty string.")
                item[key] = ""
            
    if missing_output_ids:
        logger.error(f"[{dataset_name}] Missing output fields for IDs: {missing_output_ids}")
        raise HTTPException(
            status_code=400,
            detail=f"{dataset_name}: 以下题目缺少 output 或 Output 字段: {missing_output_ids}"
        )
        
    return predictions

def calculate_accuracy(predictions: List[Dict[str, Any]], ground_truth: List[Dict[str, Any]], mode: str) -> float:
    """
    计算准确率
    :param predictions: 预测结果列表
    :param ground_truth: 标准答案列表
    :param mode: 'single' 或 'multi'
    :return: 准确率 (0.0 - 1.0)
    """
    if not isinstance(predictions, list):
        raise HTTPException(status_code=400, detail="Uploaded file content must be a JSON list.")
    
    total_count = len(ground_truth)
    if total_count == 0:
        return 0.0
        
    correct_count = 0
    
    # 尝试建立 ID 映射
    # 预测结果如果有 ID 字段，优先使用 ID 匹配
    # 否则按顺序匹配（假设顺序一致）
    
    # 标准答案映射
    gt_map = {str(item.get('ID')): item.get('Answer') for item in ground_truth if 'ID' in item}
    
    # 检查预测结果是否包含 ID
    has_id = any('ID' in p or 'id' in p for p in predictions)
    
    pred_map = {}
    if has_id:
        for p in predictions:
            pid = str(p.get('ID') or p.get('id'))
            # 优先取 output，其次取 Output
            val = None
            if 'output' in p:
                val = p['output']
            elif 'Output' in p:
                val = p['Output']
            pred_map[pid] = val
    
    for i, gt_item in enumerate(ground_truth):
        gid = str(gt_item.get('ID'))
        gt_answer = gt_item.get('Answer')
        
        pred_output = None
        
        if has_id:
            pred_output = pred_map.get(gid)
        else:
            # 按索引匹配
            if i < len(predictions):
                pred_item = predictions[i]
                if 'output' in pred_item:
                    pred_output = pred_item['output']
                elif 'Output' in pred_item:
                    pred_output = pred_item['Output']
        
        if pred_output is None:
            continue
            
        # 比对逻辑
        is_correct = False
        
        if mode == 'single':
            # 单选题 / 定位题 / 操作题：字符串完全匹配（忽略大小写和首尾空格）
            if isinstance(pred_output, str) and isinstance(gt_answer, str):
                if pred_output.strip().upper() == gt_answer.strip().upper():
                    is_correct = True
        elif mode == 'multi':
            # 多选题：集合完全匹配
            p_set = set()
            g_set = set()
            
            # 处理标准答案
            if isinstance(gt_answer, list):
                g_set = set(str(x).strip().upper() for x in gt_answer)
            elif isinstance(gt_answer, str):
                g_set = set([gt_answer.strip().upper()])
                
            # 处理预测结果
            if isinstance(pred_output, list):
                p_set = set(str(x).strip().upper() for x in pred_output)
            elif isinstance(pred_output, str):
                # 如果预测结果是字符串，尝试解析或直接作为单元素
                # 假设如果是多选，预测结果也应该是列表，或者是逗号分隔字符串？
                # 这里假设如果只给字符串，就当做一个选项
                p_set = set([pred_output.strip().upper()])
                
            if p_set == g_set:
                is_correct = True
                
        if is_correct:
            correct_count += 1
            
    return round(correct_count / total_count, 4)

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
    
    # 1. 加载标准答案
    gt_one_single = load_json(TYPE_ONE_SINGLE_PATH)
    gt_one_multi = load_json(TYPE_ONE_MULTI_PATH)
    gt_two = load_json(TYPE_TWO_PATH)
    gt_three = load_json(TYPE_THREE_PATH)
    
    # 2. 读取并解析上传的文件
    try:
        content_single = await file_type_one_single.read()
        pred_one_single = json.loads(content_single)
        validate_and_preprocess(pred_one_single, gt_one_single, "第一类题型-单选题")
        
        content_multi = await file_type_one_multi.read()
        pred_one_multi = json.loads(content_multi)
        validate_and_preprocess(pred_one_multi, gt_one_multi, "第一类题型-多选题")
        
        content_two = await file_type_two.read()
        pred_two = json.loads(content_two)
        validate_and_preprocess(pred_two, gt_two, "第二类题型-定位题")
        
        content_three = await file_type_three.read()
        pred_three = json.loads(content_three)
        validate_and_preprocess(pred_three, gt_three, "第三类题型-针灸操作题")

    except HTTPException as he:
        raise he
    except json.JSONDecodeError as e:
        logger.error(f"JSON Decode Error: {e}")
        raise HTTPException(status_code=400, detail="上传的文件必须是有效的JSON格式")
    except Exception as e:
        logger.error(f"File Read Error: {e}")
        raise HTTPException(status_code=500, detail=f"文件读取失败: {str(e)}")
        
    # 3. 计算正确率
    # 单选题 - 完全匹配
    score_single = calculate_accuracy(pred_one_single, gt_one_single, 'single')
    # 多选题 - 选项集合完全匹配
    score_multi = calculate_accuracy(pred_one_multi, gt_one_multi, 'multi')
    # 第二类定位题 - 单选模式 (根据数据观察，答案为单字符)
    score_two = calculate_accuracy(pred_two, gt_two, 'single')
    # 第三类操作题 - 单选模式 (根据数据观察，答案为单字符)
    score_three = calculate_accuracy(pred_three, gt_three, 'single')
    
    # 4. 计算平均分
    average_score = round((score_single + score_multi + score_two + score_three) / 4, 4)
    
    logger.info(f"Scores calculated: S1={score_single}, S2={score_multi}, S3={score_two}, S4={score_three}, Avg={average_score}")
    
    # 5. 存入数据库
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
