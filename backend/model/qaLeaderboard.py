from sqlalchemy import Column, Integer, String, DateTime,Double
from core.database import Base

class QALeaderboard(Base):
    __tablename__ = "qa_leaderboard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    llm_name = Column(String)
    llm_org = Column(String)
    a1_score = Column(Double)
    a2_score = Column(Double)
    a3_score = Column(Double)
    a4_score = Column(Double)
    b_score = Column(Double)
    x_score = Column(Double)
    avg_score = Column(Double)
    created_at = Column(DateTime)

        # __repr__方法用于输出该类的对象被print()时输出的字符串，如果不想写可以不写
    def __repr__(self):
        return "<QALeaderboard(llm_name='%s', llm_org='%s', a1_score='%s', a2_score='%s', a3_score='%s', a4_score='%s', b_score='%s', x_score='%s', avg_score='%s')>" % (
                   self.llm_name, self.llm_org, self.a1_score, self.a2_score, self.a3_score, self.a4_score, self.b_score, self.x_score, self.avg_score)
