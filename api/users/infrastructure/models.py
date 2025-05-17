from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship
from api.infrastructure.db.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    reviews = relationship("ReviewModel", back_populates="user")
