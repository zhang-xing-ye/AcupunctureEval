from sqlalchemy import Column, Integer, String, DateTime,Double
from core.database import Base

class VQALeaderboard(Base):
    __tablename__ = "vqa_leaderboard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    llm_name = Column(String)
    llm_org = Column(String)
    type_one_single_score = Column(Double)
    type_one_multi_score = Column(Double)
    type_two_score = Column(Double)
    type_three_score = Column(Double)
    avg_score = Column(Double)
    created_at = Column(DateTime)

    # __repr__方法用于输出该类的对象被print()时输出的字符串，如果不想写可以不写
    def __repr__(self):
        return "<VQALeaderboard(llm_name='%s', llm_org='%s', type_one_single_score='%s',type_one_multi_score='%s',type_two_score='%s',type_three_score='%s',avg_score='%s',created_at='%s')>" % (
                   self.llm_name, self.llm_org, self.type_one_single_score, self.type_one_multi_score, self.type_two_score, self.type_three_score, self.avg_score, self.created_at)
