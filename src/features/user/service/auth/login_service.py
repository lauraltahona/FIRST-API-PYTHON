from src.features.user.dtos.user_dto import UserDtoLogin
from src.errors.exceptions.auth_exception import InvalidCredentialException, InvalidTokenException
from src.features.user.service.auth.jwt_config import create_access_token, decode_token

class AuthService:
    def __init__(self, repository, pwd_context):
        self.repository = repository
        self.pwd_context = pwd_context

    async def login(self, loginDto: UserDtoLogin) -> dict: 
        user = self.repository.get_by_email(loginDto.email)

        if user is None:
            raise InvalidCredentialException()

        if not self.pwd_context.verify(loginDto.password, user.password):
            raise InvalidCredentialException()

        token = create_access_token(data={"sub": user.id})
        return token

    async def refresh(self, refresh_token: str) -> dict:
        payload = decode_token(refresh_token)

        if payload.get("type") != "refresh":
            raise InvalidTokenException()

        # aquí, en el siguiente paso, chequeamos blacklist con payload["jti"]

        user_id = payload.get("sub")
        new_access_token = create_access_token(data={"sub": user_id})
        return {"access_token": new_access_token}