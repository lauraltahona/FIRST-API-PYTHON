from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from src.errors.exceptions.base_exception import AppException

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

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message
        }
    )