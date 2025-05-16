from sqlalchemy.orm import Session

from api.books.application.repositories.book_repository import BookRepo
from api.books.domain.models import Book
from api.books.infrastructure.models import BookModel


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
                authors=result.authors,
                average_rating=result.average_rating,
                number_of_ratings=result.number_of_ratings,
                sum_of_ratings=result.sum_of_ratings
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
                authors=book.authors,
                average_rating=book.average_rating,
                number_of_ratings=book.number_of_ratings,
                sum_of_ratings=book.sum_of_ratings
            )
            for book in result
        ]

    def update_book(self, book: Book) -> Book:
        """
        Update a book.
        :param book: The book object to update.
        :return: The updated book object.
        """
        self.session.query(BookModel).filter(BookModel.id == book.id).update({
            BookModel.average_rating: book.average_rating,
            BookModel.number_of_ratings: book.number_of_ratings,
            BookModel.sum_of_ratings: book.sum_of_ratings
        })
        self.session.commit()