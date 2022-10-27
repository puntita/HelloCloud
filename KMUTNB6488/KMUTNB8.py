import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import sessionmaker , relationship , backref
Base = declarative_base()
engine = sqlalchemy.create_engine('postgresql://webadmin:LAInen57820@node37009-puntita.proen.app.ruk-com.cloud:5432/jj1')

class Students(Base):
    __tablename__ = 'Students' 
    student_id = Column(String(13),primary_key = True,nullable = True) 
    S_f_name = Column(String(30),nullable = False) 
    S_l_name = Column(String(30),nullable=False) 
    S_e_mail = Column(String(50), nullable=False) 

    def __repr__(self):
        return '<User(student_id = {}, S_f_name = {}, S_l_name = {}, S_e_mail ={})>'.format(self.student_id, self.S_f_name, self.S_l_name, self.S_e_mail)
        

class Registration(Base):
    __tablename__ = 'Registration' 
    id = Column(Integer(), primary_key = True)
    student_id = Column(String(13)) 
    sub_id = Column(String(15),nullable = False) 
    year = Column(String(4),nullable=False) 
    semester = Column(String(1),nullable=False)  
    grade = Column(String(2))

    def __repr__(self):
        return '<User(student_id = {}, sub_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, \
            self.sub_id, self.year , self.semester, self.grade)

class Subjects(Base):
    __tablename__ = 'Subjects' 
    sub_id = Column(String(15),primary_key = True) 
    subject_name = Column(String(50),nullable = False) 
    credit = Column(Integer(),nullable=False) 
    teacher_id = Column(String(3),nullable=False) 
    def __repr__(self):
        return '<User(sub_id = {}, subject_name = {}, credit = {}, teacher_id ={})>'.format(self.sub_id, \
            self.subject_name, self.credit , self.teacher_id)

class Teacher(Base):
    __tablename__ = 'Teachers' 
    teacher_id = Column(String(3),primary_key=True, nullable=True)
    T_f_name = Column(String(50), nullable=True)
    T_l_name = Column(String(30), nullable=True)
    T_e_mail = Column(String(50), nullable=True)

    def __repr__(self):
            return '<User(teacher_id = {} , T_f_name= {} , T_l_name = {} , T_e_mail = {})>'.format(self.teacher_id,\
                    self.T_f_name, self.T_l_name , self.T_e_mail)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


user1 = Students(
    student_id ='6406022620088',
    S_f_name='Puntita',
    S_l_name='Chaungchawna',
    S_e_mail ='6406022620088@kmutnb.ac.th'
)


user2 = Students(
    student_id ='6406022620070',
    S_f_name='Rawiporn',
    S_l_name='Suamsiri',
    S_e_mail ='6406022620070@kmutnb.ac.th'
)

user3 = Students(
    student_id ='6406022620061',
    S_f_name='Mathawee',
    S_l_name='Robkhob',
    S_e_mail ='6406022620061@kmutnb.ac.th'
)

regis1 = Registration(
    student_id ='6406022620088',
    sub_id='060233113',
    year='2565',
    semester ='1',
    grade = 'C+'
)

regis11 = Registration(
    student_id ='6406022620088',
    sub_id='060233201',
    year='2565',
    semester ='1',
    grade = 'B+'
)

regis2 = Registration(
    student_id ='6406022620070',
    sub_id='060233113',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis22 = Registration(
    student_id ='6406022620070',
    sub_id='060233201',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis3 = Registration(
    student_id ='6406022620061',
    sub_id='060233113',
    year='2565',
    semester ='1',
    grade = 'B+'
)

regis33 = Registration(
    student_id ='6406022620061',
    sub_id='060233201',
    year='2565',
    semester ='1',
    grade = 'C'
)

Subjects1 = Subjects(
    sub_id ='060233113',
    subject_name='ADVANCED COMPUTER PROGRAMMING',
    credit='3',
    teacher_id ='AMK'
)

Subjects2 = Subjects(
    sub_id ='060233201',
    subject_name='NETWORK ENGINEERING LABORATO',
    credit='1',
    teacher_id ='WKN'
)

teacher1 = Teacher(
    teacher_id='AMK',
    T_f_name='Anirach',
    T_l_name='Mingkhwan',
    T_e_mail='Anirach@gmail.com'
)
teacher2 = Teacher(
    teacher_id='WKN',
    T_f_name='Watcharachai',
    T_l_name='Kongsiriwattana',
    T_e_mail='Watcharachai@gmail.com'
)

session.add_all([user1,user2,user3,regis1, regis11, regis2, regis22, regis3, regis33,Subjects1 ,Subjects2,teacher1,teacher2])
print(session.query(Students).all())
session.commit()