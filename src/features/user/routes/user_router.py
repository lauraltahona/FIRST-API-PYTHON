from fastapi import APIRouter, Depends
from src.features.user.controller.user_controller import UserController
from src.features.user.dependencies.dependencies import get_user_service
from src.features.user.dtos.user_dto import UserDtoRegister, UserDtoResponse
from src.features.user.service.user_service import UserService

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/", response_model=UserDtoResponse)
def register_user(user_dto: UserDtoRegister, service: UserService = Depends(get_user_service)):
    print("Recibiendo solicitud para registrar usuario:", user_dto)
    controller = UserController(service)
    return controller.save(user_dto)