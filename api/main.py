from fastapi import FastAPI

from api.infrastructure.db.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Rating API",
    description="API for rating books",
    version="1.0.0"
)