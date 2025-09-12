from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.config import get_settings

from src.books.api.routes import router as books_router
from src.users.api.routes import router as users_router

settings = get_settings()

app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0",
    debug=settings.DEBUG,
    redirect_slashes=False,
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for err in exc.errors():
        field = ".".join(str(loc) for loc in err["loc"] if isinstance(loc, str))
        errors[field] = err["msg"]

    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "errors": errors
        }
    )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Allow both localhost and 127.0.0.1
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    books_router,
    prefix="/api/books",
    tags=["books"]
)

app.include_router(
    users_router,
    prefix="/api/users",
    tags=["users"]
)
