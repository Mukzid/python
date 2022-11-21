from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres", echo = True)

class Students(Base):
   __tablename__ = 'Students'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   age = Column(String)
   grade = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

s = Students(name = 'Praveen', age = 23, grade = 'A')
session.add(s)
session.commit()

session.add_all([
   Students(name="John", age=30, grade="second"), 
   Students(name="bharath", age=25, grade="fourth"), 
   Students(name="praveen", age=24, grade="sthird")]
)

session.commit()