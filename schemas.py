from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class MovieCreate(BaseModel):
    title: str
    director: str
    genre: str
    year: int

class MovieUpdate(BaseModel):
    title: str
    director: str
    genre: str
    year: int

class MovieResponse(BaseModel):
    id: int
    title: str
    director: str
    genre: str
    year: int
    available: bool

    class Config:
        from_attributes = True

class RentalResponse(BaseModel):

    id: int

    user_id: int

    movie_id: int

    rent_date: str

    return_date: str | None

    class Config:
        from_attributes = True