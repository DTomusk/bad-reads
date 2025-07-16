from uuid import UUID
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.book_review_response import BookReviewResponse

class GetBookReviews():
    def __init__(self, review_repository: AbstractReviewRepo):
        self.review_repository = review_repository

    def execute(self, book_id: UUID) -> BookReviewResponse:
        reviews = self.review_repository.get_reviews_by_book_id(book_id)
        return BookReviewResponse(reviews=reviews)