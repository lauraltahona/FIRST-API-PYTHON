from src.config.db.db_config import Database
from src.config.db.base_declarative import Base
from fastapi import FastAPI

app = FastAPI()

db = Database()
db.connect()

Base.metadata.create_all(bind=db.get_engine()) # traer todas las tablas que hereden de Base y unelas y crealas en la base que te estoy pasando con engine



@app.get("/")
def health():
    return {"message":"API is down!"}
 