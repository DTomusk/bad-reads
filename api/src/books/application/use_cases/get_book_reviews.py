from uuid import UUID
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.review_response import ReviewResponse

class GetBookReviews():
    def __init__(self, review_repository: AbstractReviewRepo):
        self.review_repository = review_repository

    def execute(self, book_id: UUID, sort: str) -> list[ReviewResponse]:
        if sort == "newest":
            sort_by = "date_created"
            sort_order = "desc"
        elif sort == "oldest":
            sort_by = "date_created"
            sort_order = "asc"
        else:
            raise ValueError(f"Invalid sort order: {sort}")
        return self.review_repository.get_reviews_by_book_id(book_id, sort_by, sort_order)