class AppException(Exception):

    def __init__(self, message: str, status_code: int, error: str, code: str):
        self.message = message
        self.status_code = status_code
        self.error = error
        self.code = code
        super().__init__(message)