import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #manipular tablas de la BD

sqlite_file_name = "../database.sqlite"   #nombre de la base de datos
base_dir = os.path.dirname(os.path.realpath(__file__)) # leer directorio actual database.py

database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}" # unir las dos url de arriba

engine = create_engine(database_url,echo=True) # motor de la base de datos 

Session = sessionmaker(bind=engine) # enlace de la sesion a el motor de la base de datos

Base = declarative_base()  # una instancia para el manejo de las tablas de la BD