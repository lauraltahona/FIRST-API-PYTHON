from features.user.dtos.user_dto import UserDtoRegister
from features.user.model.user import User
from src.config.db.db_config import Database
from passlib.context import CryptContext
import uuid

class UserService():

    pwd_context = CryptContext(schemes=["bcrypt"])

    def __init__(self, repository):

        self.repository = repository

    def save(self, user_dto: UserDtoRegister):
        # user = User(**user.model_dump()) # devuelve un diccionario
        # # para no tener que hacer manualmente: User(name=user_data.name, email=user_data.email, password=user_data.password)
        hashed = self.pwd_context.hash(user_dto.password)

        user = User(
            id=str(uuid.uuid4()),
            email=user_dto.email,
            password=hashed
        )
        
        return self.repository.save(user)