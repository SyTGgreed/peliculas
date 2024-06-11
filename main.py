
from fastapi import FastAPI
import socket
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import  engine, Base
from Middlewears.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'
app.version = '0.0.1'
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)






movies = [
    {
        "id" : 1,
        "title" : "Avatar",
        "overview" : "En un exuberante planeta llamado Pandora, viven los Na'vi",
        "year" : 2009,
        "rating" : 7.8,
        "category" : "Acción"
    },
    {
        "id" : 2,
        "title" : "Avatar",
        "overview" : "En un exuberante planeta llamado Pandora, viven los Na'vi",
        "year" : 2009,
        "rating" : 7.8,
        "category" : "Acción"
    }
]

def obtener_ip():
    nombre_host = socket.gethostname()
    ip_local = socket.gethostbyname(nombre_host)
    return ip_local



@app.get('/', tags=['home'])
def message():
    return "trabaje vago :v :3 "

    




if __name__== '__main__':
    ip = obtener_ip()
    print(ip)