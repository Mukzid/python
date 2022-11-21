from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres", echo=False)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('age', String),
   Column('grade', String),
)
meta.create_all(engine)

'''For inserting one row'''
sql_insert = students.insert().values(name = 'Praveen', age = 23, grade = 'A')
con = engine.connect()
res = con.execute(sql_insert)

'''For inserting multiple rows'''
con = engine.connect()
res = con.execute(students.insert(), [
    {'name': 'John', 'age': 30, 'grade': 'second'},
    {'name': 'bharath', 'age': 25, 'grade': 'fourth'},
    {'name': 'John', 'age': 24, 'grade': 'third'},
])