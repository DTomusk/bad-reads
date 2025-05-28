from sqlalchemy import UUID
from sqlalchemy.orm import Session

from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.domain.models import Book
from src.books.infrastructure.models import BookModel, AuthorModel


class BookRepo(AbstractBookRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_book_by_id(self, book_id: UUID) -> Book:
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
    
    def get_books(self, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get all books.
        :return: A list of book objects.
        """
        result = (self.session.query(BookModel)
            .order_by(getattr(BookModel, sort_by).asc() if sort_order == "asc" else getattr(BookModel, sort_by).desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all())
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
    
    def get_books_by_author(self, author_id: UUID, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get books by author.
        :param author_id: The ID of the author to filter by
        :param page: The page number for pagination
        :param page_size: The number of items per page
        :param sort_by: The field to sort by
        :param sort_order: The sort order ('asc' or 'desc')
        :return: A list of book objects.
        """
        result = (self.session.query(BookModel)
            .join(BookModel.authors)
            .filter(AuthorModel.id == author_id)
            .order_by(getattr(BookModel, sort_by).asc() if sort_order == "asc" else getattr(BookModel, sort_by).desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all())
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