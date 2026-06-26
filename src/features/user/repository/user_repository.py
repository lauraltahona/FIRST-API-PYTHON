from typing import List
from src.errors.exceptions.server_exceptions import ServerException
from src.shared.interfaces.crud.crud import ICrudRepository
from src.features.user.model.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.errors.exceptions.database_exceptions import DatabaseException


class UserRepository(ICrudRepository[User, str]):

    def __init__(self, session: Session):
        """inicializar el repositorio con una instancia de la Session"""
        self.session = session

    def save(self, user: User) -> User:
        try:
            print("Guardando usuario en la base de datos:", user)
            self.session.add(user)
            self.session.commit() # optimizar
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            print("Error al guardar el usuario:", e)
            raise e # el repositorio no se encarga de manejar el error Solo garantiza que la transacción no quede dañada.
            # el raise e hace que no se quede escondido el error, basicamente, lo devuelve
        

    def delete(self, id: str):
        pass

    def update(self, User):
        pass

    async def get_by_id(self, id: str) -> User | None:
        try:

            return self.session.get(User, id)
            
        except SQLAlchemyError as e:
             # se loquea el error real internamente 
            print(f"[DB ERROR] {str(e)}")  # después esto será un logger
            # pero al resto del sistema se manda algo limpio
            raise DatabaseException()
        except Exception as e: 
            print(f"[UNEXPECTED ERROR] {str(e)}")
            raise ServerException()

    def get_all(self) -> List[User] :
        pass

