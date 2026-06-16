from fastapi import FastAPI
from sqlalchemy.orm import Session
import utils
import oauth2
import models
import schemas
from database import engine, SessionLocal
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Movie Library API"}

@app.post("/register")
def register(user: schemas.UserCreate):

    db = SessionLocal()

    new_user = models.User(
        username=user.username,
        password=utils.hash(user.password),
        role="consumer"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {"message": "User registered"}

@app.post("/token")
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends()
):

    db = SessionLocal()

    db_user = db.query(
        models.User
    ).filter(
        models.User.username == user_credentials.username
    ).first()

    if not db_user:
        return {
            "message":"Invalid username"
        }

    if not utils.verify(
        user_credentials.password,
        db_user.password
    ):
        return {
            "message":"Invalid password"
        }

    access_token = oauth2.create_access_token(
        data={
            "user_id":db_user.id
        }
    )

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

@app.get("/me")
def me(
    current_user=Depends(
        oauth2.get_current_user
    )
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "role": current_user.role
    }

@app.post("/movies")
def create_movie(

    movie: schemas.MovieCreate,

    current_user=Depends(
        oauth2.get_current_admin
    )

):

    db = SessionLocal()

    new_movie = models.Movie(

        title=movie.title,
        director=movie.director,
        genre=movie.genre,
        year=movie.year

    )

    db.add(new_movie)

    db.commit()

    db.refresh(new_movie)

    db.close()

    return new_movie

@app.get("/movies")
def get_movies():

    db = SessionLocal()

    movies = db.query(
        models.Movie
    ).all()

    db.close()

    return movies


@app.get("/movies/{id}")
def get_movie(id: int):

    db = SessionLocal()

    movie = db.query(
        models.Movie
    ).filter(
        models.Movie.id == id
    ).first()

    db.close()

    return movie

@app.put("/movies/{id}")
def update_movie(

    id: int,

    movie: schemas.MovieUpdate,

    current_user=Depends(
        oauth2.get_current_admin
    )

):

    db = SessionLocal()

    db_movie = db.query(
        models.Movie
    ).filter(
        models.Movie.id == id
    ).first()

    if db_movie is None:

        db.close()

        return {
            "message":"Movie not found"
        }

    db_movie.title = movie.title
    db_movie.director = movie.director
    db_movie.genre = movie.genre
    db_movie.year = movie.year

    db.commit()

    db.refresh(db_movie)

    db.close()

    return db_movie

@app.delete("/movies/{id}")
def delete_movie(

    id: int,

    current_user=Depends(
        oauth2.get_current_admin
    )

):

    db = SessionLocal()

    movie = db.query(
        models.Movie
    ).filter(
        models.Movie.id == id
    ).first()

    if movie is None:

        db.close()

        return {
            "message":"Movie not found"
        }

    db.delete(movie)

    db.commit()

    db.close()

    return {
        "message":"Movie deleted"
    }

@app.post("/movies/{id}/rent")
def rent_movie(

    id: int,

    current_user=Depends(
        oauth2.get_current_user
    )

):

    db = SessionLocal()

    movie = db.query(
        models.Movie
    ).filter(
        models.Movie.id == id
    ).first()

    if movie is None:

        db.close()

        return {
            "message": "Movie not found"
        }

    if movie.available == False:

        db.close()

        return {
            "message": "Movie unavailable"
        }

    rental = models.Rental(

        user_id=current_user.id,

        movie_id=id,

        rent_date=str(
            datetime.now()
        )

    )

    movie.available = False

    db.add(rental)

    db.commit()

    db.close()

    return {
        "message": "Movie rented successfully"
    }

@app.post("/movies/{id}/return")
def return_movie(

    id:int,

    current_user=Depends(
        oauth2.get_current_user
    )

):

    db=SessionLocal()

    rental=db.query(
        models.Rental
    ).filter(

        models.Rental.movie_id==id,

        models.Rental.user_id==current_user.id,

        models.Rental.return_date==None

    ).first()

    if rental is None:

        db.close()

        return {
            "message":"Rental not found"
        }

    movie=db.query(
        models.Movie
    ).filter(
        models.Movie.id==id
    ).first()

    movie.available=True

    rental.return_date=str(
        datetime.now()
    )

    db.commit()

    db.close()

    return {
        "message":"Movie returned"
    }

@app.get("/users/me/rentals")
def my_rentals(

    current_user=Depends(
        oauth2.get_current_user
    )

):

    db=SessionLocal()

    rentals=db.query(
        models.Rental
    ).filter(

        models.Rental.user_id==current_user.id

    ).all()

    db.close()

    return rentals