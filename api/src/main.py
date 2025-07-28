from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import get_settings

from src.books.api.routes import router as books_router
from src.users.api.routes import router as users_router
from src.bookclubs.api.routes import router as book_club_router

settings = get_settings()

app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0",
    debug=settings.DEBUG,
    redirect_slashes=False,  # Disable automatic trailing slash redirects
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

app.include_router(
    book_club_router,
    prefix="/api/book-clubs",
    tags=["book-clubs"]
)