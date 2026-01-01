import sys
import os

# 修正后的导入方式，基于backend作为根目录
from core.database import Base, engine
# 必须显式导入所有模型，这样它们才会注册到 Base.metadata 中
from model.qaLeaderboard import QALeaderboard
from model.vqaLeaderboard import VQALeaderboard

def init_db():
    print(f"正在使用数据库连接: {engine.url}")
    print("开始创建数据库表...")
    # create_all 会创建所有继承自 Base 且已导入的表
    Base.metadata.create_all(bind=engine)
    print("数据库表创建成功！")

if __name__ == "__main__":
    init_db()