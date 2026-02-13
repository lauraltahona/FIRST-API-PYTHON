from src.config.db.db_config import Database
from src.config.db.base_declarative import Base
from fastapi import FastAPI

from src.features.user.model import user

app = FastAPI()

db = Database()
db.connect()


"""
Para que Base (una metaclase) escanee y descubra todas las clases que se heredan de ella,
necesitamos importar todos los módulos donde dichas clases de tabla (heredadas de Base) 
están definidas al módulo donde llamamos Metadata.create_all(engine)."""
Base.metadata.create_all(bind=db.get_engine()) # traer todas las tablas que hereden de Base y unelas y crealas en la base que te estoy pasando con engine



@app.get("/")
def health():
    return {"message":"API is down!"}
 