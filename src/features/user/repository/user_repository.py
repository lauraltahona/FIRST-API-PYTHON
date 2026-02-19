from typing import List
from src.shared.interfaces.crud import ICrudRepository
from src.features.user.model import User
from src.config.db import Database
from sqlalchemy import Session

class UserRepository(ICrudRepository[User, str]):

    def __init__(self, database: Database):
        """inicializar el repositorio con una instancia de Database"""
        self.database = database

    def save(User):
        pass

    def delete(id: str):
        pass

    def update(User):
        pass

    def get_by_id(id: str):
        pass

    def get_all() -> List[User] :
        pass

