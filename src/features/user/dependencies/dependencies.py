from fastapi import Depends
from sqlalchemy.orm import Session
from src.features.user.controller.auth_controller import AuthController
from src.features.user.service.auth.login_service import AuthService
from src.features.user.controller.user_controller import UserController
from src.config.db.db_config import Database
from src.features.user.repository.user_repository import UserRepository
from src.features.user.service.user_service import UserService
from passlib.context import CryptContext


db = Database()

def get_pwd_context():
    return CryptContext(schemes=["bcrypt"])

def get_user_service(session: Session = Depends(db.get_db), pwd_context: CryptContext = Depends(get_pwd_context)):
    repository = UserRepository(session)
    return UserService(repository, pwd_context)

def get_user_controller(service: UserService = Depends(get_user_service)):
    return UserController(service)

def get_auth_service(session: Session = Depends(db.get_db), pwd_context: CryptContext = Depends(get_pwd_context)):
    repository = UserRepository(session)
    return AuthService(repository, pwd_context)

def get_auth_controller(service: AuthService = Depends(get_auth_service)):
    return AuthController(service)
