from uuid import UUID
from src.books.domain.models import Book
from src.infrastructure.api.models import Failure, Outcome
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.api.schemas.book_detail_response import BookDetailResponse


class GetBookDetails:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(self, book_id: UUID) -> Outcome[Book]:
        """ Get book details by its ID """
        # Get the book details
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            return Outcome[Book](isSuccess=False, failure=Failure(error="Book not found", code=404))
        
        return Outcome[Book](isSuccess=True, data=book)