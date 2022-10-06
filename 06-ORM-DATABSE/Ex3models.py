from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime, Float

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Datetime)
    price = Column(Float)

    def __repr__(self):
        return "<Book(title='{}', author='{}', page={}, published={}, price{})>"\
            .format(self.title, self.author, self.pages, self.published, self.price)
            