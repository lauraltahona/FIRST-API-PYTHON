from fastapi import APIRouter, Depends, Request
from src.config.rate_limit import limiter
from src.features.user.dependencies.dependencies import get_auth_controller
from src.features.user.controller.auth_controller import AuthController
from src.features.user.dtos.user_dto import UserDtoLogin
from src.features.user.dtos.token_dto import RefreshRequest, TokenDto

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/login", response_model=TokenDto)
@limiter.limit("5/minute")
async def login(request: Request, login_dto: UserDtoLogin, controller: AuthController = Depends(get_auth_controller)):
    return await controller.login(login_dto)

@auth_router.post("/refresh", response_model=TokenDto)
async def refresh(refresh: RefreshRequest, controller: AuthController = Depends(get_auth_controller)):
    return await controller.refresh(refresh.refresh_token)