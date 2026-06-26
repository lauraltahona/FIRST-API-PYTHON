from fastapi import APIRouter, Depends
from src.features.user.controller.user_controller import UserController
from src.features.user.dependencies.dependencies import get_user_service, get_user_controller
from src.features.user.dtos.user_dto import UserDtoRegister, UserDtoResponse
from src.features.user.service.user_service import UserService
from src.features.user.controller.user_controller import UserController

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/", response_model=UserDtoResponse)
async def register_user(user_dto: UserDtoRegister, controller: UserController = Depends(get_user_controller)):
    return await controller.save(user_dto)

@user_router.get("/{id}", response_model=UserDtoResponse)
async def get_by_id(id: str, controller: UserController = Depends(get_user_controller)):
    return await controller.get_by_id(id)