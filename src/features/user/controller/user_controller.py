from fastapi import HTTPException

from src.features.user.dtos.user_dto import UserDtoRegister, UserDtoResponse

class UserController:

    def __init__(self, service):
        self.service = service

    def save(self, req: UserDtoRegister) -> UserDtoResponse:
        print("Controlador: procesando solicitud de registro de usuario:", req)
        user = self.service.save(req)

        return UserDtoResponse.model_validate(user)
       
    async def get_by_id(self, id: int) -> UserDtoResponse:
        user = self.service.get_by_id(id)
        return UserDtoResponse.model_validate(user)

