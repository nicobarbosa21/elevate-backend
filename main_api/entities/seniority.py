from sqlalchemy import Column, Integer, String
from ..db import Base

class Seniority(Base):
    __tablename__ = 'seniorities'

    id = Column(Integer, primary_key=True)
    level = Column(String, nullable=False)
    description = Column(String)

    def __init__(self, level, description=None):
        self.level = level
        self.description = description