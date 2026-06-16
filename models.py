from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    genre = Column(String)
    year = Column(Integer)
    available = Column(Boolean, default=True)

class Rental(Base):

    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    movie_id = Column(
        Integer,
        ForeignKey("movies.id")
    )

    rent_date = Column(String)

    return_date = Column(
        String,
        nullable=True
    )
