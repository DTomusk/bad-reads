from sqlalchemy import UUID, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.infrastructure.db.database import Base


class BookModel(Base):
    __tablename__ = "books"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    
    ratings = relationship("RatingModel", back_populates="book")

    def __repr__(self):
        return f"<BookModel(id={self.id}, title={self.title}, author={self.author})>"
    
class RatingModel(Base):
    __tablename__ = "ratings"

    id = Column(UUID, primary_key=True, index=True)
    book_id = Column(UUID, ForeignKey("books.id"), index=True)
    user_id = Column(UUID, index=True)
    rating = Column(Float, index=False)

    book = relationship("BookModel", back_populates="ratings")

    def __repr__(self):
        return f"<RatingModel(id={self.id}, book_id={self.book_id}, user_id={self.user_id}, rating={self.rating})>"