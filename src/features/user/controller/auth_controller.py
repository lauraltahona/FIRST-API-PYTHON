
from src.features.user.dtos.token_dto import TokenDto
from src.features.user.dtos.user_dto import UserDtoLogin

class AuthController():
    def __init__(self, auth_service):
        self.service = auth_service


    async def login(self, loginDto: UserDtoLogin) -> TokenDto:
        token = await self.service.login(loginDto)
        return TokenDto(access_token=token)

    async def refresh(self, refresh_token: str) -> TokenDto:
        tokens = await self.service.refresh(refresh_token)
        return TokenDto(**tokens)