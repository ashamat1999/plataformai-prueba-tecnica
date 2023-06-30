from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date
from sqlalchemy.orm import declarative_base

"""
Class to define each sqlalchemy model from each table of DDBB.
"""
Base = declarative_base()

class UnitMeasure(Base):
    """
    UnitMeasure class to define measures table model.
    """
    __tablename__ = 'UnitMeasure'

    unit_measure_id = Column(Integer(), primary_key=True)
    measure_name = Column(String(50))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Products(Base):
    """
    Products class to define products table model.
    """
    __tablename__ = 'Products'

    product_name = Column(String(), primary_key=True)
    price = Column(Numeric())
    unit_measure_id = Column(Integer, ForeignKey('UnitMeasure.unit_measure_id'))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Sales(Base):
    """
    Sales class to define sales table model.
    """
    __tablename__ = 'Sales'

    sale_id = Column(Numeric(), primary_key=True)
    quantity = Column(Integer(), nullable=False)
    product_name = Column(Integer, ForeignKey('Products.product_name'))
    sale_date = Column(Date())

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}