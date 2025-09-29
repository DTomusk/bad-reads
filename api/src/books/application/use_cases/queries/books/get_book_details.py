from uuid import UUID
from src.books.domain.models import Book
from src.books.application.repositories.book_repository import AbstractBookRepo

class GetBookDetails:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(self, book_id: UUID) -> Book:
        """ Get book details by its ID """
        # Get the book details
        return self.book_repository.get_book_by_id(book_id)
        