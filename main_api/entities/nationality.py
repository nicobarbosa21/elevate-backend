from sqlalchemy import Column, Integer, String
from ..db import Base

class Nationality(Base):
    __tablename__ = 'nationalities'

    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    country_code = Column(String, unique=True, nullable=False)

    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code