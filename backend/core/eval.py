"""
公共评测模块
提供文件解析、数据验证、对齐策略、计分等可复用功能
"""
from typing import List, Dict, Any, Union, Optional, Tuple
from fastapi import HTTPException, UploadFile
import json
import logging
import os

logger = logging.getLogger(__name__)


def load_json_file(path: str) -> List[Dict[str, Any]]:
    """
    加载JSON文件

    Args:
        path: JSON文件路径

    Returns:
        解析后的JSON数据（列表）

    Raises:
        HTTPException: 文件不存在或解析失败
    """
    if not os.path.exists(path):
        logger.error(f"Dataset file not found: {path}")
        raise HTTPException(
            status_code=500,
            detail=f"标准答案文件未找到: {path}"
        )

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise HTTPException(
                    status_code=500,
                    detail=f"标准答案文件格式错误，必须是JSON数组: {path}"
                )
            return data
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in {path}: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"标准答案文件JSON格式错误: {path}"
        )
    except Exception as e:
        logger.error(f"Failed to load {path}: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"加载标准答案失败: {str(e)}"
        )


async def parse_upload_file(file: UploadFile) -> List[Dict[str, Any]]:
    """
    解析上传的JSON文件

    Args:
        file: FastAPI UploadFile对象

    Returns:
        解析后的JSON数据（列表）

    Raises:
        HTTPException: 解析失败
    """
    try:
        content = await file.read()
        data = json.loads(content)
        if not isinstance(data, list):
            raise HTTPException(
                status_code=400,
                detail=f"上传文件必须是JSON数组格式: {file.filename}"
            )
        return data
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in uploaded file {file.filename}: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"上传文件JSON格式错误: {file.filename}"
        )
    except Exception as e:
        logger.error(f"Failed to parse uploaded file {file.filename}: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"文件解析失败: {str(e)}"
        )


def normalize_field_name(
    item: Dict[str, Any],
    preferred: str,
    alternatives: List[str],
) -> Optional[Any]:
    """
    标准化字段名获取（处理大小写、空格等变体）

    Args:
        item: 数据项
        preferred: 首选字段名
        alternatives: 备选字段名列表

    Returns:
        字段值，如果都不存在则返回None
    """
    if preferred in item:
        return item[preferred]
    for alt in alternatives:
        if alt in item:
            return item[alt]
    return None


def validate_predictions(
    predictions: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
    dataset_name: str,
    output_field: str = "output",
    allow_partial: bool = False,
) -> List[Dict[str, Any]]:
    """
    验证预测数据的完整性和一致性

    Args:
        predictions: 预测数据列表
        ground_truth: 标准答案列表
        dataset_name: 数据集名称（用于错误提示）
        output_field: 输出字段名（output或其他）
        allow_partial: 是否允许部分预测（题量不一致）

    Returns:
        预处理后的预测数据

    Raises:
        HTTPException: 验证失败
    """
    expected_count = len(ground_truth)
    actual_count = len(predictions)
    
    # 检查题目数量
    if not allow_partial and actual_count != expected_count:
        logger.error(
            f"[{dataset_name}] Count mismatch: expected {expected_count}, got {actual_count}"
        )
        raise HTTPException(
            status_code=400,
            detail=f"{dataset_name}: 题目数量与标准答案不匹配，"
                   f"要求 {expected_count} 题，实际 {actual_count} 题"
        )
    
    # 检查output字段完整性（兼容 output/Output）
    missing_output_ids = []
    null_output_ids = []
    
    for item in predictions:
        # 获取ID（兼容ID/id）
        item_id = str(item.get('ID') or item.get('id') or 'Unknown')
        
        # 检查output字段是否存在
        has_output = 'output' in item
        has_Output = 'Output' in item
        
        if not has_output and not has_Output:
            missing_output_ids.append(item_id)
            continue
        
        # 检查output值是否为None并转换
        if has_output and item['output'] is None:
            null_output_ids.append(item_id)
            item['output'] = ""
            logger.warning(
                f"[{dataset_name}] ID {item_id}: output为None，已转换为空字符串"
            )
        
        if has_Output and item['Output'] is None:
            null_output_ids.append(item_id)
            item['Output'] = ""
            logger.warning(
                f"[{dataset_name}] ID {item_id}: Output为None，已转换为空字符串"
            )
    
    # 汇总错误
    if missing_output_ids:
        error_summary = (
            f"{dataset_name}: 以下 {len(missing_output_ids)} 题缺少 output 或 Output 字段: "
            f"{', '.join(missing_output_ids[:10])}"
        )
        if len(missing_output_ids) > 10:
            error_summary += f" ...（共{len(missing_output_ids)}题）"
        
        logger.error(error_summary)
        raise HTTPException(status_code=400, detail=error_summary)
    
    if null_output_ids and len(null_output_ids) > 0:
        logger.info(
            f"[{dataset_name}] 已将 {len(null_output_ids)} 题的空值output转换为空字符串"
        )
    
    return predictions


def align_by_id(
    predictions: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    按ID对齐预测和标准答案

    Args:
        predictions: 预测数据
        ground_truth: 标准答案

    Returns:
        (pred_map, gt_map) ID到数据的映射
    """
    # 标准答案映射（兼容Answer/answer）
    gt_map = {}
    for item in ground_truth:
        gid = str(item.get('ID'))
        answer = normalize_field_name(item, 'answer', ['Answer'])
        gt_map[gid] = answer
    
    # 预测结果映射（兼容output/Output和ID/id）
    pred_map = {}
    for item in predictions:
        pid = str(item.get('ID') or item.get('id'))
        output = normalize_field_name(item, 'output', ['Output'])
        pred_map[pid] = output
    
    return pred_map, gt_map


def normalize_answer(value: Any) -> Union[str, List[str]]:
    """
    标准化答案格式，支持多种多选题输入格式

    Args:
        value: 原始答案（字符串或列表）

    Returns:
        标准化后的答案（字符串统一大写去空格，列表元素统一处理）
    """
    if isinstance(value, list):
        # 列表：去重、排序、标准化每个元素
        normalized = [str(x).strip().upper() for x in value if x]
        return sorted(list(set(normalized)))  # 去重并排序
    elif isinstance(value, str):
        # 字符串：尝试解析多选格式（支持逗号、空格分隔）
        value = value.strip().upper()
        
        # 检测是否为多选格式（包含逗号或多个字母）
        if ',' in value:
            # 逗号分隔：A,C,D
            parts = [p.strip() for p in value.split(',') if p.strip()]
            return sorted(list(set(parts)))
        elif ' ' in value:
            # 空格分隔：A C D
            parts = [p.strip() for p in value.split() if p.strip()]
            return sorted(list(set(parts)))
        elif len(value) > 1 and value.isalpha():
            # 无分隔符多字母：ACD -> ['A','C','D']
            return sorted(list(set(value)))
        else:
            # 单选或其他格式
            return value
    else:
        return str(value).strip().upper()


def check_id_consistency(predictions: List[Dict[str, Any]], 
                        ground_truth: List[Dict[str, Any]], 
                        dataset_name: str,
                        strict: bool = False) -> Dict[str, Any]:
    """
    检查预测数据ID的一致性

    Args:
        predictions: 预测数据
        ground_truth: 标准答案
        dataset_name: 数据集名称
        strict: 是否严格模式（ID不一致时抛出异常）

    Returns:
        统计信息字典：{
            'duplicate_ids': [...],
            'missing_ids': [...],
            'extra_ids': [...],
            'coverage_rate': 0.95
        }

    Raises:
        HTTPException: strict=True且检测到问题时抛出
    """
    # 收集所有ID
    pred_ids = [str(item.get('ID') or item.get('id')) for item in predictions
                if item.get('ID') or item.get('id')]
    gt_ids = [str(item.get('ID')) for item in ground_truth if item.get('ID')]
    
    # 检查重复ID
    pred_id_counts = {}
    for pid in pred_ids:
        pred_id_counts[pid] = pred_id_counts.get(pid, 0) + 1
    duplicate_ids = [pid for pid, count in pred_id_counts.items() if count > 1]
    
    # 检查缺失和多余的ID
    pred_id_set = set(pred_ids)
    gt_id_set = set(gt_ids)
    missing_ids = list(gt_id_set - pred_id_set)
    extra_ids = list(pred_id_set - gt_id_set)
    
    # 计算覆盖率
    coverage_rate = len(pred_id_set & gt_id_set) / len(gt_id_set) if gt_id_set else 0.0
    
    result = {
        'duplicate_ids': duplicate_ids,
        'missing_ids': missing_ids,
        'extra_ids': extra_ids,
        'coverage_rate': round(coverage_rate, 4)
    }
    
    # 记录日志
    if duplicate_ids:
        logger.warning(
            f"[{dataset_name}] 发现 {len(duplicate_ids)} 个重复ID: "
            f"{', '.join(duplicate_ids[:5])}"
            f"{' ...等' if len(duplicate_ids) > 5 else ''}"
        )
    if missing_ids:
        logger.warning(
            f"[{dataset_name}] 缺失 {len(missing_ids)} 个ID: "
            f"{', '.join(missing_ids[:5])}"
            f"{' ...等' if len(missing_ids) > 5 else ''}"
        )
    if extra_ids:
        logger.warning(
            f"[{dataset_name}] 多余 {len(extra_ids)} 个ID: "
            f"{', '.join(extra_ids[:5])}"
            f"{' ...等' if len(extra_ids) > 5 else ''}"
        )
    
    logger.info(f"[{dataset_name}] ID覆盖率: {coverage_rate:.2%}")
    
    # 严格模式下抛出异常
    if strict and (duplicate_ids or missing_ids or extra_ids):
        error_parts = []
        if duplicate_ids:
            error_parts.append(f"重复ID: {len(duplicate_ids)}个")
        if missing_ids:
            error_parts.append(f"缺失ID: {len(missing_ids)}个")
        if extra_ids:
            error_parts.append(f"多余ID: {len(extra_ids)}个")
        
        raise HTTPException(
            status_code=400,
            detail=f"{dataset_name}: ID不一致 - {', '.join(error_parts)}"
        )
    
    return result


def score_single_choice(pred_output: Any, gt_answer: Any) -> bool:
    """
    单选题计分：字符串完全匹配（忽略大小写和首尾空格）

    Args:
        pred_output: 预测输出
        gt_answer: 标准答案

    Returns:
        是否正确
    """
    pred_norm = normalize_answer(pred_output)
    gt_norm = normalize_answer(gt_answer)
    
    # 如果预测是列表，取第一个元素（兼容单选也用数组的情况）
    if isinstance(pred_norm, list):
        pred_norm = pred_norm[0] if pred_norm else ""
    if isinstance(gt_norm, list):
        gt_norm = gt_norm[0] if gt_norm else ""
    
    return pred_norm == gt_norm


def score_multi_choice(pred_output: Any, gt_answer: Any) -> bool:
    """
    多选题计分：集合完全匹配

    Args:
        pred_output: 预测输出
        gt_answer: 标准答案

    Returns:
        是否正确
    """
    pred_norm = normalize_answer(pred_output)
    gt_norm = normalize_answer(gt_answer)
    
    # 转为集合
    pred_set = set(pred_norm) if isinstance(pred_norm, list) else {pred_norm}
    gt_set = set(gt_norm) if isinstance(gt_norm, list) else {gt_norm}
    
    return pred_set == gt_set


def calculate_accuracy(
    predictions: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
    score_mode: str = 'single',
    use_id_align: bool = True,
) -> float:
    """
    计算准确率

    Args:
        predictions: 预测结果列表
        ground_truth: 标准答案列表
        score_mode: 计分模式 'single'(单选) 或 'multi'(多选)
        use_id_align: 是否使用ID对齐（False则按顺序）

    Returns:
        准确率 (0.0 - 1.0)
    """
    total_count = len(ground_truth)
    if total_count == 0:
        return 0.0
    
    correct_count = 0
    
    # 检查是否使用ID对齐
    has_id = any('ID' in p or 'id' in p for p in predictions)
    
    if use_id_align and has_id:
        # 按ID对齐
        pred_map, gt_map = align_by_id(predictions, ground_truth)
        
        for gid, gt_answer in gt_map.items():
            pred_output = pred_map.get(gid)
            if pred_output is None:
                continue
            
            # 根据模式计分
            is_correct = False
            if score_mode == 'single':
                is_correct = score_single_choice(pred_output, gt_answer)
            elif score_mode == 'multi':
                is_correct = score_multi_choice(pred_output, gt_answer)
            
            if is_correct:
                correct_count += 1
    else:
        # 按顺序对齐
        for i, gt_item in enumerate(ground_truth):
            if i >= len(predictions):
                break
            
            pred_item = predictions[i]
            gt_answer = normalize_field_name(gt_item, 'answer', ['Answer'])
            pred_output = normalize_field_name(pred_item, 'output', ['Output'])
            
            if pred_output is None or gt_answer is None:
                continue
            
            # 根据模式计分
            is_correct = False
            if score_mode == 'single':
                is_correct = score_single_choice(pred_output, gt_answer)
            elif score_mode == 'multi':
                is_correct = score_multi_choice(pred_output, gt_answer)
            
            if is_correct:
                correct_count += 1
    
    return round(correct_count / total_count, 4)


def validate_grouped_predictions(predictions: List[Dict[str, Any]], 
                                 ground_truth: List[Dict[str, Any]], 
                                 dataset_name: str) -> None:
    """
    验证分组题型（A3/A4/B）的预测数据

    Args:
        predictions: 预测数据，每项应包含ID和outputs
        ground_truth: 标准答案，每项包含ID和questions
        dataset_name: 数据集名称（用于错误提示）

    Raises:
        HTTPException: 验证失败
    """
    expected_count = len(ground_truth)
    actual_count = len(predictions)
    
    # 检查父题数量
    if actual_count != expected_count:
        logger.error(
            f"[{dataset_name}] 父题数量不匹配: 预期 {expected_count}，实际 {actual_count}"
        )
        raise HTTPException(
            status_code=400,
            detail=f"{dataset_name}: 父题数量不匹配，要求 {expected_count} 个父题，实际 {actual_count} 个"
        )
    
    missing_id = []
    missing_outputs = []
    invalid_outputs_format = []
    subquestion_mismatch = []
    
    # 构建标准答案的父题ID到子题数量的映射
    gt_subq_counts = {}
    for gt_item in ground_truth:
        parent_id = str(gt_item.get('ID'))
        questions = gt_item.get('questions', [])
        gt_subq_counts[parent_id] = len(questions)
    
    # 验证每个父题
    for pred_item in predictions:
        parent_id = pred_item.get('ID') or pred_item.get('id')
        
        # 检查父题ID
        if not parent_id:
            missing_id.append('Unknown')
            continue
        
        parent_id = str(parent_id)
        
        # 检查outputs字段
        outputs = normalize_field_name(pred_item, 'outputs', ['Outputs'])
        if outputs is None:
            missing_outputs.append(parent_id)
            continue
        
        # 检查outputs格式（必须是list）
        if not isinstance(outputs, list):
            invalid_outputs_format.append(parent_id)
            continue
        
        # 检查子题数量
        expected_subq_count = gt_subq_counts.get(parent_id)
        if expected_subq_count is not None:
            actual_subq_count = len(outputs)
            if actual_subq_count != expected_subq_count:
                subquestion_mismatch.append(
                    f"{parent_id}(预期{expected_subq_count}题,实际{actual_subq_count}题)"
                )
    
    # 汇总错误
    errors = []
    if missing_id:
        errors.append(
            f"缺少父题ID: {', '.join(missing_id[:5])}"
            f"{' 等 ' + str(len(missing_id)) + ' 个' if len(missing_id) > 5 else ''}"
        )
    if missing_outputs:
        errors.append(
            f"缺少outputs字段: {', '.join(missing_outputs[:5])}"
            f"{' 等 ' + str(len(missing_outputs)) + ' 个' if len(missing_outputs) > 5 else ''}"
        )
    if invalid_outputs_format:
        errors.append(
            f"outputs格式错误（必须是数组）: {', '.join(invalid_outputs_format[:5])}"
            f"{' 等 ' + str(len(invalid_outputs_format)) + ' 个' if len(invalid_outputs_format) > 5 else ''}"
        )
    if subquestion_mismatch:
        errors.append(
            f"子题数量不匹配: {', '.join(subquestion_mismatch[:5])}"
            f"{' 等 ' + str(len(subquestion_mismatch)) + ' 个' if len(subquestion_mismatch) > 5 else ''}"
        )
    
    if errors:
        error_msg = f"{dataset_name}: " + "; ".join(errors)
        logger.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)

