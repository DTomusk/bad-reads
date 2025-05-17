from sqlalchemy import UUID, Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from api.infrastructure.db.database import Base


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

    def __repr__(self):
        return f"<BookModel(id={self.id}, title={self.title})>"
    
class RatingModel(Base):
    __tablename__ = "ratings"

    id = Column(UUID, primary_key=True, index=True)
    book_id = Column(UUID, ForeignKey("books.id"), index=True)
    user_id = Column(UUID, index=True)
    rating = Column(Float, index=False)
    review = Column(String, index=False)

    book = relationship("BookModel", back_populates="ratings")

    def __repr__(self):
        return f"<RatingModel(id={self.id}, book_id={self.book_id}, user_id={self.user_id}, rating={self.rating})>"
    
class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("BookModel", secondary=book_authors, back_populates="authors")

    def __repr__(self):
        return f"<AuthorModel(id={self.id}, name={self.name})>"