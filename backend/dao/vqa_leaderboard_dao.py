import logging
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model.vqaLeaderboard import VQALeaderboard

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_record(
    db: Session, 
    llm_name: str, 
    llm_org: str, 
    type_one_single_score: float,
    type_one_multi_score: float,
    type_two_score: float,
    type_three_score: float,
    avg_score: float,
    created_at: Optional[datetime] = None
) -> Optional[VQALeaderboard]:
    """
    向 vqa_leaderboard 表中插入一条新记录。
    
    参数:
        db (Session): 数据库会话对象
        llm_name (str): 模型名称
        llm_org (str): 模型所属机构
        type_one_single_score (float): 类型1单选题评分
        type_one_multi_score (float): 类型1多选题评分
        type_two_score (float): 类型2评分
        type_three_score (float): 类型3评分
        avg_score (float): 平均分
        created_at (Optional[datetime]): 创建时间，默认为当前时间
        
    返回:
        Optional[VQALeaderboard]: 插入成功的记录对象，如果失败则返回 None
    """
    if created_at is None:
        created_at = datetime.now()
        
    new_record = VQALeaderboard(
        llm_name=llm_name,
        llm_org=llm_org,
        type_one_single_score=type_one_single_score,
        type_one_multi_score=type_one_multi_score,
        type_two_score=type_two_score,
        type_three_score=type_three_score,
        avg_score=avg_score,
        created_at=created_at
    )
    
    try:
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        logger.info(f"成功完成 {llm_name} 的记录插入")
        return new_record
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"插入 {llm_name} 的记录时发生错误: {str(e)}")
        return None

def get_all_sorted_by_score(db: Session, skip: int = 0, limit: int = 20) -> List[VQALeaderboard]:
    """
    查询 vqa_leaderboard 表中的所有记录，并按 avg_score 降序排列。
    
    参数:
        db (Session): 数据库会话对象
        skip (int): 跳过的记录数，用于分页
        limit (int): 返回的记录数，用于分页
        
    返回:
        List[VQALeaderboard]: 排序后的记录列表
    """
    try:
        # 查询所有记录并按 avg_score 降序排序
        records = db.query(VQALeaderboard).order_by(VQALeaderboard.avg_score.desc()).offset(skip).limit(limit).all()
        logger.info(f"成功查询 {len(records)} 条 VQA 记录，按 avg_score 降序排列")
        return records
    except SQLAlchemyError as e:
        logger.error(f"查询 VQA 记录时发生错误: {str(e)}")
        return []

def get_total_count(db: Session) -> int:
    """
    查询 vqa_leaderboard 表中的记录总数。
    
    参数:
        db (Session): 数据库会话对象
        
    返回:
        int: 记录总数
    """
    try:
        count = db.query(VQALeaderboard).count()
        return count
    except SQLAlchemyError as e:
        logger.error(f"查询 VQA 记录总数时发生错误: {str(e)}")
        return 0
