from sqlalchemy import create_engine
from sqlalchemy import Column, MetaData, Table
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

assoc_table = Table('association',Base.metadata,
					Column('parent_id',Integer,ForeignKey('parent.id')),
					Column('child__id',Integer,ForeignKey('child.id'))
	)

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
	
class Parent(Base):
	__tablename__ = 'parent'
	id = Column(Integer, primary_key=True)
	children = relationship("Child",secondary = assoc_table,
							primaryjoin = (assoc_table.c.parent_id == id),
							secondaryjoin = (assoc_table.c.child__id == Child.id),
							backref = backref('parents',lazy = 'dynamic'),
							lazy = 'dynamic')
	
	
		
engine = create_engine("sqlite:///tutorial.db",echo = True)
Base.metadata.create_all(engine)
