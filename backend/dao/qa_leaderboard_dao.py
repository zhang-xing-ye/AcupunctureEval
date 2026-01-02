import logging
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model.qaLeaderboard import QALeaderboard

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_record(
    db: Session, 
    llm_name: str, 
    llm_org: str, 
    a1_score: float, 
    a2_score: float, 
    a3_score: float, 
    a4_score: float, 
    b_score: float, 
    x_score: float, 
    avg_score: float,
    created_at: Optional[datetime] = None
) -> Optional[QALeaderboard]:
    """
    向 qa_leaderboard 表中插入一条新记录。
    
    参数:
        db (Session): 数据库会话对象
        llm_name (str): 模型名称
        llm_org (str): 模型所属机构
        a1_score (float): A1 类评分
        a2_score (float): A2 类评分
        a3_score (float): A3 类评分
        a4_score (float): A4 类评分
        b_score (float): B 类评分
        x_score (float): X 类评分
        avg_score (float): 平均分
        created_at (Optional[datetime]): 创建时间，默认为当前时间
        
    返回:
        Optional[QALeaderboard]: 插入成功的记录对象，如果失败则返回 None
    """
    if created_at is None:
        created_at = datetime.now()
        
    new_record = QALeaderboard(
        llm_name=llm_name,
        llm_org=llm_org,
        a1_score=a1_score,
        a2_score=a2_score,
        a3_score=a3_score,
        a4_score=a4_score,
        b_score=b_score,
        x_score=x_score,
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

def get_all_sorted_by_score(db: Session, skip: int = 0, limit: int = 20) -> List[QALeaderboard]:
    """
    查询 qa_leaderboard 表中的所有记录，并按 avg_score 降序排列。
    
    参数:
        db (Session): 数据库会话对象
        skip (int): 跳过的记录数（分页偏移量）
        limit (int): 返回的最大记录数
        
    返回:
        List[QALeaderboard]: 排序后的记录列表
    """
    try:
        # 查询所有记录并按 avg_score 降序排序，支持分页
        records = db.query(QALeaderboard)\
            .order_by(QALeaderboard.avg_score.desc())\
            .offset(skip)\
            .limit(limit)\
            .all()
        logger.info(f"成功查询 {len(records)} 条 QA 记录（skip={skip}, limit={limit}），按 avg_score 降序排列")
        return records
    except SQLAlchemyError as e:
        logger.error(f"查询 QA 记录时发生错误: {str(e)}")
        return []

def get_total_count(db: Session) -> int:
    """
    查询 qa_leaderboard 表中的记录总数。
    
    参数:
        db (Session): 数据库会话对象
        
    返回:
        int: 记录总数
    """
    try:
        count = db.query(QALeaderboard).count()
        return count
    except SQLAlchemyError as e:
        logger.error(f"查询 QA 记录总数时发生错误: {str(e)}")
        return 0
