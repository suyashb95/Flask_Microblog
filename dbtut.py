from sqlalchemy import create_engine
from sqlalchemy import Column, MetaData, Table
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parent(Base):
	__tablename__ = 'parent'
	id = Column(Integer, primary_key=True)
	child_id = Column(Integer,ForeignKey('child.id'))
	
class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parents = relationship('Parent',backref = "child")
	
		
engine = create_engine("sqlite:///tutorial.db",echo = True)
