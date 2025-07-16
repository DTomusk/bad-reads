from uuid import UUID
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.review_response import ReviewResponse

class GetBookReviews():
    def __init__(self, review_repository: AbstractReviewRepo):
        self.review_repository = review_repository

    def execute(self, book_id: UUID) -> list[ReviewResponse]:
        return self.review_repository.get_reviews_by_book_id(book_id)