from fastapi import APIRouter
from fastapi import  Path, Query ,Depends
from fastapi.responses import JSONResponse
from config.database import Session
from models.movie import movie as   Movie_model
from typing import  List
from fastapi.encoders import jsonable_encoder
from Middlewears.jwt_bearer import JWTbearer
from services.movie import movie_services
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie],status_code=200, dependencies=[Depends(JWTbearer())])
def get_movies() -> List[Movie]:
    # crear instancia de la sesion
    db = Session()
    result = movie_services(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/{id}',tags=['movie'], response_model=Movie)
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie:
    db = Session()
    result = movie_services(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'],response_model=List[Movie])    # parametros query se pone un / al final del endpoint
def get_movies_by_category(category : str = Query(min_length=5, max_length=15)) -> List[Movie]: # parametros query
    db = Session()
    result = movie_services(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'],response_model=dict,status_code=201)
def create_movie(movie : Movie) -> dict:
    db = Session()
    Movie_model(title=movie.title)
    movie_services(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"message":"Se ha registrado la pelicula"})

@movie_router.delete('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id : int) -> dict:
    db = Session()
    result = db.query(Movie_model).filter(Movie_model.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':"No se ha encontrado"})
    movie_services(db).delete_movie(id)
    db.commit()
    return JSONResponse(status_code=200,content={"message":"se ha eliminado la pelicula"})

@movie_router.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def update_movie(id: int, movie:Movie) -> dict:
    db = Session()
    result = movie_services(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No se encontro"})
    movie_services

    movie_services(db).update_movie(id, movie)
    
    return JSONResponse(status_code=200,content={"message":"Se ha modificado exitosamente"})