from uuid import UUID
from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.book_detail_response import BookDetailResponse


class GetBookDetails:
    def __init__(self, book_repository: AbstractBookRepo, review_repository: AbstractReviewRepo):
        self.book_repository = book_repository
        self.review_repository = review_repository

    def execute(self, book_id: UUID) -> BookDetailResponse:
        """ Get book details by its ID """
        # Get the book details
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Get the reviews for the book
        reviews = self.review_repository.get_reviews_by_book_id(book_id)

        return BookDetailResponse.from_domain(book, reviews)