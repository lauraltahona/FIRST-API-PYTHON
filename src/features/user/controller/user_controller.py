from fastapi import HTTPException

from src.features.user.dtos.user_dto import UserDtoRegister, UserDtoResponse,  UserDtoLogin

class UserController:

    def __init__(self, service):
        self.service = service

    async def save(self, req: UserDtoRegister) -> UserDtoResponse:
        print("Controlador: procesando solicitud de registro de usuario:", req)
        user = self.service.save(req)

        return UserDtoResponse.model_validate(user)


               
    async def get_by_id(self, id: str) -> UserDtoResponse:
        user = await self.service.get_by_id(id)
        return UserDtoResponse.model_validate(user)

