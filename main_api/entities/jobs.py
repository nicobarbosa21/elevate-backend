from sqlalchemy import Column, Integer, String
from ..db import Base

class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    salary = Column(Integer, nullable=False)

    def __init__(self, title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary