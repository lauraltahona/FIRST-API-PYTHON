from src.config.db.db_config import Database
from src.config.db.base_declarative import Base
from fastapi import FastAPI
from src.config.middlewares.cors import setup_cors
from src.errors.exceptions.base_exception import AppException
from src.errors.handlers.exception_handlers import app_exception_handler

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

app.add_exception_handler(AppException, app_exception_handler)
app.include_router(user_router)


 