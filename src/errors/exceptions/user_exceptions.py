from src.errors.exceptions.base_exception import AppException

class UserNotFoundException(AppException):
    
    def __init__(self, user_id: int):
        super().__init__(
            message=f"Usuario con id '{user_id}' no encontrado", 
            status_code=404
        )
        