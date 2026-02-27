from features.user.dtos.user_dto import UserDtoRegister
from features.user.model.user import User
from src.config.db.db_config import Database

class UserService():

    def __init__(self, repository):

        self.repository = repository

    def save(self, user: UserDtoRegister):
        user = User(**user.model_dump) # devuelve un diccionario
        # para no tener que hacer manualmente: User(name=user_data.name, email=user_data.email, password=user_data.password)
        return self.repository.save(user)