from pydantic import BaseModel, Field
from typing import  Optional

class Movie(BaseModel):
    id : Optional[int]= None       #---> campo tipo opcional 
    title : str = Field(default="Mi pelicula",min_length= 5,max_length=20) 
    overview : str = Field(default="Descripcion de la pelicula",min_length= 10,max_length=50)
    year : int = Field(default="2022",le=2022)
    rating : float =  Field(ge=1,le=10)   #--> ge mayor o igual, le menor o igual
    category : str = Field(min_length= 5, max_length=12)

    class config:
        schema_extra = {
            "example":{
                "id" :1,
                "tilte": "Mi pelicula",
                "overview" : "Descripcion de la pelicula",
                "año" : 2022,
                "rating" : 9.8,
                "category" : "Accion"
            }
        }
