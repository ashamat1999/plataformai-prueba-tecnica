from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class UnitMeasure(Base):
    __tablename__ = 'UnitMeasure'

    unit_measure_id = Column(Integer(), primary_key=True)
    measure_name = Column(String(50))




