from src.features.user.dtos.user_dto import UserDtoRegister
from src.features.user.model.user import User
from passlib.context import CryptContext
from src.errors.exceptions.user_exceptions import UserNotFoundException
import uuid

class UserService():


    def __init__(self, repository):
        self.repository = repository
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    async def save(self, user_dto: UserDtoRegister):
        # user = User(**user.model_dump()) # devuelve un diccionario
        # # para no tener que hacer manualmente: User(name=user_data.name, email=user_data.email, password=user_data.password)
        print("Servicio: procesando solicitud de registro de usuario:", user_dto)

        hashed = self.pwd_context.hash(user_dto.password)
        user = User(
            id=str(uuid.uuid4()),
            email=user_dto.email,
            password=hashed
        )
        print("Creando usuario:", user)
        return self.repository.save(user)
    
    async def get_by_id(self, id: int):
        
        existingUser = self.repository.get_by_id(id)

        if not existingUser: 
            raise UserNotFoundException(id)

