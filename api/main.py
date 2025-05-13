from fastapi import FastAPI

from api.infrastructure.db.database import Base, engine
from api.ratings.api.routes import router as rating_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0"
)

app.include_router(
    rating_router,
    prefix="/ratings",
    tags=["ratings"]
)