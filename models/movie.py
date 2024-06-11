from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class movie(Base):   # entidad de la BD
    __tablename__ = "Movies"   # nombre de la tabla

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
