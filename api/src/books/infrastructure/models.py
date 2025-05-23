from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, Integer, String, Table, Index
from sqlalchemy.orm import relationship
from src.infrastructure.db.database import Base
from src.users.infrastructure.models import UserModel


# Association table for the many-to-many relationship between books and authors
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", UUID, ForeignKey("books.id"), primary_key=True),
    Column("author_id", UUID, ForeignKey("authors.id"), primary_key=True)
)

class BookModel(Base):
    __tablename__ = "books"

    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, index=True)
    average_rating = Column(Float, index=False)
    number_of_ratings = Column(Integer, index=False)
    sum_of_ratings = Column(Float, index=False)
    
    ratings = relationship("RatingModel", back_populates="book")
    authors = relationship("AuthorModel", secondary=book_authors, back_populates="books")
    reviews = relationship("ReviewModel", back_populates="book")

    def __repr__(self):
        return f"<BookModel(id={self.id}, title={self.title})>"
    
class RatingModel(Base):
    __tablename__ = "ratings"

    id = Column(UUID, primary_key=True, index=True)
    book_id = Column(UUID, ForeignKey("books.id"), index=True)
    user_id = Column(UUID, ForeignKey("users.id"), index=True)
    rating = Column(Float, index=False)

    book = relationship("BookModel", back_populates="ratings")
    user = relationship("UserModel", back_populates="ratings")
    reviews = relationship("ReviewModel", back_populates="rating")

    def __repr__(self):
        return f"<RatingModel(id={self.id}, book_id={self.book_id}, user_id={self.user_id}, rating={self.rating})>"
    
class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(UUID, primary_key=True, index=True)
    book_id = Column(UUID, ForeignKey("books.id"), index=True)
    user_id = Column(UUID, ForeignKey("users.id"), index=True)
    text = Column(String, index=False)
    rating_id = Column(UUID, ForeignKey("ratings.id"), index=True)
    date_created = Column(DateTime, index=False)

    book = relationship("BookModel", back_populates="reviews")
    user = relationship("UserModel", back_populates="reviews")
    rating = relationship("RatingModel", back_populates="reviews")
    
class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("BookModel", secondary=book_authors, back_populates="authors")

    def __repr__(self):
        return f"<AuthorModel(id={self.id}, name={self.name})>"