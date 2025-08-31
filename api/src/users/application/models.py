from sqlalchemy import UUID, Column, String, Index
from sqlalchemy.orm import relationship
from src.infrastructure.db.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    reviews = relationship("ReviewModel", back_populates="user")
    ratings = relationship("RatingModel", back_populates="user")

    def __repr__(self):
        return f"<UserModel(id={self.id}, email={self.email})>"
