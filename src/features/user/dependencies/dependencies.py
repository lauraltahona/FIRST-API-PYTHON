from fastapi import Depends
from sqlalchemy.orm import Session
from src.config.db.db_config import Database
from src.features.user.repository.user_repository import UserRepository
from src.features.user.service.user_service import UserService

db = Database()

def get_user_service(session: Session = Depends(db.get_db)):
    repository = UserRepository(session)
    return UserService(repository)