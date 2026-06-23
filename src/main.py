from src.config.db.db_config import Database
from src.config.db.base_declarative import Base
from fastapi import FastAPI
from src.config.middlewares.cors import setup_cors

#routes
from src.features.user.routes.user_router import user_router


app = FastAPI()
setup_cors(app)

db = Database()
db.connect()


"""
Para que Base (una metaclase) escanee y descubra todas las clases que se heredan de ella,
necesitamos importar todos los módulos donde dichas clases de tabla (heredadas de Base) 
están definidas al módulo donde llamamos Metadata.create_all(engine)."""
Base.metadata.create_all(bind=db.get_engine()) # traer todas las tablas que hereden de Base y unelas y crealas en la base que te estoy pasando con engine



@app.get("/")
def health():
    return {"message":"API is up!"}

app.include_router(user_router)


 