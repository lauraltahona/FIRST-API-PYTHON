from typing import List
from src.shared.interfaces.crud import ICrudRepository
from src.features.user.model import User
from sqlalchemy.orm import Session

class UserRepository(ICrudRepository[User, str]):

    def __init__(self, db: Session):
        """inicializar el repositorio con una instancia de la Session"""
        self.db = db

    def save(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            raise e # el repositorio no se encarga de manejar el error Solo garantiza que la transacción no quede dañada.
            # el raise e hace que no se quede escondido el error, basicamente, lo devuelve
        

    def delete(self, id: str):
        pass

    def update(self, User):
        pass

    def get_by_id(self, id: str):
        pass

    def get_all(self) -> List[User] :
        pass

