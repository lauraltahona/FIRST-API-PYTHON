from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address) # obtiene la IP del cliente que está haciendo la petición

async def rate_limiter_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "TOO_MANY_REQUESTS",
            "message": "Demasiadas solicitudes, intenta de nuevo más tarde"
        },
    )

def setup_rate_limit(app: FastAPI) -> None:
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limiter_handler)