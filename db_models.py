# this file is used to make class that would store data in a db such as mySQL or any db.
from sqlalchemy import Column, Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base


base=declarative_base()


class product(base):

    __tablename__="product-table"
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    description = Column(String)
