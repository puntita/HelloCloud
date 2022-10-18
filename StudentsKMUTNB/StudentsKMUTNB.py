from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db_uri = 'sqlite:///Ex2.sqlite3'
engine = create_engine(db_uri, echo=False)

class Member(Base):
    tablename = 'member'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    join_date = Column(DateTime, nullable=False)
    vip = Column(Boolean, nullable=False)
    number = Column(Float, nullable=False)

    def repr(self):
        return '<UserModel model {}>'.format(self.id)




Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name='Toddy',
    description='im testing this',
    vip=True,
    join_date=datetime.date.today(),
    number=45.0
)
session.add(user)
session.commit()
print(user)