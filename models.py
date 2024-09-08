from sqlalchemy import Boolean, Date, Column, ForeignKey, Integer, String
from database import Base

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_serial = Column(Integer, index=True, unique=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    is_rented = Column(Boolean, default=False)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_serial = Column(Integer, index=True, unique=True)


class Rented(Base):
    __tablename__ = "rented"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))