from sqlalchemy import Column,Integer,String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
class Emp(Base):
     __tablename__="Emp"
     id=Column(Integer,primary_key=True,index=True)
     name=Column(String)
     dept=Column(String)
     sal=Column(Integer)
