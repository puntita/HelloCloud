import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from L05.Ex3models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

# Base.mentadata.drop_all(engine)
Base.mentadata.create_all(engine)

Session =  sessionmaker(bind=engine)
session = Session()

user1 = User(name='user1', fullname='Ed Jones', nickname='ed')

session.add(user1)
session.commit()

