from uuid import UUID
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.api.schemas.book_detail_response import BookDetailResponse


class GetBookDetails:
    def __init__(self, book_repository: AbstractBookRepo):
        self.book_repository = book_repository

    def execute(self, book_id: UUID) -> BookDetailResponse:
        """ Get book details by its ID """
        # Get the book details
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        return BookDetailResponse.from_domain(book)