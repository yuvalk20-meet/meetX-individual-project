from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Test(Base):
	__tablename__ = 'tests'
	id = Column(Integer, primary_key=True)
	subject = Column(String) #radio - choosing options
	grade = Column(Integer)
	picture = Column(String) #file path

	description = Column(String) 
	solution = Column(String)
	username = Column(String)   

