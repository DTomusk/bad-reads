from fastapi import FastAPI
from src.config import get_settings

from src.books.api.routes import router as books_router
from src.users.api.routes import router as users_router

settings = get_settings()

app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0",
    debug=settings.DEBUG
)

app.include_router(
    books_router,
    prefix="/books",
    tags=["books"]
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["users"]
)
