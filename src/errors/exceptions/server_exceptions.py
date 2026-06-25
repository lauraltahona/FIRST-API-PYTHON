from src.errors.exceptions.base_exception import AppException

class ServerException(AppException):

    def __init__(self):
        super().__init__(
            message="Error interno con el servidor", 
            status_code=500
        )