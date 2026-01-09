from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    dni = Column(Integer, unique=True, nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    country_id = Column(Integer, ForeignKey('nationalities.id'), nullable=False)
    seniority_id = Column(Integer, ForeignKey('seniorities.id'), nullable=False)

    job = relationship("Jobs", backref="employees")
    nationality = relationship("Nationality", backref="employees")
    seniority = relationship("Seniority", backref="employees")

    def __init__(self, name, last_name, age, dni, job_id, country_id, seniority_id):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.dni = dni
        self.job_id = job_id
        self.country_id = country_id
        self.seniority_id = seniority_id
