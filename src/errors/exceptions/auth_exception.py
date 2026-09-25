from src.errors.exceptions.base_exception import AppException

class InvalidCredentialException(AppException):
    def __init__(self):
        super().__init__(
            message="Email o contraseña incorrecta", 
            status_code=401, 
            code="INVALID_CREDENTIAL", 
            error="invalid_credential"
        )

class TokenExpiredException(AppException):
    def __init__(self):
        super().__init__(
            message="El token ha expirado",
            status_code=401,
            code="TOKEN_EXPIRED",
            error="token_expired"
        )

class TokenBlacklistedException(AppException):
    def __init__(self):
        super().__init__(
            message="El token ha sido revocado",
            status_code=401,
            code="TOKEN_BLACKLISTED",
            error="token_blacklisted"
        )

class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(
            message="Token inválido",
            status_code=401,
            code="INVALID_TOKEN",
            error="invalid_token"
        )