from fastapi import HTTPException

from src.features.user.dtos.user_dto import UserDtoRegister, UserDtoResponse

class UserController:

    def __init__(self, service):
        self.service = service

    def save(self, req: UserDtoRegister) -> UserDtoResponse:
        try:
            print("Controlador: procesando solicitud de registro de usuario:", req)
            user = self.service.save(req)
            return UserDtoResponse.model_validate(user)
        except ValueError as e: # error "esperado" de negocio: "ese email ya existe"
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e: # error inesperado, de sistema: "La base de datos se cayó"
            raise HTTPException(status_code=500, detail="Internal Server Error")