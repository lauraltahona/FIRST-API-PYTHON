from typing import List
from src.shared.interfaces.crud import ICrudRepository
from src.features.user.model import User
from src.config.db import Database
from sqlalchemy import Session

class UserRepository(ICrudRepository[User, str]):

    def __init__(self, database: Database):
        """inicializar el repositorio con una instancia de Database"""
        self.database = database

    def save(self, entity: User) -> User:
        try:
            db = self.database.get_db()
            db.add(entity)
            db.commit()
            db.refresh(entity)
            return entity
        except Exception as e:
            db.rollback()
            raise e # el repositorio no se encarga de manejar el error Solo garantiza que la transacción no quede dañada.
            # el raise e hace que no se quede escondido el error, basicamente, lo devuelve
        finally:
            db.close()

        

    def delete(self, id: str):
        pass

    def update(self, User):
        pass

    def get_by_id(self, id: str):
        pass

    def get_all(self) -> List[User] :
        pass

