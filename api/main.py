from fastapi import FastAPI

from api.books.api.routes import router as books_router
from api.users.api.routes import router as users_router


app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0"
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
