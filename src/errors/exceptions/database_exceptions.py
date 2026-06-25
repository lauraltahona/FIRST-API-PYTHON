from src.errors.exceptions.base_exception import AppException

class DatabaseException(AppException):

    def __init__(self):
        super().__init__(
            message="Error interno de base de datos", 
            status_code=500
        )