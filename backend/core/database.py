import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 获取当前文件所在目录的上一级目录（即 backend 目录）
# os.path.abspath(__file__) 获取当前文件的绝对路径
# os.path.dirname(...) 获取其父目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼接数据库文件的绝对路径
# 将 BASE_DIR 和 "acue_app.db" 拼接成完整的数据库文件路径
DB_PATH = os.path.join(BASE_DIR, "acue_app.db")

# 构造 SQLite 连接字符串
# 格式为 sqlite:/// + 数据库文件的绝对路径
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# 创建数据库引擎
# create_engine 是 SQLAlchemy 的入口点
# connect_args={'check_same_thread': False} 是 SQLite 特有的配置，允许在不同线程中使用同一个连接
# echo=True 表示在控制台打印生成的 SQL 语句，方便调试
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={'check_same_thread': False}, 
    echo=True
)

# 创建声明式基类
# 所有模型类都应继承自这个 Base 类
Base = declarative_base()

# 创建 SessionLocal 类
# sessionmaker 是一个工厂函数，用于创建 Session 类
# autocommit=False: 禁止自动提交事务，需要手动 commit
# autoflush=False: 禁止自动刷新，需要手动 flush
# bind=engine: 将 Session 绑定到创建的引擎上
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 获取数据库会话的依赖函数
# 用于 FastAPI 的依赖注入
def get_db():
    """
    获取数据库会话生成器。
    
    Yields:
        Session: SQLAlchemy 数据库会话对象
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        # 确保在使用完会话后关闭它，释放资源
        db.close()
