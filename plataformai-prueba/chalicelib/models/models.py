from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Relationship, backref
from datetime import datetime

Base = declarative_base()

class UnitMeasure(Base):
    __tablename__ = 'UnitMeasure'

    unit_measure_id = Column(Integer(), primary_key=True)
    measure_name = Column(String(50))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Products(Base):
    __tablename__ = 'Products'

    product_name = Column(String(), primary_key=True)
    price = Column(Numeric())
    unit_measure_id = Column(Integer, ForeignKey('UnitMeasure.unit_measure_id'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
