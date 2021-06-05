import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import or_

# Conectar ao postgres
engine = create_engine('postgresql://postgres:kamisama123@localhost/postgres', echo=False)


Session = sessionmaker(bind=engine)
session = Session() # Initialize the session. To query against the db.

Base = declarative_base()
"""
`declarative_base` is factory function that constructs a base class for declarative class definitions.
SQL alchemy should know about the models we've defined. So we let it no by extending from Base.
"""

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine) #Cria a tabela

##### ADICIONANDO DADOS #####
student1 = Student(name="Jerin", age=27, grade="Fifth")
session.add(student1)
session.commit()


student2 = Student(name="Carol", age=27, grade="Fifth")
student3 = Student(name="Jerin", age=25,grade="Third")

session.add_all([student2, student3]) #para adicionar mais de um valor, colocar dentro de uma lista.
session.commit()


#LENDO DADOS#

students = session.query(Student)

for student in students:
    print(student.name,student.age)

### DADOS EM ORDEM ###
students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name,student.age)


### FILTRANDO DADOS ###
students = session.query(Student).filter(Student.name=="Jerin").first()
print(student.name,student.age)

USANDO OU:
students = session.query(Student).filter(or(Student.name=="Jerin", Student.name=="Carol")

for student in students:
    print(student.name, student.age)
                                         

### COUNT ###
student_count = session.query(Student).filter(or_(Student.name=="Jerin", Student.name=="Carol")).count()
print(student_count)

### ATUALIZAR UM VALOR NA TABELA ###
student = session.query(Student).filter(Student.name=="Jerin")
student.name = "Anita"
session.commit()

###DELETAR UM VALOR###
student = session.query(Student).filter(Student.name=="Carol").first()
# session.delete(student)
# session.commit()

print(student.name)
