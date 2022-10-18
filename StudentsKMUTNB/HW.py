from asyncio.windows_events import NULL
from models import Base, Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, CHAR,Integer, String, Text, DateTime, Float, Boolean, PickleType,VARCHAR,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# Create engine
db_uri = 'sqlite:///HW.sqlite3'
engine = create_engine(db_uri, echo=False)

Base = declarative_base()


class students_table(Base):
    __tablename__ = 'Students' 
    student_id = Column(CHAR(13),primary_key = True) 
    f_name = Column(VARCHAR(30),nullable = False) 
    l_name = Column(VARCHAR(30),nullable=False) 
    e_mail = Column(VARCHAR(50)) 


class registration_table(Base):
    __tablename__ = 'Registration' 
    student_id = Column(CHAR(13),ForeignKey=True,primary_key = True) 
    subject_id = Column(VARCHAR(15),ForeignKey= True,nullable = False) 
    year = Column(CHAR(4),nullable=False) 
    semester = Column(CHAR(1),nullable=False)  
    grade = Column(CHAR(2))
 

class subjects_table(Base):
    __tablename__ = 'Subjects' 
    student_id = Column(VARCHAR(15),primary_key = True) 
    subject_name = Column(VARCHAR(50),nullable = False) 
    credit = Column(Integer(30),nullable=False) 
    teacher_id = Column(CHAR(3)) 
 
class teachers_table(Base):
    __tablename__ = 'Teachers' 
    teacher_id = Column(CHAR(3),primary_key = True) 
    f_name = Column(VARCHAR(30),nullable = False) 
    l_name = Column(VARCHAR(30),nullable = False) 
    e_mail = Column(VARCHAR(50)) 
 
    def __repr__(self):
        return '<UserModel model {}>'.format(self.id)
        


Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name='Kyle',
    description='im testing this',
    vip=True,
    join_date=datetime.date.today(),
    number=45.0
)