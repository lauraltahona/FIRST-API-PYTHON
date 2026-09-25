from src.features.user.dtos.user_dto import UserDtoLogin
from src.errors.exceptions.auth_exception import InvalidCredentialException
from src.features.user.service.auth.jwt_config import create_access_token
class AuthService:
    def __init__(self, repository, pwd_context):
        self.repository = repository
        self.pwd_context = pwd_context

    async def login(self, loginDto: UserDtoLogin):
        user = await self.repository.get_by_email(loginDto.email)

        if user is None:
            raise InvalidCredentialException()

        if not self.pwd_context.verify(loginDto.password, user.password):
            raise InvalidCredentialException()

        token = create_access_token(data={"sub": user.id})
        return token