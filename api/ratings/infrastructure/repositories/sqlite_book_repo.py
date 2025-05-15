from sqlalchemy.orm import Session

from api.ratings.application.repositories.book_repository import BookRepo
from api.ratings.domain.models import Book
from api.ratings.infrastructure.models import BookModel


class SqliteBookRepo(BookRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_book_by_id(self, book_id: str) -> Book:
        """
        Get a book by its ID.
        :param book_id: The ID of the book to retrieve.
        :return: The book object.
        """
        result = self.session.query(BookModel).filter(BookModel.id == book_id).first()
        if result:
            return Book(
                id=result.id,
                title=result.title,
                author=result.author,
            )
    
    def get_books(self) -> list[Book]:
        """
        Get all books.
        :return: A list of book objects.
        """
        result = self.session.query(BookModel).all()
        return [
            Book(
                id=book.id,
                title=book.title,
                author=book.author,
            )
            for book in result
        ]
        