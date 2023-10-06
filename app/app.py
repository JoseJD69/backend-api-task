import inject
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api import app_router
from app.config import di_configuration

inject.configure(di_configuration)
# CORS
ALLOWED_ORIGINS = "*"

app = FastAPI(title="Backend Task", description="Backend Task for connection to GITHUB history", version="1.0.0")
app.include_router(app_router, prefix="/api/v1", tags=["api"])


@app.options("/{rest_of_path:path}", include_in_schema=False)
def preflight_handler(request) -> Response:
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


class UnicornException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/health")
async def health():
    return {"status": "ok", "description": "Backend Task for connection to GITHUB history"}
