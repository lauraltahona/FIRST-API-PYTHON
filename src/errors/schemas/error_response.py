
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str      # nombre corto del tipo de error, ej "not_found", "database_error"
    code: str       # código interno o identificador estable, ej "USER_NOT_FOUND"
    detail: str     # mensaje humano-legible, puede cambiar libremente


