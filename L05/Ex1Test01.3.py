import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from L05.Ex3models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

# Base.mentadata.drop_all(engine)
Base.mentadata.create_all(engine)

Session =  sessionmaker(bind=engine)
session = Session()

for instance in session.query(User).filter(User.name.in_(('user1,' 'user2'))):
    print(instance.name, instance.fullname)
