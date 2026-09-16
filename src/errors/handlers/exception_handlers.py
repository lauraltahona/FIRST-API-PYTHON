from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from src.errors.exceptions.base_exception import AppException
from  src.errors.schemas.error_response import ErrorResponse

logger = logging.getLogger(__name__)

async def app_exception_handler(
    request: Request,
    exc: AppException
):
    if exc.status_code >= 500:
        logger.error(
            f"{exc.status_code} en {request.method} {request.url.path}: {exc.message}",
            exc_info=True,
        )
    else:
        logger.warning(
            f"{exc.status_code} en {request.method} {request.url.path}: {exc.message}",
        ) 

    error_response = ErrorResponse(
        error=exc.error,
        code=exc.code,
        detail=exc.message
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )

async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Excepción no controlada en {request.method}, {request.url.path}: {str(exc)}",
        exc_info=True
    )

    error_response = ErrorResponse(
        error="internar_error",
        code="INTERNAL_SERVER_ERROR",
        detail="Ocurrió un error inesperado"
    )

    return JSONResponse(status_code=500, content=error_response.model_dump())
