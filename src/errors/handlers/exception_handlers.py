from fastapi import Request
from fastapi.responses import JSONResponse

from src.errors.exceptions.base_exception import AppException

async def app_exception_handler(
    request: Request,
    exc: AppException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message
        }
    )